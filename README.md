# Humanities Writing Companion · 人文学科写作伙伴

> An agent skill for humanities scholars whose primary deliverable is a long-form argumentative text — history, philosophy, literature, cultural studies, art history, religious studies, classics. Written in the open [Agent Skills](https://agentskills.io) (SKILL.md) format — works with Claude Code, the Claude Agent SDK, and any agent that supports the format.

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](./LICENSE)
[![Skill format: Agent Skills](https://img.shields.io/badge/skill%20format-Agent%20Skills%20(SKILL.md)-orange)](https://agentskills.io)
[![Status: stable](https://img.shields.io/badge/status-stable-green)]()
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20280772.svg)](https://doi.org/10.5281/zenodo.20280772)
[![Wiki](https://img.shields.io/badge/📖_Wiki-tutorials_%26_guides-blue)](https://github.com/tizzy916/humanities-writing-companion/wiki)

**[📖 Wiki](https://github.com/tizzy916/humanities-writing-companion/wiki)** · **[中文版 README](./README.zh.md)** · **[Skill source · English](./SKILL.md)** · **[Skill source · 中文](./SKILL.zh.md)**

---

## Table of contents

- [Positioning](#positioning)
- [What this skill takes seriously](#what-this-skill-takes-seriously)
- [A typical interaction](#a-typical-interaction)
- [Core features](#core-features)
- [Supported humanities disciplines](#supported-humanities-disciplines)
- [Showcase: Before / After](#showcase-before--after)
- [Install](#install)
- [Quick start · three typical scenarios](#quick-start--three-typical-scenarios)
- [Comparison with adjacent tools](#comparison-with-adjacent-tools)
- [Project structure](#project-structure)
- [Design philosophy](#design-philosophy)
- [Citation](#citation)
- [Contributing](#contributing)
- [About the Author](#about-the-author)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## Positioning

**End-to-end writing assistant for humanities scholars** — covering the full lifecycle of a humanities paper from research question to submission disclosure:

```
research question → literature map → planning → drafting → revision →
adversarial review → AI-trace cleanup → blind-reading check → AI-use disclosure
```

Built for fields where **prose IS the argument** — history, philosophy, literature, cultural studies, art history, religious studies, classics, intellectual history, science studies, and adjacent humanities-aligned fields.

Not a polishing tool. Not a citation manager. Not a research pipeline. **A thinking partner that stays with you across the whole arc.**

### 12 modes covering the writing lifecycle

| Stage | Modes |
|---|---|
| **Pre-writing** | Mode H · Research-question sharpening · Mode I · Literature mapping · Mode J · Plan-only outlining |
| **Drafting** | Mode C · Conception → new content · Mode A · Paragraph dialogue |
| **Review** | Mode B · Chapter review (4-layer critique) · Mode D · Devil's advocate (calibratable 1–5 + methodology-focus) |
| **Revision** | Mode E · Writing-bottleneck assistance · Mode F · Draft revision (with revision-coach sub-mode) |
| **Pre-submission** | Mode G · Blind reading · Mode K · AI-use disclosure |
| **Post-review** | Mode L · Revision workflow (defense/external-review comment integration, revision-dossier system) |

Plus a **citation toolchain** (`scripts/`): consistency checking, format conversion (Chicago / MLA / APA / GB7714), and metadata candidate lookup through Crossref/OpenAlex (not source-text or claim verification). In agent-capable environments (e.g., Claude Code), Mode B/D reviews can fan out to parallel reviewer agents, and pending claims can be checked against sources with provenance, support, and limitations recorded separately.

---

## What this skill takes seriously

Three things generic AI writing tools do not handle for humanities:

**1. Voice preservation is a core scholarly value, not stylistic decoration.**
In humanities, the author's voice carries epistemic weight: it signals which intellectual tradition the author writes from, which interlocutors they take seriously, which moves are theirs and which are borrowed. A paper polished into "standard academic English" loses this signal. This skill helps you write more like yourself, not less.

**2. Argument and prose are inseparable.**
In empirical research, you can have a perfect experiment ruined by bad writing. In humanities, the writing IS the argument — a slack sentence, a vague concept, an unwarranted transition is an argumentative failure. This skill works at the level of argument-through-prose.

**3. The reviewer is real and adversarial.**
Humanities reviewers are not gentle. A theoretical concept will be tested for sharpness; a historical claim will be tested for evidence; a philosophical argument will be tested for the strongest counter. This skill simulates that adversary internally so the paper meets it before submission.

---

## A typical interaction

```
You: 帮我看看这段。我在论福柯的全景敞视主义如何延伸到数字平台。

[skill reads the paragraph + your style profile]

Companion:
  I notice three things, in order of priority.

  🔴 Foundation: you're using "全景敞视" as a metaphor for platform 
     surveillance, but Foucault's original concept turns on architecture 
     producing a specific subject-position. Platforms produce a different 
     subject (data subject, not body in a cell). You may want to either 
     (a) name the analogy as analogy and discuss the difference, or 
     (b) borrow Zuboff's "instrumentarian power" which fits the data case 
     more cleanly. Which direction do you want to go?

  🟡 Argument: paragraph 2 jumps from "platforms collect data" to "this 
     constitutes surveillance" without the middle step about visibility-
     as-power. A friendly reader will not follow.

  🟢 Voice: your style profile has "first-person with em-dash insertion." 
     Paragraph 3 starts with "本文认为…" which reads like cliché. Want to 
     restore the first-person?

You: 走方向 (b). 改吧。

[skill produces revision; you keep the version that sounds like you]
```

This is what "thinking partner, not polishing tool" means in practice.

---

## Core features

### Four-layer critique (not single-axis polishing)

```
Layer 1 · Foundation   "Does this paper hold up scholarly?"
Layer 2 · Structure    "How is the argument unfolding?"
Layer 3 · Paragraph    "What is this paragraph doing?"
Layer 4 · Sentence     "Is this sentence right? Well-said?"
```

**Scope-aware priority**: start with consequential argument issues in a full review; complete a requested local edit when it does not depend on resolving those issues.

### Devil's advocate with anti-sycophancy

Simulates three reviewers + one well-intentioned reader:
- Reviewer A · Theoretically demanding
- Reviewer B · Historically empirical
- Reviewer C · Methodologically skeptical
- Reader D · Well-intentioned but confused (**distinctive design**: places where a friendly reader gets confused are weak points in the argument)

**Evidence-based correction**: do not concede merely under pressure, but retract a challenge when even one decisive source passage or valid argument defeats it. Reviewer intensity never permits ignoring a correction.

### Deep voice learning and preservation ("My hand writes my voice")

Not just sentence preferences. Also:
- **Argumentative rhythm** (linear / spiral / variable-tempo)
- **Scholarly posture** (critical inheritance / dialogical advance)
- **Rhetorical function of citation** (authority anchor / critical target / dialogue interface / narrative / conceptual tool)
- **AI-trace checklist** (8 categories of unexamined patterns ≠ AI cliché ≠ scholarly cliché)

### Discipline-specific dimensions

Different chapter types get different critique strategies:
- Historical narrative · anachronism, counterfactual stress, source handling
- Philosophical argument · conceptual derivation, cross-theoretical transplantation, strongest objection
- Literary criticism · close reading vs. interpretation, genre awareness, form and meaning
- Cultural studies · power-knowledge framing, positionality, generalization range
- Art history · description vs. interpretation, provenance, reception
- Religious studies / classics · source-language rigor, tradition awareness, insider-outsider position
- Case analysis (cross-disciplinary)

### ADHD-friendly interaction

- Feedback batched 3-5 per round
- Quick wins first
- Topic-jump support (a jump may be an insight signal)
- Pomodoro-friendly task units
- Reorientation summaries every 4-5 turns

### Reflexive writing support (distinctive module)

If your research itself involves human-AI collaboration (autoethnography of AI-assisted writing), the skill provides six categories of "reflexive moments":

🔄 Direction change · 🚫 Refusal · 🎭 Voice conflict · 🔧 Tool dependency · 💡 Unexpected insight · 🤖 AI-trace awareness

**Scholarly basis** (citable in your paper):
- Christou (2026). *Reconfiguring Reflexivity in the Era of AI*. *Qualitative Inquiry*.
- Wiles (2025). *Recursive Cognition in Practice*. *International Journal of Qualitative Methods*.
- Panke (2025). *How Can (A)I Research This? An Autoethnographic Exploration of Generative AI*.

### Engineering infrastructure

Borrowed from software engineering, in service of humanities writing:
- **Version management**: minor version = commit / major = release / `_drafts/` = feature branch
- **Revision log**: every change recorded with diff + reason (like git commit message)
- **Feedback reports**: Blocker / Major / Minor / Question tiers (from code review)
- **Systematic verification checklists**: argument completeness / concept consistency / citation completeness / style consistency
- **`[VERIFY]` / `[待核对]` hard marker**: anti-citation-hallucination — cannot enter submission version

### Twelve work modes (not one)

- **Mode A** — paragraph-level dialogue
- **Mode B** — chapter-level review
- **Mode C** — conception → new content writing (with collaborative drafting protocol)
- **Mode D** — devil's advocate (calibratable 1–5, methodology-focus sub-mode)
- **Mode E** — writing bottleneck assistance (5 unblocking strategies)
- **Mode F** — draft revision (two-version comparison, anti-AI-cliché, revision-coach sub-mode)
- **Mode G** — blind reading (mechanical promise-delivery check)
- **Mode H** — research-question sharpening (Socratic dialogue: from vague interest to a sharp, write-able question, with "so what" test and interlocutor identification)
- **Mode I** — literature mapping (organizes what you have already read into camps and debates — never searches literature for you)
- **Mode J** — plan-only outlining (discipline-aware standard arcs; plans the paper without writing prose)
- **Mode K** — AI-use disclosure (audits actual AI involvement, 4-tier categorization, journal-ready disclosure statement)
- **Mode L** — revision workflow (defense/external-review comment integration: one revision dossier per comment, status-authoritative master table)

### Engineering helper scripts

[`scripts/`](./scripts) provides five tools requiring zsh and Python 3, with no third-party Python packages:

| Script | Purpose |
|--------|---------|
| `ai-trace-scan.sh` | Scan clichés and transition pile-ups |
| `pending-checks.sh` | Aggregate all `[VERIFY]` / `[待核对]` / `❓ to discuss` / `[AI DRAFT]` markers |
| `citation-consistency.py` | Citation-format consistency check (brackets / commas / connectors / EN/CN names / page numbers) |
| `citation-format-convert.py` | Convert a BibTeX bibliography between Chicago (Author-Date) / MLA 9 / APA 7 / GB/T 7714 |
| `citation-verify.py` | Look up Crossref/OpenAlex metadata candidates (FOUND / FUZZY_MATCH / NOT_FOUND / ERROR); no source-text or claim verification |

---

## Supported humanities disciplines

This skill organizes humanities scholarship in a **three-layer architecture**, so the discipline-routing system can match where the author actually works — not just to one of a flat list of seven slots. Authors declare their discipline at onboarding (or the skill infers from the draft); routing then loads the matching layer.

### L1 · Six humanities main disciplines

These are the canonical L1 humanities disciplines. Each carries a core set of methodological concerns generic AI writing tools miss.

| L1 discipline | Object of study | Core methodological concerns |
|---|---|---|
| **Literature · 文学** | Texts (poetry, fiction, drama, essay) | Close reading vs. interpretation · Genre awareness · Form-meaning fit · Intertextuality |
| **History · 史学** | Past events, persons, societies | Anachronism · Counterfactual stress · Source handling (primary vs. secondary) · Causal-chain transparency · Historiographical positioning |
| **Philosophy · 哲学** | Concepts, arguments, normative claims | Conceptual derivation · Argument form (formal vs. material) · Cross-theoretical transport cost · Steel-manning the strongest objection · Modal scope |
| **Linguistics · 语言学** | Language structure and use | Data source (corpus vs. intuition vs. elicitation) · Form vs. function · Description vs. prescription · Cross-linguistic claim scope |
| **Art studies · 艺术学** | Art works (painting, sculpture, music, film, architecture) | Description vs. interpretation (keep separate) · Provenance and materiality · Reception history · Medium-specific form analysis |
| **Religious studies · 宗教学** | Religious traditions, texts, practices | Source-language rigor (original vs. translation) · Tradition position · Insider/outsider (emic vs. etic) · Comparative method |

### L2 · Common subfields (not exhaustive)

Subfields **inherit all the methodological concerns of their parent L1**, plus any specific constraints the author declares at onboarding. Examples — many more possible:

| Parent L1 | Example subfields |
|---|---|
| Literature | Classical Chinese literature · Modern Chinese literature · Comparative literature · Literary theory · Literary criticism · Foreign-language literatures |
| History | Chinese history · World history · Economic history · Social history · Cultural history · Urban history · Periodized fields (Tang history, early modern Europe, etc.) |
| Philosophy | Chinese philosophy · Western philosophy (analytic vs. continental) · Ethics · Aesthetics · Political philosophy · Philosophy of science · Phenomenology |
| Linguistics | Historical linguistics · Sociolinguistics · Pragmatics · Typology · Discourse analysis |
| Art studies | Art history · Musicology · Film studies · Theatre studies · Architectural history |
| Religious studies | Christian studies · Buddhist studies · Daoist studies · Comparative religion |

If your subfield isn't listed, declare it at onboarding — it inherits from its parent L1 automatically.

### L3 · Cross-disciplinary fields (explicit multi-inheritance)

These are humanities fields that explicitly draw from multiple L1s. The skill loads the methodological concerns of **all parent L1s plus the L3-specific overlay**.

| L3 field | Inherits from | L3-specific overlay |
|---|---|---|
| **Cultural studies · 文化研究** | Literature + History + Sociology | Power/knowledge framing · Positionality · Generalization range |
| **Classics · 古典学** | Literature + History + Philosophy + Religious studies + Archaeology | Textual criticism (manuscript tradition) · Philological rigor · Reception history |
| **Intellectual history · 思想史** | History + Philosophy | Begriffsgeschichte vs. Cambridge School · Context vs. text · Avoiding presentism |
| **History of science · 科学史** | History + Science + Philosophy | Internal vs. external history · Whig-history vigilance · Technical accuracy · Case-study calibration |
| **Media studies · 媒介研究** | Literature + Cultural studies + Philosophy of technology | Medium-morphology · Reception studies · Tech-social co-construction |
| **Digital humanities · 数字人文** | Any L1 + Computation | Data reproducibility · Tool transparency · Algorithmic bias · Methodological disclosure of computational choices |
| **Gender studies · 性别研究** | Literature + History + Cultural studies | Gender ontology · Historicizing gender · Intersectionality |
| **Postcolonial studies · 后殖民研究** | Literature + History + Cultural studies | Positionality · Translation politics · Resisting Eurocentrism |
| **Environmental humanities · 环境人文** | Literature + History + Science | Anthropocene framing · Multi-species perspective · Scale problems (local vs. planetary) |

### Humanities-adjacent fields (welcome with scope note)

Some fields are formally classified as social science but include strong humanities-style sub-traditions (where prose IS the argument). This skill welcomes such work:

| Field | What we serve | What we don't serve |
|---|---|---|
| **Communication studies · 传播学** (humanities-style) | Media ecology school (Innis / McLuhan / Postman / Carey); critical communication; humanities-aligned cultural-media research | Empirical/experimental communication research, content analysis as quantitative method |
| **Educational research · 教育学** (humanities-style) | History of education · Philosophy of education · Curriculum theory in humanities mode · Critical pedagogy | Quantitative educational psychology · Empirical learning-outcomes research |

Inheritance: communication studies (humanities-style) ← Media studies + Philosophy + Cultural studies. Educational research (humanities-style) ← History + Philosophy + Cultural studies.

### Fallback protocol — if you still don't see your field

Tell the skill at onboarding:

1. **Object of study**: text / past event / concept / phenomenon / artifact / practice / language structure / …
2. **Primary method**: close reading / archival research / argument analysis / ethnography / comparison / philological work / …

The skill will infer your closest L1 + any relevant L3 overlays, write it to `_writing-config/discipline.md`, and proceed. You can refine the declaration anytime.

The full methodology rubric for each L1 / L3 entry lives in `references/disciplines.md` — this README table is the surface map; the skill carries the full rubric.

---

## Showcase: Before / After

An illustrative exercise, not a validated quotation from a named scholar. The supplied material is deliberately limited:

> **Draft.** All apprentices learn primarily from written rules. The two workshop interviews demonstrate that formal rules always take priority over experience.
> **Reading note supplied by the author.** In these two interviews, apprentices describe consulting written rules for routine tasks and asking experienced workers about unusual cases.

The skill should identify the mismatch before strengthening the prose:

> **Finding · claim–evidence mismatch.** The interviews describe two forms of learning; they do not establish that rules always take priority. Two workshop interviews also do not justify “all apprentices.” This judgment uses the supplied note; the interview records have not been checked.

If the author requests a revision, a bounded proposal is:

> **After.** In the two interviews summarized here, apprentices describe using written rules for routine tasks and turning to experienced workers in unusual situations. These accounts suggest that the roles of rules and experience vary with the task. [VERIFY: check the original interview records and add their actual locators.]

The revision narrows the claim to the material supplied and makes the remaining source check visible. It does not invent a quotation, page number, or external scholarly authority. The author still decides whether this interpretation fits the full evidence.

---

## Install

### As a Claude Code skill

```bash
git clone https://github.com/tizzy916/humanities-writing-companion.git \
  ~/.claude/skills/humanities-writing-companion

chmod +x ~/.claude/skills/humanities-writing-companion/scripts/*.sh
```

Or as a project-level skill (vault / project only):

```bash
git clone https://github.com/tizzy916/humanities-writing-companion.git \
  ./.claude/skills/humanities-writing-companion
```

### Claude Code loading

Claude Code auto-scans `~/.claude/skills/` and `./.claude/skills/` on startup. After install, say "I'm working on a humanities paper" or any of the trigger phrases below.

### Without git (ZIP download)

No git required: on the [GitHub repository page](https://github.com/tizzy916/humanities-writing-companion), click **Code → Download ZIP**, unzip, and move the unzipped folder to `~/.claude/skills/humanities-writing-companion` (or `./.claude/skills/humanities-writing-companion` for project-level install). Then make the shell scripts executable:

```bash
chmod +x ~/.claude/skills/humanities-writing-companion/scripts/*.sh
```

### Claude desktop app / claude.ai

The Claude desktop app and claude.ai also support custom skills: package the skill folder (the directory containing `SKILL.md`) as a `.zip` and upload it in your Claude settings, under the capabilities/skills section (the exact menu wording may vary as the product evolves — look for "Skills"). Note that the `scripts/` toolchain requires a shell-capable environment (Claude Code / agent mode); in chat-only environments the skill's dialogue modes work, but scripts do not run.

### Claude Agent SDK

`SKILL.md` can be loaded into your system prompt directly. The skill is plain text — no runtime dependencies.

### Other agents (open SKILL.md format)

This skill is written in the open [Agent Skills](https://agentskills.io) format: a folder containing `SKILL.md` plus plain-text `references/` and `scripts/`. Any agent that supports the format — or that can simply read `SKILL.md` (and, when routed there, `references/*.md`) into context — can use it: clone this repo into wherever your agent discovers skills. The `scripts/` toolchain requires **zsh and Python 3**. Citation lookup additionally needs network access to Crossref and OpenAlex; the other checks run locally.

### Verify the installation

After installing, start a new conversation and either:

1. Ask Claude: **"What skills do you currently have loaded?"** — `humanities-writing-companion` should appear in the list; or
2. Say a trigger phrase directly, e.g. **"review my section"** or **"帮我看看这段"** — the skill should activate and respond in its four-layer-critique voice rather than as a generic polisher.

If neither works, check that the folder sits directly under `~/.claude/skills/` (i.e., `~/.claude/skills/humanities-writing-companion/SKILL.md` exists) and restart Claude Code.

### Trigger phrases

**English**: "paper," "essay," "chapter," "dissertation," "argument," "thesis," "revise," "voice," "review my section," "stuck on writing," "devil's advocate," "reviewer attack"

**Chinese**: 论文 · 写作 · 润色 · 改论文 · 帮我看看这一章 · 我手写我口 · 这个论证有没有问题 · 我写不下去了 · 审稿人会怎么攻击

When an academic draft is already in context, casual requests such as "take a look at this paragraph" · 帮我看看这段话 also apply.

---

## Quick start · three typical scenarios

### Scenario 1: new paper, first use

Say to Claude: "I want to write a paper on X."

The skill starts from your idea and any materials already supplied, helping you form a research question or requested draft. It asks only for consequential missing information. Profiles and folders are created as needed when you choose ongoing file-based work.

### Scenario 2: revising an existing chapter

```
"Help me read this chapter"      → Mode B (chapter review) → 4-tier feedback report
"Help me revise this paragraph"  → Mode A (paragraph dialogue) → diagnose + suggest + reason
"I'm stuck"                      → Mode E (bottleneck) → one suitable next move
```

### Scenario 3: fighting AI cliché (two-version comparison)

If your paper has been through AI polishing but you want to restore the original voice:

```
Mode F · draft revision → compare AI-polished vs. original → keep improvements + restore voice
```

---

## Comparison with adjacent tools

| Tool | Their focus | Where this skill differs |
|------|-------------|--------------------------|
| **Jenni AI** | Real-time autocompletion + literature search | We do thought-dialogue, not autocompletion. Real-time prediction skips the cognitive work that humanities argument needs. |
| **Paperpal** | Academic language polishing (STEM/biomed-leaning) | We're a writing architecture (12 modes, 4-layer critique, discipline routing), not a point polishing tool. |
| **Yomu AI** | Sourcely literature engine + paragraph feedback | We assume the author manages literature (Zotero/Drive). Mode I helps organize what you've already read — never replaces the reading. |
| **Thesify** | Paper Digest + Purpose-Check | Mode G is inspired by Purpose-Check. We use it within a broader four-layer critique workflow plus reviewer calibration. |
| **HyperWrite Devil's Advocate** | Point-tool counter-argument generation | Mode D is a full devil's-advocate mode with 1–5 calibration, methodology-focus sub-mode, and evidence-based concessions (anti-sycophancy). |
| **Grammarly / DeepL Write** | Grammar / translation polishing | We never rewrite for "clarity" at the cost of voice. "My hand writes my voice" is a core principle, not optional. |
| **Generic ChatGPT / Claude (no skill)** | General-purpose chat | We carry persistent style profile, reader profile, revision log, four-layer critique, discipline routing, AI-trace checklist, and citation toolchain across sessions. |

---

## Project structure

```
humanities-writing-companion/
├── SKILL.md                          ← Core skill file (EN: scope, evidence rules, task router, compact critique)
├── SKILL.zh.md                       ← Chinese mirror (中文版)
├── references/                       ← On-demand manuals (each with a `.zh.md` Chinese mirror)
│   ├── critique-review.md            ← Detailed four-layer questions and review coverage
│   ├── disciplines.md                ← Full discipline dimension tables (L1/L2/L3/adjacent + fallback)
│   ├── modes-prewriting.md           ← Mode H / I / J full protocols
│   ├── mode-c-drafting.md            ← Mode C four-stage drafting flow
│   ├── mode-d-adversarial.md         ← Mode D devil's-advocate full protocol
│   ├── mode-e-bottleneck.md          ← Mode E bottleneck strategies
│   ├── mode-f-revision.md            ← Mode F revision workflow
│   ├── modes-submission.md           ← Mode G / K full protocols
│   ├── deep-style.md                 ← Deep style understanding & preservation
│   ├── multilingual-writing.md       ← Mixed-language writing norms
│   ├── style-profile-template.md     ← Style profile ("constitution of voice") template
│   ├── ai-trace-checklist.md         ← AI-trace scan checklist
│   ├── project-management.md         ← Project folder + version management
│   ├── revision-workflow.md          ← Mode L revision-dossier workflow manual
│   └── target-reader-profile-template.md  ← Target reader profile template
├── scripts/                          ← Helper scripts (zsh + Python 3)
│   ├── README.md                     ← Script usage
│   ├── ai-trace-scan.sh              ← AI cliché scan (zsh)
│   ├── pending-checks.sh             ← Pending marker aggregation (zsh)
│   ├── citation-consistency.py       ← Citation format consistency (Python 3)
│   ├── citation-format-convert.py    ← Chicago/MLA/APA/GB7714 converter (v4.0+)
│   └── citation-verify.py            ← Crossref/OpenAlex metadata candidate lookup
├── README.md                         ← This file
├── README.zh.md                      ← 中文 README
├── CHANGELOG.md                      ← Version history
├── LICENSE                           ← CC BY-NC 4.0
└── CITATION.cff                      ← Academic citation metadata
```

**Bilingual status**: the project is fully bilingual. SKILL.md, README, CONTRIBUTING, the `references/` manuals, and `scripts/README` each exist as an English file plus a `.zh.md` Chinese mirror; script comments are bilingual as well. Both languages of trigger work either way (the description field in SKILL.md handles both).

---

## Design philosophy

### "My hand writes my voice"

Academic rigor and personal expression are not opposites. "Standard academic prose" usually means the death of individuality. The skill helps the author speak in their own voice rather than pressing their words into a prefabricated mold.

### Thought first, format second

Revision priority:
1. Force of the argument
2. Precision of concepts
3. Effectiveness of structure
4. Quality of expression
5. Format compliance

Always top-down. Do not fuss with commas in a paragraph whose underlying argument is broken.

### Engineering rigor, humanistic expression

Borrows software engineering best practices (version management, unit tests, code review) in service of humanities writing. Engineering rigor does NOT mean turning the paper into code — it means every revision is traceable, argument quality is verifiable, the writing process is resumable, and problems are processed in layers.

---

## Citation

If your research uses this skill, please cite it in the methodology section.

**BibTeX**:
```bibtex
@software{shen_humanities_writing_companion_2026,
  author       = {Shen, Cong},
  title        = {Humanities Writing Companion: An Agent Skill for Voice-Preserving Humanities Academic Writing},
  year         = {2026},
  publisher    = {Zenodo},
  version      = {5.1.0},
  doi          = {10.5281/zenodo.20280772},
  url          = {https://doi.org/10.5281/zenodo.20280772}
}
```

**Plain-text attribution** (for skill metadata, footers, etc.):
```
Based on Humanities Writing Companion by Shen Cong
https://github.com/tizzy916/humanities-writing-companion
```

See [`CITATION.cff`](./CITATION.cff) for full machine-readable metadata (GitHub's "Cite this repository" button will use it automatically).

### Citing companion tools

If you also use [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) in the same project, please cite both. ARS attribution format (per CC BY-NC 4.0):

```
Based on Academic Research Skills by Cheng-I Wu
https://github.com/Imbad0202/academic-research-skills
```

---

## Contributing

Issues and PRs welcome:
- New work-mode proposals
- Extensions to the AI-trace checklist
- Discipline-specific examples (medieval studies, art conservation, ethnomusicology, etc.)
- Additional citation-format support (APA / Chicago / MLA / GB/T 7714 / journal-specific)
- Translation-quality improvements to the bilingual mirrors (`references/`, `scripts/`)

See [`CONTRIBUTING.md`](./CONTRIBUTING.md).

---

## About the Author

Shen Cong — BFA, Experimental Art, Central Academy of Fine Arts (CAFA); MA, History of Science, Tsinghua University (advisor: [Hu Yilin](https://yilinhut.net/author/admin)); Founder & CEO of [Tianyu Vision](https://tianyu.art/), a sci-art studio working on scientific visualization, science communication, and sci-art convergence.

This skill came out of writing the author's own MA thesis, *Technical Liberalism*. He noticed that almost every AI writing tool on the market pulled toward **polishing and averaging** — whereas humanities scholarship needs the opposite: protecting the author's scholarly voice, stress-testing argumentative rigor, and surviving adversarial peer review. So he built this skill — not to write *for* him, but to *read* for him, delivering at each of four layers (basic rigor / argument development / paragraph function / sentence-level expression) the kind of critique a real humanities scholar would actually give.

📮 [GitHub @tizzy916](https://github.com/tizzy916) · shencong916@gmail.com · Corrections, collaboration, and conversation welcome.

---

## License

**[CC BY-NC 4.0](./LICENSE)** (Creative Commons Attribution-NonCommercial 4.0 International) — free for non-commercial use, modification, and distribution. Requires attribution.

> ⚠️ **License change (v3.0.0, 2026-05-19)**: This project relicensed from **MIT to CC BY-NC 4.0**. Versions ≤ v2.1.0 remain under MIT and retain their original commercial-use rights for those specific versions. From v3.0.0 onwards, **commercial use is prohibited without a separate license**.

### Commercial Use

This skill is licensed under CC BY-NC 4.0 — **non-commercial use only** (academic research, teaching, personal projects, open-source derivatives, internal research workflows).

For commercial licensing inquiries — embedding in a paid product, paid consulting or editing services using this skill, commercial SaaS integration, agency use on behalf of paying clients — contact the author for a commercial license:

📮 **shencong916@gmail.com** (Shen Cong · Tianyu Vision)

The author retains the right to grant commercial licenses on a case-by-case basis. Citing this skill in academic publications is always permitted regardless of license tier.

---

## Acknowledgments

Methodological inspiration and scholarly basis:

- Christou, P. A. (2026). [Reconfiguring Reflexivity in the Era of AI](https://journals.sagepub.com/doi/10.1177/10778004261445052). *Qualitative Inquiry*.
- Wiles, F. (2025). [Recursive Cognition in Practice](https://journals.sagepub.com/doi/10.1177/16094069251381709). *International Journal of Qualitative Methods*.
- Panke, S. (2025). [How Can (A)I Research This?](https://journals.sagepub.com/doi/10.1177/00224871251325065).
- Foucault, M. (1984). What is Enlightenment? — "diagnostic of the present" as methodological tradition
- Stiegler, B. (2013). *What Makes Life Worth Living: On Pharmacology* — "critical pharmacology"

Some design patterns inspired by:

- [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) — the upstream pipeline this skill complements; the Concession Threshold pattern in their reviewer module inspired Mode D's "minimum standard before conceding"
- [Voice DNA + Audience Profile pattern](https://aiblewmymind.substack.com/p/claude-skills-ai-write-like-you) — inspired the style profile + reader profile pairing
- [Thesify](https://www.thesify.ai/) Purpose-Check — inspired Mode G blind reading
