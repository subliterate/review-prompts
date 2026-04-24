#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    'README.md',
    'kernel/README.md',
    'kernel/scripts/claude-setup.sh',
    'kernel/slash-commands/kreview.md',
    'kernel/slash-commands/kdebug.md',
    'kernel/slash-commands/kverify.md',
    'systemd/README.md',
    'systemd/scripts/claude-setup.sh',
    'systemd/slash-commands/systemd-review.md',
    'systemd/slash-commands/systemd-debug.md',
    'systemd/slash-commands/systemd-verify.md',
]

for rel in REQUIRED:
    path = ROOT / rel
    if not path.exists():
        print(f'missing required path: {rel}', file=sys.stderr)
        raise SystemExit(1)

readme = (ROOT / 'README.md').read_text(encoding='utf-8')
for needle in ['kernel/scripts/claude-setup.sh', 'systemd/scripts/claude-setup.sh', '/kreview', '/systemd-review']:
    if needle not in readme:
        print(f'README.md is missing expected reference: {needle}', file=sys.stderr)
        raise SystemExit(1)

print('validation_ok')
