# Hamu shared contract

Source of truth for everything the Hamu skills share. Edit here, then run `scripts/sync-shared.sh` to copy it into every skill's `references/_shared/`.

| File | What it defines |
|---|---|
| `contract/intake.md` | Reuse rules, permission question, auto-detection, the 3 questions, guardrails mode |
| `contract/applicability-matrix.md` | Framework ids and when each one applies |
| `contract/ownership-matrix.md` | Check id format, which skill owns which check, overlap decisions |
| `contract/severity.md` | Severity, confidence, method, scoring, go/no-go |
| `contract/run-protocol.md` | `.audit/` layout, run steps, runtimes and fallbacks, safety rules |
| `contract/report-template.md` | Layered report structure and output formats |
| `schemas/context.schema.json` | `.audit/context.json` |
| `schemas/finding.schema.json` | `.audit/findings/<skill>.json` |
| `examples/` | Valid example files for both schemas |

Change the schema version when a change breaks existing files. All skills and the roll-up must accept the same major version.
