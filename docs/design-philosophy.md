# Design Philosophy · Why This Is Not Another Polishing Tool

> **Language / 语言**: **English (current)** · [中文](design-philosophy.zh.md)

> This document explains why the humanities-writing-companion skill is the way it is. It is not usage documentation (that is the job of [SKILL.md](../SKILL.md) / [SKILL.zh.md](../SKILL.zh.md) and the [README](../README.md) / [README.zh.md](../README.zh.md)) but a **design statement** — a record of the judgments and trade-offs that run through the whole skill, so that a reader can see the stance behind each module, extend the skill in a way consistent with that stance, or, if they disagree, know exactly what they are disagreeing with.

---

## Prologue · A Concrete Scene

I started building this skill from a very concrete frustration.

I had just handed a long essay to an AI for a round of "polishing." When the text came back, it read more evenly than my original: every sentence balanced, every paragraph opening with an "It is worth noting" or "It is not hard to see," the whole register uniformly cool and detached, like a set of meeting minutes. But the more I read, the more uneasy I became — was this even mine? Could I still recognize the traces of my own thinking in this prose? The asymmetrical judgments I had made, the hesitations where I'd held something back, the leaps that forced two seemingly unrelated fields together — where had they gone?

In that moment I realized: the problem with AI polishing tools is not that they "do a bad job." They do a very good job — at *writing a standard academic paper*. But academic writing is not merely "standard." It is the textual trace left by a particular person thinking through a particular problem. When the AI erases that particular person, what it takes away is not typos and broken syntax — it is the thinking itself.

This skill is my response to that frustration.

---

## I · Thought First, Format Second

Mainstream AI writing tools order their priorities like this:

```
格式 → 表达 → 结构 → 概念 → 论证
```

They start with what is easiest to do — spelling, grammar, sentence shape. These are the layers a computer handles best, and the layers where the user most readily sees a result. But the core of a humanities paper has never lived at this layer. Whether a paper holds up does not turn on where its commas sit; it turns on whether its claims can withstand rebuttal, whether its concepts have genuine explanatory force, whether its structure is the best path for the argument's advance.

So this skill inverts the order:

```
论证 → 概念 → 结构 → 表达 → 格式
```

This is a priority for broad reviews, applied within the author's requested scope. When a foundation problem is evidenced, explain it first. A narrow sentence edit can still proceed where its corrections do not depend on resolving that problem; the skill must not silently expand the assignment.

This rule has a counterintuitive consequence: the early feedback you get from this skill often **won't make your prose "look" better**. It will make you see what you'd rather not — whether your core concept is a rhetorical label rather than an analytical tool, whether the several theoretical resources you claim to be synthesizing actually form a unified perspective, whether your literature review is trying to "appear erudite" or genuinely in dialogue with those scholars. These problems cannot be solved with better sentences. They send you back to the argument itself.

I think this kind of "inverted priority" is exactly the assistance humanities authors actually need.

---

## II · The Epistemological Self-Awareness of "My Hand Writes My Voice"

One line gets emphasized again and again across the skill: **"My hand writes my voice" — every revision you suggest should preserve and strengthen the author's individual voice.**

This sounds like a UX principle — "respect user preferences." But it is in fact an epistemological claim.

Here is how I think about it. Voice is not a fixed essence that pre-exists writing, waiting for the AI to "identify" and "protect." Voice is continuously constructed and evolved through the practice of writing. As part of the writing toolkit, AI has been participating in that construction all along — just as pen and paper, the typewriter, and Word once shaped how writers express themselves. This implies two things.

First, the goal is not to "isolate" AI's influence. That cannot be done, and should not be attempted. Every writing tool shapes its author. What matters is whether that shaping has passed through the author's reflection.

Second, the goal is to make the AI increasingly able to "think and express in the author's way." This sounds like the "identify your personal style" pitch of Voice DNA–type tools, but there is a fundamental difference: Voice DNA assumes there is a "true self" waiting to be discovered and sealed off, whereas I assume an **author who is still evolving**. The AI's job is to keep pace with that evolution, not to tether the author to the "self" of some fixed point in time.

This matters because it determines how the skill handles the anxiety of **"AI changed my voice."** The skill's answer is: the anxiety is pointed in the wrong direction. What you should really be wary of is not "AI changed my voice" — any tool changes a writer — but **"I am accepting AI output without examination."** The difference is not how much the AI changed, but whether the author was present while it changed.

Mode F (draft revision) is designed precisely for this situation: when an author brings an AI-polished version in for revision, each change is to be classified as an "improvement" or an "alienation," then improvements are kept and alienated passages restored. This is not "anti-AI"; it is folding AI's influence into the author's conscious choice.

---

## III · The Engineering Metaphor: Scaffolding, Not Decoration

A set of engineering metaphors runs through the skill:

- minor version = git commit
- major version = release
- `_drafts/` = feature branch
- feedback tiers = code review's blocker / major / minor / question
- systematic verification = unit test
- cross-session resumption = CI/CD resume-from-breakpoint

I have seen tools that use engineering metaphors as a prop to "look professional," and that use is decorative and uninteresting. I use these metaphors because they supply a **real cognitive architecture** — they give the author a set of capabilities that used to exist only in engineering:

**Traceability.** Every revision records a diff and a reason, which means three months later I can go back and ask, "Why did I cut that passage back then?" — relying not on memory but on a commit-like record. Revisions in academic writing often span months, even years; without this capacity for retracing, an author will keep forgetting their own judgments.

**Verifiability.** A "unit test" for an argument sounds odd — a scholarly argument is obviously not a boolean. But the value of a verification checklist is not "tick it all and you're right"; it is **making sure no dimension was forgotten**. A common failure mode is for an author, mid-revision, to focus only on the one or two things they care about most (say, conceptual precision) and forget to check citation completeness / chapter cumulativeness / stylistic consistency. The checklist is not a judge; it is a checklist.

**Resumability.** The core insight of CI/CD is that "any interruption should be recoverable from the last stable state." Academic writing is constantly interrupted — meetings, holidays, getting stuck, switching topics. The skill's anti-drift protocol (session-state checkpoints + anchor files + revision log) borrows this idea, turning a long paper project into a long-running service rather than a one-shot deal.

**Layered processing.** Code review's blocker / major / minor / question tiers force a reviewer to distinguish "must fix" from "could fix." That distinction is just as crucial for academic writing — a paper having 50 improvable spots is perfectly normal, but only 3 of them are blockers. If an author treats all 50 alike, they sink into a polishing loop that never ends.

The engineering metaphor is not meant to turn a paper into code; it is meant to give the author the tools to **stay sane** through the uncertainty of the writing process.

---

## IV · Anti-Sycophancy vs. Dialogical Posture: A Seemingly Contradictory Design

Two of the skill's principles look like they are fighting each other:

**Scholarly posture** (the style profile): advance dialogically, acknowledge an interlocutor's contribution before naming its limits — treat Rancière, Stiegler, Mumford, and others as interlocutors, not targets to be shot down.

**Anti-sycophancy mechanism** (devil's advocate mode): assess the evidence rather than pressure or a count of conditions. A single decisive source passage or valid counterargument is enough to withdraw or narrow a challenge; a refuted objection must not be repeated.

How do these reconcile?

My answer is: they address **two completely different relationships.**

The scholarly posture concerns the relationship between the author and **the already-published scholarly literature**. That relationship is one-directional and asymmetrical — Rancière cannot jump out and rebut your paraphrase of him. So the author must take the initiative to give the other party the "strongest version" of their position before criticizing it. This is scholarly ethics.

The anti-sycophancy mechanism concerns the relationship between the author and **the AI they are currently in dialogue with**. That relationship is bidirectional, but with a peculiar asymmetry — during training the AI was optimized for "user satisfaction," which gives it a strong tendency to concede. That tendency conflicts with the very nature of scholarly dialogue. A genuinely critical peer does not retract a challenge because you've grown impatient.

So the two principles are not fighting. What they say is:

> Be generous toward **the literature already written**; be strict toward **the critique now underway**.

The "minimum standard before conceding" checklist in devil's advocate mode (the author cites specific literature, redefines a conceptual boundary, raises a new counter-example, and so on) is not there to make the AI hard on the author. It is there to **keep the AI from playing a fake peer**. A "critique" that yields under emotional pressure is worthless — it can neither help the author find blind spots nor rehearse the attacks of a real reviewer.

This design comes from an observation: the feedback many people get when they use AI for "stress testing" is distorted, because the AI conceded the moment they pushed back. They think the argument held; in fact the AI just didn't feel like pressing further. On this point the skill deliberately gives up "user-friendliness" — when devil's advocate mode is engaged, the author is actively asking for an unfriendly interlocutor.

---

## V · ADHD Adaptation: As a Cognitive-Architecture Choice

The skill has a whole section on ADHD adaptation — batched feedback / quick wins first / topic-jump support / reorientation points. The way that section is written might lead someone to mistake it for an "inclusivity feature," a concession to users with certain cognitive traits.

I want to be clear — it is not. It is a **cognitive-architecture choice**, and it holds for all authors.

Academic writing has several intrinsic features:

- long-tail dependencies (revising one claim may require returning to a chapter from three months ago)
- discontinuous attention (a train of thought is constantly interrupted, pulled toward a side branch, or altered by newly read literature)
- leaping insight (the most important progress often happens during an "irrelevant" change of subject)

These features are not exclusive to "ADHD users" — they are the normal condition of any deeply thoughtful writing process. But mainstream writing tools tend to assume a **linear, focused, long-session author** — you open the document, edit from top to bottom, finish in a single sitting. That assumption does not match reality.

The skill's ADHD adaptation is, in essence, an acknowledgment of that mismatch, followed by interaction patterns designed to work *with* the actual writing process:

- **3–5 items per round**: because that is genuinely how many revision suggestions a human can absorb in a single exchange. Hand someone a 20-item list and the author takes the list and changes nothing.
- **Quick wins first**: because the author needs a sense of progress to keep going. Fixing one inconsistent citation format is easier to convert into the feeling of "I did something" than debating a fundamental argumentative flaw — and that feeling is the fuel that sustains stamina.
- **Topic-jump support**: when the author suddenly leaps from Chapter 3 to an idea about the introduction, don't say "let's finish Chapter 3 first." That leap may be intuition perceiving a not-yet-articulated argumentative connection; dragging the author back by force will destroy it.

None of these designs are proprietary to ADHD. They are **respect for the actual rhythm of academic writing** — it just happens that authors with ADHD are the first to notice the mismatch with mainstream tools, which is why the section uses the word "ADHD."

---

## VI · Reflexive Writing: Recursion Is Not a Contradiction

The skill's reflexive-writing module is a recursive structure. If the author's research itself involves human-AI collaboration (e.g., an autoethnography of AI-assisted writing / a study of cognitive agency in the age of AI), then the author's *process of using the skill* **itself** becomes part of the research. The skill is a tool, but at the same time it is an object of study.

Many people find this contradictory — you can't be both the researcher and the object of research. But this "contradiction" is in fact common in the humanities. For instance:

- the anthropologist doing ethnography is themselves in the field
- the sociologist studying class themselves occupies a class position
- the philosopher critiquing technology is themselves using technological tools

These are not bugs; they are features. Acknowledging the researcher's presence is more honest — and often more insightful — than pretending to "objective neutrality." Methodological traditions like autoethnography and reflexivity are built precisely on that acknowledgment.

The skill's classification of "six kinds of reflexive moment" (🔄 direction change / 🚫 refusal / 🎭 voice conflict / 🔧 tool dependency / 💡 unexpected insight / 🤖 AI-trace awareness) is a material-gathering framework for exactly this kind of reflexive research. Each category corresponds to a kind of AI-collaboration experience worth discussing in a paper. Recent work by Christou (2026), Wiles (2025), Panke (2025), and others provides a methodological reference point for this kind of reflexive research — this module has an explicit scholarly basis in SKILL.md.

I raise this because many AI writing tools deliberately make themselves **invisible** — they want the reader, finishing the author's paper, to have no idea AI was involved. I think that "invisibility" is, in certain contexts, dishonest. If the author's research itself concerns the human-AI relationship, then the AI tool's invisibility erases an important research dimension.

The skill does not try to be invisible. What it offers is a **researchable collaborative process** — interaction logs, revision logs, reflexive-moment classification — and all of this exists not "for convenience" but to turn AI collaboration into research material that can be cited in a paper and examined by peers.

---

## VII · From the Particular to the General: An Honest Account of the Design's Origin

I want to close this document with an honest declaration.

This skill was not designed starting from "the general needs of academic writing." It grew out of **one specific humanities paper project** — I was writing a paper of my own, gradually discovered I needed these tools, and then sedimented those tools into a skill. Before its public release, the skill was full of specific context like "v3.8 / 6.10 manuscript comparison" and "technical liberalism vs. craft liberalism" — these were the traces of the skill's real evolution.

To turn the skill into a **general humanities-writing skill**, I replaced all that personal context with generic placeholders (see the commit history). But I want to say one thing: de-personalizing is not the same as "de-particularizing."

The reason this skill can be more specific than a "general academic writing tool" is precisely that it grew out of a specific project. The problems it handles — "comma-strung run-on sentences," "introduce a scholar at length, then criticize," "logical over-filling," and so on — were not designed in a vacuum; they are real problems encountered in one specific author's real writing.

This origin has two implications:

**Strength**: the skill has a fairly accurate grasp of "what humanities authors are actually doing," rather than guessing in the abstract.

**Limitation**: its initial form may carry that project's disciplinary leanings (humanities / a philosophical bent / Chinese-language writing / an art-history lineage). In other disciplines and settings, it may not transplant cleanly.

I don't want to pretend this is neutral. [`docs/cross-domain-testing.md`](cross-domain-testing.md) invites authors from other disciplines to test the skill, precisely so that the design can grow up amid more particulars — rather than becoming a "general framework" detached from any concrete context.

Generality should arise from **the intersection of multiple particulars**, not from a hollow shell abstracted out of them.

---

## Coda · The Skill Is Not a Tool, but Infrastructure

If I had to sum up this skill's design philosophy in one sentence, it would be this —

**The skill is not a tool, but infrastructure.**

A tool is something you put back when you're done — a hammer, scissors, a grammar checker. Infrastructure is the thing you work *on top of* — the power grid, git, a writing environment.

Mainstream AI writing tools are tools. They solve a specific task (polish / retrieve / continue) and then exit. They make no ongoing commitment to the author's cognitive process.

This skill wants to be infrastructure. Through a whole apparatus — version management, revision logs, the style profile, the target-reader profile, the reference index, reflexive records, checkpoints + anchor files — it turns a long paper project into **a continuously running system**: the author can interrupt, return, leap, change their mind, while the system stays ready with context for the next session.

This ambition may be too large. But if we accept that what humanities authors are really doing is not "producing prose" but "thinking through a problem over the long term," then only infrastructure-level assistance matches the scale of the thing. The scale of a polishing tool is simply too small.

---

## After This Document

If you've read this far and find this set of positions acceptable, you are welcome to try the skill in your own writing. If you think one of the principles is wrong — especially if you think **the first principle** (thought before format) does not hold in your discipline — please come to [Discussions / Ideas](https://github.com/tizzy916/humanities-writing-companion/discussions/categories/ideas) and argue against me. The skill's design stance is not beyond challenge, but the challenge has to happen at the same level (the level of design philosophy), rather than staying at the level of an "add this feature" request.

One last invitation: if your paper itself studies the human-AI relationship / the technology of writing / cognitive agency, you are welcome to treat this skill as an object of study. All its design decisions are recorded in the repository; all its traces of evolution are visible. You can cite it ([CITATION.cff](../CITATION.cff)), criticize it, fork it into a competing version — its existence is not meant to be adopted, but to let dialogue happen between adversaries with **a concrete design stance**.

---

*This document is open. If a reader would like to join the discussion of the design philosophy, PRs and proposals in Discussions are welcome.*
