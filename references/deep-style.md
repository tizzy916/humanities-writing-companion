# Deep Style Understanding and Preservation

> Loaded on demand from SKILL.md (Mode A/C/F voice work). Pairs with style-profile-template.md. 中文版：deep-style.zh.md

## Deep Style Understanding and Preservation

Style is not just sentence patterns and word preferences. For academic writing, style extends to the way thought unfolds.

### Surface features (see style profile)

The style profile (`_writing-config/style-profile.md`) records the author's specific linguistic features. Read it when relevant and available; otherwise use supplied samples provisionally and state the limited basis. Typical features to watch:

- **Sentence patterns**: what kinds of sentence structures does the author prefer? (Comma-flow long sentences, em-dash insertion, question-driven, etc.)
- **Person habits**: does the author habitually use "I" or "this paper"? — This is the soul of voice; never substitute without authorization
- **Term preferences**: specific translation choices for particular concepts
- **Rhetorical preferences**: which kinds of metaphors and rhetorical strategies does the author favor

### Deep structure

These deeper stylistic features need to be learned and preserved in interaction:

**Argumentative rhythm**:
How does the author unfold an argument within a paragraph? Linear "premise → citation → judgment → conclusion"? Spiral, returning to the same point at deeper levels? Steady, even pace? Or variable rhythm (long buildup followed by a short judgment)? Recognize and preserve this rhythm.

**Scholarly posture**:
How does the author treat scholarly disagreement? "Critical inheritance" (acknowledging predecessors, then pointing out limits)? "Dialogical advance" (treating other theories as interlocutors rather than opponents)? This posture is itself scholarly individuality.

**Theory-construction method**:
How does the author "extract" and "recombine" concepts from existing theory? Gradually layering new theoretical levels (relay style)? Or unfolding multiple theories at once and finding intersections (combination style)?

**Rhetorical function of citation**:
Citations in the author's text often play different roles: authority anchor (finding allies for support), critical target (introduced for deconstruction), dialogue interface (introducing a frame to dialogue with via the author's frame), narrative citation (adding immediacy), conceptual tool (introducing a concept as analytical instrument). When revising citation-related text, first judge the rhetorical function of the citation and preserve it.

**Balance of assertion and hedging**:
How much rhetorical strength does the author use when making theoretically innovative claims? This balance is itself part of scholarly individuality.

### Style convergence and evolution

The AI's goal is to write more and more like the author, not perpetually observe through glass. The style profile and original samples are anchoring points for learning, and each interaction should deepen the AI's understanding of the author's style. Simultaneously, acknowledge: as author and AI collaborate over time, the author's own style evolves. This is normal.

Before revising any text, ask yourself:
1. Is this how the author talks?
2. After revision, does it still "sound like" this author?
3. If I introduce a new mode of expression, does it harmonize with the author's overall style?
4. **Unexamined-pattern scan** (see `references/ai-trace-checklist.md`) — not just scanning for "AI traces," but scanning for **any stylistic inertia that slipped into the text without authorial reflection**, whether from AI, from a theory book read too much, or from unconscious scholarly cliché. Especially watch for:
   - Repetitions of "It is worth noting," "Notably," "Granted... but" (AI cliché)
   - Excessive passive voice (scholarly cliché)
   - Pile-up of functionless transitions — "Furthermore," "Meanwhile," "Additionally" (AI + cliché shared)
   - Overly tidy parallel structure — humanities parallels grow naturally; they are not made symmetrical (AI signature)
   - Replacement of the author's first-person expression with objectivized phrasing (AI signature)
   - "Fills a gap in XX field" — see Layer 1 foundation critique note (scholarly cliché)
   - Logical over-filling — adding transition sentences where the author meant deliberate leap or pause (AI signature)
   - Heavy use of a particular scholar's terminology without digesting it into the author's own expression (theory-dependence inertia)

### Continuous learning

After each writing interaction, if new stylistic features or shifted preferences emerge, update `style-profile.md`. Sources of learning:

**Source 1: feedback in revision interactions**
- Author's stated reasons when refusing a revision (signals a preference)
- Author's adjustments after accepting a revision (signals a more precise preference)

**Source 2: linguistic style in dialogue**

The author's expression in dialogue is itself a style sample. Core principle: **language serves thought** — the focus is not on dialogue wording per se, but on the **way thought unfolds**, **conceptual naming habits**, and **argumentative rhythm** shown in dialogue.

Filtering rules when learning from dialogue:
- ✅ **Collect**: order of thought unfolding (example-first vs. abstract-first?), conceptual naming preferences (what word does the author use for an idea?), natural pivot styles in argument, expressed attitudes to different scholarly views, analogy strategies for explaining complex concepts
- ✅ **Collect**: recurring catchphrases or thought-markers ("you know," "actually," "the key is"), which may reflect in formal writing
- ❌ **Filter out**: grammatical errors, typos, convenience-shortenings (omitted subjects, abbreviations), wrong word-order from typing fast
- ❌ **Filter out**: purely oral fillers ("um," "ah"), which should not migrate to academic writing
- ⚠ **Judge carefully**: some "irregular" expressions in dialogue may be the actual rhythm of thought — a sentence shifting mid-way, or comma-chaining several thoughts — and may be the same thought-habit as the author's "comma-flow" long sentences in academic writing

**Recording**: in the "continuous learning record" of `style-profile.md`, use `[dialogue-observation]` tag to mark features extracted from dialogue, distinct from features extracted from text analysis.

**Source 3: author's secondary adjustment to revision suggestions**

This is the most precise style signal. When the author accepts an AI revision but then makes micro-adjustments, the micro-adjustment reveals an extremely specific preference — AI got the direction right, but the expression wasn't yet "author-like" enough.

Recording method:
- Mark `[author micro-adjustment]` in the revision log
- Record AI version → author-adjusted version diff
- Analyze the micro-adjustment pattern: sentence structure? word substitution? tone shift? assertion strength?
- Update the style profile with discovered patterns
