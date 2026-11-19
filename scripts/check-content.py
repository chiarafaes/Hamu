#!/usr/bin/env python3
"""Content rules from CLAUDE.md that a machine can check.
Usage: python3 scripts/check-content.py
- Every skill reference file (except checks.md and _shared) has front matter
  with `last_verified` (YYYY-MM-DD) and a non-empty `sources` list.
- No em-dashes in Markdown, JSON or SKILL.md content.
- hamu-accessibility checks.md covers every WCAG 2.2 level A and AA criterion.
- every rubric (R) check in hamu-performance-ux and hamu-seo-visibility has rubric examples.
- every SKILL.md status line names the plugin version from plugin.json.
No third-party dependencies.
"""
import json, pathlib, re, sys

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

WCAG22_A_AA = """1.1.1 1.2.1 1.2.2 1.2.3 1.2.4 1.2.5 1.3.1 1.3.2 1.3.3 1.3.4 1.3.5 1.4.1
1.4.2 1.4.3 1.4.4 1.4.5 1.4.10 1.4.11 1.4.12 1.4.13 2.1.1 2.1.2 2.1.4 2.2.1 2.2.2
2.3.1 2.4.1 2.4.2 2.4.3 2.4.4 2.4.5 2.4.6 2.4.7 2.4.11 2.5.1 2.5.2 2.5.3 2.5.4
2.5.7 2.5.8 3.1.1 3.1.2 3.2.1 3.2.2 3.2.3 3.2.4 3.2.6 3.3.1 3.3.2 3.3.3 3.3.4
3.3.7 3.3.8 4.1.2 4.1.3""".split()

a11y = PLUGIN / "skills/hamu-accessibility/references/checks.md"
if a11y.exists():
    covered = set()
    for line in a11y.read_text(encoding="utf-8").splitlines():
        if line.startswith("| A11Y."):
            cols = [c.strip() for c in line.split("|")]
            if len(cols) > 3:
                covered.update(re.findall(r"\d\.\d+\.\d+", cols[3]))
    missing = [sc for sc in WCAG22_A_AA if sc not in covered]
    if missing:
        fail(a11y, "WCAG 2.2 A/AA criteria without a check: " + ", ".join(missing))

RUBRIC_SKILLS = {
    "hamu-performance-ux": ("PX.", ("ux-heuristics.md", "conversion.md", "store-listing.md"), ("PX.CRO.",)),
    "hamu-seo-visibility": ("SEO.", ("content-rubric.md",), ()),
}
for skill, (prefix, rubric_files, exempt) in RUBRIC_SKILLS.items():
    ref_dir = PLUGIN / "skills" / skill / "references"
    catalogue = ref_dir / "checks.md"
    if not catalogue.exists():
        continue
    rubric_text = "".join(
        (ref_dir / n).read_text(encoding="utf-8") for n in rubric_files if (ref_dir / n).exists()
    )
    for line in catalogue.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| " + prefix):
            continue
        cols = [c.strip() for c in line.split("|")]
        check_id, how = cols[1], cols[5] if len(cols) > 5 else ""
        if "R" in how.split() and not check_id.startswith(exempt or ("\0",)) and f"| {check_id} |" not in rubric_text:
            fail(catalogue, f"{check_id} is a rubric check without rubric examples")

plugin_version = json.loads((PLUGIN / ".claude-plugin/plugin.json").read_text())["version"]
for skill_md in sorted(PLUGIN.glob("skills/*/SKILL.md")):
    m = re.search(r"^> Status: ([0-9]+\.[0-9]+\.[0-9]+)", skill_md.read_text(encoding="utf-8"), re.M)
    if not m or m.group(1) != plugin_version:
        fail(skill_md, f"status line must start with the plugin version {plugin_version}")

if bad:
    sys.exit(1)
print("content rules ok")
