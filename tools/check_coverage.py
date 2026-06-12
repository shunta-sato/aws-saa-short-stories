#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""用語カバレッジ検証: stories/ の front matter と用語集YAMLを突合し docs/coverage.md を生成する。

使い方:
  python3 tools/check_coverage.py [path/to/SAA-C03_categorized.yaml]

YAMLを渡さない場合は front matter の整合チェック(重複・形式)のみ行う。
"""
import sys, re, glob, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def parse_front_matter(path):
    txt = open(path, encoding='utf-8').read()
    m = re.match(r'---\n(.*?)\n---\n', txt, re.S)
    if not m:
        return None
    fm = {}
    terms = []
    in_terms = False
    for line in m.group(1).splitlines():
        if line.startswith('terms:'):
            in_terms = True
            continue
        if in_terms and line.strip().startswith('- '):
            terms.append(line.strip()[2:].strip())
            continue
        in_terms = False
        if ':' in line:
            k, v = line.split(':', 1)
            fm[k.strip()] = v.strip()
    fm['terms'] = terms
    return fm


def main():
    yaml_path = sys.argv[1] if len(sys.argv) > 1 else None
    stories = sorted(glob.glob(os.path.join(ROOT, 'stories', '*', '*.md')))
    errors, rows = [], []
    assigned = {}  # term_id -> story relpath

    for s in stories:
        rel = os.path.relpath(s, ROOT)
        fm = parse_front_matter(s)
        if not fm:
            errors.append(f'{rel}: front matter がありません')
            continue
        for key in ('universe', 'family', 'episode'):
            if key not in fm:
                errors.append(f'{rel}: front matter に {key} がありません')
        folder_family = os.path.basename(os.path.dirname(s))
        fam = fm.get('family', '')
        if folder_family not in (fam, fam.replace('_architecture', '')):
            errors.append(f'{rel}: フォルダ({folder_family})とfamily({fam})が不一致')
        for t in fm['terms']:
            if t in assigned:
                errors.append(f'重複担当: {t} ({assigned[t]} と {rel})')
            assigned[t] = rel
        rows.append((rel, fm))

    glossary = {}
    if yaml_path:
        import yaml
        y = yaml.safe_load(open(yaml_path, encoding='utf-8'))
        glossary = {t['term_id']: t['taxonomy_family'] for t in y['term_glossary']}
        for t, rel in assigned.items():
            if t not in glossary:
                errors.append(f'{rel}: 用語集に存在しないterm_id: {t}')

    # generate docs/coverage.md
    out = ['# 用語カバレッジ', '', f'担当済み: {len(assigned)}語'
           + (f' / 全{len(glossary)}語' if glossary else ''), '']
    out += ['| 編 | universe | 担当語数 |', '|---|---|---|']
    for rel, fm in rows:
        out.append(f"| {rel} | {fm.get('universe','?')} | {len(fm['terms'])} |")
    if glossary:
        out += ['', '## family別の残り', '']
        fams = {}
        for t, f in glossary.items():
            fams.setdefault(f, []).append(t)
        for f in sorted(fams):
            missing = sorted(set(fams[f]) - set(assigned))
            status = '✅ 完了' if not missing else f'残り{len(missing)}語'
            out.append(f'### {f} ({len(fams[f])}語) — {status}')
            if missing:
                out.append('')
                out.append(', '.join(f'`{t}`' for t in missing))
            out.append('')
    open(os.path.join(ROOT, 'docs', 'coverage.md'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')

    print(f'stories: {len(rows)}, assigned terms: {len(assigned)}')
    if errors:
        print('ERRORS:')
        for e in errors:
            print(' -', e)
        sys.exit(1)
    print('OK: docs/coverage.md を更新しました')


if __name__ == '__main__':
    main()
