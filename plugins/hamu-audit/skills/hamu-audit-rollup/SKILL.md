---
name: hamu-audit-rollup
description: Merge findings from the Hamu audit skills into one deduplicated report with a combined score, go/no-go verdict, HTML dashboard and Word/PDF deliverable. Use after one or more Hamu audits, or to turn a single Hamu audit into a client report.
---

# hamu-audit-rollup

> Status: scaffold (phase 0). The shared contract is in place; the checks are built in a later phase. Do not use for real audits yet.

## Always read first

- `references/_shared/contract/intake.md`
- `references/_shared/contract/run-protocol.md`
- `references/_shared/contract/severity.md`
- `references/_shared/contract/report-template.md`
- `references/_shared/contract/applicability-matrix.md`
- `references/_shared/contract/ownership-matrix.md`

## To build

- Merge and deduplicate by `check_id` and `owner_skill`
- Combined scoring and verdict per `severity.md`
- Re-audit diff from `.audit/history/`
- Renderers: markdown, self-contained HTML dashboard, docx and pdf
