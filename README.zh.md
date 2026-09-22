# 人文学科写作伙伴 · Humanities Writing Companion

> 一个为人文学者设计的 agent skill，服务于以长篇论证性文本为主要交付物的写作——历史、哲学、文学、文化研究、艺术史、宗教学、古典学。采用开放的 [Agent Skills](https://agentskills.io)（SKILL.md）格式——Claude Code、Claude Agent SDK 以及任何支持该格式的 agent 都可以使用。

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](./LICENSE)
[![Skill format: Agent Skills](https://img.shields.io/badge/skill%20format-Agent%20Skills%20(SKILL.md)-orange)](https://agentskills.io)
[![Status: stable](https://img.shields.io/badge/status-stable-green)]()
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20280772.svg)](https://doi.org/10.5281/zenodo.20280772)
[![Wiki](https://img.shields.io/badge/📖_Wiki-教程与指南-blue)](https://github.com/tizzy916/humanities-writing-companion/wiki)

**[📖 Wiki 教程](https://github.com/tizzy916/humanities-writing-companion/wiki)** · **[English README](./README.md)** · **[Skill 源文件 · 英文](./SKILL.md)** · **[Skill 源文件 · 中文](./SKILL.zh.md)**

---

## 目录

- [定位](#定位)
- [本 skill 严肃对待的三件事](#本-skill-严肃对待的三件事)
- [一次典型的交互](#一次典型的交互)
- [核心特性](#核心特性)
- [支持的人文学科](#支持的人文学科)
- [Showcase · 真实 Before / After 案例](#showcase--真实-before--after-案例)
- [安装](#安装)
- [快速上手 · 三个典型场景](#快速上手--三个典型场景)
- [与同类工具的差异](#与同类工具的差异)
- [项目结构](#项目结构)
- [设计哲学](#设计哲学)
- [引用本工作](#引用本工作)
- [贡献](#贡献)
- [关于作者](#关于作者--about-the-author)
- [License](#license)
- [致谢](#致谢)

---

## 定位

**人文学者的端到端写作助手**——覆盖一篇人文论文从研究问题到投稿披露的完整生命周期:

```
研究问题 → 文献地图 → 规划 → 起草 → 修订 →
对抗性审稿 → AI 痕迹清理 → 盲读核对 → AI 使用披露
```

服务于**"文字本身就是论证"**的领域——历史、哲学、文学、文化研究、艺术史、宗教学、古典学、思想史、科学史以及相邻的人文导向学科。

本 skill 不是润色工具,不是引用管理器,也不是研究流水线。**本 skill 是一个陪你走完整个写作弧线的思维伙伴。**

### 覆盖写作全生命周期的 12 个模式

| 阶段 | 模式 |
|---|---|
| **写作前** | Mode H · 研究问题 sharpening · Mode I · 文献脉络梳理 · Mode J · 规划专项模式 |
| **起草** | Mode C · 构思 → 新内容写作 · Mode A · 段落对话 |
| **审读** | Mode B · 章节审读(四层批判) · Mode D · 魔鬼代言人(1-5 级 calibration + 方法论专项) |
| **修订** | Mode E · 写作瓶颈辅助 · Mode F · 底稿修订(含 revision-coach 子模式) |
| **投稿前** | Mode G · 盲读核对 · Mode K · AI 使用披露 |
| **评审后** | Mode L · 修订工作流(答辩/外审意见整合,修订档案制) |

外加**引用工具链**(`scripts/`):格式一致性扫描、格式转换(Chicago / MLA / APA / GB7714)、Crossref/OpenAlex 元数据候选检索（不核验原文或论断支持）。在具备 agent 编排能力的环境(如 Claude Code)中,Mode B/D 审读可以分派给并行审稿 agent；待核断言可查阅来源，分别记录出处、支持关系与局限。

---

## 本 skill 严肃对待的三件事

通用 AI 写作工具不会处理人文学科的这三件事：

**1. 声音保持是核心学术价值，不是风格装饰。**
在人文学科里，作者的声音承载认识论重量：它表明作者从哪个智识传统中写作、把谁视为对话者、哪些动作是自己的而哪些是借来的。一篇被润色成"标准学术英语"的论文，丢失的就是这种信号。本 skill 帮助你写得更像自己，而不是更不像。

**2. 论证和散文是不可分离的。**
实证研究里，糟糕的写作可以毁掉一个完美的实验。但人文学科里，**写作就是论证本身**——一句疲软的话、一个含糊的概念、一个未经辩护的过渡，都是论证失败。本 skill 在"散文中的论证"层面工作。

**3. 审稿人是真实而对抗性的。**
人文审稿人不温和。一个理论概念会被测试其锋利度；一个历史断言会被测试其证据；一个哲学论证会被测试最强的反对意见。本 skill 在内部模拟这种对抗，让论文在投稿前就先遇上。

---

## 一次典型的交互

```
你：帮我看看这段。我在论福柯的全景敞视主义如何延伸到数字平台。

[skill 读取该段 + 你的写作风格档案]

伙伴：
  我注意到三件事，按优先级排序。

  🔴 基底问题：你把"全景敞视"用作平台监控的隐喻，但福柯的原初概念
     依赖于一种建筑学装置生产出特定的主体位置。平台生产的是另一种主体
     （数据主体，而不是关在牢房里的身体）。你可以选择 (a) 把这个类比
     明确为类比并讨论差异；或者 (b) 用 Zuboff 的"工具型权力"，更贴合
     数据情境。你想走哪个方向？

  🟡 论证问题：第二段从"平台收集数据"跳到"这构成了监控"，没有补上中间
     "可见性即权力"的环节。一个善意读者会跟不上。

  🟢 文风问题：你的风格档案里写"第一人称 + 破折号插入"。第三段以"本文
     认为……"开头，读起来像八股。要不要恢复第一人称？

你：走方向 (b)。改吧。

[skill 给出修订；你保留听起来像你自己的版本]
```

这就是"思想对话伙伴，而不是润色工具"在实践中的样子。

---

## 核心特性

### 四层批判模式（不是单一润色）

```
第一层 · 基底批判 — "这篇论文在学术上成立吗？"
第二层 · 结构批判 — "论证是怎样展开的？展开得好吗？"
第三层 · 段落批判 — "这一段在做什么？做好了吗？"
第四层 · 语句批判 — "这句话说对了吗？说好了吗？"
```

**按范围确定优先级**：全文审阅先处理重要论证问题；局部修改不依赖这些问题的解决时，完成用户所要求的修改。

### 魔鬼代言人 + 抗谄媚机制

模拟三种审稿人 + 一个善意困惑读者：
- 审稿人 A · 理论苛刻型
- 审稿人 B · 历史实证型
- 审稿人 C · 方法论质疑型
- 读者 D · 善意困惑型（**独到设计**：能让善意读者困惑的地方就是论证薄弱处）

**依据证据纠正**：不因压力无依据让步；但一条决定性的原文或有效推理足以推翻异议，就应撤回。审稿强度不允许无视纠正。

### 文风深层学习与保持（"我手写我口"）

不只是句式偏好，还包括：
- **论证节奏**（线性 / 螺旋 / 张弛）
- **学术姿态**（批判性继承 / 对话性推进）
- **引用的修辞功能**（权威锚点 / 批判靶标 / 对话接口 / 叙事性 / 概念工具）
- **AI 痕迹排查清单**（八类未审视表达模式 ≠ AI 套话 ≠ 学术八股）

### 学科特殊维度

不同章节类型对应不同的批判策略：
- 历史叙事 · 时代错位、反事实压力测试、史料处理
- 哲学论证 · 概念推演、跨理论嫁接、最强反对意见
- 文学批评 · 细读与诠释、文体意识、形式与意义
- 文化研究 · 权力-知识框架、位置性、概括范围
- 艺术史 · 描述与诠释、来源、接受史
- 宗教学 / 古典学 · 源语严谨性、传统意识、内外位置
- 案例分析（跨学科共用）

### ADHD 友好的交互设计

- 反馈分批：每轮 3-5 项最多
- 快速胜利优先
- 跳跃跟随（话题跳跃可能是洞见信号）
- 番茄钟友好的任务单元
- 长对话每 4-5 轮给"我们现在在哪"摘要

### 自反性写作支持（独到模块）

如果作者的研究本身涉及人-AI 协作（autoethnography of AI-assisted writing），本 skill 提供六类"反思时刻"分类：

🔄 方向转变 / 🚫 拒绝 / 🎭 声音冲突 / 🔧 工具依赖 / 💡 意外洞见 / 🤖 AI 痕迹觉察

**学术依据**（在论文里可直接引用）：
- Christou (2026). *Reconfiguring Reflexivity in the Era of AI*. *Qualitative Inquiry*.
- Wiles (2025). *Recursive Cognition in Practice*. *International Journal of Qualitative Methods*.
- Panke (2025). *How Can (A)I Research This? An Autoethnographic Exploration of Generative AI*.

### 工程化基础设施

借鉴软件工程的最佳实践，服务于人文写作：
- **版本管理**：小版本 = commit / 大版本 = release / `_drafts/` = feature branch
- **修改日志**：每次修改记录 diff + reason（像 git commit message）
- **反馈报告**：Blocker / Major / Minor / Question 四级（借鉴 code review）
- **系统性验证清单**：论证完整性 / 概念一致性 / 引用完整性 / 文风一致性
- **`[VERIFY]` / `[待核对]` 硬标记**：抗引用幻觉——绝不允许进入投稿版本

### 十二个工作模式（不是单一对话模式）

- **模式 A** — 段落级对话
- **模式 B** — 章节级审读
- **模式 C** — 构思 → 新内容写作（含协作式起草协议）
- **模式 D** — 魔鬼代言人（1–5 级 calibration，方法论专项子模式）
- **模式 E** — 写作瓶颈辅助（五种解冻策略）
- **模式 F** — 底稿修订（双版本对照，对抗 AI 腔调，含 revision-coach 子模式）
- **模式 G** — 盲读核对（机械检查"承诺-兑现"）
- **模式 H** — 研究问题锐化（苏格拉底式对话：从模糊兴趣到可写的锋利问题，含 "so what" 测试与真实对话者识别）
- **模式 I** — 文献脉络梳理（把你已经读过的文献整理成阵营与论战地图——绝不替你搜文献）
- **模式 J** — 规划专项（学科感知的标准论证弧线；只做大纲，不写正文）
- **模式 K** — AI 使用披露（审计实际 AI 参与度，四级分类，生成期刊可用的披露声明）
- **模式 L** — 修订工作流（答辩/外审意见整合：一条意见一份修订档案，状态权威主表索引）

### 工程化辅助脚本

[`scripts/`](./scripts) 提供五个零依赖工具：

| 脚本 | 用途 |
|------|------|
| `ai-trace-scan.sh` | 扫描套话与连接词堆砌 |
| `pending-checks.sh` | 汇总所有 `[VERIFY]` / `[待核对]` / `❓ 待讨论` / `[AI 草稿]` 标记 |
| `citation-consistency.py` | 引用格式一致性扫描（括号 / 逗号 / 连接词 / 中英姓名 / 页码） |
| `citation-format-convert.py` | BibTeX 文献表在 Chicago（著者-出版年）/ MLA 9 / APA 7 / GB/T 7714 之间转换 |
| `citation-verify.py` | 检索 Crossref/OpenAlex 元数据候选（FOUND / FUZZY_MATCH / NOT_FOUND / ERROR）；不核验原文或论断支持 |

---

## 支持的人文学科

本 skill 用**三层架构**组织人文学科,以便学科路由系统真正匹配作者的工作位置——而不是套用一个扁平的七项清单。作者在 onboarding 时声明学科(或 skill 从草稿中推断),路由按对应层级加载。

### L1 · 人文学科六个一级大类

这些是经典的人文学科 L1 大类。每个携带一组通用 AI 写作工具看不见的核心方法论关切。

| L1 大类 | 研究对象 | 核心方法论关切 |
|---|---|---|
| **文学 · Literature** | 文本(诗、小说、戏剧、散文) | 文本细读 vs 解释 · 文类意识 · 形式-意义贴合 · 互文性 |
| **史学 · History** | 过去的事件、人物、社会 | 时代错置 · 反事实压力 · 史料处理(一手 vs 二手)· 因果链透明 · 史学史定位 |
| **哲学 · Philosophy** | 概念、论证、规范命题 | 概念派生 · 论证形式(形式 vs 实质)· 跨理论移植代价 · 最强反对的 steel-man · 模态范围 |
| **语言学 · Linguistics** | 语言结构与使用 | 数据来源(corpus / 直觉 / 启发实验)· 形式 vs 功能 · 描述 vs 规定 · 跨语言主张范围 |
| **艺术学 · Art Studies** | 艺术作品(绘画、雕塑、音乐、电影、建筑) | 描述 vs 解释(必须分开)· 来源与物质性 · 接受史 · 媒介特异的形式分析 |
| **宗教学 · Religious Studies** | 宗教传统、文本、实践 | 源语言严谨度(原文 vs 译本)· 传统位置 · 内部/外部(emic vs etic)· 比较方法 |

### L2 · 常见子学科(非穷举)

子学科**继承父 L1 的全部方法论关切**,外加作者在 onboarding 时声明的具体约束。例子——还有更多可能:

| 父 L1 | 子学科示例 |
|---|---|
| 文学 | 中国古代文学 · 中国现当代文学 · 比较文学 · 文学理论 · 文学批评 · 外国文学 |
| 史学 | 中国史 · 世界史 · 经济史 · 社会史 · 文化史 · 城市史 · 断代史(唐史、近代史等)|
| 哲学 | 中国哲学 · 西方哲学(分析 / 大陆)· 伦理学 · 美学 · 政治哲学 · 科学哲学 · 现象学 |
| 语言学 | 历史语言学 · 社会语言学 · 语用学 · 类型学 · 话语分析 |
| 艺术学 | 艺术史 · 音乐学 · 电影学 · 戏剧学 · 建筑史 |
| 宗教学 | 基督教研究 · 佛教研究 · 道教研究 · 宗教比较学 |

如果你的子学科未列出,在 onboarding 时声明即可——自动继承父 L1。

### L3 · 跨学科 / 交叉领域(显式多重继承)

这些是人文领域中显式从多个 L1 取材的领域。skill 会加载**所有父 L1 的方法论关切 + L3 特化叠加**。

| L3 领域 | 继承自 | L3 特化叠加 |
|---|---|---|
| **文化研究 · Cultural Studies** | 文学 + 史学 + 社会学 | 权力-知识框架 · 位置性 · 概括范围 |
| **古典学 · Classics** | 文学 + 史学 + 哲学 + 宗教学 + 考古学 | 文本批评(写本传统)· 语文学严谨度 · 接受史 |
| **思想史 · Intellectual History** | 史学 + 哲学 | 概念史方法(Begriffsgeschichte vs Cambridge School)· 语境 vs 文本 · 避免现时主义 |
| **科学史 · History of Science** | 史学 + 科学 + 哲学 | 内史 vs 外史 · 辉格史警惕 · 技术准确性 · 案例研究校准 |
| **媒介研究 · Media Studies** | 文学 + 文化研究 + 技术哲学 | 媒介形态学 · 接受研究 · 技术-社会共构 |
| **数字人文 · Digital Humanities** | 任一 L1 + 计算 | 数据可重复性 · 工具透明 · 算法偏倚 · 计算选择的方法论披露 |
| **性别研究 · Gender Studies** | 文学 + 史学 + 文化研究 | 性别本体论 · 历史化性别 · 交叉性 |
| **后殖民研究 · Postcolonial Studies** | 文学 + 史学 + 文化研究 | 位置性 · 翻译政治 · 抵抗欧洲中心主义 |
| **环境人文 · Environmental Humanities** | 文学 + 史学 + 科学 | 人类纪框架 · 多物种视角 · 尺度问题(局部 vs 行星)|

### 人文邻近领域(欢迎,带 scope 注释)

有些领域形式上归在社会科学,但包含强烈人文导向的子传统(文字本身就是论证)。本 skill 欢迎这类工作:

| 领域 | 服务什么 | 不服务什么 |
|---|---|---|
| **传播学 · Communication Studies**(人文路径)| 媒介环境学派(Innis / McLuhan / Postman / Carey);批判传播学;人文导向的文化-媒介研究 | 实证 / 实验传播学,作为量化方法的内容分析 |
| **教育学 · Educational Research**(人文路径)| 教育史 · 教育哲学 · 人文模式的课程理论 · 批判教育学 | 量化教育心理学 · 实证学习成效研究 |

继承关系:传播学(人文路径)← 媒介研究 + 哲学 + 文化研究。教育学(人文路径)← 史学 + 哲学 + 文化研究。

### 兜底协议——如果你仍然找不到自己的领域

在 onboarding 时告诉 skill:

1. **研究对象**:文本 / 过去事件 / 概念 / 现象 / 物件 / 实践 / 语言结构 / ……
2. **主要方法**:文本细读 / 档案研究 / 论证分析 / 民族志 / 比较 / 语文学工作 / ……

skill 会推断最接近的 L1 + 相关 L3 叠加,写入 `_writing-config/学科档案.md`,然后继续。你可以随时细化声明。

每个 L1 / L3 entry 的完整方法论 rubric 在 `references/disciplines.zh.md` 中——本 README 表是表面地图,skill 内部承载完整 rubric。

---

## Showcase · 修改前后示例

这是教学练习，不是某位学者的已核验引语。刻意只提供有限材料：

> **原稿。** 所有学徒主要依靠书面规程学习。两次工坊访谈证明，正式规则总是优先于经验。
> **作者提供的阅读笔记。** 两次访谈中，学徒都说常规操作时查阅书面规程，遇到例外情况时请教有经验的工人。

skill 应在强化文字前指出材料与主张的距离：

> **发现 · 主张与证据不匹配。** 访谈笔记描述了两种学习方式，没有证明规则总是优先。两次工坊访谈也不能支撑“所有学徒”。该判断依据提供的笔记，尚未核对访谈原始记录。

如果作者要求修改，可提出范围有限的版本：

> **修改后。** 这里概述的两次访谈中，学徒描述了常规操作时查阅书面规程、遇到例外时请教有经验工人的做法。这些叙述提示，规则与经验的作用可能随任务而变化。[待核对：查访谈原始记录并补充真实定位。]

修改让论断范围与已有材料相称，并保留来源核验缺口。不编造引语、页码或外部学术权威；这项解释是否符合全部证据，仍由作者判断。

---

## 安装

### 作为 Claude Code skill 安装

```bash
git clone https://github.com/tizzy916/humanities-writing-companion.git \
  ~/.claude/skills/humanities-writing-companion

chmod +x ~/.claude/skills/humanities-writing-companion/scripts/*.sh
```

或者作为项目级 skill（仅当前 vault / project 可用）：

```bash
git clone https://github.com/tizzy916/humanities-writing-companion.git \
  ./.claude/skills/humanities-writing-companion
```

### Claude Code 加载

Claude Code 启动时会自动扫描 `~/.claude/skills/` 和 `./.claude/skills/`。安装后说"我在写人文论文"或下方任意触发词即可激活。

### 不用 git（ZIP 下载）

无需 git：在 [GitHub 仓库页面](https://github.com/tizzy916/humanities-writing-companion) 点击 **Code → Download ZIP**，解压后把解压出的文件夹移动到 `~/.claude/skills/humanities-writing-companion`（项目级安装则放到 `./.claude/skills/humanities-writing-companion`），然后给 shell 脚本加执行权限：

```bash
chmod +x ~/.claude/skills/humanities-writing-companion/scripts/*.sh
```

### Claude 桌面版 / claude.ai

Claude 桌面版与 claude.ai 也支持自定义 skill：把 skill 文件夹（即包含 `SKILL.md` 的目录）打包为 `.zip`，在 Claude 设置中的能力/skills 相关板块上传（具体菜单措辞可能随产品迭代变化——找 "Skills" 字样即可）。注意：`scripts/` 工具链需要可执行 shell 的环境（Claude Code / agent 模式）；纯对话环境下 skill 的各对话模式可用，但脚本不会运行。

### Claude Agent SDK 接入

`SKILL.md` 可直接加载到系统提示词中。skill 是纯文本，无运行时依赖。

### 其他 agent（开放 SKILL.md 格式）

本 skill 采用开放的 [Agent Skills](https://agentskills.io) 格式：一个包含 `SKILL.md` 以及纯文本 `references/`、`scripts/` 的文件夹。任何支持该格式的 agent——或者只要能把 `SKILL.md`（及按需路由到的 `references/*.md`）读入上下文——都可以使用：把本仓库 clone 到你的 agent 发现 skills 的目录即可。`scripts/` 工具链需要 **zsh 和 Python 3**。引用查询还需要联网访问 Crossref 和 OpenAlex；其余检查可在本地运行。

### 验证安装

安装后新开一个对话，二选一：

1. 直接问 Claude：**"你现在加载了哪些 skills？"**——列表中应出现 `humanities-writing-companion`；或
2. 直接说一个触发词，例如 **"帮我看看这段"** 或 **"review my section"**——skill 应当激活，并以四层批判的方式回应，而不是像通用润色工具那样回答。

如果两者都不生效，检查文件夹是否直接位于 `~/.claude/skills/` 之下（即 `~/.claude/skills/humanities-writing-companion/SKILL.md` 存在），然后重启 Claude Code。

### 触发词

**中文**：论文 · 写作 · 润色 · 改论文 · 帮我看看这一章 · 我手写我口 · 这个论证有没有问题 · 我写不下去了 · 审稿人会怎么攻击

**英文**："paper," "essay," "chapter," "dissertation," "argument," "thesis," "revise," "voice," "review my section," "stuck on writing," "devil's advocate"

已有学术稿件语境时，随口说“帮我看看这段话”或“take a look at this paragraph”也适用。

---

## 快速上手 · 三个典型场景

### 场景 1：新论文初次使用

对 Claude 说："我想写一篇关于 X 的论文。"

skill 从你的想法和已有材料出发，帮助形成研究问题或交付所需草稿，只询问会影响结果的缺失信息。选择持续文件协作后，再按需建立档案与目录。

### 场景 2：修改已有章节

```
"帮我看看这一章"     → 模式 B（章节级审读）→ 四级反馈报告
"帮我改这段"         → 模式 A（段落级对话）→ 诊断 + 建议 + 理由
"我写不下去了"       → 模式 E（写作瓶颈）→ 一个合适的下一步
```

### 场景 3：对抗 AI 腔调（双版本对照）

如果你的论文经过 AI 润色，但想恢复原始文风：

```
模式 F · 底稿修订 → 对照 AI 润色版与原始版本 → 保留改善 + 恢复声音
```

---

## 与同类工具的差异

| 工具 | 它的定位 | 本 skill 与之差异 |
|------|---------|------------------|
| **Jenni AI** | 实时自动续写 + 文献发现 | 我们做思想对话,不做续写。实时预测会跳过人文论证所需的认知工作 |
| **Paperpal** | 学术语言润色(偏理科/生医) | 我们是写作架构(12 个模式 + 四层批判 + 学科路由),不是单点润色工具 |
| **Yomu AI** | Sourcely 文献引擎 + 段落反馈 | 文献由作者自管(Zotero / Drive)。Mode I 帮你整理读过的,从不替你读你没读的 |
| **Thesify** | Paper Digest + Purpose-Check | Mode G 借鉴了 Purpose-Check,但放在四层批判 + reviewer calibration 的更大工作流里 |
| **HyperWrite Devil's Advocate** | 单点反方论证生成 | Mode D 是完整模式:1-5 级 calibration + 方法论专项 + 基于证据的让步机制(抗谄媚) |
| **Grammarly / DeepL Write** | 语法 / 翻译润色 | 我们绝不为了"清晰"牺牲声音。「我手写我口」是核心原则不是可选项 |
| **通用 ChatGPT / Claude(无 skill)** | 通用对话 | 我们跨对话持续维护:写作风格档案、读者档案、修改日志、四层批判、学科路由、AI 痕迹清单、引用工具链 |

---

## 项目结构

```
humanities-writing-companion/
├── SKILL.md                          ← 核心 skill 文件(英文,精简入口:原则、路由表、四层批判、模式存根)
├── SKILL.zh.md                       ← 中文镜像版
├── references/                       ← 按需加载手册(每个都有 `.zh.md` 中文镜像)
│   ├── critique-review.md            ← 详细四层问题与审阅覆盖检查
│   ├── disciplines.md                ← 完整学科维度表(L1/L2/L3/邻近 + 兜底协议)
│   ├── modes-prewriting.md           ← 模式 H / I / J 完整协议
│   ├── mode-c-drafting.md            ← 模式 C 四阶段起草流程
│   ├── mode-d-adversarial.md         ← 模式 D 魔鬼代言人完整协议
│   ├── mode-e-bottleneck.md          ← 模式 E 写作瓶颈策略
│   ├── mode-f-revision.md            ← 模式 F 底稿修订工作流
│   ├── modes-submission.md           ← 模式 G / K 完整协议
│   ├── deep-style.md                 ← 文风深层理解与保持
│   ├── multilingual-writing.md       ← 多语言写作规范
│   ├── style-profile-template.md     ← 写作风格档案("声音宪法")模板
│   ├── ai-trace-checklist.md         ← AI 痕迹排查清单
│   ├── project-management.md         ← 项目文件夹 + 版本管理规范
│   ├── revision-workflow.md          ← Mode L 修订档案制工作流手册
│   └── target-reader-profile-template.md  ← 目标读者档案模板
├── scripts/                          ← 工程工具链(零依赖)
│   ├── README.md                     ← 脚本使用说明
│   ├── ai-trace-scan.sh              ← AI 套话扫描(zsh)
│   ├── pending-checks.sh             ← 待办标记汇总(zsh)
│   ├── citation-consistency.py       ← 引用格式一致性(Python 3)
│   ├── citation-format-convert.py    ← Chicago/MLA/APA/GB7714 转换(v4.0+)
│   └── citation-verify.py            ← Crossref/OpenAlex 元数据候选检索
├── README.md                         ← 英文 README
├── README.zh.md                      ← 本文件
├── CHANGELOG.md                      ← 版本历史
├── LICENSE                           ← CC BY-NC 4.0
└── CITATION.cff                      ← 学术引用元数据
```

**双语状态**：项目已完全双语化。SKILL.md、README、CONTRIBUTING、`references/` 的全部手册以及 `scripts/README` 均为英文文件 + `.zh.md` 中文镜像成对存在；脚本注释同样双语。两种语言的触发词都能激活 skill（SKILL.md 的 description 字段同时处理两种语言）。

---

## 设计哲学

### "我手写我口"

学术严谨与个人表达不对立。"标准学术语体"往往意味着个性的消亡。skill 帮助作者用自己的声音说话，而不是把文字压入预制模具。

### 思想优先，格式其次

修改优先级：
1. 论证的力量
2. 概念的精确
3. 结构的有效
4. 表达的质量
5. 格式的规范

永远从上往下工作。不要在一个论证有根本缺陷的段落里纠结逗号。

### 工程化严谨，人文化表达

借鉴软件工程的最佳实践（版本管理、单元测试、code review），但服务于人文写作的特殊性。工程化不是把论文变成代码，而是让每次修改可追溯、论证质量可验证、写作过程可接续、问题分层处理。

---

## 引用本工作

如果你的研究使用了本 skill，请在方法论部分引用。

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

**纯文本署名**(用于 skill 元数据、页脚等):
```
Based on Humanities Writing Companion by Shen Cong
https://github.com/tizzy916/humanities-writing-companion
```

完整机读元数据见 [`CITATION.cff`](./CITATION.cff)(GitHub 的 "Cite this repository" 按钮会自动调用该文件)。

### 同时引用 Companion 工具

如果你在同一项目中同时使用了 [academic-research-skills](https://github.com/Imbad0202/academic-research-skills),请同时引用两者。ARS 的署名格式(遵循 CC BY-NC 4.0):

```
Based on Academic Research Skills by Cheng-I Wu
https://github.com/Imbad0202/academic-research-skills
```

---

## 贡献

欢迎 issue 与 PR：
- 新的工作模式提议
- AI 痕迹排查清单的扩充
- 学科特异性示例（中世纪研究、艺术保护、民族音乐学等）
- 不同引用格式（APA / Chicago / MLA / GB/T 7714 / 期刊自定义）的支持
- 双语镜像的翻译质量改进（`references/`、`scripts/`）

详见 [`CONTRIBUTING.zh.md`](./CONTRIBUTING.zh.md)。

---

## 关于作者 / About the Author

沈聪,中央美术学院实验艺术学院本科,清华大学科学史系硕士(导师 [胡翌霖](https://yilinhut.net/author/admin)),科技文创公司 [天与视界 TIANYU VISION](https://tianyu.art/) 创始人 & CEO。

本 skill 诞生于学位论文《技术自由主义》的写作过程——作者发现市面上的 AI 写作工具几乎都偏向"润色与平均化",而人文学术写作真正需要的是**反向的能力**:保护作者的学术声音、检验论证的严密性、扛住真实审稿人的对抗。所以做了这个 skill——不是替自己写,而是替自己读,在四个层级(基础严密性 / 论证展开 / 段落功能 / 句子措辞)分别提供一个真实人文学者会给出的批评。

📮 [GitHub @tizzy916](https://github.com/tizzy916) · shencong916@gmail.com · 论文、合作、纠错欢迎来信

---

## License

**[CC BY-NC 4.0](./LICENSE)**(知识共享 署名-非商业性使用 4.0 国际许可协议)——非商业用途自由使用、修改、分发,要求 attribution。

> ⚠️ **License change (v3.0.0, 2026-05-19)**:本项目从 **MIT 改为 CC BY-NC 4.0**。v2.1.0 及更早版本仍按 MIT 发布,保留原始商用权利(仅限这些特定版本)。从 v3.0.0 起,**未经单独授权禁止商业用途**。

### 商业用途 / Commercial Use

本 skill 采用 CC BY-NC 4.0 协议——**仅限非商业用途**(学术研究、教学、个人项目、开源衍生、机构内部研究流程)。

如需商业使用——嵌入付费产品、使用本 skill 提供付费咨询或编辑服务、商业 SaaS 集成、代客商业写作服务——请联系作者获取商业 license:

📮 **shencong916@gmail.com**(沈聪 · 天与视界 TIANYU VISION)

作者保留按个案授予商业 license 的权利。**在学术发表中引用本 skill 不受 license 层级影响,始终允许。**

---

## 致谢

本 skill 的方法论灵感与学术依据：

- Christou, P. A. (2026). [Reconfiguring Reflexivity in the Era of AI](https://journals.sagepub.com/doi/10.1177/10778004261445052). *Qualitative Inquiry*.
- Wiles, F. (2025). [Recursive Cognition in Practice](https://journals.sagepub.com/doi/10.1177/16094069251381709). *International Journal of Qualitative Methods*.
- Panke, S. (2025). [How Can (A)I Research This?](https://journals.sagepub.com/doi/10.1177/00224871251325065).
- Foucault, M. (1984). What is Enlightenment? — "对当下的诊断"作为方法论传统
- Stiegler, B. (2013). *What Makes Life Worth Living: On Pharmacology* — "批判药理学"

部分设计模式参考：

- [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) — 本 skill 作为互补的上游流水线；他们的 reviewer 模块中的 Concession Threshold 模式启发了模式 D 的"让步前最低标准"
- [Voice DNA + Audience Profile 模式](https://aiblewmymind.substack.com/p/claude-skills-ai-write-like-you) — 启发了写作风格档案与目标读者档案的配对设计
- [Thesify](https://www.thesify.ai/) Purpose-Check — 启发了模式 G 盲读核对
