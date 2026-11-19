#!/usr/bin/env python3
"""Validate Hamu JSON files against the shared schemas.
Usage: python3 scripts/validate.py            -> validates shared/examples
       python3 scripts/validate.py .audit     -> validates an audit folder
Needs: pip install jsonschema
"""
import json, sys, pathlib
from jsonschema import Draft202012Validator, FormatChecker

ROOT = pathlib.Path(__file__).resolve().parent.parent
SCHEMAS = ROOT / "plugins/hamu-audit/shared/schemas"
ctx_v = Draft202012Validator(json.loads((SCHEMAS / "context.schema.json").read_text()), format_checker=FormatChecker())
fnd_v = Draft202012Validator(json.loads((SCHEMAS / "finding.schema.json").read_text()), format_checker=FormatChecker())
rol_v = Draft202012Validator(json.loads((SCHEMAS / "rollup.schema.json").read_text()), format_checker=FormatChecker())

target = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "plugins/hamu-audit/shared/examples"
files = [p for p in target.rglob("*.json") if "history" not in p.parts]
bad = 0
for p in files:
    data = json.loads(p.read_text())
    if "overall" in data:
        v = rol_v
    elif "audit_id" in data and "findings" not in data:
        v = ctx_v
    else:
        v = fnd_v
    errs = list(v.iter_errors(data))
    if errs:
        bad += 1
        for e in errs:
            print(f"FAIL {p}: {'/'.join(map(str, e.path))}: {e.message}")
    else:
        print(f"ok   {p.relative_to(target)}")
    if v is fnd_v and not errs:
        ids = [f["id"] for f in data["findings"]]
        if len(ids) != len(set(ids)):
            bad += 1; print(f"FAIL {p}: duplicate finding ids")
sys.exit(1 if bad else 0)
