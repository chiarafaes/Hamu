---
framework: PIPEDA
name: Canada Personal Information Protection and Electronic Documents Act (federal private sector)
last_verified: 2026-11-19
sources:
  - https://laws-lois.justice.gc.ca/eng/acts/P-8.6/
  - https://www.priv.gc.ca/en/privacy-topics/privacy-laws-in-canada/the-personal-information-protection-and-electronic-documents-act-pipeda/
  - https://www.dlapiper.com/en/insights/publications/2026/06/canada-tables-bill-c36-the-protecting-privacy-and-consumer-data-act
status: current law verified; reform bill status cross-checked with secondary sources
---

# PIPEDA

## When it applies

Private-sector organisations that collect, use or disclose personal information in the course of commercial activity in Canada, and cross-border flows to and from Canada. Quebec (Law 25), Alberta and British Columbia have their own substantially similar private-sector laws. Note Quebec in the report when users are there.

## Reform

Bill C-27 died in January 2025. Bill C-36 (Protecting Privacy and Consumer Data Act) was tabled on 15 June 2026 and would replace Part 1 of PIPEDA. Not law yet. Do not check against it (verify progress before each run).

## Fair information principles (Schedule 1) and checks

| Principle | Check |
|---|---|
| 1 Accountability: a named person responsible for compliance | SP.PRIVACY.LOCAL-OFFICER |
| 2 Identifying purposes | SP.PRIVACY.CONTENT |
| 3 Consent, meaningful and, for sensitive data, express | SP.CONSENT.*, SP.PRIVACY.FORMS |
| 4 Limiting collection | SP.PRIVACY.FORMS |
| 5 Limiting use, disclosure and retention | SP.PRIVACY.RETENTION |
| 6 Accuracy | manual |
| 7 Safeguards | SP.TLS.*, SP.ACCESS.*, SP.INFRA.ENCRYPT |
| 8 Openness: policies available | SP.PRIVACY.POLICY |
| 9 Individual access | SP.PRIVACY.RIGHTS |
| 10 Challenging compliance: complaint route | SP.PRIVACY.CONTENT |

Breaches with a real risk of significant harm are reported to the Privacy Commissioner and to affected people, and all breaches are recorded and kept for 24 months (Breach of Security Safeguards Regulations). Checked as process only (SP.PRIVACY.BREACH).

Anti-spam: CASL requires consent for commercial electronic messages. SP.PRIVACY.FORMS checks the opt-in for Canadian users.
