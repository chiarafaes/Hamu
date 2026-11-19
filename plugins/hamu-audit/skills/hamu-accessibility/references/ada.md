---
framework: ADA
name: Americans with Disabilities Act, Title II (state and local government) and Title III (public accommodations)
last_verified: 2026-11-19
sources:
  - https://www.ada.gov/resources/2024-03-08-web-rule/
  - https://www.ada.gov/title-ii-web-rule/
  - https://www.federalregister.gov/documents/2026/04/20/2026-07663/extension-of-compliance-dates-for-nondiscrimination-on-the-basis-of-disability-accessibility-of-web
  - https://www.ecfr.gov/current/title-28/chapter-I/part-35/subpart-H
status: Title II rule and the April 2026 extension verified on the Federal Register; Title III has no web regulation
---

# ADA

## Title II (state and local governments)

- Final rule published April 2024, technical standard WCAG 2.1 level AA (28 CFR 35.200).
- Compliance dates, as extended by the interim final rule of 20 April 2026:
  - public entities serving a population of 50,000 or more: **26 April 2027**,
  - smaller public entities and special district governments: **26 April 2028**.
- Exceptions in the rule include archived content, preexisting conventional electronic documents, some third-party content, password-protected individualised documents, and preexisting social media posts.
- Further changes are under discussion (a separate rulemaking for K-12 and challenges to the rule's scope). Verify before each run.

Applies only to US public entities. Rare for Hamu clients. Status `applies` only with `public_sector = true` and `established_in` US.

## Title III (businesses open to the public)

- No web regulation. DOJ guidance (March 2022) says websites of public accommodations must be accessible, without naming a standard.
- Courts and settlements usually point to WCAG 2.0 or 2.1 AA. Lawsuits are frequent for US-facing e-commerce.
- Hamu maps WCAG failures to ADA Title III as `best_practice`, never as a legal conclusion, with `legal_review: true` on the executive summary line.

## Mapping

Only criteria that exist in WCAG 2.0 or 2.1 map to ADA. Criteria new in 2.2 stay WCAG22-only.
