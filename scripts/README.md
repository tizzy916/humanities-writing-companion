# scripts/ · Engineering Support Tools

> **Language / 语言**: **English (current)** · [中文](README.zh.md)

> The scripts in this directory are where the "engineering rigor" principle from SKILL.md
> actually lands — AI self-awareness is the soft norm, scripts are the hard mechanism.
> Only together do the two genuinely guard against drift and oversight.

**A citation toolchain is new as of v4.0** (format conversion + Crossref verification).

---

## The five scripts

### 1. `ai-trace-scan.sh` · AI-trace and academic boilerplate scan

**Purpose**: Scans a document for the high-frequency filler phrases listed in `references/ai-trace-checklist.md`, along with the over-piling of connective words.

**Usage**:
```bash
# Single-file scan
./scripts/ai-trace-scan.sh path/to/chapter.md

# Scan an entire paper project directory
./scripts/ai-trace-scan.sh path/to/paper/
```

**When to run**:
- After revising each chapter in Mode F (draft revision)
- Before running Mode B (chapter-level review)
- The final check before a paper is finished

**Output**: line number + line content + frequency warning for each match

**How frequency is counted**: connector frequency (此外 / 同时 / …) is counted by **occurrence, not by line** — four 此外 packed into one paragraph (one line, as Chinese Markdown often is) trip the >3 threshold just like four separate lines do.

**Note**: The scanner only "flags suspects" — whether a flagged phrase actually needs changing is still the author's call (some "boilerplate" is a deliberate choice in a particular context).

---

### 2. `pending-checks.sh` · Pending-marker roundup

**Purpose**: Pulls out every unfinished marker in a project (citations awaiting verification, arguments awaiting discussion, AI drafts, and so on).

**Usage**:
```bash
# An entire project directory
./scripts/pending-checks.sh path/to/paper/

# A single file
./scripts/pending-checks.sh path/to/chapter.md
```

**Markers scanned**:
| Marker | Meaning | Handling priority |
|------|------|-----------|
| `[VERIFY]` / `[待核对]` | AI cited from memory / unverified fact | 🔴 Must be cleared to zero before submission |
| `❓ to discuss` / `❓ 待讨论` | An argumentative choice the author must decide | 🟡 Handle as the work advances |
| `[AI DRAFT]` / `[AI 草稿，待作者审阅]` | An AI-drafted paragraph not yet reviewed | 🟢 Remove the marker after review |
| `>>>` | A spot the AI was unsure about while drafting | 🔵 Handle immediately after drafting |
| `[author micro-adjustment]` / `[作者微调]` | The author's second-pass tweak to an AI suggestion | 🟣 Write back into the writing-style profile |

The draft aliases `[AI draft, pending author review]` and `[AI 草稿]` are also recognized. The summary counts matching lines within each marker category; repeated markers of the same category on one line count once. Directory scans include `.md` files only.

**When to run**:
- At the start of every conversation (to see what remains unfinished)
- The final checklist before submission
- A status summary when resuming across conversations

---

### 3. `citation-consistency.py` · Citation-consistency scan

**Purpose**: Checks the whole text for citation-format consistency (not conformance).

**Usage**:
```bash
python3 scripts/citation-consistency.py path/to/paper/main.md
```

**What it scans for**:
1. Mixed bracket types (half-width `()` vs. full-width `（）`)
2. Mixed commas inside citations (`,` vs. `，`)
3. Inconsistent multi-author connectors (`&` / `and` / `与` / `和` / `、`)
4. Inconsistent name forms when the same source is cited (Chinese translated name vs. original surname)
5. Inconsistent page-number formats (`p. X` / `第 X 页`, etc.)

Single pages and page ranges within one style (`p. 2` / `pp. 3–4`, or `第 2 页` / `第 3–4 页`) are treated as consistent. Differences in spacing or language remain review items.

**When to run**:
- A local consistency check after finishing a chapter
- A whole-text uniformity audit before submission
- A regression check after introducing new sources

**Exit codes**: `0` = no issues · `1` = issues found (review needed) · `2` = input unreadable (missing file / directory passed)

**Important boundaries**:
- This script only checks "is it consistent," not "does it conform to APA / Chicago / GB/T 7714"
- For conformance checking, work through the `_writing-config/引用格式速查.md` **inside your own paper project** by hand — that file lives in the user's project (created per `references/project-management.md`), it is *not* a file of this repository
- Heuristic regex scanning may produce a few false positives; results need human review

---

### 4. `citation-format-convert.py` · Citation-format conversion (new in v4.0)

**Purpose**: Converts a BibTeX bibliography into one of four mainstream academic citation formats (for preparing the reference list before submission).

**Supported formats**:
- **Chicago Author-Date** — most common in history and the humanities
- **MLA 9** — most common in literature and linguistics
- **APA 7** — most common in education, psychology, and parts of the social sciences
- **GB/T 7714 numeric sequential system** — the Chinese national standard for journals

**Usage**:
```bash
# Output to stdout
python3 scripts/citation-format-convert.py refs.bib --to chicago

# Output to a file
python3 scripts/citation-format-convert.py refs.bib --to apa --out refs-apa.txt

# Sort by author (default), by year, by key, or by input order
python3 scripts/citation-format-convert.py refs.bib --to mla --sort year
```

**When to run**:
- Preparing the final reference list before submission (when the target journal has specific format requirements)
- Switching the same paper between journals (to regenerate quickly)
- Before producing the Mode K (AI-use disclosure) output

**Supported BibTeX types**: `@book`, `@article`, `@incollection`, `@inbook`, `@inproceedings`, `@thesis`, `@phdthesis`

**Parser behavior**: the balanced-brace parser handles nested braces (`title = {The {DNA} Story}`), single-line entries, and quoted values — the common shapes of real Zotero exports. Entries that cannot be parsed are **reported on stderr and skipped, never silently merged or corrupted**.

**Exit codes**: `0` = all entries converted · `1` = some entries could not be parsed (reported; the rest are converted) · `2` = nothing parsed or input unreadable

**Important boundaries**:
- **Not a replacement for BibLaTeX / CSL** — those support each journal's idiosyncratic variants; if your toolchain can use BibLaTeX, prefer it
- This script serves the "in-flight" scenario: you have a BibTeX library on hand and want to generate a list for a particular journal right now
- **Each format has a wealth of subtle rules and journal-specific variants** — always check the output against the target journal's style guide, and treat the output as a draft rather than a finished product
- It handles only the reference **list**, not the inline citations **within** the prose (those require understanding document structure)

---

### 5. `citation-verify.py` · Citation candidate lookup (new in v4.0)

**Purpose**: Extracts supported author-year citations from a Markdown draft and retrieves candidate metadata from Crossref, **cascading to OpenAlex** when Crossref has no candidate. The returned candidates help an author investigate citations that may have been invented or misremembered. This is a heuristic search, not proof of citation authenticity or exhaustive coverage of the draft.

**Network disclosure**: Running the script sends the extracted author names and years to the third-party Crossref and OpenAlex services; it does not upload the full draft. Confirm external metadata queries are within the task's authorized scope. For local-only work, use the other four scripts and leave source verification pending.

**Usage**:
```bash
# Human-readable report
python3 scripts/citation-verify.py path/to/draft.md

# Quiet mode + JSON output (for CI / programmatic processing)
python3 scripts/citation-verify.py path/to/draft.md --quiet --json
```

**Runtime**: requests are rate-limited to 1/sec per API, so a draft with 50 citations takes roughly **1–2 minutes** (longer when the OpenAlex cascade kicks in). Budget accordingly.

**Results fall into four categories**:
- **✓ FOUND**: a candidate's surname metadata matches within the API's year filter, with its title and container shown in the output. **This does not establish work identity, edition, quotation accuracy, or claim support.** Common surnames like (Smith, 2010) can match unrelated works. **Always compare the returned metadata with the work actually cited.**
- **⚠ FUZZY_MATCH**: a near but imperfect name match (similarity ≥0.5 and <1.0) — could be a misspelling or a different author; needs review. Only an exact surname match after case/outer-whitespace normalization can receive FOUND; similarity is not a calibrated confidence score
- **✗ NOT_FOUND**: no match in Crossref **or** OpenAlex — **be alert**, but **not necessarily a hallucination** (see boundaries below)
- **⚡ ERROR**: the lookup itself failed (network timeout, API outage, malformed response) and no backend returned a candidate — this is a **lookup failure, not evidence the work is fake**. Never delete a citation because of an ERROR verdict; re-run later or check manually. (Errors are reported distinctly and never silently counted as NOT_FOUND.)

**Exit codes** (for CI / agent gating):
| Code | Meaning |
|------|---------|
| `0` | every citation FOUND (or no citations parsed) |
| `1` | at least one FUZZY_MATCH or NOT_FOUND — review needed |
| `2` | at least one ERROR (network/parse failure), or unreadable input file |

For compatibility, zero parsed citations still returns `0`; **this is not a verification pass**. The parser does not cover every footnote, numeric, grouped, or multilingual citation form. Read the parsed count before interpreting the exit code.

**When to run**:
- After Mode B (chapter-level review), before Mode G (blind-reading check)
- Any chapter the AI drafted (after Mode C output)
- The final compliance check before submission

**Important boundaries**:
- **FOUND ≠ verified.** Compare the returned title and container (when available) with the cited work; verify the edition, quoted text, and claim support against the source itself
- **Crossref and OpenAlex together still do not index everything.** Many humanities works (especially: monographs from small university presses, untranslated foreign-language books, dissertations, archival sources, classical texts) are **absent from both** — for these, "NOT_FOUND" is the expected result and does **not** indicate a problem
- What this script is good at is catching **hallucinated LLM journal-article citations** — the area index coverage is best
- For monograph, archival, and classics citations, the right tool is the `[VERIFY]` / `[待核对]` marker protocol (see SKILL.md), not this script
- Network requests are politely rate-limited to 1 per second per API to protect these public-good services (set the optional `OPENALEX_API_KEY` environment variable if OpenAlex throttles anonymous searches under heavy load)

---

## Installation and permissions

Before first use, give the shell scripts execute permission:

```bash
chmod +x scripts/ai-trace-scan.sh scripts/pending-checks.sh
```

The Python scripts need no special installation — they depend only on the Python 3 standard library.

---

## Tests

`scripts/tests/run_tests.sh` (zsh) is a minimal regression suite over all five scripts, with fixtures under `scripts/tests/fixtures/` (mixed Chinese/English citations, a directory with planted AI clichés, nested-brace BibTeX, pending markers). It asserts hit counts, exit-code contracts, directory-mode scanning, and friendly errors on missing files. CI runs it on every push.

The suite also runs `scripts/tests/test_regressions.py`: deterministic, offline tests for bilingual markers, near-name verdicts, malformed API responses, fallback recovery, and valid singular/plural page forms. No draft text or synthetic test data is sent to an API in the offline run.

```bash
zsh scripts/tests/run_tests.sh                 # full run (includes one live network test)
SKIP_NETWORK=1 zsh scripts/tests/run_tests.sh  # offline run (CI default)
```

---

## How they map to SKILL.md

| Script | Corresponding SKILL.md section |
|------|-------------------|
| `ai-trace-scan.sh` | Deep Style Understanding · unexamined expression-pattern scanning |
| `pending-checks.sh` | Feedback Reports · 4-tier classification + anti-drift protocol |
| `citation-consistency.py` | Multilingual Academic Writing · citation-format consistency check + Systematic Verification · citation-completeness check |
| `citation-format-convert.py` | Format preparation before Mode K (AI-use disclosure) / multi-journal submission switching |
| `citation-verify.py` | Systematic Verification · citation authenticity / the automated complement to the `[VERIFY]` marker protocol |

---

## Design principles

1. **Zero-dependency first**: shell scripts use zsh + grep; Python scripts use only the standard library
2. **Fail safe**: nonexistent directories, empty matches, and the like all return a friendly message rather than crashing
3. **Readable output**: reports meant to be read directly, with no extra parsing needed
4. **Honest boundaries**: every script states plainly what it does and what it does not — to avoid giving the author the false certainty that "if everything is checked off, there's no problem"
