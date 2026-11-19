---
framework: CRA
name: Cyber Resilience Act (Regulation (EU) 2024/2847)
last_verified: 2026-11-19
sources:
  - https://eur-lex.europa.eu/eli/reg/2024/2847/oj
  - https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act
  - https://www.dlapiper.com/en/insights/publications/2026/02/cyber-resilience-act-the-fine-line-between-saas-and-digital-products
  - https://www.orrick.com/en/Insights/2026/09/EU-Cyber-Resilience-Act-New-Guidance-Clarifies-Scope-Reporting
status: dates and articles verified; Commission scope guidance cross-checked with secondary sources
---

# CRA

## Timeline

| Date | What applies |
|---|---|
| 10 Dec 2024 | Entry into force |
| 11 Jun 2026 | Rules on conformity assessment bodies (Chapter IV) |
| 11 Sep 2026 | Art. 14 reporting of actively exploited vulnerabilities and severe incidents, via the ENISA single reporting platform. Applies also to products already on the market (Art. 69(3)). |
| 11 Dec 2027 | All other obligations, including Annex I essential requirements and CE marking |

## Scope

In scope: products with digital elements placed on the EU market, hardware and software, including downloadable apps, desktop software, firmware and libraries placed on the market commercially.

Remote data processing solutions (Art. 3(2)) are in scope only when designed by or for the manufacturer and needed for the product to perform a function.

Out of scope or excluded: standalone SaaS that is not the remote processing of a product (per the Commission guidance, reported as published in 2026, verify), products covered by sector rules (medical devices, cars, aviation), non-commercial open source.

Applicability rule for the skill:
- `connected_product = true`, or the organisation ships an installable app, desktop software, SDK or firmware in the EU: `applies`.
- Mobile app that is only a thin client for SaaS: `likely`, note "check whether the app is placed on the market as a product".
- Website or SaaS only: `not_applicable`.

## Essential requirements the checks map to (Annex I)

| Annex I | Topic | Check |
|---|---|---|
| Part I | Secure by default configuration, no known exploitable vulnerabilities at release, access control, confidentiality and integrity, data minimisation, attack surface limitation, logging, secure updates | SP.DEPS.VULN, SP.ACCESS.*, SP.TLS.*, SP.LOG.SECURITY |
| Part II | Vulnerability handling: SBOM, coordinated vulnerability disclosure policy, contact address for reports, security updates without delay and free of charge | SP.DEPS.SBOM, SP.DISCLOSE.CVD, SP.DISCLOSE.SECURITYTXT |

Reporting duty (Art. 14): early warning within 24 hours, notification within 72 hours, final report later. The skill only checks that a process exists (SP.RESIL.INCIDENT, `needs_manual`).
