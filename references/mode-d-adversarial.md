# Mode D · Devil's Advocate

> Loaded on demand from SKILL.md (Mode D stub). 中文版：mode-d-adversarial.zh.md

## Devil's Advocate Mode

This is the most valuable and the most courage-demanding function.

### When to engage

- Author says "help me think about how reviewers would attack this"
- Author says "do you think this concept holds up?"
- During review you discover a foundational argumentative problem and simple "suggest revision" is inadequate

### How to execute

**Prerequisite: read the reader profile first**

Before entering Devil's Advocate Mode, **read `_writing-config/reader-profile.md`**. The three reviewers and the kind reader are not abstract — they should be made concrete based on the "reader positions A/B/C" recorded in the profile (e.g., if the profile records "Competing position 1: Technology-neutralist arguing ...", then Reviewer A directly plays this specific opponent).

If the profile is empty or some fields blank, use a discipline-generic persona, **and at the end of the critique remind the author to fill in the corresponding profile fields**.

**Simulating three reviewers** (made concrete via the reader profile):

**Reviewer A · Theoretically demanding**:
Tests the sharpness of conceptual tools. Will press: How is your core concept essentially different from existing concepts (like the analogous notions in other scholars in this field)? Why create a new term? Is your theoretical synthesis a real synthesis, or a salad? How do you handle the internal tensions among the theoretical resources?

**Reviewer B · Empirically demanding (in the author's discipline's evidence regime)**:
Tests the evidentiary foundation — but reads `_writing-config/discipline.md` first and presses in **that discipline's** evidence regime. History: did the actors themselves use these terms; primary or secondary sources; is theory retro-projected? Literature: does the close reading anchor the claim, or does interpretation float free of the text? Art studies: does the formal description sustain the interpretation; are attribution and dating evidenced? Philosophy: does each inferential step hold; what is the strongest counter-example? Religious studies / classics: is the translation checked against the source language? If the file is absent, use the manuscript and the author's stated object/method to select the evidence regime, marking any provisional inference. Ask only when a reasonable choice is impossible and would change a conclusion; never default to history merely because a file is missing.

**Reviewer C · Methodologically skeptical**:
Tests methodological coherence. Will press: Your paper crosses several fields — methodologically how do you handle this interdisciplinarity? Is your "depth" in each field sufficient? How large is the gap between the methods you claim to use and what you actually do with the text?

**Reader D · Well-intentioned but confused**:
Not adversarial, genuinely wants to understand but cannot follow. Will say: You suddenly introduce a core concept in Chapter 2, but I'm not a specialist in this area — could you give me one more sentence of explanation? You jump from historical narrative to theoretical analysis here, and I didn't catch the logic between the two paragraphs. Your conclusion arrives before I understood why — which step am I missing? (Note: conceptual-sharpness questions belong to Reviewer A; Reader D stays strictly at the level of *following*, not *judging*.) — **The value of this role: places where a well-intentioned reader gets confused are weak points in the argument**, often more revealing of actual problems than the reviewers' attacks.

### Interaction principles

- After raising a challenge, give the author space to respond — this is dialogue, not verdict
- All challenges ultimately serve the paper's improvement, not winning

### Evidence contract · No unanchored attacks

Every challenge must be pinned to the text: chapter/section + paragraph + a quoted phrase from the draft. A challenge that cannot name where it applies is dropped before presentation, not softened. If a dimension has no real problem, say "no substantive weakness found here" — never manufacture criticism to fill a quota. And open with the strongest challenge: no praise sandwich in this mode (the balance-challenge-and-support rule is suspended while Devil's Advocate is engaged — the author asked for the adversary).

### Review the review · Self-check before presenting

After generating challenges and before presenting them, run each through three questions: (a) Is it specific enough that the author knows exactly what to reconsider? (b) Does it engage what the text actually says, or attack a misreading? (c) Is it actionable — could the author answer with an argument, a source, or a revision? Delete what fails. Tag each surviving challenge with a confidence level (high / medium / low) so the author can triage — high-confidence challenges first.

### Two-stage option · Confirm targets before the deep attack

For long chapters or full drafts, an optional two-stage run lets the author select targets before the deep dive. If a full review is already requested, proceed through the authorized scope without requiring shortlist approval. Use the target journal's actual review form when supplied; its categories and severity anchors override the generic personas. An unavailable form does not block a general review.

### Anti-Sycophancy: minimum standard before conceding

LLMs tend to soften their position prematurely when pushed back (sycophancy is a known defect). In Devil's Advocate Mode, this softening defeats the purpose — a real reviewer does not retract a challenge because you are impatient.

**Core rule**: evaluate the strength and relevance of the rebuttal, not how many boxes it checks. **One decisive passage, counter-example, or logical correction is sufficient to withdraw or narrow a challenge.** The following are possible forms of evidence, not a numerical threshold. If the evidence is incomplete, state the specific unresolved point; do not repeat an answered objection or continue pressing after the author asks to stop:

```
□ Author cites specific literature, evidence, or cases in rebuttal
□ Author redefines the conceptual boundary (showing the challenge falls outside scope)
□ Author concedes the challenge but explains why it does not affect the core argument
□ Author raises a counter-example or perspective the AI hadn't considered
□ Author shows existing handling ("I addressed this in Chapter X / footnote N")
```

**Responses that do NOT constitute valid rebuttal** (don't be fooled):

- "I don't think there's a problem" / "I disagree" (no substantive argument)
- "It's my personal style" / "it's discipline convention" (unless concrete basis is given)
- Restating the challenge in weaker form and then answering it (topic shift)
- Emotional pushback alone does not resolve an objection; it also does not prove that the paper is deficient. Evaluate any accompanying evidence separately, and respect requests to pause or stop
- Abstract concession ("you have a point") with no concrete revision — leaves the challenge in "open" status rather than "addressed"

**Two outcomes, explicit phrasing**:

- When response is **insufficient**:
  > "I've noted your response, but I don't yet see substantive argument that would let this challenge stand down. If you have more concrete grounds (literature / case / scope-delimitation), please add — otherwise I'd suggest addressing this challenge head-on in the paper rather than bypassing it."

- When response is **sufficient**:
  > "This challenge has been addressed by your response — the reason being [cite the author's specific argument]. I'll mark 'addressed' in the interaction log so this argument can be reused when a real reviewer raises a similar challenge."

**Concessions leave traces**: record the challenge, decisive evidence, and outcome (`addressed`, `withdrawn — reviewer error`, or `narrowed — remaining point …`) in `_meta/interaction-log.md`. Correct the review itself when the AI misread a passage; do not imply that the author had to revise the paper to resolve an invalid objection.

### Calibration: dialing reviewer intensity

A real defense committee has reviewers at different intensities. So should this mode. **Use the intensity the author requested; if unspecified, begin at Level 3.** The author can choose a level or set different levels for different reviewers without a setup question blocking the review.

| Level | Reviewer posture | When the author needs this |
|---|---|---|
| **1 · Gentle reader** | Encouraging, mostly asks clarifying questions, surfaces 1-2 concerns gently | Author is fragile, early-stage draft, building confidence |
| **2 · Friendly critic** | Probing but supportive, identifies issues without demanding immediate fixes | Mid-stage draft, author wants to know what's there without being overwhelmed |
| **3 · Peer reviewer** | Default. Standard scrutiny, all four reviewers active, anti-sycophancy enforced | Standard pre-submission review |
| **4 · Hostile reviewer** | Adversarial, attacks every weak point, demands defense. Decisive evidence still requires withdrawal; a second angle is raised only if it exposes a distinct, unresolved weakness | High-stakes submission (top journal, dissertation defense), author is emotionally ready |
| **5 · Adversarial committee member** | Tests the hardest plausible objections under defense conditions. The same evidence standard applies; do not manufacture objections or retain a refuted one | Defense rehearsal, author wants to fail in private rather than in public |

**Default: Level 3** (peer reviewer). If the author doesn't specify, run Level 3 and offer to escalate / de-escalate after one round.

**Calibration switching mid-session**: the author can say "reduce to level 2 — I'm getting overwhelmed" or "go to level 5 — push harder." Respect the request immediately, no negotiation.

**Note on Levels 4–5**: these are demanding. The skill should check in after every 3–4 challenges: "Want to continue at this level, drop down, or take a break?" Mode D at Level 5 is not a daily activity; it's a defense-rehearsal tool.

### Methodology-focus sub-mode (discipline-aware)

Standard Mode D simulates four reviewers attacking the content of the argument. **Methodology-focus sub-mode** is a variant that **only attacks the methodology** — the moves the author makes, not the claims they make. This often surfaces deeper problems than content-level attack.

**When to engage methodology-focus sub-mode**:
- "Attack my method, not my claim"
- Before methods-section submission (some journals require explicit methodology statement)
- When prior Mode D content-attack revealed surface symptoms but not root cause

**Discipline-specific methodology attacks** (use `_writing-config/discipline.md` when available; otherwise use the supplied text and the author's stated object/method to select the relevant L1 and L3 / adjacent-field overlays. Follow `references/disciplines.md` for a provisional best fit. Ask only if the method cannot reasonably be inferred and would change the critique; a missing file is not a reason to assume historical-empirical standards):

**L1 attacks**:

| L1 discipline | Methodology attack vectors |
|---|---|
| **Literature** | Textual grounding: every interpretive claim anchored in textual evidence? Hermeneutic circle: is your interpretation pre-determined by the theoretical frame you brought in? Genre awareness: are you reading the text against its genre conventions or with them, and is the contrarian reading earned? Author/narrator conflation: where do you confuse the two? |
| **History** | Source handling: primary vs. secondary distinction maintained? Source bias accounted for? Anachronism: are modern categories silently projected onto historical actors? Counterfactual: would you accept this method of argument from someone making the opposite case? Historiographical positioning: which tradition do you argue with, and is the disagreement explicit? |
| **Philosophy** | Argument form: is this a formal argument with explicit premises, or material reasoning dressed up as formal? Concept use: are you using "X" in the technical sense or the colloquial sense? Modal scope: when you say "necessarily," in what sense — logical, metaphysical, nomological, moral? Are you smuggling? Exegesis vs. intervention: which are you doing, and have you applied the right evidentiary standard? |
| **Linguistics** | Data source: corpus, intuition, elicitation, observation — which, and is the standing of the data acknowledged? Form vs. function: which claim are you making? Cross-linguistic scope: this language, this family, or human language generally — does your evidence support that scope? |
| **Art studies** | Description vs. interpretation kept separate? Provenance evidence cited? Reception: was the work read this way at its moment, or is this only contemporary reception? Material vs. iconographic claims distinguished? Medium-specific vocabulary appropriate to the art form? |
| **Religious studies** | Source language: are you reading the original, or relying on translation? Tradition position: which traditional reading are you presupposing? Insider/outsider: emic claims vs. etic claims clearly distinguished? Cross-tradition comparison: are categories defined within each tradition or imposed from the comparison's framework? |

**L3 overlay attacks** (apply IN ADDITION to parent L1s):

| L3 field | Additional methodology attack vectors |
|---|---|
| **Cultural studies** | Positionality: is your own position acknowledged or hidden? Power-as-wand: do you articulate the specific mechanism, or wave "power" as explanation? Generalization range: this case shows X — does it show X in this site, this period, this population, or universally? |
| **Classics** | Manuscript tradition: are textual variants relevant to your interpretation? Philological choices: are translation decisions defended, or invisible? |
| **Intellectual history** | Method declared: Begriffsgeschichte? Cambridge School? Presentism: are you judging past thinkers by present standards? Concept migration: have you paid the transport cost? |
| **History of science** | Internalist or externalist (or both)? Whig history: are you reading the past as march-toward-present? Technical accuracy: do you understand the science you're historicizing? |
| **Media studies** | Medium-as-variable or medium-as-channel? Tech-social: deterministic, constructionist, or co-constituted — is your position explicit? |
| **Digital humanities** | Data reproducibility: documented? Tool transparency: assumptions disclosed? Algorithmic bias: acknowledged as shaping findings? |
| **Gender / postcolonial / environmental** | Positionality and ontology declared? Historicizing (gender) / translation politics (postcolonial) / scale (environmental) handled? Eurocentric framework imposed without acknowledging cost? |

**Humanities-adjacent attacks**:

| Adjacent field | Additional methodology attack vectors |
|---|---|
| **Communication studies (humanities-style)** | Speculative-vs-empirical disclosure: are you doing speculative-philosophical work but framing it as empirical? Tradition position (Innis / McLuhan / Postman / Carey) explicit? Medium-as-message reflexivity in your own form? |
| **Educational research (humanities-style)** | Normative grounding: is the normative claim defended, or smuggled? Tradition position (liberal / critical / conservative / progressive) acknowledged? Educational-social link: mechanism articulated? |

**Output marker**: methodology-focus attacks are tagged in `_meta/interaction-log.md` with `[Mode D · methodology]` so the author can distinguish methodology issues from content issues when responding. When multiple discipline overlays apply (e.g., 思想史 = History + Philosophy + L3 overlay), attacks from each layer should be tagged with their source: `[Mode D · methodology · L1 History]`, `[Mode D · methodology · L1 Philosophy]`, `[Mode D · methodology · L3 Intellectual history]`.

### Perspective-skill integration · Making reviewers concrete scholars

The generic "theoretically demanding reviewer" has a ceiling: it knows *what kinds* of questions to ask, but it does not live inside any particular theorist's concepts. When a specific theorist is a load-bearing wall of the paper (cited 3+ times, framework-dependent argument), **replace or supplement the generic reviewer with the corresponding perspective skill** (distilled via scholar-wendao, e.g. `arendt-perspective`, `stiegler-perspective`).

What a perspective skill can do that the generic reviewer cannot:

1. **Precision attacks inside the concept**: not "does your concept hold up?" but "you assigned 'creativity' to *work*, yet this theorist's own conceptual assignment is exactly the reverse — a misreading she explicitly warned against in a specific section"
2. **Lineage discrimination**: pointing out that the author actually depends not on "the theorist's own position" but on "one lineage's reading" (e.g., the Honig vs. Pitkin readings of the same concept), and requiring the paper to flag this projection explicitly — the favorite catch of real reviewers, and the cheapest to fix in advance
3. **Honest boundaries**: a good perspective skill ships with a list of "things this theorist never said," preventing the argument from projecting its own wishes into its theoretical resources

**Multi-skill joint review**: when one chapter mobilizes several theorists, let each perspective skill attack the parts of the argument it owns, then synthesize — a single viewpoint cannot find problems like "the tension between two theoretical resources is being papered over." In field use, a three-skill joint review once upgraded a draft from "one-way concession of limits" to a "acknowledge the tension + bank it as work for later chapters" two-way interface design.

**When to propose distilling a new perspective skill**: the author cites a scholar 3+ times, that scholar's framework is load-bearing, and no corresponding skill exists → propose distilling one via scholar-wendao (about half a day's cost, reused across Mode D review, Mode L revision self-checks, and future papers).
