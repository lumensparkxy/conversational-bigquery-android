#!/usr/bin/env python3
"""Validate specification structure only; no application or cloud tests."""
from pathlib import Path
import re
import sys
from urllib.parse import unquote

root = Path(__file__).resolve().parents[1]
errors = []
required = ['README.md', 'docs/specifications/README.md']
required += [f'{d}/README.md' for d in ('android', 'backend', 'contracts', 'infra', 'tests', 'scripts')]
specs = sorted((root / 'docs/specifications').glob('[0-9][0-9]-*.md'))
if len(specs) != 12:
    errors.append(f'Expected 12 numbered specifications, found {len(specs)}')
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
