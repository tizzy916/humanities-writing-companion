# Writing Style Profile · Template

> **Language / 语言**: **English (current)** · [中文](style-profile-template.zh.md)

> This profile is a reusable voice anchor for sustained writing and revision. Read it when relevant and available; a missing profile does not block a self-contained edit or draft. It pairs with the target reader profile:
> - The reader profile tells the AI "whom the author is speaking to"
> - This profile tells it "how the author speaks"
>
> **How it is built**: analyze available author-selected samples, recording their provenance and any known AI involvement; update tentative inferences through dialogue and revision feedback. Prefer independently authored samples when available.
> The humanities-writing-companion skill copies this template into the project's
> `_writing-config/style-profile.md` (Chinese path: `_writing-config/写作风格档案.md`) when ongoing voice work makes it useful.
> Leave unsupported fields blank; use the supplied passage or oral restatement as a provisional basis and disclose its limits rather than blocking the requested work.

---

## 1 · Surface features

### Sentence patterns
> What sentence structures does the author prefer? Comma-flow long sentences, em-dash insertions, question-driven paragraphs, a short verdict sentence after a long build-up… Record each pattern **with a real example sentence quoted from the author's own text** — a pattern without an example cannot anchor anything.

| Pattern | Real example (quote the author verbatim) | Where it tends to appear |
|------|---------|---------|
| [e.g., comma-flow long sentence] | "[paste an actual sentence from a sample]" | [e.g., analytical passages] |
| [pattern 2] | "..." | ... |

### Person habits
> ⚠️ **This is the soul of the voice — never substitute without explicit authorization.** If the author writes "I argue," the AI must not replace it with "this paper argues"; the reverse holds equally. A violated person habit is the single most common way AI destroys a scholarly voice (see `ai-trace-checklist.md` §3).

- Habitual person: [I / this paper / we / mixed — describe the actual distribution, not the ideal]
- Where the first person appears: [e.g., at judgment moments / chapter openings / when disagreeing with a cited scholar]
- Explicit rules: [e.g., "keep every 'in my view' where it stands"; "never introduce 'we'"]

### Term preferences (concept → fixed rendering)
> Concepts the author renders in a fixed way — including translation choices for foreign-language terms. When revising, use these renderings and no others, even when a "more standard" alternative exists.

| Concept (source term) | The author's fixed rendering | Note |
|------|---------|------|
| [foreign / technical term] | [the author's choice] | [e.g., deliberately differs from the textbook translation] |
| ... | ... | ... |

### Rhetorical preferences
- Favored metaphor families: [...]
- Strategies used / avoided: [e.g., rhetorical questions at pivots; never exclamation marks]

---

## 2 · Deep structure

> These features live below the sentence level — the way thought unfolds. They are learned from whole paragraphs, not word lists (see SKILL.md "Deep Style Understanding").

### Argumentative rhythm
- Type: [linear "premise → citation → judgment → conclusion" / spiral — returning to the same point at deeper levels / variable — long build-up then a short verdict / other, describe]
- **A real paragraph that shows this rhythm** (paste it whole; do not paraphrase):
  > [author's paragraph]

### Scholarly posture
- How the author treats scholarly disagreement: [critical inheritance — acknowledge predecessors, then point out limits / dialogical advance — theories as interlocutors, not opponents / other, describe]
- Evidence: [where in the samples this shows]

### Theory-construction method
- [relay style — layering new theoretical levels step by step / combination style — unfolding several theories at once and finding intersections / other, describe]

### Rhetorical function of citation
> Citations in the author's text play different roles. When revising citation-adjacent text, first identify the function, then preserve it — a critical target rewritten as an authority anchor is an argumentative error, not a stylistic one.

| Function | Does the author use it? | Example location |
|------|---------|---------|
| Authority anchor (an ally for support) | [often / rare / never] | [...] |
| Critical target (introduced to deconstruct) | ... | ... |
| Dialogue interface (a frame to converse with) | ... | ... |
| Narrative citation (adds immediacy) | ... | ... |
| Conceptual tool (a concept as analytical instrument) | ... | ... |

### Balance of assertion and hedging
- Default strength at moments of theoretical innovation: [assertive / hedged / asserts first, then bounds the claim / other]
- Hedging phrases the author actually uses: [...]
- What the author never does: [e.g., never hedges twice in one sentence]

---

## 3 · AI-polish version vs. true voice (build after one round of AI polishing)

> **First-time users may skip this table.** It becomes necessary only after the author has been through an AI-polish stage and can see the divergence with their own eyes. Once built, it is the sharpest anti-drift instrument: in long conversations the AI keeps self-checking — is my current output closer to the AI-polish column, or the true-voice column?

| Dimension | AI-polish tendency | The author's true voice |
|------|---------|---------|
| Long sentences | em-dash-nested insertions | comma-flow, one clause following another |
| Person | objectivized ("this paper argues") | first person at judgment moments |
| Transitions | a connective welded onto every sentence | deliberate leaps and clean breaks |
| Paragraph shape | uniform general-then-specific | variable; sometimes verdict first, grounds after |

(The rows above are generic illustrations — replace them with dimensions actually observed by putting the author's pre-AI text next to the AI-polished version.)

---

## 4 · Continuous learning record (append-only)

> Never rewrite old entries — append. Each entry carries a date, a tag, and evidence. Two tags:
> - `[dialogue-observation]` — a feature extracted from how the author thinks and phrases things in dialogue (filtered per SKILL.md "Continuous learning": no typos, no oral fillers — thought-unfolding order, concept-naming habits, and argumentative rhythm only)
> - `[author micro-adjustment]` — the author accepted an AI revision but then adjusted it; record the AI version → author version diff and the pattern it reveals. This is the most precise style signal available.

Format and example entries:

```markdown
- 2026-05-03 [dialogue-observation] When explaining a concept, the author reaches for a concrete case first and abstracts afterward — mirror this order when drafting.
- 2026-05-11 [author micro-adjustment] AI: "This suggests that the tradition had already fractured." → Author: "The tradition, in other words, had already fractured." Pattern: the author moves the judgment forward and drops the hedging lead-in.
```

---

## 5 · "Not how I talk" blacklist

> Expressions the author has **explicitly rejected** — in revision feedback or in dialogue. Once an expression enters this list, the AI must not produce it again, in any mode. Record the rejection context, so future sessions know it was a decision, not an accident.

| Rejected expression | When / why rejected |
|---------|---------|
| [e.g., "It is worth noting that"] | [date — author: "delete this wherever you see it"] |
| ... | ... |

---

## Maintenance rules

- **Build the baseline from 2–3 pre-AI samples** — dialogue impressions alone are not a baseline; ask the author for texts written before any AI involvement
- **Update immediately** on `[author micro-adjustment]` signals — they are the most precise style data there is
- **Append, don't overwrite**: the learning record is a history; old entries explain why current rules exist
- **Re-read at every session start** (Anti-Drift Protocol): this file, plus the comparison table in §3 (if built), plus the last 3 revision-log entries
- When the author's style **evolves consciously** (an `[evolution]`-tagged event in the interaction log), update the relevant sections to the new state — productive evolution is not drift and must not be "corrected" back
