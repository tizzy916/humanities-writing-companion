# Pre-submission Modes · Mode G (blind reading) & Mode K (AI-use disclosure)

> Loaded on demand from SKILL.md (Mode G/K stubs). 中文版：modes-submission.zh.md

### Mode G: Blind reading (promise-delivery mechanism)

**What's unique about this mode**: AI temporarily **turns off scholarly judgment** and only mechanically checks "did the author do what they said they would do?" Borrows from Thesify's Purpose-Check design — avoid AI's subjective processing, let the author themselves see whether the paper delivered on its promises.

**Context isolation must be real**: not reading `_writing-config/` does not erase author context already present in the conversation. When available, use a fresh reviewer agent with no inherited history, giving it only the manuscript and these checking instructions; do not supply the author's intended argument, earlier discussion, or profiles. State what it received. If an isolated run is unavailable, deliver a **promise-delivery check in the current context** and disclose that author-intent isolation was not achieved. Neither form is anonymous peer review. Promise extraction and matching still require interpretation; flag borderline calls.

**When to engage**:

- After a chapter draft is complete ("I just finished Chapter 3, run blind reading")
- Before final submission ("one more promise-delivery pass before submission")
- After large revisions (structural changes may have unhooked previously-delivered promises)
- Author's intuition "something's off but I can't say what" — often an implicit promise was not delivered

**Workflow**:

0. **Completeness pre-check**: blind reading assumes a draft with an ending. If the text stops mid-way or contains author-facing alternatives (A/B forks, `>>>` markers, scaffolding sections), either defer the run or mark the affected promises "not yet written — excluded" instead of ❌. Exclude AI-workflow markers (`[AI DRAFT]`, `>>>`, source-note sections) from promise extraction entirely.

1. **Extract promises** (mechanical operation):
   - Scan introduction, chapter openings, section openings
   - Find all sentences of the form:
     - "This paper will..."
     - "This chapter will explore..."
     - "This section first... then... finally..."
     - "I will argue..."
     - "Below, in three parts, I respond to this question:..."
   - Record each promise with source location (chapter / paragraph)

2. **Check delivery** (mechanical operation):
   - In conclusion / chapter end / section end, look for corresponding response
   - **Delivery may be distributed**: a chapter-opening claim can be delivered progressively across the body rather than at the end — search the whole span and cite where
   - **Don't evaluate quality** — only judge "is there a response?"
   - Partial delivery (said A, B but not C) also explicitly noted

3. **Output format**:
   ```
   === [Isolated reading / Current-context promise-delivery check] · [chapter] ===
   Context: [fresh agent; manuscript only / existing conversation retained]

   ## ✅ Promises delivered
   - Promise: "this chapter will explore the tension between X and Y" (§1 ¶2)
     Delivery: §5 ¶3-4 directly handle the tension

   ## ⚠️ Partially delivered
   - Promise: "this section answers in three parts: A, B, C" (§3 ¶1)
     Delivery: A in §3.1, B in §3.2, but no corresponding section for C

   ## ❌ Promises not delivered
   - Promise: "I will return to scholar Z's critique in the conclusion" (intro ¶5)
     Delivery: not found — conclusion does not mention Z

   ## 🤔 Implicit promises (AI inference, may be wrong)
   - Chapter-opening introduces a core concept but chapter-end never returns to it — should there be closure?
   ```

4. **Key constraints — things AI does NOT do in this mode**:

   - Does not evaluate "is this promise scholarly worthwhile" — that's Layer 1 (foundation) work
   - Does not suggest rewriting un-delivered promises — only flags the "promise-delivery gap"
   - Does not write the missing responses — leaves to author whether to add delivery or retract promise
   - Does not load `_writing-config/` files for this check; claims of author-context isolation require a genuinely fresh run as specified above

**Why this mode is valuable**: writing over long periods causes "promise drift" — the promises in the intro get replaced by discoveries in the argumentative process, but the author doesn't feel it. Blind reading is a mirror, placing the "original promise" and "actual delivery" side by side.

**Comparison with other modes**:
- Mode B chapter review: evaluates quality
- **Mode G blind reading: only checks delivery** — narrower, more mechanical, less prone to error

---

### Mode K: AI-use disclosure (target-policy check)

Draft a factual record of AI use and adapt it to the **current policy of the target journal or institution**. Do not generalize about how permissive humanities or STEM journals are. This skill's categories are an internal audit aid, not a publishing standard or evidence that a use is permitted.

**When to engage**:
- Before journal submission or dissertation deposit
- When the author asks what to disclose about AI use

**Workflow**:

1. **Audit actual uses**, including earlier drafts and other tools:
   - Read `_meta/interaction-log.md`, `_meta/revision-log.md`, available drafts, and any reflexive notes.
   - For each use, record tool/version if known, date or period, function, affected material, and how the author reviewed or reworked it. Write `unknown` for missing details.
   - Record both historical use and what survives in the current manuscript. Who requested an edit does not establish whether AI generated its wording.

2. **Optional internal categories (Tier 0–4; five labels)**:
   - **Tier 0 · No AI involvement**: the available record supports no AI use in preparing the manuscript. Missing logs do not establish Tier 0.
   - **Tier 1 · Proofreading / translation / formatting**: record the exact function and whether generated wording or translation was adopted; a translation can contain substantial AI-generated language.
   - **Tier 2 · Thinking partner / review**: Socratic dialogue, brainstorming, outlining, adversarial review, or promise-delivery checking. Record conceptual or structural contributions even without prose drafting.
   - **Tier 3 · Prose drafting or suggested wording**: AI drafted passages or proposed wording during preparation; record what was incorporated, discarded, or subsequently rewritten.
   - **Tier 4 · Extensive prose drafting**: AI drafted large parts of the manuscript. Describe the extent only at the granularity the records support; there is no universal percentage threshold.
   These labels summarize functions and extent; they are not a universal risk ranking. Keep all applicable uses visible. The target policy may classify translation, rewriting, or conceptual work differently.

3. **Verify the target's current policy — never from memory.** Read the official policy in a web-capable environment, or use policy text supplied by the author and label its provenance. Record the URL/title, retrieval date or supplied version, applicable clauses, and any uncertainty about currency. Compare **actual uses** to the policy's own terms, including required wording and placement. If the policy cannot be verified or leaves a use unclear, deliver a factual disclosure draft marked `policy compatibility unverified`; do not invent a conservative rule or claim compliance. Flag only conflicts supported by the verified policy.

4. **Draft from the audit, using the target's required form where available**:

   **Short template**:
   > In preparing this manuscript, I used [tool/version, if known] during [period] for [specific functions and affected material]. [State accurately whether wording, translations, ideas, or structure were adopted and how they were reviewed.] The author is responsible for the final manuscript.

   **Detailed template**:
   > **AI use disclosure.** During preparation, I used [tool/version, period] for [specific use 1], [specific use 2], and [specific use 3]. In [sections], [records-supported extent] was [AI-drafted / translated / revised with AI]. The author [specific review and reworking]. [If relevant: earlier AI-generated drafts were discarded and the passages were redrafted; describe this without deleting the earlier use.] The author is responsible for all claims, citations, and final wording.

   An optional appendix may use:
   > | Section/material | Actual AI function and period | What was retained or discarded | Author review/reworking | Evidence or uncertainty |
   > |---|---|---|---|---|
   > | §2 | First draft from the author's outline | [actual disposition] | [actual review] | [log/draft or reconstructed account] |

   Do not include a blanket “AI generated no prose” statement unless the record supports it; proofreading and translation can also introduce wording. Do not call a style scan proof of authorship or provenance.

5. **Placement**: follow the verified journal or institutional instructions. If placement is unknown, keep the statement as a separate draft with placement pending; do not present acknowledgments, a footnote, a cover letter, or a declaration page as a universal default.

6. **Save to** `_meta/AI-use-statement.md` (Chinese: `AI 使用披露.md`), or deliver inline when file output is unavailable or not requested. Mark author review and policy-verification status separately.

**Author verification prompts** (ask only about gaps not already answered):
- Were there other tools, functions, or earlier drafts missing from the audit?
- Which generated wording, translation, ideas, or structural suggestions were adopted?
- Are any dates, versions, or quantities uncertain?

**Hard constraints**:
- Do not omit actual use to make a manuscript appear compatible with a policy. Correct factual overstatement as readily as understatement; wanting clearer wording alone is not evidence of misconduct.
- Describe specific AI functions without assigning AI authorship or inferring a journal's rule about it. Use the verified target policy for submission requirements.
- If a single internal summary label is useful, retain the highest historical Tier alongside the detailed use record. It is not a journal eligibility verdict; non-prose structural contributions remain visible as Tier 2.
- **Rewriting, removing an AI draft from view, and passing `ai-trace-scan` do not erase historical AI use or justify downgrading the disclosure record.** Record the rewrite as a later event. Whether earlier use must appear in the submitted statement depends on the verified target policy; never infer an exemption from stylistic similarity or a scanner result.
- **Missing or partial logs**: reconstruct the history with the author, label it as a reconstruction, and retain uncertainties. Do not fabricate percentages or turn absence of records into absence of AI use.
- The author remains responsible for the submitted manuscript; local checks do not establish journal acceptance or policy approval.
