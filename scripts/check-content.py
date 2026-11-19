#!/usr/bin/env python3
"""Content rules from CLAUDE.md that a machine can check.
Usage: python3 scripts/check-content.py
- Every skill reference file (except checks.md and _shared) has front matter
  with `last_verified` (YYYY-MM-DD) and a non-empty `sources` list.
- No em-dashes in Markdown, JSON or SKILL.md content.
No third-party dependencies.
"""
import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PLUGIN = ROOT / "plugins/hamu-audit"
DATE = re.compile(r"^last_verified:\s*\d{4}-\d{2}-\d{2}\s*$", re.M)
SOURCES = re.compile(r"^sources:\s*\n(\s+-\s+\S.*\n)+", re.M)
EM_DASH = "—"

bad = 0

def fail(path, msg):
    global bad
    bad += 1
    print(f"FAIL {path.relative_to(ROOT)}: {msg}")

for ref in sorted(PLUGIN.glob("skills/*/references/*.md")):
    if ref.name == "checks.md":
        continue
    text = ref.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        fail(ref, "missing front matter")
        continue
    fm = m.group(1) + "\n"
    if not DATE.search(fm):
        fail(ref, "front matter needs last_verified: YYYY-MM-DD")
    if not SOURCES.search(fm):
        fail(ref, "front matter needs a non-empty sources list")

for path in sorted(ROOT.rglob("*")):
    if ".git" in path.parts or not path.is_file():
        continue
    if path.suffix not in {".md", ".json"}:
        continue
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if EM_DASH in line:
            fail(path, f"line {n}: em-dash, use plain punctuation")

if bad:
    sys.exit(1)
print("content rules ok")
