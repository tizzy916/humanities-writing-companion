# Writing Project Operations Handbook

> **Language / 语言**: **English (current)** · [中文](project-management.zh.md)

> This file defines the file structure, version-management rules, and reference-management workflow for a writing project.
> It is an "operations-layer" guide — when SKILL.md touches file operations, follow this file to carry them out.

---

## 1. Project Folder Structure

Each paper or long-form piece is a self-contained project folder. **Reuse a project path already supplied or established in the session. Ask for a location only when persistence is needed and no path is known; otherwise deliver inline.** Any stable directory works (e.g., `~/Documents/Papers/`, or a folder inside the user's note vault). All examples below use a generic root named `Papers/`:

```
Papers/                                 ← optional parent directory (use the established location)
└── [paper-name]/                       ← paper project folder
    ├── _writing-config/                    ← per-paper configuration; never shared implicitly
    │   ├── style-profile.md                ← the author's voice record (copy from references/style-profile-template.md; Chinese: 写作风格档案.md)
    │   ├── reader-profile.md               ← paired with the style profile — voice and audience are inseparable (copy from references/target-reader-profile-template.md; Chinese: 目标读者档案.md)
    │   ├── discipline.md                   ← L1/L2/L3 discipline declaration, written during onboarding (Chinese: 学科档案.md)
    │   ├── research-question.md            ← Mode H output (Chinese: 研究问题.md)
    │   ├── literature-map.md               ← Mode I output (Chinese: 文献地图.md)
    │   ├── outline.md                      ← Mode J output (Chinese: 论文大纲.md)
    │   ├── citation-style.md               ← the user's chosen citation-format quick reference (Chinese: 引用格式速查.md)
    │   └── academic-writing-checklist.md   ← pre-submission self-check (Chinese: 学术写作检查清单.md)
    │
    ├── [paper-name].md                 ← main draft (short papers: complete single file)
    ├── chapters/                       ← main draft (long-form/dissertations: chaptered multi-file; choose one of the two)
    ├── _meta/
    │   ├── revision-log.md             ← changelog, one entry per change (Chinese: 修改日志.md)
    │   ├── version-archive/            ← major-version snapshots (Chinese: 版本归档/)
    │   ├── revision-workflow/          ← Mode L revision dossiers (see revision-workflow.md; Chinese: 修订工作流/)
    │   ├── writing-progress.md         ← chapter completion tracking (Chinese: 写作进度.md)
    │   └── interaction-log.md          ← writing-discussion log (Chinese: 交互记录.md)
    ├── _drafts/                        ← chapter drafts, experimental fragments (like a feature branch)
    ├── _feedback/                      ← feedback-report archive
    ├── _export/                        ← export scripts/templates (docx/pdf are exports, not sources of truth)
    └── _references/
        ├── reference-list.md           ← bibliography in the user's chosen format (Chinese: 参考文献表.md)
        └── attachments/                ← electronic copies (PDF/EPUB)
```

**File-path naming note**: the tree above shows English defaults (matching the examples in SKILL.md); the Chinese equivalents in parentheses are equally valid. Use whichever matches the author's writing language — the structure is what matters, not the language of the labels.

All relative paths in this handbook are rooted in the individual paper folder. Keep reader, discipline, research question, literature map, outline, citation style, and checklist specific to that paper; a second paper must not overwrite them. Only author-level style preferences may be reused from a shared profile when the author explicitly chooses that arrangement. Record the shared source and keep paper-specific overrides local. For an existing shared configuration, preserve the original and copy only the entries verified to belong to the current paper; ask about ambiguous ownership rather than moving everything.

Create configuration files only as needed: profiles during relevant setup, `discipline.md` when known, and `research-question.md` / `literature-map.md` / `outline.md` when Modes H / I / J actually produce them.

### Single file vs. chaptered multi-file

- **Single-file main draft**: the default for journal articles under ~10k words — easy to export, easy to search
- **chapters/ multi-file**: the default for dissertations and manuscripts above ~50k characters — cleaner context when revising one chapter, chapter-level fan-out for parallel review, version backups can cover only the changed chapter
- When chaptered, file names encode physical order only and **never carry version numbers**:

```text
chapters/
├── 00_abstract.md
├── 00_introduction.md
├── 01_[chapter-one-title].md
├── 02_[chapter-two-title].md
└── 06_references.md
```

❌ Never `04_chapter4_v2.md`, `04_chapter4_final.md`, `04_chapter4_fixed.md` — version information lives in the frontmatter `version` field and the changelog, not in file names.

### First-time initialization

When a persistent writing project is requested, use the structure above. Reuse established answers and ask only about missing essentials:
- The individual paper folder (use the supplied path; ask only if unknown)
- The paper title (used to name the folder and the main draft)
- Single file or chaptered multi-file (advise using the criteria above)
- The citation format (create the matching quick-reference file)
- Whether a draft already exists (if so, import it as v1.0)

When creating `_writing-config/`, copy the two profile templates (`references/style-profile-template.md`, `references/target-reader-profile-template.md`) rather than improvising a structure — the style profile is then filled by analyzing 2–3 of the author's pre-AI writing samples.

---

## 2. Version Management

### Design philosophy

Borrow git's approach to versioning, but adapt it to the realities of academic writing:
- **Minor version = commit**: every meaningful change records its diff and reason
- **Major version = tag/release**: snapshot after completing a round of systematic revision
- **_drafts/ = feature branch**: experimental writing attempts that leave the main draft untouched

### Minor version (patch)

Trigger: a local change within a single conversation. Does not generate a snapshot file.

Record in the changelog:
```markdown
## vX.Y.Z · YYYY-MM-DD HH:MM
**Scope**: [chapter/paragraph location]
**Type**: [argument restructuring / expression polish / citation fix / structural adjustment / new content]
**Source**: [AI-suggested / author-initiated / co-developed]
**Summary**: one sentence
**Diff**:
> [!diff]
> - Original: "..."
> + Revised: "..."
**Reason**: [why this change]
**Verification**: [✅ passed voice-consistency check / ⚠️ needs author confirmation]
```

**The `Source` field is required on every entry.** It records who initiated the change:

- `AI-suggested`: the AI proposed the revision; record author review or acceptance separately rather than assuming it from the edit
- `author-initiated`: the author decided the change (the AI executed it, or the author edited directly)
- `co-developed`: the direction emerged from dialogue and belongs to neither side alone

This field records who initiated a change, not who generated its wording. Also state the actual AI function in the summary (e.g., author-requested AI drafting, proofreading, or outline review), including whether generated material was retained. Mode K audits those facts and the available drafts; `author-initiated` does not mean no AI involvement. Record uncertain provenance as uncertain rather than inferring it from the source label.

Example entry:

```markdown
## v2.3.1 · 2026-05-12 14:30
**Scope**: Chapter 2, section 3, paragraph 2
**Type**: expression polish
**Source**: AI-suggested
**Summary**: removed a hollow lead-in; the judgment sentence moved forward
**Diff**:
> [!diff]
> - Original: "It is worth noting that this shift was not an isolated event."
> + Revised: "This shift was not an isolated event."
**Reason**: "It is worth noting" is a high-frequency cliché (see ai-trace-checklist.md); the judgment is more direct without it
**Verification**: ✅ passed voice-consistency check
```

### Major version (major)

Trigger conditions (any one):
- A chapter rewrite is complete
- The change covers more than 10% of the full text
- A complete chapter-level review has been finished and all its revisions applied
- The author explicitly asks for a version snapshot

Procedure:
1. Increment the version number (e.g., v1.5 → v2.0)
2. Copy the main draft to `_meta/version-archive/vX.Y_YYYYMMDD.md`
3. Update the `version` field in the main draft's frontmatter
4. Update the writing-progress table
5. Record a major-version summary in the changelog

### Version naming conventions (field-distilled)

Core principle: **resident sources + milestone archives + versioned exports**. Version numbers mark *state nodes*, not every everyday edit.

- Three-segment versions: `vMAJOR.MINOR.PATCH` — MAJOR = one complete revision phase (e.g., v6 defense-feedback integration); PATCH = a deliverable node
- Archive naming: `v[version]_YYYYMMDD_[state-or-scope].md` (e.g., `v6.0_20260505_introduction_pre-revision-backup.md`); full chapter-set backups use a folder `chapters_backup_YYYYMMDD_HHMMSS_[reason]/`
- **Single source of truth declaration**: the markdown sources are the only source of truth for writing; docx / pdf are exports — never revise an export directly and pour it back
- Export names carry version and purpose: `[paper]_v6.0.17_YYYYMMDD_submission-final.docx`

### Using _drafts/

When the author wants to try an uncertain line of argument:
1. Create a new file in `_drafts/` (e.g., `_drafts/chapter3_alternative-A.md`)
2. Experiment freely there
3. If the approach is adopted → merge it into the main draft and delete the draft
4. If abandoned → keep it as a record of thinking, or delete it

---

## 3. Reference Management

### Bibliographic information

All cited works are recorded in `_references/reference-list.md`, including:
- Complete entries formatted in the citation style the user chose
- Citation-location markers (which chapters cite the work)
- Source markers for the electronic copy (📁 Drive / 📝 Vault note / ⚠️ to be obtained)
- Vault backlinks (where a corresponding reading note or concept card exists)

### Reference attachments
- Google Drive: a thematically organized e-book library (primary storage)
- Local attachments/: works cited frequently during active work

### Reference-retrieval workflow
When the user says "I need to cite 《XX》":
1. Check the reference list → 2. If a Drive marker exists, help download it → 3. Read the contents → 4. Format it into the user's configured citation style

### Bulk reference download and index building

When the author is about to begin a systematic revision, it is worth building a complete local reference library first:

1. **Extract the reference list**: pull all entries from the bibliography section of the main draft
2. **Search for each electronic copy in turn**:
   - Search Google Drive first (`google_drive_search`)
   - Then check whether the vault holds a PDF attached to a reading note
   - Mark works that cannot be obtained as ⚠️
3. **Download locally**: store every PDF found in `_references/attachments/`, following the naming rule `SurnameYear.pdf` (e.g., `Foucault1975.pdf`)
4. **Build a reference index**: create `_references/reference-index.md`; each entry holds its citation key, a one-sentence summary, core-concept keywords, the chapters that cite it, and the status of its local path
5. **Incremental updates**: update the index each time a new citation is added later

### Vault integration
- Reading notes: `[[《书名》读书笔记]]`
- Concept cards: `[[概念名]]`
- Person profiles: `[[人名]]`

---

## 4. Interaction Log

After every substantive writing discussion, append to `_meta/interaction-log.md`:
- **Paper thread**: what was discussed, what decisions were made
- **Skill thread**: what needs surfaced, what improvements were made (if you are developing the skill in parallel)
- **Reflexive notes**: thoughts that could feed the paper's reflexive-critique chapter (where applicable)

### Session-state checkpoint

For an ongoing file-based project, save a concise checkpoint after meaningful edits or decisions: completed work, current version/location, decisions, unverified issues, and next action. See "Persistent projects and resumption" in SKILL.md; a one-off chat can keep this information inline.

The checkpoint exists so that, on cross-session resumption, the AI can quickly rebuild the full working context rather than relying on memory that may have been compacted away.

---

## 5. Inbox Integration

If the user's vault has an Inbox system, append a brief record to the Inbox after each edit to a paper file.

> How to decide: check whether the vault root holds a `SYSTEM.md` file. If so, read its Inbox rules and follow them. If there is no `SYSTEM.md`, or it defines no Inbox, skip this step to avoid duplicate records.

---

## 6. Export Workflow

Once the paper is finished, export according to the user's choice:
- **.docx**: invoke the docx skill
- **.pdf**: invoke the pdf skill
- **.tex**: generate a LaTeX source file using the requested or existing template; ask only if an unresolved template choice materially affects the output
- Run the academic-writing checklist before exporting
