---
framework: HIPAA
name: US HIPAA Security, Privacy and Breach Notification Rules (45 CFR Parts 160 and 164)
last_verified: 2026-11-19
sources:
  - https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164
  - https://www.hhs.gov/hipaa/for-professionals/security/index.html
  - https://www.reginfo.gov/ (HIPAA Security Rule rulemaking, RIN 0945-AA22)
  - https://www.fiercehealthcare.com/health-tech/feds-push-back-hipaa-security-rule-overhaul-july-2027
status: current rule verified; status of the proposed Security Rule update cross-checked with secondary sources
---

# HIPAA readiness

Applies only when the organisation is a covered entity (health plan, clearinghouse, provider that bills electronically) or a business associate handling protected health information (PHI) for one, and has US patients or members. A European health app is usually not under HIPAA unless it serves US covered entities. Readiness only.

## Rule status

- The current Security Rule (2003, amended 2013) remains in force.
- A proposed update (NPRM published 6 January 2025) would remove the "addressable" category and require, among others, MFA, encryption at rest and in transit, asset inventories and annual audits. Per Reginfo.gov the final action moved to long-term actions with a projected date of July 2027 (secondary sources, verify before quoting).
- The skill checks against the current rule and notes the proposed items as `best_practice`.

## Security Rule safeguards and Hamu evidence

| Section | Topic (own words) | Evidence from Hamu checks |
|---|---|---|
| 164.308(a)(1) | Security management: risk analysis, risk management, sanctions, activity review | manual |
| 164.308(a)(3), (a)(4) | Workforce security and information access management | SP.ACCESS.* |
| 164.308(a)(5) | Security awareness and training, including password management and log-in monitoring | SP.AUTH.BRUTE, manual |
| 164.308(a)(6) | Security incident procedures | SP.RESIL.INCIDENT |
| 164.308(a)(7) | Contingency plan: backup, disaster recovery, emergency mode | SP.RESIL.BACKUP |
| 164.308(b), 164.314 | Business associate agreements | SP.PRIVACY.DPA |
| 164.310 | Physical safeguards: facility, workstation, device and media | manual |
| 164.312(a) | Access control: unique user id, emergency access, automatic logoff, encryption (addressable) | SP.AUTH.SESSION, SP.INFRA.ENCRYPT |
| 164.312(b) | Audit controls | SP.LOG.SECURITY |
| 164.312(c) | Integrity | SP.INPUT.*, SP.DEPS.SRI |
| 164.312(d) | Person or entity authentication | SP.AUTH.*, SP.AUTH.MFA |
| 164.312(e) | Transmission security | SP.TLS.* |
| 164.316 | Policies, procedures, documentation kept 6 years | manual |

## Breach notification

45 CFR 164.400 to 414: notify affected individuals without unreasonable delay and no later than 60 days after discovery. Breaches of 500 or more people also go to HHS and, for a state or jurisdiction, to prominent media. Checked as process only (SP.RESIL.INCIDENT).

## Web-specific risk

HHS guidance on online tracking technologies (2022, updated 2024) was partly vacated by a US court in June 2024 (verify current state). Still treat tracking pixels on pages with PHI (patient portals, appointment booking) as `high` under SP.CONSENT.PRE-TRACK with HIPAA as `evidence_for` and `legal_review: true`.
