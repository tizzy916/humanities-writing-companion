# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [5.1.0] — 2026-09-22

### Changed

- Reduced both skill entrypoints to a task router, scope/authorization rules, evidence boundaries, and compact four-layer critique; moved detailed critique prompts into a bilingual reference pair.
- Replaced mandatory per-paragraph reconfirmation and minimum-reading-count gates with task-scoped execution; retained optional Socratic coaching and authorial control.
- Changed reviewer concessions to follow decisive evidence rather than a fixed number of conditions. Promise–delivery checks now distinguish isolated reviewers from an existing conversation.
- Made AI-use categories internal audit labels, tied submission advice to the actual target policy, and removed scanner-based disclosure downgrades.
- Isolated configuration per paper. Replaced the unverified scholarly showcase with an explicitly illustrative, source-bounded exercise. Corrected shell requirements to zsh.

### Fixed

- Pending-marker scans now recognize English and Chinese forms consistently.
- Near surname matches remain FUZZY_MATCH; malformed API responses remain ERROR instead of NOT_FOUND. Clarified that metadata candidates and zero parsed citations do not verify a manuscript.
- Singular/plural page notation and page ranges no longer produce a false mixed-style warning.

### Validation

- Added 15 offline regression tests and CI checks for both entrypoint descriptions, resource links, and discovered bilingual reference pairs. Static checks do not establish semantic equivalence or writing quality.
- Local validation: 59 top-level offline checks passed (including a suite of 15 new regression tests); one live-network test skipped. Six bounded usage scenarios exercised. These checks do not establish full writing-quality or cross-platform performance.

---

## [5.0.2] — 2026-07-13

**Citation-metadata fix only.**

### Fixed

- **Concept DOI corrected everywhere**: all "Concept DOI" references pointed to `10.5281/zenodo.20280773`, which is actually the **v4.1.1 version-specific DOI** — it permanently resolves to the v4.1.1 archive (old title, old repository name) instead of the latest version. The true Concept DOI is [`10.5281/zenodo.20280772`](https://doi.org/10.5281/zenodo.20280772), which always resolves to the newest archived release. Corrected in the README DOI badges and BibTeX blocks (both languages), CITATION.cff identifiers, the release checklists, and the v4.1.1 changelog entry's DOI link (kept as an erratum-style correction since it is a live pointer, not a historical record).

---

## [5.0.1] — 2026-07-13

**Platform-neutral repositioning. Docs and metadata only — no skill content changed.**

### Changed

- **Repository renamed**: `claude-skill-humanities-writing-companion` → `humanities-writing-companion` (GitHub redirects all old URLs). Every hardcoded repository URL updated: READMEs, CITATION.cff, .zenodo.json, docs/, issue-template config, and the `citation-verify.py` User-Agent.
- **Positioning de-branded from Claude**: the skill is written in the open [Agent Skills](https://agentskills.io) (SKILL.md) format and is not Claude-only. Updated accordingly: README taglines and format badge, citation titles ("A Claude Skill…" → "An Agent Skill…") in CITATION.cff / .zenodo.json / README BibTeX, the `claude-skill` keyword (→ `agent-skill`), the GitHub repo description, and CONTRIBUTING's entry-point list. New "Other agents (open SKILL.md format)" install note in both READMEs. Factual Claude Code / claude.ai / Agent SDK install instructions are retained.

---

## [5.0.0] — 2026-07-03

**Progressive-disclosure restructure. Ships together with 4.3.0 (below) in a single release.**

The 4.3.0 audit's single largest finding was token economy: the SKILL.md body (~2,000 lines, ~35k tokens) was injected in full on every activation — 3.7× the official <500-line guideline — while the in-file "Selective Loading Guide" promised an on-demand behavior the platform cannot deliver for same-file sections. v5.0.0 makes that guide true by moving the conditional 60% of the body into `references/`.

### Changed — architecture (no content was rewritten; sections moved verbatim, then re-pointed)

- **SKILL.md body: ~2,000 → ~830 lines** (SKILL.zh.md likewise). What stays resident: positioning, core principles (incl. rule precedence + flagged-diff), setting up, four-layer critique + quick-decision routing, discipline routing protocol + index, feedback reports, systematic verification, Smart Reference Loading (`[VERIFY]`), scripts table, work-mode entries (A/B/C/L full; D/E/F/G/H/I/J/K as decision-carrying stubs), multi-agent collaboration, cross-skill, conversation style, ADHD interaction, anti-drift.
- **Nine new on-demand reference pairs** (all bilingual, CI-checked): `disciplines` (full L1/L2/L3/adjacent dimension tables, arcs, methodology attack tables, fallback protocol), `modes-prewriting` (H/I/J), `mode-c-drafting` (four-stage flow, speak-first drafting, from-scratch orchestration, reflexive writing), `mode-d-adversarial` (personas, anti-sycophancy phrasings, calibration, evidence contract details), `mode-e-bottleneck` (strategies, rhetorical-action menu, capability boundary), `mode-f-revision`, `modes-submission` (G/K), `deep-style`, `multilingual-writing`.
- **Selective Loading Guide rewritten as the actual router**: task → sections in the core file → which `references/` file to Read. The Navigation table (redundant with it) was removed.
- Every mode stub carries its hard constraints and routing signals inline (e.g., Mode E keeps the first-response protocol and typology table; Mode D keeps the concession threshold and evidence contract summary) — the stub is enough to act correctly; the reference file is the full protocol.
- All cross-references re-pointed (fallback protocol, Stage-3 handoffs, perspective-skill integration); READMEs' project structure updated; CI heading-parity check extended to all 18 bilingual pairs.

### Impact

- Per-activation context cost drops from ~35k to ~14k tokens (−60%); a typical task re-reads one reference file (+1–3k) only when routed there.
- Deployment note: the skill already required multi-file support (references/ existed since v4.x); packaging shape is unchanged — targets that flatten to a single file should concatenate `references/*.md` after SKILL.md.

---

## [4.3.0] — 2026-07-03

**Audit-driven release: a 31-agent QA audit (14 mode simulations, 4 static audits, 7-channel market scan, 5-judge panel) → every confirmed defect fixed, plus mechanisms adapted from the strongest peer tools.**

### Fixed — routing & metadata

- **Frontmatter description rewritten to 992 chars (was 1,727 — 69% over the 1,024-char Agent Skills spec limit).** On platforms that truncate at 1,024/1,536 chars, the most aggressive casual triggers never reached the router. New structure: one-line positioning → strongest ~10 triggers (bilingual, merged) → three "Not"s. Chinese twin compressed to 393 chars.
- **Selective-loading wiring**: Mode A/B/C rows now load Discipline-Specific Dimensions + discipline.md (the routing protocol demanded them "on every critique" but the loading table never wired them into the two highest-frequency scenarios) and Smart Reference Loading (`[VERIFY]` rules) during drafting/revision.
- Quick-decision table: three new routes — oral-first drafting → Mode C Stage 3; de-AI with no original → Mode F fallback; "does this concept hold up?" during conception → Mode C step 1 first, Mode D only after initial shape.

### Fixed — internal contradictions (all confirmed by simulation)

- **Rule precedence block** (new, in Core Principles): mode-internal hard constraints > cross-cutting style rules; quick-wins-first suspended while a 🔴 Layer-1 blocker is open; the "2–3 options" rule suspended during Socratic questioning.
- From-scratch scenario rewritten as an H→I→J→C orchestration — its old step 2 ("suggest reading") directly violated Mode I's iron rule.
- Mode C step 1.4 self-contradiction resolved: questions first; candidate paths only from what the author articulated.
- Bottleneck Strategy 5 no longer suggests reading from memory (directional themes only) and warns against prescribing reading for self-doubt bottlenecks.
- "Three scripts" → five (both SKILL files).

### Added — mode upgrades

- **Global flagged-diff rule**: every substantive edit ships as original → proposed + one-line reason, executed only on confirmation.
- **Minimal-start protocol**: casual first contact gets ≤2 questions and immediate work; full 6-item onboarding only once a durable project relationship forms; chat-only environments keep profiles inline; distress arrivals skip onboarding → Mode E.
- **Mode D**: evidence contract (every challenge pinned to chapter/paragraph/quote; no manufactured criticism; no praise sandwich); review-the-review self-check with per-challenge confidence tags; two-stage option (confirm targets, then deep-dive; real review forms override generic personas); Reviewer B re-cast as discipline-routed empiricist; Reader D de-duplicated from Reviewer A; Level 4 mechanical anchor; methodology-focus discipline.md fallback.
- **Mode E** (lowest-scoring mode in simulation, 5.5/10): first-response protocol (acknowledge → classify with ≤2 questions → route); bottleneck typology → strategy routing (question-not-sharp / argument-hollow / emotional / input-shortage / perfectionism); rhetorical-action menu (moves, never finished sentences); capability boundary with human-support referral; mode-switching exits (was a routing dead end).
- **Mode L**: four-way triage (accept / partially accept / defend / reviewer-misread, with response-only dossiers and "verify the misreading against the text first"); response-letter / 修改说明 workflow step with register principles and CN thesis conventions; master table doubles as traceability matrix; optional rebuttal re-review via Mode D persona; the 1–3-comment exclusion no longer applies when a response letter is required.
- **Mode K**: journal policy never asserted from memory (paste or fetch, else conservative default); Template C is now an actual template (paragraph + per-section appendix); tool+version+dates in all templates; placement guidance; tiers merge upward; "I rewrote it heavily" does not demote Tier 3 (regeneration test); log-reconstruction interview; Tier-4 warning carries a remediation path.
- **Modes H/I/J**: anti-fabrication rules mirroring Mode I's iron rule (H's puzzle-mapping; I's gap probes carry low-confidence framing; literature-map claims carry provenance tags); stalemate/exit ramps and re-entry shortcuts (J→C enters at Stage 3; H→C skips core-pressing); Mode J genre arcs (book review, response essay, grant proposal, self-translation) and a restructuring sub-flow; interlocutor placeholders; bilingual name merging (巫鸿/Wu Hung).
- **Modes B/G**: partial/forked-draft handling (unwritten ≠ undelivered); AI-draft review semantics; "blind" defined in one place (two switches, both off); completeness pre-check; distributed-delivery matching.
- **Anti-drift**: checkpoint triggers are deterministic events (post-batch, post-decision, every ~10 turns) instead of the undetectable "session end"; interaction-log reads bounded (last 2 checkpoints + open items).
- **Multi-agent collaboration**: sub-agent contract (profile excerpts + discipline dimensions + calibration + four-tier return schema + anchored findings + anti-sycophancy self-check); fan-out confirmation and ≤5 reviewer cap; "the author is the final eye."
- **Claim-support audit** in Systematic Verification: six-category classification (no support / weak / overstated / misattributed / contradicts / unverifiable) — existence is the script's job, support requires the loaded text.
- STS explicitly served under L3.4; feedback report's two axes defined (body = content, four-tier list = index).

### Added — toolchain & infrastructure

- **scripts/citation-verify.py**: Crossref → OpenAlex cascade; FOUND now prints the matched title + container for human confirmation (surname+year alone had rubber-stamped a *different* Foucault's optics paper); new ERROR verdict for network failures (no more "timeout → NOT_FOUND → delete a real reference"); exit-code contract (0/1/2); unimplemented `--bib` removed.
- **scripts/ai-trace-scan.sh**: directory mode fixed (zsh array + quoted globs — it previously matched nothing and printed a false "✅ no AI traces" with exit 0); counts occurrences, not lines.
- **scripts/citation-format-convert.py**: regex parser replaced with a balanced-brace parser — nested braces, single-line entries, quoted/bare values all parse; unparseable entries reported and skipped, never silently mangled.
- **scripts/citation-consistency.py**: friendly errors; exit codes for CI use.
- **scripts/tests/**: 7 fixtures + 58-assertion offline suite (61 with network), all passing. **.github/workflows/ci.yml**: py_compile, zsh -n, tests, description-length check, bilingual heading-parity across 9 file pairs.
- **references/style-profile-template.md(.zh.md)** (new pair): the "constitution of voice" finally has a template.
- **references/ai-trace-checklist**: reverse check — over-imitation guard (signature-feature density vs the author's base rate) + noise budget; explicit note that the checklist is not an AIGC-detector evasion tool.
- **references/revision-workflow**: triage + response-letter sections (templates, register, CN 修改说明 conventions, traceability matrix, rebuttal re-review).
- **references/project-management**: private vault path removed; directory map includes discipline.md / research-question.md / literature-map.md / outline.md; revision-log `Source:` field defined (Mode K's audit basis).
- **docs/release-checklist.md(.zh.md)** (new pair).

### Changed

- README pairs: TOC; "Seven work modes" → twelve; script table 3 → 5; zip/desktop install paths + verify step; BibTeX 4.3.0; bilingual-status updated. CITATION.cff / .zenodo.json: version, date, abstract brought current. CHANGELOG gained the missing [4.1.1] entry.

### Rationale

v4.2 folded field practice into the skill; v4.3 folds *testing* into it. The audit's five-judge panel scored the pre-release skill 6.9/10 weighted — strongest on humanities specificity (8) and lifecycle coverage (7.5), weakest on token economy (3) and metadata (4.5). This release repairs everything repairable without restructuring. The remaining token-economy debt (SKILL.md body ~500 lines with content sunk to references/) is deliberately deferred to v5.0 — it changes packaging across deployment targets and deserves an atomic, reviewable change of its own.

---

## [4.2.0] — 2026-06-11

**Field-distilled release: everything in this version was first proven in real paper-revision practice, then folded back into the skill.**

The source material: a complete defense-feedback integration cycle on a master's thesis (17 revision dossiers, 4 execution tracks, 100% closure, actual time 55% of plan), a second paper bootstrapped on oral-history methodology, and the version-management conventions that stabilized over three months of daily use.

### Added

- **Mode L · Revision workflow (defense/external-review comment integration)** — the 12th mode. Every reviewer comment becomes an independent revision dossier (location / current text / verbatim comment / plan / draft / verification) indexed by a status-authoritative master table. 5-state status system (pending / in-progress / partial / completed / needs-rework) with a hard definition of "done" (chapter files changed AND revision log recorded). Track grouping by chapter/theme instead of linear or priority-only execution. Author-intent-first deviation rules. Full manual in new `references/revision-workflow.md` + `references/revision-workflow.zh.md`.

- **Mode D · Perspective-skill integration** — formalizes the practice of replacing generic reviewers with theorist-specific perspective skills (distilled via scholar-wendao) when a theorist is load-bearing (cited 3+ times). Three capabilities beyond the generic reviewer: precision attacks inside the concept, lineage discrimination (author depends on one school's *reading*, not "the theorist's own position"), and honest boundaries ("things this theorist never said"). Multi-skill joint review for chapters mobilizing several theorists. Field-proven: a perspective-skill self-check once surfaced a conceptual misalignment one level deeper than the advisor's own objection.

- **Multi-Agent Collaboration section** — for agent-capable environments (Claude Code, desktop agent mode). Governing principle: **diagnosis parallelizes, drafting does not.** Mode D multi-reviewer fan-out (mutually invisible reviewer agents, closer to real peer review than one AI role-playing four reviewers); Mode B chapter-parallel review with the explicit caveat that Layer-1 critique and cross-chapter consistency must stay in the main conversation; claim verification via deep-research-type tools with a 4-tier evidence system (A primary-verified / B reliable second-hand / C oral history / D unverified) where the tier governs assertion strength in the paper.

- **Pre-revision self-check SOP** (in revision-workflow reference): before executing a dossier involving a theorist, self-check the draft with the corresponding perspective skill; fix the dossier draft before executing into chapters.

- **`chapters/` multi-file structure** in project-management references — field-proven for dissertations and 50k+ character manuscripts: per-chapter revision context, chapter-level review fan-out, partial backups. File names encode physical order only, never version numbers.

- **Version naming conventions** in project-management references — "resident sources + milestone archives + versioned exports": three-segment versions mark state nodes, not everyday edits; markdown sources are the single source of truth, docx/pdf are exports; archive and export naming schemas.

- **"Scripts before manual checklists" calling convention** — in shell-capable environments, script-covered checks (cliché scan, citation consistency, pending markers) run as scripts first, with human judgment applied to results; the manual checklist is the fallback, not the default.

### Changed

- **scripts/ table in both SKILL files** now lists all five scripts (citation-format-convert.py and citation-verify.py were missing from the Chinese table since v4.0).
- **Cross-Skill Collaboration** rewritten: adds scholar-wendao/perspective skills, deep-research-type tools, citation-proofing and thesis-formatting tools (division of labor: in-process consistency here, final-format audit there), and meeting-notes tools as Mode L input.
- **Navigation, selective-loading guide, quick-triage tree, frontmatter descriptions** updated for Mode L and multi-agent collaboration in both languages.
- **scripts/ai-trace-scan.sh, scripts/pending-checks.sh**: `grep | wc -l` pipelines hardened with `|| true` so zero-match files no longer abort under `set -e` / `set -o pipefail`.
- **scripts/ai-trace-scan.sh shebang fixed to zsh** — the previous `#!/usr/bin/env bash` shebang crashed on macOS's bundled bash 3.2 (`unbound variable` when iterating the multibyte pattern array under `set -u`); the script was always documented as zsh.

### Rationale

v4.0/4.1 expanded the skill's *coverage* (modes H-K, discipline architecture). v4.2 closes the loop in the other direction: practices that emerged spontaneously during real use — revision dossiers, perspective-skill reviewers, evidence tiers for oral-history claims, chapters/ structure — were being re-invented per project from memory. Folding them into the skill makes them load-bearing infrastructure instead of tribal knowledge. This is also the skill practicing what it preaches: the interaction log's "Skill line" exists precisely so that usage experience flows back into the tool.

---

## [4.1.1] — 2026-05-19

**Version bump only — first Zenodo-archived release.**

### Changed

- `CITATION.cff` version bumped to 4.1.1 (single-line change; functionally identical to v4.1.0).
- Published primarily to trigger the first archive event of the newly activated Zenodo↔GitHub integration, establishing the permanent Concept DOI [10.5281/zenodo.20280772](https://doi.org/10.5281/zenodo.20280772) citable in papers that use this skill.

---

## [4.1.0] — 2026-05-19

**Discipline architecture refactor: flat 7-entry list → 3-layer architecture.**

The previous "Supported humanities disciplines" section listed seven entries (history, philosophy, literature, cultural studies, art history, religious studies, classics) as if they were at the same conceptual layer. They were not — three were L1 main disciplines, one was an L2 subfield, two were L3 cross-disciplinary fields. The set also reflected the author's own research range (history of science / technology philosophy / cultural studies) rather than the actual map of humanities scholarship.

This release restructures the discipline architecture so users from any humanities or humanities-adjacent field can find their position.

### Added

- **L1 layer · 6 main humanities disciplines**: Literature, History, Philosophy, Linguistics (new), Art studies (replacing Art history as the broader parent), Religious studies. Each gets a refined methodology rubric with 5-7 core concerns.
- **L2 layer · subfield inheritance mechanism**: subfields (e.g., 中国古代文学, 经济史, 伦理学, 艺术史, 音乐学) inherit all parent L1 concerns and may add subfield-specific overlays. Documented common subfield overlays for each L1.
- **L3 layer · 9 cross-disciplinary fields with explicit multi-inheritance**:
  - Cultural studies (← Literature + History + Sociology)
  - Classics (← Literature + History + Philosophy + Religious studies + Archaeology)
  - Intellectual history (← History + Philosophy) — *new entry*
  - History of science (← History + Science + Philosophy) — *new entry*
  - Media studies (← Literature + Cultural studies + Philosophy of technology) — *new entry*
  - Digital humanities (← any L1 + Computation) — *new entry*
  - Gender studies (← Literature + History + Cultural studies) — *new entry*
  - Postcolonial studies (← Literature + History + Cultural studies) — *new entry*
  - Environmental humanities (← Literature + History + Science) — *new entry*
- **Humanities-adjacent fields · welcomed with explicit scope notes**:
  - Communication studies (humanities-style, e.g., media ecology school: Innis / McLuhan / Postman / Carey)
  - Educational research (humanities-style, e.g., history of education, philosophy of education, critical pedagogy)
  Each comes with explicit "what we serve / what we don't serve" boundaries, inheritance chain, and field-specific overlay.
- **Fallback protocol**: for any field not on the list — author declares `object of study` + `primary method`, skill infers closest L1 + relevant overlays. Suggests refinement as project develops.

### Changed

- **Onboarding step 1 upgraded to 3-layer elicitation**: now asks separately for L1 (required), L2 (optional), L3 (optional, possibly multiple), and humanities-adjacent declaration. `_writing-config/discipline.md` schema updated.
- **Discipline routing protocol rewritten** to handle layer composition (L1-only, L1+L2, L1+L3 with multi-inheritance, adjacent-field with documented overlay). Tagged outputs in `_meta/interaction-log.md` now identify which layer each attack originates from (e.g., `[Mode D · methodology · L1 History]`, `[Mode D · methodology · L3 Intellectual history]`).
- **Mode D methodology-focus attack table** restructured: 6 L1 attack vectors + 9 L3 overlay attacks + 2 humanities-adjacent attacks. Author with `discipline.md` declaring `史学 + 哲学 + L3 思想史` now gets all three sets of attacks loaded.
- **Mode J standard arc table** restructured: 6 L1 arcs + selected L3 / adjacent arcs (incl. communication studies humanities-style arc, educational research humanities-style arc). Authors in fields with humanities-style sub-traditions now have arc templates.
- **README disciplines section** rewritten with full 3-layer table including L1 (6), L2 (examples), L3 (9), humanities-adjacent (2), and fallback protocol. Same in `README.zh.md`.

### Rationale

The previous flat seven-entry list:
- Mixed conceptual layers (L1 / L2 / L3 not distinguished) — confused users trying to declare their discipline
- Excluded fields where prose IS the argument but where the discipline is formally social science (communication studies, educational research) — these users had no entry point
- Reflected the author's own research range (history of science, technology philosophy, cultural studies) rather than the actual humanities map — newcomers from literature, linguistics, religious studies, art studies (broadly) had partial or no coverage

The 3-layer architecture with explicit multi-inheritance + humanities-adjacent welcome solves all three.

### Migration notes

- Existing `_writing-config/discipline.md` files written under v4.0.0 still work — the new schema is additive (old `discipline: history` is parsed as `L1: History`).
- Users who previously declared "literature" now get the expanded L1 Literature concerns (close reading, theoretical scaffolding, quotation-as-evidence, narrator distinction, genre, form-meaning, intertextuality). The first three were in v4.0.0; the last four are new.
- Users in communication studies / educational research who previously had no entry point should re-declare in onboarding using the new humanities-adjacent option.

---

## [4.0.0] — 2026-05-19

**Major repositioning + capability expansion. End-to-end humanities writing assistant.**

This release is a strategic refactor. Earlier versions positioned the skill as a "humanities-side companion" to academic-research-skills (ARS). v4.0 establishes the skill as an **independent end-to-end writing assistant for humanities scholars** covering the full lifecycle of a humanities paper.

### Added

- **Mode H · Research-question sharpening (Socratic)** — earliest-stage mode. Turns vague topic into sharp, write-able research question through structured Socratic dialogue. Includes humanities-specific question taxonomy (re-reading / re-construction / intervention), the "so what" test, interlocutor identification, and verb-sharpening. Output: `_writing-config/research-question.md`.

- **Mode I · Literature mapping** — organizes references the author has already read into a working camp-and-debate map. Hard rule: does NOT do literature search for the author (no citation hallucination, no replacement of irreducible reading work). Includes optional scholar-wendao integration: load-bearing scholars can be auto-suggested for perspective-skill generation. Output: `_writing-config/literature-map.md`.

- **Mode J · Plan-only outlining** — pure outline mode, no draft writing. Extracted from Mode C to enforce planning discipline. **Discipline-aware**: pulls discipline-specific standard arcs (philosophy concept-puzzle arc, history historiographical-narrative arc, literature theoretical-frame arc, etc.) from `_writing-config/discipline.md`. Output: `_writing-config/outline.md`.

- **Mode K · AI-use disclosure (humanities-journal-specific)** — generates the AI-use disclosure statement required for journal submission. Includes a humanities-specific 4-tier categorization (0: no AI / 1: proofreading-translation-format only / 2: thinking partner / 3: prose-assisted / 4: prose-substantial) and three template options (short footnote / standard methods paragraph / detailed appendix). Audits `_meta/interaction-log.md` and revision history. Warns when AI-use tier exceeds typical humanities journal policy. Output: `_meta/AI-use-statement.md`.

- **Mode D calibration (1–5 levels)** — reviewer intensity is now dialable. Level 1 (gentle reader) through Level 5 (adversarial committee member). Level 3 (peer reviewer) is the default. Author can switch levels mid-session; Concession Threshold tightens at Level 5 (3-of-5 conditions instead of default 2-of-5). Level 4–5 trigger periodic check-in prompts.

- **Mode D methodology-focus sub-mode** — attacks the methodology rather than the content of the argument. Discipline-aware: surfaces discipline-specific methodology vulnerabilities (history: source handling, anachronism; philosophy: argument form, modal scope; literature: hermeneutic circle, genre awareness; etc.). Often surfaces deeper problems than content-level attack.

- **Mode F.coach sub-mode (revision-coach)** — Mode F variant where the skill withholds the revision until the author works through 3–5 diagnostic questions at the relevant critique layer. Slower but trains the author to internalize the four-layer critique. Tagged in revision log as `[coached]`.

- **`scripts/citation-format-convert.py`** — converts BibTeX bibliography between four major humanities citation styles: Chicago (Author-Date), MLA 9, APA 7, and GB/T 7714 (顺序编码制, Chinese national standard). Zero dependencies (Python 3 stdlib only). Supports `@book`, `@article`, `@incollection`, `@inbook`, `@inproceedings`, `@thesis`. Sanity-tested against canonical examples in all four styles. Honest about limitations — not a BibLaTeX/CSL replacement, output should be checked against target journal's style guide.

- **`scripts/citation-verify.py`** — verifies in-prose citations against the Crossref API, flagging hallucinated citations (LLM made-up journal articles). Three verdicts: FOUND / FUZZY_MATCH / NOT_FOUND. Network-rate-limited to 1 req/sec for politeness. Explicitly scoped: Crossref coverage is best for English-language journal articles in indexed journals; NOT_FOUND is expected (and not a problem) for monographs, archival sources, classics, dissertations, foreign-language works — for those, the `[VERIFY]` marker workflow remains the right tool.

- **End-to-end positioning** in both READMEs: full writing lifecycle from research-question sharpening → submission disclosure, with 11 modes mapped to lifecycle stages.

### Changed

- **Removed `## Companion: academic-research-skills` section**. The skill is no longer framed as a humanities-side complement to ARS. ARS remains a designed-acknowledged influence (Concession Threshold pattern in Mode D anti-sycophancy), but is now treated as one of several lateral tools in the Comparison section rather than a designated companion.

- **Rewrote Comparison with adjacent tools** table: lateral positioning against Jenni AI, Paperpal, Yomu AI, Thesify, HyperWrite Devil's Advocate, Grammarly / DeepL Write, and generic ChatGPT / Claude. ARS removed from the table.

- **Rewrote Positioning section** in both `README.md`/`README.zh.md` and `SKILL.md`/`SKILL.zh.md` to emphasize end-to-end coverage and explicitly contrast with "not a research pipeline / not a polishing tool / not a citation manager."

- **CITATION.cff abstract** rewritten to describe all 11 modes and the citation toolchain. ARS reference retained with narrower scope ("acknowledged design influence on early versions").

- **Navigation and Selective Loading Guide** in both SKILL files updated to register new modes H/I/J/K and Mode D/F sub-modes; added task-type routing rows.

- **`scripts/README.md`** updated for the 5-script toolchain: `ai-trace-scan.sh`, `pending-checks.sh`, `citation-consistency.py`, `citation-format-convert.py`, `citation-verify.py`.

### Acknowledgment retained (not removed)

- ARS's Concession Threshold pattern (Mode D anti-sycophancy) and overall design-influence remain credited in CITATION.cff (`references`) and in the SKILL.md Cross-Skill Collaboration section. This is a design-acknowledgment, not a license-derived attribution requirement (model/pattern borrowing does not constitute CC BY-NC 4.0 "Adapted Material" — content authored independently).

### Migration notes for users

- If you used v3.0.0 expecting it to be the "writing half" of an ARS-paired workflow: v4.0 covers the whole writing-side workflow itself. You can still use ARS in parallel if you want (no breaking integration), but the v4.0 modes (H/I/J/K + enhanced D/F) replicate the writing-relevant capabilities of ARS within a humanities-specific design.
- New `_writing-config/` files: `research-question.md` (Mode H), `literature-map.md` (Mode I), `outline.md` (Mode J). Discipline routing now requires `_writing-config/discipline.md`.
- New `_meta/` file: `AI-use-statement.md` (Mode K).
- Existing v3.0.0 projects continue to work — the new modes are additive.

---

## [3.0.0] — 2026-05-19 (earlier same day)

**License change: MIT → CC BY-NC 4.0.**

### Changed

- License changed from MIT to CC BY-NC 4.0 (Creative Commons Attribution-NonCommercial 4.0 International).
- Versions ≤ v2.1.0 remain under MIT and retain their original commercial-use rights for those specific versions.
- From v3.0.0 onwards, commercial use is prohibited without a separate license.
- Updated LICENSE, README badges, CITATION.cff license field, CONTRIBUTING.md.
- Added Commercial Use section to README with inquiry contact (shencong916@gmail.com).
- Author identification upgraded across CITATION.cff and .zenodo.json: `tizzy916` → `Shen, Cong` with affiliation.

---

## [2.1.0] — 2026-05-19 (earlier same day)

**ARS companion section, citation conventions, humanities discipline routing.**

### Added

- Dedicated `## Companion: academic-research-skills` section in both READMEs with division-of-labor diagram and design-lineage attribution.
- `## Supported humanities disciplines` README section: seven main disciplines + cross-disciplinary case, each with failure modes the skill watches for.
- `## Showcase · Before / After` example demonstrating four-layer critique refusing to descend below a broken foundation.
- `### Discipline routing protocol` in SKILL.md: discipline becomes a load-bearing routing variable. Onboarding step 1 upgraded to enforce explicit discipline elicitation.
- Citation section enhanced with proper BibTeX, plain-text attribution block, and "Citing companion tools" subsection for ARS attribution per its CC BY-NC 4.0 license.
- CITATION.cff: full author (Shen Cong + alias + affiliation) and ARS added as `type: software` reference.

---

## [2.0.0] — 2026-05-17

- Initial release of bilingual SKILL.md and READMEs.
- Repository renamed to `claude-skill-humanities-writing-companion`.

## [1.0.0] — 2026-05

- Initial public release as `academic-writer`.
