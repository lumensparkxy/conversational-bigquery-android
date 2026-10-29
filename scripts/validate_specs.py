#!/usr/bin/env python3
"""Validate specification structure only; no application or cloud tests."""
from pathlib import Path
import json
import re
import sys
from urllib.parse import unquote

root = Path(__file__).resolve().parents[1]
errors = []
required = ['README.md', 'docs/specifications/README.md']
required += [f'{d}/README.md' for d in ('android', 'backend', 'contracts', 'infra', 'tests', 'scripts')]
specs = sorted((root / 'docs/specifications').glob('[0-9][0-9]-*.md'))
index = (root / 'docs/specifications/README.md').read_text()
if not specs or [int(p.name[:2]) for p in specs] != list(range(1, len(specs) + 1)):
    errors.append('Numbered specifications must be nonempty and sequential from 01')
for spec in specs:
    if f'({spec.name})' not in index:
        errors.append(f'Chapter missing from specification index: {spec.name}')
for relative in required:
    path = root / relative
    if not path.is_file() or len(path.read_text().strip()) < 60:
        errors.append(f'Missing/empty document: {relative}')
checked = 0
for path in root.rglob('*'):
    relative = path.relative_to(root)
    if any(part in ('.git', 'work', '__pycache__') for part in relative.parts):
        continue
    if not path.is_file():
        continue
    if path.name in ('.env', 'google-services.json', 'application_default_credentials.json', 'local.properties') or path.suffix in ('.pem', '.key', '.jks', '.keystore'):
        errors.append(f'Forbidden private artifact name: {relative}')
    if path.suffix != '.md':
        continue
    checked += 1
    for example in re.findall(r'```json\s*\n(.*?)\n```', path.read_text(), re.S):
        try:
            json.loads(example)
        except json.JSONDecodeError as exc:
            errors.append(f'Invalid fenced JSON in {relative}: {exc}')
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', path.read_text()):
        if '://' in target or target.startswith(('#', 'mailto:')):
            continue
        target = unquote(target.split('#')[0])
        if not (path.parent / target).exists():
            errors.append(f'Broken file link in {relative}: {target}')
if errors:
    print('\n'.join(errors), file=sys.stderr)
    sys.exit(1)
print(f'PASS: {len(specs)} numbered specs; {checked} Markdown files; required structure and local file links. Application tests NOT run.')
