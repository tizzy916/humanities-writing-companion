# Mode F · Draft Revision (two-version comparison)

> Loaded on demand from SKILL.md (Mode F stub). 中文版：mode-f-revision.zh.md

### Mode F: Draft revision (two-version comparison)

When the author brings an existing draft (e.g., an AI-polished version) for systematic revision. This is an independent workflow; the core challenge is **preserving structural improvements of the draft while removing AI traces and restoring the author's own voice**.

**Prerequisites**:

- The draft file (e.g., an AI-polished version the author has not yet reviewed)
- An original version (the author's early manuscript without AI intervention, for true-voice comparison)
- Style profile already established

**No-original fallback**: when no pre-AI manuscript exists, steps 3a–3b have no baseline. Use the available style profile and the author's stated argument or notes; ask for a restatement only when the intended claim is genuinely missing. On an explicit revision request, proceed within that scope and deliver flagged diffs. Explain that original-voice comparison is unavailable. Rewriting does not erase earlier AI use or change its disclosure record (see Mode K).

**Thin or missing style profile**: state the limitation. Use existing samples where available; otherwise perform the requested limited revision without claiming to restore the author's authentic voice. A short profile interview is optional when the author wants closer voice matching, not a gate for every revision.

**Workflow**:

1. **Read through the draft**: build holistic understanding, mark AI-trace-dense zones
2. **Develop a revision plan**: per chapter, list issue types (AI traces / citation norms / argument reinforcement / structural adjustment), order by priority
3. **Chapter-by-chapter revision** (each chapter follows):
   - 3a. **Compare with original**: what did the original say in this chapter? What did the draft preserve? What was changed?
   - 3b. **Judge each change**: is this change an "improvement" (clearer structure, better citation norm) or an "alienation" (loss of voice, AI cliché introduced)?
   - 3c. **Execute revision**: keep improvements, restore alienated parts (from original or by rewriting in author's voice)
   - 3d. **Unexamined-pattern scan**: use `ai-trace-checklist.md` item by item
   - 3e. **Voice verification**: read the revised paragraph aloud — does it sound like the author?
   - 3f. **Over-imitation check**: signature features (first person, comma-flow long sentences, rhetorical questions) must not exceed their base rate in the author's own samples — a de-AI-ed paragraph that *caricatures* the author is still alienation (see the reverse check in ai-trace-checklist.md)
4. **Citation format unification**: per style profile's "normative issues" table, item by item
5. **Create version snapshot**: after each chapter's revision, create a minor version per project-management.md

**Key principles**:

- Work in manageable chapter batches. If the author requests a full revision, continue through the authorized scope; if practical limits prevent completion, name the exact remainder instead of treating a fixed chapter count as a stopping rule.
- Revision is not "polish" — it involves argumentative-level judgment and must operate under the four-layer critique guidance.
- When both versions are unsatisfactory, propose or apply a reasoned rewrite within the authorized scope. Ask only if choosing between incompatible interpretations would change the author's intended claim; do not re-request permission paragraph by paragraph.
- Every revision is recorded in the revision log, marked "restored original expression" / "kept draft improvement" / "rewritten."
- In chat-only environments (no file system), deliver diffs inline and say explicitly that snapshots/logs are skipped — never skip them silently.

#### Mode F.coach sub-mode: revision-coach (don't give the answer)

Standard Mode F directly proposes revised text after each diagnosis. **Mode F.coach is a variant**: instead of giving the revised text, the skill gives the author **a set of diagnostic questions** about the problematic passage. The author answers them — then, and only then, does the skill propose revision options.

**Why this matters**: pedagogically, getting the answer too quickly prevents the author from developing the diagnostic muscle. A scholar should not need the skill in five years; Mode F.coach trains the author to internalize the four-layer critique.

**When to engage Mode F.coach**:
- Author asks: "teach me how to see this myself"
- Author is early-career and the same revision pattern keeps recurring (the skill notices in the revision log) — in this case, *propose* coaching and get a yes before switching; no silent mode switch
- Author says "I keep making the same mistake — help me learn to catch it"

**Workflow** (replaces the "execute revision" step in standard Mode F):

After diagnosing a passage problem, **do NOT immediately propose a revision**. Instead:

1. **Issue 3–5 diagnostic questions** at the relevant critique layer:
   - L1 questions: "What is this paragraph trying to claim, in one sentence? If you removed this paragraph, what would be lost in the argument?"
   - L2 questions: "What does this paragraph do in the chapter? Is the next paragraph picking up where this one left off, or jumping?"
   - L3 questions: "Where is the topic sentence? Does the rest of the paragraph stay with it, or does it drift?"
   - L4 questions: "Read the sentence aloud. Where does your breath naturally pause? Does the punctuation match?"

2. **Wait for author response**. Do not anticipate, do not preemptively answer.

3. **After author answers**, name what the author noticed:
   - "You said the paragraph is trying to claim X. Re-read it — does it actually claim X, or something narrower?"
   - "You said the topic sentence is sentence 2. The rest of the paragraph mostly comments on sentence 4 — there's a drift."

4. **Now propose revision** — but ideally, by this point, the author has already seen the revision. Confirm rather than impose.

5. **Record in revision log** with tag `[coached]` so the pattern is visible across sessions.

**Mode F.coach is slower than Mode F.** A revision that takes 5 minutes in standard Mode F may take 20 minutes in coach mode. The trade is depth of author skill, not speed.

**Switching**: author can say "skip coaching — just give me the revision" at any point. Respect immediately.
