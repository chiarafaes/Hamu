---
name: hamu-accessibility
description: Audit a website or app for accessibility against WCAG 2.2, EN 301 549, the European Accessibility Act, the Web Accessibility Directive and ADA/Section 508, including the accessibility statement and a manual test script. Use for an accessibility audit, WCAG or EAA check, or for accessibility pointers while building.
---

# hamu-accessibility

> Status: scaffold (phase 0). The shared contract is in place; the checks are built in a later phase. Do not use for real audits yet.

## Always read first

- `references/_shared/contract/intake.md`
- `references/_shared/contract/run-protocol.md`
- `references/_shared/contract/severity.md`
- `references/_shared/contract/report-template.md`
- `references/_shared/contract/applicability-matrix.md`
- `references/_shared/contract/ownership-matrix.md`

## Owns

Check ids with prefix `A11Y.` (see ownership matrix).

## To build

- `references/checks.md`: check catalogue (id, frameworks, method, default severity, how to test per runtime)
- `references/<framework>.md`: one file per framework, with `last_verified` and sources
- Guardrails mode pointers per domain
