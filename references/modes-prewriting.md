# Pre-writing Modes · Mode H (research question) · Mode I (literature map) · Mode J (outline)

> Loaded on demand from SKILL.md (Mode H/I/J stubs). 中文版：modes-prewriting.zh.md

### Mode H: Research-question sharpening (Socratic)

The earliest-stage mode. Author has an interest, a topic, or a vague sense of what they want to say — not yet a defensible research question. Mode H turns vague interest into a sharp, write-able question through Socratic dialogue.

**Crucial: this is NOT PICO, NOT hypothesis-testing.** Humanities research questions follow different shapes. Generic AI scoping prompts will produce empty STEM-flavored questions. Mode H operates inside the humanities conventions.

**When to engage**:
- "我想研究 X / I want to do something on X" (vague)
- Before a proposal / dissertation prospectus
- When stuck between several possible directions
- When the author has a draft but realizes the question driving it isn't sharp

**Workflow** (a teaching default, not a required number of turns):

Use Socratic dialogue when the author wants to develop their own question. When they explicitly request candidate questions or a draft and supply enough context, produce the requested result directly, label tentative claims and evidence gaps, and retain their final scholarly judgment. Reuse answers already supplied; ask only for information that materially blocks the task.

1. **Locate the field**: which discipline (or which inheritance, e.g., "intellectual history = history + philosophy")? What sub-area within it? **Read `_writing-config/discipline.md`** if it exists. Otherwise use the manuscript and the object/method already described by the author; state any provisional inference. Ask only if the discipline cannot reasonably be inferred and the answer would change the analysis, not merely because a file is missing.

2. **Find the puzzle**:
   - What is contested? What do scholars currently disagree about in this area?
   - What is undertheorized? What is described but not analyzed?
   - What is over-saturated? Where is one more paper on the same thing not going to add value?
   - What's been emerging recently that the older literature missed?

   **Anti-fabrication rule (mirrors Mode I's iron rule)**: map the puzzle from what the *author* reports reading. Pose candidates as questions ("is there a live debate over X in your area?"), never assert specific works, positions, or debates from memory; if you must name one, tag it `[VERIFY]`. Ask one question at a time — the four probes above are a menu, not a volley.

3. **Identify the type of humanities research question**. Most humanities questions fall into one of three types — name the one this question belongs to (hybrids are fine: name a primary and a secondary):
   - **Re-reading** (重读): a classic text / thinker / event read against the dominant interpretation
   - **Re-construction** (重构): assembling or re-organizing a tradition / genealogy / debate
   - **Intervention** (介入): bringing historical / conceptual resources into a current debate

4. **The "so what" test**: ask the author to complete: "If I succeed in answering this question, then ___ (which scholarly conversation moves, which assumption gets challenged, which gap closes)?" If the author can't complete it, the question is not yet sharp.

5. **Identify the real interlocutor**: who is the strongest opponent? Who would say "we already know this" or "you're wrong"? **The interlocutor is more important than the topic** — a question without an interlocutor is not a research question, it's a topic. If the author can only point to "the standard narrative," accept a placeholder — "the standard account as represented in [a textbook/review the author names]" — and mark it for sharpening in Mode I.

6. **Sharpen the verb**: vague questions use vague verbs ("explore," "examine," "discuss"). Sharp questions use specific verbs ("argue against," "re-interpret," "show that," "trace the genealogy of," "complicate the standard reading"). Push the author to commit to a verb.

7. **Output to `_writing-config/research-question.md`** (Chinese: `研究问题.md`):
   ```markdown
   # Research question (Mode H output, v1)

   ## Field
   [discipline + sub-area, with inheritance if applicable]

   ## Question type
   [re-reading / re-construction / intervention]

   ## The question (single sentence, sharp verb)
   [e.g., "I will argue that Stiegler's reading of Heidegger's pharmakon obscures the political stakes Plato originally encoded."]

   ## What's at stake (so-what)
   [1-2 sentences]

   ## Real interlocutor
   [name + position they would defend]

   ## Tentative claim
   [the answer-shape, not yet defended]

   ## Open: things I still need to figure out
   - …
   ```

**Crucial constraints**:
- Keep the author responsible for the final question. You may propose candidate formulations when requested; distinguish their stated commitments from AI-proposed possibilities.
- Until the so-what test is answered concretely, label the question provisional rather than validated.
- If the input is a topic (e.g., "I want to write about Foucault and AI"), help narrow it. When requested, provide a provisional question or exploratory draft with explicit assumptions instead of blocking all progress.

**Stalemate exit**: if the so-what test remains unresolved, record what is missing without assuming the cause is under-reading. Save the provisional question and open items in `research-question.md`; offer Mode I, targeted reading, or an exploratory draft according to the author's request. Do not keep pressing through repeated rounds.

**Mode-switching hints**:
- Question sharp enough → switch to **Mode I** (literature mapping: who else has fought over this)
- Question sharp, literature already known → switch to **Mode J** (plan the paper)
- Question sharp, ready to write → switch to **Mode C** (drafting)

---

### Mode I: Literature mapping

Organizes what the author has already read into a working map. **Iron rule: this mode does NOT do literature search for the author.** AI lit-search creates citation hallucination and replaces the irreducible scholarly work of reading. Mode I is downstream of reading, not a substitute for it.

**When to engage**:
- Before writing a literature-review section
- When the author has read several references but cannot yet articulate how they relate
- When the author needs to position their argument against existing positions
- After Mode H, when the question is sharp and now needs to be located in a conversation

**Workflow**:

0. **Use the declared discipline or infer it from the supplied text and method**; read `_writing-config/discipline.md` when available. Ask only when reasonable inference is impossible and the answer would change the map — its shape is discipline-specific: art history may organize by generations, media, or curatorial-theoretical layers rather than camps; primary sources, artist writings, and catalogs sit in a different layer from secondary scholarship.

1. **Use references the author has actually read**, with available notes or excerpts. There is no minimum count: adequacy depends on the question and scope. An 8–15-work set can be a manageable teaching exercise, not an admission requirement. Format is flexible: names + works or full citations. Merge bilingual names for the same scholar into one entry (巫鸿/Wu Hung). **For a small set, produce a provisional map and state its coverage limits; identify needed reading by topic without inventing titles. With no works or notes at all, offer an empty mapping template and identify the missing input.**

2. **Group by intellectual lineage / school / camp** (this is the central skill). Ask the author:
   - Who would these scholars cite each other approvingly?
   - Who would oppose whom?
   - What are the camps / traditions / debates that organize this field?

   If the author cannot articulate the relations — which is often exactly why they came — you may propose candidate groupings, built **only** from the works the author listed, each tagged `[my reading — unverified]`, for the author to confirm, correct, or reject. The author's confirmation, not your memory, is what enters the map. Camps are also not the only shape: generations, medium genealogies, or method traditions may organize the field better — say which shape you're using and why.

3. **Map oppositions and dialogues**. Output a structure like:
   ```
   Camp A (X-ian / X-tradition): [scholar1, scholar2, scholar3]
     ↕ disagrees with
   Camp B (Y-ian / Y-tradition): [scholar4, scholar5]
     ↕ ignored by
   Camp C (Z-ian / Z-tradition): [scholar6, scholar7]
     [Camp C operates in a different language game; not really in the same debate]
   ```

4. **Locate the author's position**:
   - Which camp does the author write from? Which camp does the author oppose?
   - Is the author trying to broker between camps? Reframe the whole debate?
   - **Be honest with the author**: sometimes authors think they're in camp A but their actual moves put them in camp B. Surface this gently.

5. **Gap detection** (without doing literature search):
   - "You cite [scholar X] from Camp A but not [scholar Y from Camp A] — deliberate? Y is usually read alongside X."
   - "You don't cite anyone from Camp B — is this a deliberate intervention or an oversight?"
   - **Never assert a scholar / work the author hasn't mentioned exists** — only ask whether they considered it. If the author hasn't read it, they go read it; the AI doesn't fill in.

6. **Optional: scholar-wendao integration**. If the author cites a specific scholar 3+ times and that scholar's framework is load-bearing for the argument, suggest:
   > "I notice you cite Stiegler 5 times — his framework seems load-bearing. Want to generate a `stiegler-perspective` skill via [scholar-wendao](https://github.com/tizzy916/scholar-wendao-skill) and use it as Reviewer X in Mode D?"

7. **Output to `_writing-config/literature-map.md`** (Chinese: `文献地图.md`):
   ```markdown
   # Literature map (Mode I output, v1)

   ## My position
   [camp / orientation, with key allies and opponents]

   ## Camp A: [label]
   - Scholar 1 (work, year) — core claim relevant to my paper (provenance: author-stated / AI-memory `[VERIFY]`): …
   - Scholar 2 (work, year) — …

   ## Camp B: [label]
   - …

   ## Key debates (the conversations my paper joins)
   1. Debate over X: A says ___, B says ___, my move: ___
   2. …

   ## Open gaps (things I should read more of)
   - …

   ## Possible scholar-wendao perspectives
   - [scholar X] — would be Reviewer X in Mode D for stress-testing
   ```

**Crucial constraints**:
- Never invent a reference / citation / scholar / work the author hasn't named.
- Never summarize a work the author hasn't named. (You can ask "have you read Y on this?" — but don't tell the author what Y says.)
- Gap-probing questions that name a scholar the author hasn't mentioned must carry low-confidence framing ("I may be misremembering — worth checking whether…") — a confidently-asked question can plant a phantom reference as effectively as an assertion.
- Cold start (no project structure yet): use an established project path when available. If persistence is requested but no path is known, ask for the location; otherwise deliver the map inline. Do not invent a directory location.
- The mode helps **organize**, not **discover**.

**Mode-switching hints**:
- Map complete → **Mode J** (plan the paper against the mapped conversation)
- Mapping reveals the question isn't sharp → back to **Mode H**
- Coverage is limited → deliver a provisional map, name the gaps, and suggest targeted reading

---

### Mode J: Plan-only outlining

Pure outline mode — no draft writing. Extracted from Mode C so the author can plan without inadvertently triggering drafting. **Discipline-aware**: pulls discipline-specific standard arcs from `_writing-config/discipline.md`.

**When to engage**:
- "Help me outline a chapter on X" / "I need to plan this paper" / "What structure should this take?"
- After Mode H + Mode I (research question + literature mapped) — Mode J is the natural next step
- When restructuring an existing draft

**Workflow**:

1. **Confirm scope**: chapter / full paper / dissertation / book proposal / book chapter? **Length matters** — a 6,000-word journal article and a 25,000-word dissertation chapter have entirely different arc shapes.

2. **Read context**:
   - `_writing-config/discipline.md` for discipline-specific arc
   - `_writing-config/research-question.md` if exists (Mode H output)
   - `_writing-config/literature-map.md` if exists (Mode I output)
   - `_writing-config/reader-profile.md` for target audience

   Missing files do not imply missing context: first use the supplied manuscript, notes, and prior author statements to identify discipline, question, literature, and audience. State reasonable provisional inferences. Ask only when a necessary fact cannot reasonably be inferred and would change the outline. If the claim itself remains unclear, mark it provisional and identify that gap; do not rerun onboarding solely because `research-question.md` is absent.

3. **Apply discipline-specific arc**. Each L1 main discipline has a recurring rhetorical structure. L3 cross-disciplinary fields and adjacent fields combine multiple L1 arcs with their own overlays. Use these as starting templates (the author can deviate, but the deviation should be a choice not an oversight):

   **L1 arcs** (6):

   | L1 | Standard arc |
   |---|---|
   | **Literature** | Theoretical frame → close reading → generalization back to frame / re-reading the frame through the text |
   | **History** | Historiographical positioning → narrative → analytic argument → broader significance / re-periodization |
   | **Philosophy** | Concept-puzzle → conceptual analysis → defense against strongest objection → consequences for downstream debate |
   | **Linguistics** | Research question + data source → linguistic analysis → claim → cross-linguistic / theoretical implication |
   | **Art studies** | Description → contextualization (provenance, materiality, reception) → interpretation → consequences for history of seeing/hearing/perceiving |
   | **Religious studies** | Text-philological work → tradition-positioning → interpretive argument → bearings on contemporary scholarship |

   **L3 / adjacent arcs** (selected examples — combine parent L1 arcs with L3-specific moves):

   | L3 / adjacent | Standard arc |
   |---|---|
   | **Cultural studies** | Case + theoretical lens → analytic unfolding → reflexive turn on the analysis itself |
   | **Classics** | Textual criticism → tradition-positioning → interpretive argument → reception consequences |
   | **Intellectual history** | Method declaration → context reconstruction → text analysis → concept-migration narrative |
   | **History of science** | Technical contextualization (the science) → historical narrative → analytic argument → relevance to contemporary science / historiography |
   | **Media studies** | Medium-morphology framing → analytic case → tech-social co-construction argument → consequences for media theory |
   | **Communication studies (humanities-style, e.g., media ecology)** | Speculative-philosophical framing (e.g., bias of communication, medium-effect) → tradition-positioning → case analysis as illustration / argument → consequences for understanding communication-society relation |
   | **Educational research (humanities-style, e.g., history/philosophy of education)** | Normative grounding (what should education do) → historical or philosophical case → analytic argument → consequences for practice / theory |
   | **Cross-disciplinary case** | Case → why this case → analytic work → calibrated generalization (with explicit scope limits) |

   **Other genres** (the arcs above assume papers/chapters):
   - **Book review**: summary-in-context → critical assessment → stakes for the field
   - **Response essay**: restate the target's claim (steel-manned) → locate the disagreement precisely → counter-argument → what survives of the target
   - **Grant / fellowship proposal**: problem + so-what → positioning in the field → plan of work → feasibility signals
   - **Self-translation** (moving your own paper across languages): not an outlining task — see Multilingual Academic Writing, plus a Mode F-style pass where the "original" is the source-language version

4. **Build outline section by section**:
   - Each section gets: (a) function in argument, (b) key claim, (c) key evidence/source/text, (d) ~word target
   - Function is critical: "what does this section DO for the argument" not "what topic does it cover"

5. **Cross-check against research question**:
   - Does every section serve the question?
   - Are there sections that look like the topic but don't advance the question? (cut)
   - Are there steps the argument needs that aren't yet in the outline? (add)

6. **Output to `_writing-config/outline.md`** (Chinese: `论文大纲.md`):
   ```markdown
   # Outline (Mode J output, v1)

   ## Paper meta
   - Title: …
   - Question (from Mode H): …
   - Target length: … words
   - Discipline arc applied: …

   ## §1. [Section heading]
   - Function: [opens the puzzle / establishes literature gap / etc.]
   - Key claim: …
   - Key evidence/sources: …
   - Target: ~800 words

   ## §2. …

   ## Argument trace (sanity check)
   - Claim 1 (§1) → supports → claim 2 (§3) → supports → main thesis (§5)
   ```

**Scope**: Mode J delivers an outline by default, with a one-sentence thesis per section. If the author also asks for paragraphs, that request authorizes a switch to Mode C: briefly name the switch and draft from the existing outline at Stage 3, without a separate permission round. Keep exploratory prose labeled as a draft.

**Restructuring an existing draft**: when the trigger is reorganizing existing text rather than planning new, insert a mapping step before step 4 — extract each existing section's *function* (not topic) into a list, map those functions against the target arc, and mark each keep / move / merge / cut / add. The outline output records this mapping, so the author sees what happens to every existing section.

**Mode-switching hints**:
- Outline done, ready to write → **Mode C** (drafting)
- Outline done, want to stress-test before writing → **Mode D** (devil's advocate on the outline itself)
- Outline reveals research question is weak → back to **Mode H**
