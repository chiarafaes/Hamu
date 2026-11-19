---
framework: COPPA
name: US Children's Online Privacy Protection Act and FTC COPPA Rule (16 CFR Part 312), as amended in 2025
last_verified: 2026-11-19
sources:
  - https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-312
  - https://www.ftc.gov/legal-library/browse/rules/childrens-online-privacy-protection-rule-coppa
  - https://www.federalregister.gov/ (90 FR, 22 April 2025, COPPA Rule amendments)
status: dates verified with Federal Register references in law firm sources; rule text verify on eCFR before quoting sections
---

# COPPA

## When it applies

Operators of websites, apps or online services directed to children under 13, or with actual knowledge that they collect personal information from a child under 13, and that have US users. Mixed audience services (directed to children but not primarily) may age-screen and apply COPPA only to under-13 users.

## 2025 amendments

Published 22 April 2025, effective 23 June 2025, compliance by **22 April 2026** for most provisions. Main changes:
- Separate verifiable parental consent before disclosing a child's data to third parties, including for targeted advertising, unless the disclosure is integral to the service.
- A written information security programme for children's personal information.
- A written data retention policy. Keep data only as long as reasonably necessary, no indefinite retention.
- Expanded definition of personal information (includes biometric identifiers), and a definition of "mixed audience" service.
- More detail in the direct notice to parents and in the online notice.

## Checks

| Item | Check |
|---|---|
| Neutral age screen before collecting data on a mixed audience service, without nudging a false age | SP.PRIVACY.COPPA |
| Verifiable parental consent before collecting from under 13, with an FTC-accepted method | SP.PRIVACY.COPPA |
| Separate consent before third-party disclosure or targeted ads | SP.PRIVACY.COPPA, SP.CONSENT.PRE-TRACK |
| Online notice with the required content, linked from the home page and every collection point | SP.PRIVACY.US-NOTICE |
| Parents can review and delete the child's data | SP.PRIVACY.RIGHTS |
| Written security programme and retention policy | SP.PRIVACY.RETENTION, `needs_manual` |

Civil penalties are adjusted yearly for inflation (per violation, more than USD 50,000 in 2025). Do not quote an amount without checking the current FTC figure.
