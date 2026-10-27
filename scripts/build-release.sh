#!/usr/bin/env bash
# Builds dist/JobSearchOS.zip (whole repo) and dist/JobSearchOS.plugin (installable plugin only).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
cp plugin/skills/sweep/SKILL.md plugin/automations/sweep-procedure.md
python3 scripts/build-examples.py >/dev/null
bash scripts/scan-personal-data.sh
rm -rf dist && mkdir -p dist
zip -qr dist/JobSearchOS.zip . -x '.git/*' 'dist/*' '*.DS_Store'
( cd plugin && zip -qr ../dist/JobSearchOS.plugin . -x '*.DS_Store' )
ls -l dist
