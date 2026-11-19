---
name: hamu-security-privacy
description: Audit a website, web app, API or mobile app for security and privacy readiness: GDPR and Belgian cookie rules, EU consumer law, AI Act transparency, NIS2, CRA, PCI DSS, OWASP ASVS, plus SOC 2, ISO 27001, ISO 42001 and HIPAA readiness. Use for a security or privacy audit, compliance check, GDPR check, cookie check, or for security and privacy pointers while building.
---

# hamu-security-privacy

> Status: scaffold (phase 0). The shared contract is in place; the checks are built in a later phase. Do not use for real audits yet.

## Always read first

- `references/_shared/contract/intake.md`
- `references/_shared/contract/run-protocol.md`
- `references/_shared/contract/severity.md`
- `references/_shared/contract/report-template.md`
- `references/_shared/contract/applicability-matrix.md`
- `references/_shared/contract/ownership-matrix.md`

## Owns

Check ids with prefix `SP.` (see ownership matrix).

## To build

- `references/checks.md`: check catalogue (id, frameworks, method, default severity, how to test per runtime)
- `references/<framework>.md`: one file per framework, with `last_verified` and sources
- Guardrails mode pointers per domain
