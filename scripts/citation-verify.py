#!/usr/bin/env python3
"""
citation-verify.py — 引用候选检索 / Citation candidate lookup (Crossref + OpenAlex)

Extracts supported author-year citations from a Markdown file and searches the
Crossref public API, cascading to OpenAlex when Crossref has no match (OpenAlex
covers many monographs and older humanities works that Crossref misses). Flags:
    1. CITATIONS WITH NO CANDIDATE FOUND in either queried index. Index absence
       is not evidence that the cited work does not exist.
    2. CITATIONS WHERE THE AUTHOR NAME ONLY FUZZY-MATCHES (probable typo or
       different work)
    3. QUERIES THAT FAILED (network/parse error) — reported as ERROR, never
       silently converted to NOT_FOUND

用法 / Usage:
    python3 citation-verify.py <draft.md>
    python3 citation-verify.py <draft.md> --quiet --json

Runtime: requests are rate-limited to 1/sec per API to be polite, so a draft
with 50 citations takes roughly 1–2 minutes. Budget accordingly.

Exit codes (for CI / agent gating):
    0 — every citation FOUND (or no citations parsed; not a verification pass)
    1 — at least one FUZZY_MATCH or NOT_FOUND (review needed)
    2 — at least one ERROR (network/parse failure), or unreadable input file

诚实声明 / Honest disclaimer:
    - "FOUND" means a candidate's surname metadata matched exactly after case
      and outer-whitespace normalization, within the API's year filter. It does
      NOT establish work identity, edition, quotation accuracy, or claim support.
      Common surnames (Smith, 2010) can match unrelated works. Compare the
      returned title/container with the work actually cited.
    - Crossref and OpenAlex together still do not index everything. Many
      humanities works (monographs from small university presses, untranslated
      foreign-language works, dissertations, archival sources, classical texts)
      are absent. A "NOT_FOUND" verdict for those is expected and not a problem.
    - This script catches the LLM-hallucination case (made-up journal article
      citations) — that's where index coverage is good.
    - For monograph / archival / classics citations, the [VERIFY] marker
      protocol in SKILL.md is the right tool, not this script.
    - Running this script sends extracted author names and years to the third-party
      Crossref and OpenAlex services. It does not upload the full draft. Use local
      checks instead when external metadata queries are outside the user's scope.

API refs: https://api.crossref.org/works · https://api.openalex.org/works
"""

import argparse
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path
from difflib import SequenceMatcher


CROSSREF_URL = "https://api.crossref.org/works"
OPENALEX_URL = "https://api.openalex.org/works"
USER_AGENT = "humanities-writing-companion/5.1.0 (https://github.com/tizzy916/humanities-writing-companion; mailto:shencong916@gmail.com)"


class QueryError(Exception):
    """A backend query failed (network / HTTP / parse). Distinct from 'no match'."""


# ----------------------------- Inline citation parsing -----------------------------

# Patterns to match in-prose citations across styles.
# Conservative — we accept some false negatives (missed citations) over false positives.
PATTERNS = [
    # Chicago author-date / APA author-year: (Foucault, 1975, p. 23) or (Foucault 1975)
    re.compile(r'\(([A-Z][a-zA-ZÀ-ſ\-]+(?:\s+(?:and|&)\s+[A-Z][a-zA-ZÀ-ſ\-]+)*)[,\s]+(\d{4})[a-z]?(?:[,\s]+p?p?\.?\s*[\d\-–]+)?\)'),
    # Chicago narrative: Foucault (1975) ...
    re.compile(r'\b([A-Z][a-zA-ZÀ-ſ\-]+)\s+\((\d{4})[a-z]?\)'),
    # Chinese: (福柯, 1975)
    re.compile(r'[(（]([^()（）]+?)[，,]\s*(\d{4})[a-z]?[)）]'),
]


def extract_citations(text):
    """Returns list of (author_name, year) tuples found in prose. Deduplicated."""
    seen = set()
    out = []
    for pattern in PATTERNS:
        for m in pattern.finditer(text):
            author = m.group(1).strip()
            year = m.group(2).strip()
            # Normalize: take last surname for compound authors
            author_main = re.split(r'\s+(?:and|&)\s+', author)[0].strip()
            key = (author_main.lower(), year)
            if key not in seen:
                seen.add(key)
                out.append((author_main, year))
    return out


# ----------------------------- Backend queries -----------------------------

def _fetch_json(url, retries=1):
    """GET url, parse JSON. One retry with backoff for transient failures."""
    last_exc = None
    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=10) as resp:
                return json.loads(resp.read())
        except Exception as exc:
            last_exc = exc
            if attempt < retries:
                time.sleep(2)
    raise last_exc


def crossref_query(author, year, rows=5):
    """Search Crossref for works by author + year. Returns list of matching items.
    Raises QueryError on network/parse failure — never silently returns []."""
    params = {
        "query.author": author,
        "filter": f"from-pub-date:{year}-01,until-pub-date:{year}-12",
        "rows": rows,
    }
    url = f"{CROSSREF_URL}?{urllib.parse.urlencode(params)}"
    try:
        data = _fetch_json(url)
        if not isinstance(data, dict) or not isinstance(data.get("message"), dict):
            raise ValueError("unexpected response shape: missing message object")
        items = data["message"].get("items")
        _validate_items(items)
        return items
    except Exception as exc:
        raise QueryError(f"Crossref query failed for ({author}, {year}): {exc}") from exc


def _validate_items(items):
    """Reject malformed backend data rather than treating it as an empty index."""
    if not isinstance(items, list):
        raise ValueError("unexpected response shape: expected an items list")
    for item in items:
        if not isinstance(item, dict):
            raise ValueError("unexpected response shape: expected a work object")
        authors = item.get("author")
        if authors is None:
            authors = []
        if not isinstance(authors, list) or any(
            not isinstance(author, dict) or not isinstance(author.get("family") or "", str)
            for author in authors
        ):
            raise ValueError("unexpected response shape: invalid author list")
        for field in ("title", "container-title"):
            values = item.get(field)
            if values is None:
                values = []
            if not isinstance(values, list) or any(not isinstance(value, str) for value in values):
                raise ValueError(f"unexpected response shape: invalid {field} list")


def openalex_query(author, year, rows=5):
    """Search OpenAlex (free, no key) for works by author + year. Items are
    normalized to the Crossref item shape so best_match() can score them.
    Raises QueryError on network/parse failure."""
    params = {
        "filter": f"raw_author_name.search:{author},publication_year:{year}",
        "per-page": rows,
        "mailto": "shencong916@gmail.com",  # OpenAlex polite pool
    }
    # OpenAlex throttles anonymous `.search` filters under heavy load;
    # a free API key (optional) lifts that: https://openalex.org/rest-api
    api_key = os.environ.get("OPENALEX_API_KEY")
    if api_key:
        params["api_key"] = api_key
    url = f"{OPENALEX_URL}?{urllib.parse.urlencode(params)}"
    try:
        data = _fetch_json(url)
        if not isinstance(data, dict) or not isinstance(data.get("results"), list):
            raise ValueError("unexpected response shape: missing results list")
        items = []
        for w in data["results"]:
            authors = []
            for auth in w.get("authorships", []):
                name = (auth.get("author") or {}).get("display_name") or auth.get("raw_author_name") or ""
                if name:
                    # Last token as a family-name approximation
                    authors.append({"family": name.split()[-1]})
            container = None
            loc = w.get("primary_location") or {}
            src = loc.get("source") or {}
            if src.get("display_name"):
                container = src["display_name"]
            doi = w.get("doi")
            if doi and doi.startswith("https://doi.org/"):
                doi = doi[len("https://doi.org/"):]
            items.append({
                "author": authors,
                "title": [w.get("display_name") or ""],
                "container-title": [container] if container else [],
                "DOI": doi,
                "type": w.get("type"),
            })
        _validate_items(items)
        return items
    except Exception as exc:
        raise QueryError(f"OpenAlex query failed for ({author}, {year}): {exc}") from exc


def best_match(items, author):
    """Pick best item matching author. Returns (item, confidence) or (None, 0)."""
    if not items:
        return None, 0.0
    best = None
    best_score = 0.0
    for item in items:
        item_authors = item.get("author") or []
        if not item_authors:
            continue
        for a in item_authors:
            family = a.get("family") or ""
            score = SequenceMatcher(None, family.strip().casefold(), author.strip().casefold()).ratio()
            if score > best_score:
                best_score = score
                best = item
    return best, best_score


# ----------------------------- Main verification loop -----------------------------

def _lookup(author, year, verbose):
    """Cascade: Crossref → OpenAlex. Returns (best_item, score, source, errors).
    source is 'Crossref' or 'OpenAlex'; errors is a list of failure messages."""
    errors = []
    # 1. Crossref
    try:
        items = crossref_query(author, year)
        best, score = best_match(items, author)
        if best is not None and score >= 0.5:
            return best, score, "Crossref", errors
    except QueryError as exc:
        errors.append(str(exc))
        if verbose:
            print(f"[!] {exc}", file=sys.stderr)
    # 2. OpenAlex cascade (humanities monographs / older works often live here)
    time.sleep(1)  # polite rate limit between backends too
    try:
        items = openalex_query(author, year)
        best, score = best_match(items, author)
        if best is not None and score >= 0.5:
            return best, score, "OpenAlex", errors
    except QueryError as exc:
        errors.append(str(exc))
        if verbose:
            print(f"[!] {exc}", file=sys.stderr)
    return None, 0.0, None, errors


def verify(text, verbose=False):
    """Returns a list of dicts with verification results."""
    citations = extract_citations(text)
    if not citations:
        return []
    results = []
    for i, (author, year) in enumerate(citations):
        if verbose:
            print(f"[{i+1}/{len(citations)}] Querying Crossref/OpenAlex for ({author}, {year})...",
                  file=sys.stderr)
        best, score, source, errors = _lookup(author, year, verbose)
        if best is None and errors:
            # Query failure(s) and no confirming match from any backend:
            # we genuinely don't know. Never report this as NOT_FOUND —
            # that would instruct the author to delete possibly-real sources.
            verdict = "ERROR"
            details = ("Could not verify ({}, {}): query failed ({}). "
                       "This is a lookup failure, NOT evidence the work is fake. "
                       "Re-run later or verify manually.").format(
                           author, year, "; ".join(errors))
            match_data = None
        elif best is None or score < 0.5:
            verdict = "NOT_FOUND"
            details = (f"No Crossref or OpenAlex match for ({author}, {year}). "
                       f"This may be a humanities work outside index coverage "
                       f"(monograph, archival, classics, dissertation, foreign-language), "
                       f"or it may not exist. Manually verify.")
            match_data = None
        elif score < 1.0:
            verdict = "FUZZY_MATCH"
            details = (f"Best match for ({author}, {year}) is similarity={score:.2f} "
                       f"(source: {source}). "
                       f"Possible spelling difference or different work.")
            match_data = best
        else:
            verdict = "FOUND"
            title = (best.get("title") or [""])[0]
            container = (best.get("container-title") or [""])[0] if best.get("container-title") else ""
            details = (f"Candidate metadata matches surname '{author}' under the {year} year filter "
                       f"(source: {source}, name similarity {score:.2f}): "
                       f"\"{title}\"" + (f" — {container}" if container else "") + ". "
                       f"FOUND is only a candidate metadata match — "
                       f"manually confirm this is the work you are citing; "
                       f"quotation accuracy and claim support are not checked.")
            match_data = best
        results.append({
            "author": author,
            "year": year,
            "verdict": verdict,
            "details": details,
            "source": source,
            "errors": errors or None,
            "match": {
                "title": (match_data.get("title") or [""])[0] if match_data else None,
                "type": match_data.get("type") if match_data else None,
                "container": match_data.get("container-title", [""])[0]
                             if match_data and match_data.get("container-title") else None,
                "doi": match_data.get("DOI") if match_data else None,
                "source": source,
            } if match_data else None,
        })
        time.sleep(1)  # polite rate limit
    return results


def exit_code(results):
    """Exit-code contract: all FOUND → 0; any FUZZY/NOT_FOUND → 1; any ERROR → 2."""
    verdicts = {r["verdict"] for r in results}
    if "ERROR" in verdicts:
        return 2
    if "NOT_FOUND" in verdicts or "FUZZY_MATCH" in verdicts:
        return 1
    return 0


def print_report(results):
    """Print human-readable report."""
    if not results:
        print("[i] No citations parsed from the input. This is not a verification pass; "
              "check whether the draft uses a supported author-year citation form.")
        return

    not_found = [r for r in results if r["verdict"] == "NOT_FOUND"]
    fuzzy = [r for r in results if r["verdict"] == "FUZZY_MATCH"]
    found = [r for r in results if r["verdict"] == "FOUND"]
    errored = [r for r in results if r["verdict"] == "ERROR"]

    print(f"\n=== Citation verification (Crossref → OpenAlex cascade) ===")
    print(f"Total citations parsed: {len(results)}")
    print(f"  ✓ Found:        {len(found)}  ← candidate metadata match; confirm same work")
    print(f"  ⚠ Fuzzy match:  {len(fuzzy)}  ← review")
    print(f"  ✗ Not found:    {len(not_found)}  ← review (or may be off-index humanities work)")
    print(f"  ⚡ Error:        {len(errored)}  ← query failed; NOT evidence of hallucination")

    if errored:
        print(f"\n## ⚡ QUERY ERRORS — could not verify, do NOT treat as fake ({len(errored)})")
        for r in errored:
            print(f"\n  ({r['author']}, {r['year']})")
            print(f"    {r['details']}")

    if not_found:
        print(f"\n## ✗ NOT FOUND in Crossref or OpenAlex ({len(not_found)})")
        for r in not_found:
            print(f"\n  ({r['author']}, {r['year']})")
            print(f"    {r['details']}")

    if fuzzy:
        print(f"\n## ⚠ FUZZY MATCH — review for typo / different work ({len(fuzzy)})")
        for r in fuzzy:
            print(f"\n  ({r['author']}, {r['year']})")
            if r["match"]:
                print(f"    Best match ({r['match']['source']}): \"{r['match']['title']}\"")
                if r["match"]["container"]:
                    print(f"    Container: {r['match']['container']}")
                if r["match"]["doi"]:
                    print(f"    DOI: {r['match']['doi']}")
            print(f"    {r['details']}")

    if found:
        print(f"\n## ✓ FOUND — candidate metadata match; CONFIRM it is yours ({len(found)})")
        for r in found:
            print(f"\n  ({r['author']}, {r['year']}) → \"{r['match']['title']}\" [{r['match']['source']}]")
            if r["match"]["container"]:
                print(f"    Container: {r['match']['container']}")
            if r["match"]["doi"]:
                print(f"    DOI: {r['match']['doi']}")
            print(f"    → Manually confirm this title/container is the work you cited —")
            print(f"      common surnames match unrelated publications.")

    print(f"\n=== Reminders ===")
    print("  · FOUND ≠ verified. It is a candidate surname match within an API year filter.")
    print("    Confirm work identity and edition, then check the quotation and claim support.")
    print("  · NOT_FOUND is expected for monographs, archival sources, classics, dissertations,")
    print("    and non-English-language works. Index coverage is strongest for English-")
    print("    language journal articles.")
    print("  · ERROR means the lookup itself failed (network etc.) — re-run or check manually.")
    print("    Never delete a citation because of an ERROR verdict.")
    print("  · This script catches the LLM-hallucination case (made-up journal articles).")
    print("    For monograph citations, use the [VERIFY] / [待核对] marker workflow.")
    print("  · FUZZY_MATCH and a near-but-different result probably means a spelling or year typo.")
    print()


def main():
    parser = argparse.ArgumentParser(
        description="Look up candidate metadata for author-year citations via Crossref and OpenAlex.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Runtime: rate-limited to 1 request/sec per API — a draft with 50 citations\n"
            "takes roughly 1-2 minutes (longer when the OpenAlex cascade kicks in).\n"
            "\n"
            "Exit codes: 0 = all FOUND (or none parsed); 1 = any FUZZY_MATCH/NOT_FOUND;\n"
            "            2 = any ERROR (network/parse failure) or unreadable input.\n"
            "Zero parsed citations does not mean verification passed.\n"
            "\n"
            "FOUND is a candidate metadata match, not verification of work identity,\n"
            "quotation accuracy, or support for your claim.\n"
            "Network disclosure: extracted author names and years are sent to the\n"
            "third-party Crossref/OpenAlex services; the full draft is not uploaded."
        ),
    )
    parser.add_argument("input", help="Input Markdown file to scan")
    parser.add_argument("--json", action="store_true", help="Output JSON instead of human report")
    parser.add_argument("--quiet", action="store_true", help="Suppress progress output")
    args = parser.parse_args()

    path = Path(args.input)
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"[!] Input file does not exist: {path}", file=sys.stderr)
        sys.exit(2)
    except IsADirectoryError:
        print(f"[!] Input is a directory, expected a Markdown file: {path}", file=sys.stderr)
        sys.exit(2)
    except OSError as exc:
        print(f"[!] Cannot read input file {path}: {exc}", file=sys.stderr)
        sys.exit(2)

    results = verify(text, verbose=not args.quiet)
    if args.json:
        json.dump(results, sys.stdout, ensure_ascii=False, indent=2)
        print()
    else:
        print_report(results)
    sys.exit(exit_code(results))


if __name__ == "__main__":
    main()
