#!/usr/bin/env python3
"""
citation-consistency.py — 引用格式一致性扫描 / Citation-format consistency scan

用法 / Usage:
    python3 citation-consistency.py <file.md>

退出码 / Exit codes:
    0 — 未发现格式问题 / no format issues found
    1 — 发现需审查的格式问题 / format issues found (review needed)
    2 — 输入文件不可读（不存在 / 是目录等） / input file unreadable (missing / a directory / etc.)

检查项 / Checks:
    1. 括号类型混用（半角 () vs 全角 （）） / Mixed parenthesis types (half-width () vs full-width （）)
    2. 引用内逗号混用（半角 , vs 全角 ，） / Mixed commas inside citations (half-width , vs full-width ，)
    3. 多作者连接词不统一（& / and / 与 / 和） / Inconsistent multi-author connectors (& / and / 与 / 和)
    4. 同一文献被引用时姓名形式不一致（中文译名 vs 英文原姓） / Inconsistent name forms for the same reference (Chinese translated name vs English surname)
    5. 页码格式不统一（p. X / p.X / 第 X 页） / Inconsistent page-number formats (p. X / p.X / 第 X 页)

注意 / Notes:
    - 这是一个启发式扫描器，可能有少量误报（尤其是不规则引用）
      This is a heuristic scanner and may produce a few false positives (especially for irregular citations)
    - 仅检查"格式不一致"，不检查"是否符合特定引用规范"（APA / Chicago / GB/T 7714）
      It only checks for "format inconsistency", not "conformance to a specific citation style" (APA / Chicago / GB/T 7714)
    - 全文/规范层面的检查，请配合 references/project-management.md 中的引用格式速查使用
      For full-text / style-level checks, use this alongside the citation-format quick reference in references/project-management.md
"""

import re
import sys
from collections import defaultdict


EN_INLINE = re.compile(r'\(([A-Z][\w\-\.\s&,]+?),?\s+(\d{4}[a-z]?)(?:,\s*p?p?\.?\s*[\d\-–]+)?\)')
ZH_INLINE = re.compile(r'（([^（）]+?)[，,]\s*(\d{4}[a-z]?)(?:[，,]\s*第?\s*[\d\-–]+\s*页?)?）')

MIX_HALF_PAREN_FULL_COMMA = re.compile(r'\(([^()]+?)，(\d{4})\)')
MIX_FULL_PAREN_HALF_COMMA = re.compile(r'（([^（）]+?),\s*(\d{4})）')


def scan(text):
    issues = []
    lines = text.split('\n')

    en_hits = sum(len(EN_INLINE.findall(line)) for line in lines)
    zh_hits = sum(len(ZH_INLINE.findall(line)) for line in lines)

    issues.append(f"引用统计 / Citation counts：英文形式 / English form (Author, year) {en_hits} / 中文形式 / Chinese form （作者，年份） {zh_hits}")
    issues.append("")

    if en_hits > 0 and zh_hits > 0:
        minority = min(en_hits, zh_hits)
        majority = max(en_hits, zh_hits)
        ratio = minority / majority if majority > 0 else 0
        if ratio > 0.05:
            issues.append(f"⚠ 括号类型混用 / Mixed parenthesis types：少数派占比 / minority share {ratio:.1%}（建议全文统一为一种 / recommend unifying to one form throughout）")

    for i, line in enumerate(lines, 1):
        for m in MIX_HALF_PAREN_FULL_COMMA.finditer(line):
            issues.append(f"  L{i}: 半角括号 + 全角逗号 / half-width parens + full-width comma → {m.group(0)}")
        for m in MIX_FULL_PAREN_HALF_COMMA.finditer(line):
            issues.append(f"  L{i}: 全角括号 + 半角逗号 / full-width parens + half-width comma → {m.group(0)}")

    connectors = {
        '&':   len(re.findall(r'\([^()]*&[^()]*\d{4}', text)),
        'and': len(re.findall(r'\([^()]*\sand\s[^()]*\d{4}', text)),
        '与':  len(re.findall(r'（[^（）]*与[^（）]*\d{4}', text)),
        '和':  len(re.findall(r'（[^（）]*和[^（）]*\d{4}', text)),
        '、':  len(re.findall(r'\([^()]*、[^()]*\d{4}', text))
              + len(re.findall(r'（[^（）]*、[^（）]*\d{4}', text)),
    }
    used = {k: v for k, v in connectors.items() if v > 0}
    if len(used) > 1:
        issues.append("")
        issues.append(f"⚠ 多作者连接词不统一 / Inconsistent multi-author connectors：{used}")
        issues.append("  建议根据所选引用格式（APA 用 & / GB/T 7714 用 ， 等）统一全文")
        issues.append("  Recommend unifying throughout per the chosen citation style (APA uses & / GB/T 7714 uses ， etc.)")

    year_to_names = defaultdict(set)
    for line in lines:
        for m in EN_INLINE.finditer(line):
            year_to_names[m.group(2)].add(('EN', m.group(1).strip()))
        for m in ZH_INLINE.finditer(line):
            year_to_names[m.group(2)].add(('ZH', m.group(1).strip()))

    name_lang_conflicts = []
    for year, refs in sorted(year_to_names.items()):
        langs = set(lang for lang, _ in refs)
        if len(langs) > 1:
            name_lang_conflicts.append((year, refs))

    if name_lang_conflicts:
        issues.append("")
        issues.append("⚠ 同一年份的引用被混用中英文姓名（可能是同一文献的不同写法） / Citations for the same year mix Chinese and English names (possibly different spellings of the same reference):")
        for year, refs in name_lang_conflicts[:5]:
            issues.append(f"  {year}: {sorted(refs)}")
        if len(name_lang_conflicts) > 5:
            issues.append(f"  ... 共 {len(name_lang_conflicts)} 个年份有此问题 / {len(name_lang_conflicts)} years have this issue in total")

    # Singular pages and page ranges belong to the same style: p./pp. is a
    # grammatical distinction, not evidence of inconsistent formatting.
    page_formats = {
        'p. / pp. X': len(re.findall(r'\bpp?\.\s+\d', text)),
        'p./pp.X (无空格 / no space)': len(re.findall(r'\bpp?\.\d', text)),
        '第 X / X-Y 页': len(re.findall(r'第\s*\d+(?:\s*[-–]\s*\d+)?\s*页', text)),
    }
    used_pages = {k: v for k, v in page_formats.items() if v > 0}
    if len(used_pages) > 1:
        issues.append("")
        issues.append(f"⚠ 页码格式不统一 / Inconsistent page-number formats：{used_pages}")

    return issues


def main():
    if len(sys.argv) < 2:
        print(f"用法 / Usage: {sys.argv[0]} <file.md>", file=sys.stderr)
        sys.exit(1)

    filepath = sys.argv[1]
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        print(f"文件不存在 / File does not exist: {filepath}", file=sys.stderr)
        sys.exit(2)
    except IsADirectoryError:
        print(f"输入是目录而非文件（请传入单个 .md 文件） / Input is a directory, expected a single .md file: {filepath}", file=sys.stderr)
        sys.exit(2)
    except OSError as exc:
        print(f"无法读取文件 / Cannot read file {filepath}: {exc}", file=sys.stderr)
        sys.exit(2)

    issues = scan(text)

    print(f"=== 引用格式一致性扫描 / Citation-format consistency scan · {filepath} ===\n")

    issue_count = sum(1 for line in issues if line.startswith('⚠') or '→' in line)

    if issues:
        for line in issues:
            print(line)

    print()
    if issue_count == 0:
        print("✅ 未发现明显的格式不一致 / No obvious format inconsistencies found")
    else:
        print(f"共发现约 {issue_count} 处需要审查的格式问题 / About {issue_count} format issue(s) need review")
    print()
    print("注 / Note：此扫描仅检测'不一致'，不评判'是否符合特定规范'。")
    print("    This scan only detects 'inconsistency', it does not judge 'conformance to a specific style'.")
    print("    全文规范检查请对照你论文项目内的 _writing-config/引用格式速查.md（用户项目文件，非本仓库文件，")
    print("    建法见 references/project-management.md）。")
    print("    For full-text style checks, compare against _writing-config/引用格式速查.md inside YOUR paper")
    print("    project (a user-project file, not part of this repo — see references/project-management.md).")

    # Exit-code contract: 0 = clean, 1 = issues found (for CI / agent gating)
    sys.exit(1 if issue_count > 0 else 0)


if __name__ == '__main__':
    main()
