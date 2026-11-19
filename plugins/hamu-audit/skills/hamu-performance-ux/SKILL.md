---
name: hamu-performance-ux
description: Audit a website or app for performance, UX and conversion: Core Web Vitals, loading, responsive layout, navigation, visual hierarchy, forms, CTAs, trust signals and funnels. Use for a speed, UX, CRO or Core Web Vitals audit, or for performance and UX pointers while building.
---

# hamu-performance-ux

> Status: scaffold (phase 0). The shared contract is in place; the checks are built in a later phase. Do not use for real audits yet.

## Always read first

- `references/_shared/contract/intake.md`
- `references/_shared/contract/run-protocol.md`
- `references/_shared/contract/severity.md`
- `references/_shared/contract/report-template.md`
- `references/_shared/contract/applicability-matrix.md`
- `references/_shared/contract/ownership-matrix.md`

## Owns

Check ids with prefix `PX.` (see ownership matrix).

## To build

- `references/checks.md`: check catalogue (id, frameworks, method, default severity, how to test per runtime)
- `references/<framework>.md`: one file per framework, with `last_verified` and sources
- Guardrails mode pointers per domain
