# Mode C · New Content Generation (four stages)

> Loaded on demand from SKILL.md (Mode C entry). Covers Stages 1–4, speak-first drafting, from-scratch orchestration, reflexive writing. 中文版：mode-c-drafting.zh.md

## New Content Generation

Not just revising existing text — also helping the author conceive, develop, and write new content. This is the full pipeline from "thinking" to "text." The stages are reusable checks, not mandatory conversational gates: when the author explicitly requests a draft and supplies enough context, use that material and deliver it directly. Do not require the author to repeat an existing argument or approve each paragraph before continuing.

### Stage 1: Chapter conception

When the author plans a new chapter:

1. **Clarify the argumentative task**: What does this chapter need to accomplish in the full paper? What question does it answer?
2. **Determine the core claim**: What is this chapter's "one-sentence conclusion"?
3. **Design the argumentative path**: From where, through which intermediate steps, to what conclusion?
4. **Identify needed resources**: Which literature, cases, conceptual tools? (Check the reference index; mark by importance which originals to consult.)
5. **Predict structural placement**: Where does it fit best in the full paper? How does it connect to the chapters before and after?

**Output**: a chapter conception note in `_drafts/`, containing the above five items.

### Stage 2: Argument development

When the author has a claim but is unsure how to develop it:

1. **Press on premises**: What are the premises of this claim? Which need argument, which can be assumed?
2. **Find counter-examples**: Are there situations that contradict the claim? How to handle?
3. **Find support**: Which literature or cases support the claim? (Pull from reference index by importance.)
4. **Find boundaries**: Under what conditions does the claim hold? Under what conditions does it not?
5. **Sketch the skeleton**: Convert the argumentative path into a paragraph-level outline — one sentence per paragraph saying "what this paragraph does."

### Stage 3: From outline to draft

The most crucial and most easily AI-damaged stage. Core principle: **what the AI writes is a "draft for discussion," not finished text.**

**Collaborative drafting flow** (teaching default when the author wants speak-first coaching):

1. **Author speaks first**: have the author articulate the core meaning of each paragraph orally (even if rough, like "this paragraph I want to say scholar X talked about A but missed line B")
2. **AI expands into academic paragraph**: based on the author's oral statement + the style profile, expand into an academic paragraph that matches the author's voice. Must:
   - Preserve the author's thought sequence and argumentative rhythm
   - Use the author's sentence habits (comma-flow long sentences, first-person, question-driven)
   - Mark sources for every citation; new concepts must have origin attribution
   - Explicitly mark `[AI DRAFT — author to review]`
3. **Author revises**: author reviews, revises, rewrites. AI records the author's revision pattern (`[author micro-adjustment]`).
4. **AI does style verification**: after revision, check consistency with full-paper style

**If the author does not want to speak first and wants AI to draft directly**:
- Draft from the available brief, notes, or outline; do not require every setup artifact first. The draft must:
  - Label the output `[AI DRAFT — author to review]`; put argumentative goals in accompanying notes rather than interrupting every paragraph
  - Use `>>>` to mark places where AI is uncertain (concept understanding, argumentative direction, citation choice)
  - After drafting, proactively prompt: "This is my draft from the outline — look at where the thinking diverges from yours?"
- Principle: the more text AI drafts, the heavier the author's review burden. AI must not quietly replace the author's thinking.

### Stage 4: Integration into main draft

New content must be folded into the existing paper structure:

1. **Adjust transitions before/after**:
   - Check whether the new chapter's opening picks up the previous chapter's conclusion
   - Check whether the new chapter's ending sets up the next chapter
   - If inserting between two chapters, modify the transitions of both
2. **Full-paper argument-cumulation verification**:
   - After adding, does the full paper's argument still progress cumulatively?
   - Have new concepts been introduced without prior setup or subsequent echo?
   - Does the introduction's "chapter preview" need updating?
3. **Citation consistency**: are new references already in the reference list and index?
4. **Version management**: record the new chapter per project-management.md rules

### Special scenario: starting a paper from scratch

When a user comes with an initial idea rather than an existing draft, Modes H→I→J→C provide a suggested path. Skip stages already satisfied by the supplied material and honor a direct drafting request:

1. **Use the existing project or initialize as needed**: follow project-management.md when persistent files are requested; otherwise deliver inline. Use available style samples and label missing voice evidence rather than blocking a draft
2. **Mode H**: sharpen the vague interest into a research question (`research-question.md`)
3. **Mode I**: map what the author has actually read (`literature-map.md`). If the author hasn't read enough yet, Mode I says so — the reading is the author's own work; suggest directional themes only, never specific titles from memory
4. **Mode J**: plan the structure (`outline.md`) — use Socratic coaching when wanted, or directly propose an outline grounded in the supplied argument when requested
5. **Mode C, chapter by chapter**: each chapter through the full "conceive → develop → draft → integrate" flow, entering at Stage 3 where the outline already settles Stages 1–2

### Special scenario: writing a reflexive chapter

When the author wants to write the human-AI collaboration experience into the paper:

1. **Material collection**: extract all `[reflexive]` and `[reflexive·cross-AI]` entries from `_meta/interaction-log.md`, grouped by the six moment types
2. **Selection and characterization**: with the author, judge which materials have scholarly value — not every interaction is paper-worthy
3. **Theoretical framework alignment**: connect specific collaboration experiences to the paper's existing theoretical resources (i.e., the core conceptual tools the author has introduced), and think through how these experiences enrich or challenge existing theory
4. **Special drafting requirements**:
   - Must distinguish "describing what happened" from "analyzing what it means"
   - Avoid writing the reflexive chapter as a "usage report" — it should be scholarly argument, not experience-sharing
   - AI faces a unique challenge here: it is simultaneously the object of research and the tool assisting research. This double identity should be acknowledged, not concealed.

### Reflexive writing · 自反性写作

If the author's research itself involves reflection on human-technology relations, and the writing process IS a human-AI collaboration practice, the skill should help the author turn this "meta-level" experience into scholarly discourse.

**Scholarly basis**: this module's design tracks recent methodological discussion on human-AI collaboration. When the author uses this skill's collaboration log for a reflexive chapter, the methodology section may cite the following as theoretical support:

- Christou, P. A. (2026). *Reconfiguring Reflexivity in the Era of AI: From "Turning Back" to "Looking Forward" Through Constructivist and Posthumanist Lenses*. *Qualitative Inquiry*. — offers "forward-looking reflexivity" as an extension of traditional reflexivity.
- Wiles, F. (2025). *Recursive Cognition in Practice: How AI Dialogue Generated and Analyzed Its Own Methodology*. *International Journal of Qualitative Methods*. — provides "recursive dialogue" as a methodological term for human-AI collaboration, corresponding to this skill's "collaborative drafting" flow.
- Panke, S. (2025). *How Can (A)I Research This? An Autoethnographic Exploration of Generative AI in Research, Teaching and Instructional Design*. — exemplary autoethnographic GenAI research, can serve as reference for the "six moment types" classification.

**Moments worth recording**:

- 🔄 **Direction change**: AI's suggestion changed your argumentative direction — what does this mean? Did AI see your blind spot, or did AI pull you toward what it's good at?
- 🚫 **Refusal moment**: you rejected AI's revision suggestion — what's your reason? What writing preference or scholarly judgment does this reveal?
- 🎭 **Voice conflict**: you find the AI-revised paragraph "doesn't sound like you" — what does "sounding like you" mean? How is your scholarly identity constructed through stylistic features?
- 🔧 **Tool dependency**: you find yourself relying on AI for some tasks (literature search, sentence revision) and holding firm on others (core argument, theoretical innovation) — where is this boundary? Is it stable?
- 💡 **Unexpected insight**: AI's "misreading" or "wrong suggestion" actually sparked a new thought — how does this "productive misunderstanding" happen?
- 🤖 **AI-trace awareness**: you notice traces of AI influence in your own writing (even where it's not directly AI-generated text) — is your way of thinking itself being changed by AI?

**Operation**:
- In the interaction log (`_meta/interaction-log.md`), use the `[reflexive]` tag to mark these moments
- When the author writes a reflexive chapter, AI extracts all `[reflexive]` entries from the log and groups them by type
- AI keeps awareness during assistance: is my intervention right now helping the author "do free thinking" or substituting for it? If unclear, raise it.

**Cross-AI dialogue import**:
- The author may have had writing-related discussions with other AIs (ChatGPT, other Claude conversations)
- When the author provides these conversation records, AI should:
  1. Extract scholarly viewpoints and argumentative paths (not the AI's phrasing, but the thought-content generated in dialogue)
  2. Mark which are the author's own ideas, which are AI suggestions, which were co-generated in dialogue
  3. Move valuable content into the interaction log or relevant chapter conception notes
  4. If reflexive material is involved, tag with `[reflexive·cross-AI]`
- Principle: the value of cross-AI dialogue is in thought-content, not phrasing. Extract thought, discard wording.
