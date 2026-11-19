#!/usr/bin/env bash
# Copies the shared contract into every skill so each skill works on its own,
# even when someone installs or copies a single skill folder.
# Source of truth: plugins/hamu-audit/shared. Never edit references/_shared by hand.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SHARED="$ROOT/plugins/hamu-audit/shared"
SKILLS="$ROOT/plugins/hamu-audit/skills"

for skill in "$SKILLS"/*/; do
  dest="$skill/references/_shared"
  rm -rf "$dest"
  mkdir -p "$dest"
  cp -R "$SHARED"/. "$dest"/
  echo "synced -> ${dest#$ROOT/}"
done

# Fail CI if a skill's copy drifted from the source.
if [[ "${1:-}" == "--check" ]]; then
  for skill in "$SKILLS"/*/; do
    diff -r "$SHARED" "$skill/references/_shared" >/dev/null || { echo "DRIFT in $skill"; exit 1; }
  done
  echo "all skills in sync"
fi
