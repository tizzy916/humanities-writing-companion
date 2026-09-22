#!/usr/bin/env zsh
# run_tests.sh — minimal regression suite for scripts/
#
# Usage:
#   zsh scripts/tests/run_tests.sh                # full run (includes one live-network test)
#   SKIP_NETWORK=1 zsh scripts/tests/run_tests.sh # skip network-dependent tests (CI default)
#
# Every assertion here reproduces a bug that was actually observed in QA:
# zsh directory-mode misses, line-vs-occurrence counting, hallucination-whitewashing
# FOUND semantics, silent NOT_FOUND on network failure, nested-brace BibTeX corruption,
# and bare tracebacks on missing files.

set -u

SCRIPT_DIR="${0:A:h}"
REPO_ROOT="${SCRIPT_DIR:h:h}"
SCRIPTS="$REPO_ROOT/scripts"
FIX="$SCRIPT_DIR/fixtures"

PASS=0
FAIL=0
SKIP=0

pass() { PASS=$((PASS + 1)); echo "  ✓ $1"; }
fail() { FAIL=$((FAIL + 1)); echo "  ✗ FAIL: $1"; }
skip() { SKIP=$((SKIP + 1)); echo "  - SKIP: $1"; }

assert_exit() {
    # assert_exit <expected> <actual> <label>
    if [ "$2" -eq "$1" ]; then pass "$3 (exit $2)"; else fail "$3 — expected exit $1, got $2"; fi
}

assert_contains() {
    # assert_contains <haystack> <needle> <label>
    if [[ "$1" == *"$2"* ]]; then pass "$3"; else fail "$3 — output missing: $2"; fi
}

assert_not_contains() {
    if [[ "$1" != *"$2"* ]]; then pass "$3"; else fail "$3 — output unexpectedly contains: $2"; fi
}

echo "=== scripts/ test suite ==="
echo ""

# ---------------------------------------------------------------- ai-trace-scan.sh
echo "## ai-trace-scan.sh"

out=$(zsh "$SCRIPTS/ai-trace-scan.sh" "$FIX/ai-trace-dir" 2>&1); rc=$?
assert_exit 0 $rc "directory mode runs"
for phrase in "值得注意的是" "本文旨在" "综上所述" "不难发现" "总而言之" "鉴于此"; do
    assert_contains "$out" "▶ 「$phrase」" "directory mode hits planted cliché: $phrase"
done
assert_contains "$out" "「此外」 appears 4 times" "occurrence-count (not line-count): 4×此外 in ONE line trips >3 threshold"
assert_not_contains "$out" "✅" "directory mode does not falsely report clean"
assert_not_contains "$out" "这引发了我们的思考" "--include='*.md' filter excludes .txt files"

out=$(zsh "$SCRIPTS/ai-trace-scan.sh" "$FIX/ai-trace-dir/chapter1.md" 2>&1); rc=$?
assert_exit 0 $rc "single-file mode runs"
assert_contains "$out" "「此外」 appears 4 times" "single-file mode: occurrence-count works"

out=$(zsh "$SCRIPTS/ai-trace-scan.sh" "$FIX/clean.md" 2>&1); rc=$?
assert_exit 0 $rc "clean file exits 0"
assert_contains "$out" "✅" "clean file reports clean"

out=$(zsh "$SCRIPTS/ai-trace-scan.sh" "$FIX/does-not-exist.md" 2>&1); rc=$?
assert_exit 1 $rc "missing path exits 1"
assert_contains "$out" "Path does not exist" "missing path: friendly error"
echo ""

# ---------------------------------------------------------------- pending-checks.sh
echo "## pending-checks.sh"

out=$(bash "$SCRIPTS/pending-checks.sh" "$FIX/pending-markers.md" 2>&1); rc=$?
assert_exit 0 $rc "single-file mode runs"
assert_contains "$out" "6 pending item(s) total" "all 5 marker kinds counted (6 lines total)"
assert_contains "$out" "[待核对]" "待核对 marker found"

out=$(bash "$SCRIPTS/pending-checks.sh" "$FIX" 2>&1); rc=$?
assert_exit 0 $rc "directory mode runs"
assert_contains "$out" "pending-markers.md" "directory mode finds markers with filenames"

out=$(bash "$SCRIPTS/pending-checks.sh" "$FIX/does-not-exist" 2>&1); rc=$?
assert_exit 1 $rc "missing path exits 1"
assert_contains "$out" "Path does not exist" "missing path: friendly error"
echo ""

# ---------------------------------------------------------------- citation-consistency.py
echo "## citation-consistency.py"

out=$(python3 "$SCRIPTS/citation-consistency.py" "$FIX/mixed-citations.md" 2>&1); rc=$?
assert_exit 1 $rc "mixed-format draft exits 1 (issues found)"
assert_contains "$out" "括号类型混用" "detects mixed parenthesis types"
assert_contains "$out" "页码格式不统一" "detects mixed page-number formats"
assert_contains "$out" "混用中英文姓名" "detects EN/ZH name-form conflict for same year"

out=$(python3 "$SCRIPTS/citation-consistency.py" "$FIX/clean.md" 2>&1); rc=$?
assert_exit 0 $rc "clean file exits 0"

out=$(python3 "$SCRIPTS/citation-consistency.py" "$FIX/does-not-exist.md" 2>&1); rc=$?
assert_exit 2 $rc "missing file exits 2"
assert_contains "$out" "File does not exist" "missing file: friendly error, no traceback"
assert_not_contains "$out" "Traceback" "missing file: no bare traceback"

out=$(python3 "$SCRIPTS/citation-consistency.py" "$FIX" 2>&1); rc=$?
assert_exit 2 $rc "directory input exits 2"
assert_not_contains "$out" "Traceback" "directory input: no bare traceback"
echo ""

# ---------------------------------------------------------------- citation-format-convert.py
echo "## citation-format-convert.py"

out=$(python3 "$SCRIPTS/citation-format-convert.py" "$FIX/test.bib" --to chicago 2>&1); rc=$?
assert_exit 0 $rc "valid bib (nested braces + single-line + quoted) exits 0"
assert_contains "$out" "The DNA Story: A Documentary History of Gene Cloning" "nested braces {The {DNA} Story} parsed intact, not truncated"
assert_contains "$out" "A Study of Nested Deeply Braces" "doubly-nested braces parsed intact"
assert_contains "$out" "Quoted Value Entry" "quoted field values parsed"
assert_contains "$out" "Watson" "single-line entry parsed"
assert_not_contains "$out" "this block is a comment" "@comment block not treated as an entry"
n_refs=$(python3 "$SCRIPTS/citation-format-convert.py" "$FIX/test.bib" --to apa 2>/dev/null | grep -c '(')
if [ "$n_refs" -eq 3 ]; then pass "exactly 3 entries converted (no merge, no drop)"; else fail "expected 3 entries, got $n_refs"; fi

out=$(python3 "$SCRIPTS/citation-format-convert.py" "$FIX/broken.bib" --to apa 2>&1); rc=$?
assert_exit 1 $rc "bib with one broken entry exits 1"
assert_contains "$out" "entry skipped" "broken entry explicitly reported, not silently merged"
assert_contains "$out" "Good, A." "good entry still converted alongside the broken one"

out=$(python3 "$SCRIPTS/citation-format-convert.py" "$FIX/does-not-exist.bib" --to apa 2>&1); rc=$?
assert_exit 2 $rc "missing file exits 2"
assert_not_contains "$out" "Traceback" "missing file: no bare traceback"

out=$(python3 "$SCRIPTS/citation-format-convert.py" "$FIX" --to apa 2>&1); rc=$?
assert_exit 2 $rc "directory input exits 2"
assert_not_contains "$out" "Traceback" "directory input: no bare traceback"
echo ""

# ---------------------------------------------------------------- citation-verify.py (offline)
echo "## citation-verify.py (offline)"

out=$(python3 - "$SCRIPTS/citation-verify.py" "$FIX/mixed-citations.md" <<'PYEOF' 2>&1
import importlib.util, sys
spec = importlib.util.spec_from_file_location("cv", sys.argv[1])
cv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cv)
cv.time.sleep = lambda s: None  # no need to be polite to stubs

text = open(sys.argv[2], encoding="utf-8").read()
cites = cv.extract_citations(text)
assert len(cites) == 5, f"expected 5 citations, got {len(cites)}: {cites}"
keys = {(a, y) for a, y in cites}
for expected in [("Foucault", "1975"), ("Bourdieu", "1984"), ("福柯", "1975"), ("Smith", "2010"), ("Li", "2015")]:
    assert expected in keys, f"missing {expected} in {keys}"
print("OK extract_citations: 5 mixed-language citations parsed")

# ERROR verdict: both backends down must NOT become NOT_FOUND
def boom(author, year, rows=5):
    raise cv.QueryError("simulated network down")
cv.crossref_query = boom
cv.openalex_query = boom
res = cv.verify("(Smith, 2010)", verbose=False)
assert res[0]["verdict"] == "ERROR", res[0]["verdict"]
assert "NOT evidence" in res[0]["details"]
assert cv.exit_code(res) == 2
print("OK ERROR verdict: network failure is ERROR (exit 2), never NOT_FOUND")

# NOT_FOUND: both backends reachable, nothing matches
cv.crossref_query = lambda a, y, rows=5: []
cv.openalex_query = lambda a, y, rows=5: []
res = cv.verify("(Smith, 2010)", verbose=False)
assert res[0]["verdict"] == "NOT_FOUND", res[0]["verdict"]
assert cv.exit_code(res) == 1
print("OK NOT_FOUND verdict: empty results from both backends (exit 1)")

# FOUND: verdict must carry title + container so the author can judge
item = {"author": [{"family": "Smith"}], "title": ["A Real Paper"],
        "container-title": ["Journal of Examples"], "DOI": "10.1/x", "type": "journal-article"}
cv.crossref_query = lambda a, y, rows=5: [item]
res = cv.verify("(Smith, 2010)", verbose=False)
assert res[0]["verdict"] == "FOUND", res[0]["verdict"]
assert "A Real Paper" in res[0]["details"], "FOUND details must include the matched title"
assert "Journal of Examples" in res[0]["details"], "FOUND details must include the container"
assert "manually confirm" in res[0]["details"].lower()
assert res[0]["match"]["source"] == "Crossref"
assert cv.exit_code(res) == 0
print("OK FOUND verdict: carries title + container + manual-confirm caveat (exit 0)")

# Cascade: Crossref empty -> OpenAlex answers, source labeled OpenAlex
cv.crossref_query = lambda a, y, rows=5: []
cv.openalex_query = lambda a, y, rows=5: [item]
res = cv.verify("(Smith, 2010)", verbose=False)
assert res[0]["verdict"] == "FOUND"
assert res[0]["match"]["source"] == "OpenAlex"
print("OK cascade: Crossref miss falls through to OpenAlex, source labeled")

# Mixed verdict exit-code contract: ERROR dominates
assert cv.exit_code([{"verdict": "FOUND"}, {"verdict": "NOT_FOUND"}, {"verdict": "ERROR"}]) == 2
assert cv.exit_code([{"verdict": "FOUND"}, {"verdict": "FUZZY_MATCH"}]) == 1
assert cv.exit_code([{"verdict": "FOUND"}]) == 0
assert cv.exit_code([]) == 0
print("OK exit-code contract: FOUND=0 / FUZZY|NOT_FOUND=1 / ERROR=2")
PYEOF
); rc=$?
if [ $rc -eq 0 ]; then
    echo "$out" | while IFS= read -r line; do pass "$line"; done
else
    fail "offline unit tests: $out"
fi

out=$(python3 "$SCRIPTS/citation-verify.py" "$FIX/does-not-exist.md" 2>&1); rc=$?
assert_exit 2 $rc "missing file exits 2"
assert_contains "$out" "does not exist" "missing file: friendly error"
assert_not_contains "$out" "Traceback" "missing file: no bare traceback"

out=$(python3 "$SCRIPTS/citation-verify.py" --help 2>&1)
assert_contains "$out" "1-2 minutes" "--help documents expected runtime"
assert_contains "$out" "Exit codes" "--help documents the exit-code contract"
echo ""

# ---------------------------------------------------------------- deterministic bug regressions
echo "## marker and citation regression tests (offline)"
python3 "$SCRIPT_DIR/test_regressions.py"
rc=$?
assert_exit 0 $rc "bilingual markers, citation verdicts, API shapes, and page styles"
echo ""

# ---------------------------------------------------------------- citation-verify.py (network)
echo "## citation-verify.py (live network)"

if [ "${SKIP_NETWORK:-0}" = "1" ]; then
    skip "live Crossref/OpenAlex round-trip (SKIP_NETWORK=1)"
else
    tmpfile=$(mktemp /tmp/cv-net-XXXXXX.md)
    echo "One citation to look up (Foucault, 1975)." > "$tmpfile"
    out=$(python3 "$SCRIPTS/citation-verify.py" "$tmpfile" --quiet 2>&1); rc=$?
    rm -f "$tmpfile"
    assert_contains "$out" "Total citations parsed: 1" "live run parses the citation"
    if [ $rc -eq 0 ] || [ $rc -eq 1 ] || [ $rc -eq 2 ]; then
        pass "live run returns a contract exit code ($rc)"
    else
        fail "live run: unexpected exit code $rc"
    fi
    assert_not_contains "$out" "Traceback" "live run: no bare traceback"
fi
echo ""

# ---------------------------------------------------------------- summary
echo "=== Summary: $PASS passed, $FAIL failed, $SKIP skipped ==="
[ $FAIL -eq 0 ]
