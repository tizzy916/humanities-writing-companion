#!/usr/bin/env bash
# pending-checks.sh — Extract all "to verify" / "to discuss" / "AI uncertain" markers in a paper project
# Usage: ./pending-checks.sh <path>   # path can be a single file or a paper project directory

set -euo pipefail

INPUT="${1:-.}"

[ -e "$INPUT" ] || { echo "Path does not exist: $INPUT" >&2; exit 1; }

if [ -d "$INPUT" ]; then
    GREP_OPTS=(-rn --include='*.md')
    GREP_COUNT_OPTS=(-rh --include='*.md')
else
    GREP_OPTS=(-n)
    GREP_COUNT_OPTS=(-h)
fi

# Keep the detail report and summary on the same bilingual marker definitions.
VERIFY_PATTERN='\[(待核对|VERIFY)\]'
DISCUSS_PATTERN='❓[[:space:]]*(待讨论|to discuss)'
DRAFT_PATTERN='\[(AI 草稿(，待作者审阅)?|AI DRAFT|AI draft, pending author review)\]'
UNCERTAIN_PATTERN='>>>'
TWEAK_PATTERN='\[(作者微调|author micro-adjustment)\]'

echo "=== Pending-marker summary · $INPUT ==="
echo ""

scan_marker() {
    local label="$1"
    local pattern="$2"
    local desc="$3"

    echo "## $label"
    echo "_${desc}_"
    echo ""
    if matches=$(grep "${GREP_OPTS[@]}" -E -- "$pattern" "$INPUT" 2>/dev/null); then
        echo "$matches" | sed 's/^/  /'
    else
        echo "  (none)"
    fi
    echo ""
}

scan_marker "🔴 [待核对] / [VERIFY] (to verify)" \
    "$VERIFY_PATTERN" \
    "AI quotes from memory, unverified facts, unconfirmed data, etc. — must be cleared to zero before submission"

scan_marker "🟡 ❓ 待讨论 / ❓ to discuss" \
    "$DISCUSS_PATTERN" \
    "Argumentation choices and theoretical-direction questions that the author must decide"

scan_marker "🟢 [AI 草稿，待作者审阅] / [AI DRAFT] (AI draft, pending author review)" \
    "$DRAFT_PATTERN" \
    "Paragraphs drafted by AI that the author has not yet reviewed — remove the marker once reviewed"

scan_marker "🔵 >>> AI 不确定 (AI uncertain)" \
    "$UNCERTAIN_PATTERN" \
    "Spots where the AI was unsure while drafting (concept understanding / line of argument / choice of citation)"

scan_marker "🟣 [作者微调] / [author micro-adjustment] (author tweak)" \
    "$TWEAK_PATTERN" \
    "The author's second-pass adjustments to AI suggestions — the most precise style signal; should be written back to the writing-style profile"

# Summary statistics
echo "## 📊 Summary"
total=0
for marker in "$VERIFY_PATTERN" "$DISCUSS_PATTERN" "$DRAFT_PATTERN" "$UNCERTAIN_PATTERN" "$TWEAK_PATTERN"; do
    c=$( (grep "${GREP_COUNT_OPTS[@]}" -E -- "$marker" "$INPUT" 2>/dev/null || true) | wc -l | tr -d ' ')
    [ "$c" -gt 0 ] && total=$((total + c))
done
echo "  $total pending item(s) total"
