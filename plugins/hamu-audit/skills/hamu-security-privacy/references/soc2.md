---
framework: SOC2
name: AICPA Trust Services Criteria (2017, with revised points of focus 2022), ids only
last_verified: 2026-11-19
sources:
  - https://www.aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services
  - https://www.aicpa-cima.com/resources/download/2017-trust-services-criteria-with-revised-points-of-focus-2022
status: structure and criteria ids verified; descriptions are own words
licence_note: AICPA text is copyrighted. Hamu uses criteria ids and own-words labels only.
---

# SOC 2 readiness

Readiness only. A SOC 2 report is an attestation by a licensed CPA firm. Type I covers design at a point in time. Type II covers operating effectiveness over a period (usually 3 to 12 months). The skill never says "SOC 2 compliant".

## Categories

| Category | Criteria | In scope |
|---|---|---|
| Security (Common Criteria) | CC1 to CC9 | always |
| Availability | A1 | if chosen |
| Confidentiality | C1 | if chosen |
| Processing Integrity | PI1 | if chosen |
| Privacy | P1 to P8 | if chosen |

## Common Criteria and Hamu evidence

| Id | Own-words label | Evidence from Hamu checks |
|---|---|---|
| CC1 | Control environment, governance, integrity | manual |
| CC2 | Communication and information, internal and external | SP.PRIVACY.POLICY, SP.DISCLOSE.* |
| CC3 | Risk assessment, including fraud and change | manual |
| CC4 | Monitoring of controls | SP.LOG.ALERT, manual |
| CC5 | Control activities and policies | manual |
| CC6 | Logical and physical access: identity, authentication, authorisation, encryption in transit and at rest, protection against malicious software | SP.ACCESS.*, SP.AUTH.*, SP.TLS.*, SP.INFRA.ENCRYPT, SP.SECRETS.* |
| CC7 | System operations: vulnerability detection, monitoring, incident response and recovery | SP.DEPS.VULN, SP.LOG.*, SP.RESIL.INCIDENT |
| CC8 | Change management | SP.DEPS.PIN, manual |
| CC9 | Risk mitigation, including vendors and business disruption | SP.RESIL.SUPPLIER, SP.PRIVACY.DPA |
| A1 | Capacity, backup, recovery testing | SP.RESIL.BACKUP |
| C1 | Identify, protect and dispose of confidential information | SP.PRIVACY.RETENTION, SP.LOG.PII |
| P1 to P8 | Notice, choice and consent, collection, use and retention, access, disclosure, quality, monitoring | SP.PRIVACY.*, SP.CONSENT.* |

## Manual checklist (needs_manual, SP.CERT.SOC2)

1. System description: boundaries, services, infrastructure, people, data.
2. Chosen categories beyond Security, and why.
3. Policies (information security, acceptable use, access, change, incident, vendor) with owner and review date.
4. Risk assessment done in the last 12 months.
5. Access reviews on a schedule, with evidence.
6. Onboarding and offboarding records, background checks where lawful.
7. Security awareness training records.
8. Vendor list with risk ratings and SOC reports or questionnaires of key vendors.
9. Change management tickets with approvals.
10. For Type II: evidence that each control ran during the whole period.
