#!/usr/bin/env bash
# Fails if the repo contains personal data. Edit BLOCKLIST for your own terms, then run before every commit.
# Usage: scripts/scan-personal-data.sh [folder]   (defaults to the repo root)
set -u
ROOT="${1:-$(cd "$(dirname "$0")/.." && pwd)}"
BLOCKLIST_FILE="$ROOT/scripts/blocklist.txt"
PATTERNS=(
  '/Users/[A-Za-z0-9._-]+'
  'GoogleDrive-[A-Za-z0-9@._-]+'
  '[A-Za-z0-9._%+-]+@(gmail|outlook|yahoo|icloud|hotmail)\.[a-z]+'
  'trig_[A-Za-z0-9]{8,}'
  'sk-[A-Za-z0-9]{20,}'
  'ghp_[A-Za-z0-9]{20,}'
)
fail=0
for p in "${PATTERNS[@]}"; do
  hits=$(grep -rIn -E -- "$p" "$ROOT" --exclude-dir=.git --exclude=scan-personal-data.sh --exclude=blocklist.txt 2>/dev/null | grep -v -E 'example\.com|your-email|\[Your' )
  if [ -n "$hits" ]; then echo "PATTERN $p"; echo "$hits"; fail=1; fi
done
if [ -f "$BLOCKLIST_FILE" ]; then
  while IFS= read -r term; do
    [ -z "$term" ] && continue
    case "$term" in \#*) continue;; esac
    hits=$(grep -rIn -i -F -- "$term" "$ROOT" --exclude-dir=.git --exclude=scan-personal-data.sh --exclude=blocklist.txt 2>/dev/null)
    if [ -n "$hits" ]; then echo "BLOCKED TERM: $term"; echo "$hits"; fail=1; fi
  done < "$BLOCKLIST_FILE"
fi
if [ $fail -eq 0 ]; then echo "scan clean"; else echo "scan FAILED: personal data found"; exit 1; fi
