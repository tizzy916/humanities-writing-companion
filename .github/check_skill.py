"""Offline packaging checks; these do not evaluate scholarly behavior."""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
errors = []
for name in ('SKILL.md', 'SKILL.zh.md'):
    path = root / name
    text = path.read_text(encoding='utf-8')
    fm = re.match(r'^---\n(.*?)\n---(?:\n|$)', text, re.S)
    if not fm:
        errors.append(f'{name}: missing frontmatter')
        continue
    # This repository uses a folded scalar; fail clearly if its schema changes.
    fields = re.fullmatch(r'name: ([a-z0-9-]+)\ndescription: >-?\n((?:  [^\n]*\n?)+)', fm.group(1))
    if not fields:
        errors.append(f'{name}: expected name and folded description')
        continue
    skill_name, lines = fields.groups()
    description = ' '.join(line.strip() for line in lines.splitlines()).strip()
    if skill_name != 'humanities-writing-companion':
        errors.append(f'{name}: unexpected skill name {skill_name!r}')
    if not 1 <= len(description) <= 1024:
        errors.append(f'{name}: description length {len(description)} outside 1..1024')
    # All entrypoint resource links must be local files within the skill.
    for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', text):
        if '://' in target or target.startswith('#'):
            continue
        resolved = (root / target.split('#', 1)[0]).resolve()
        if not resolved.is_relative_to(root) or not resolved.is_file():
            errors.append(f'{name}: missing/escaping resource {target}')
    print(f'{name}: description {len(description)} chars; resource links checked')

pairs = [(root / 'SKILL.md', root / 'SKILL.zh.md'), (root / 'README.md', root / 'README.zh.md')]
for folder in ('references', 'docs', 'scripts'):
    for en in sorted((root / folder).glob('*.md')):
        if en.name.endswith('.zh.md'):
            continue
        zh = en.with_name(en.stem + '.zh.md')
        if folder == 'references' or zh.exists():
            pairs.append((en, zh))
for en, zh in pairs:
    if not zh.is_file():
        errors.append(f'missing mirror: {zh.relative_to(root)}')
        continue
    counts = [len(re.findall(r'^#+ ', f.read_text(encoding='utf-8'), re.M)) for f in (en, zh)]
    if counts[0] != counts[1]:
        errors.append(f'heading count mismatch: {en.relative_to(root)} {counts}')
print(f'{len(pairs)} bilingual pairs checked (structure only, not semantic equivalence)')
if errors:
    raise SystemExit('\n'.join(errors))
print('Offline skill packaging checks passed.')
