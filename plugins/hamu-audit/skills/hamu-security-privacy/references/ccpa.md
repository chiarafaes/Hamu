---
framework: CCPA
name: California Consumer Privacy Act as amended by the CPRA (Cal. Civ. Code 1798.100 et seq.) and CPPA regulations (Cal. Code Regs. tit. 11, 7000 et seq.)
last_verified: 2026-11-19
sources:
  - https://cppa.ca.gov/regulations/
  - https://www.cppa.ca.gov/regulations/cpi_adjustment.html
  - https://www.cppa.ca.gov/announcements/2025/20250923.html
  - https://leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?division=3.&part=4.&lawCode=CIV&title=1.81.5
status: thresholds and 2026 regulation dates verified with the CPPA; GPC display duty cross-checked with secondary sources
---

# CCPA / CPRA

## When it applies

A for-profit business that does business in California, collects personal information of California residents, and meets one threshold (Civ. Code 1798.140(d)):
- annual gross revenue above USD 26,625,000 in the prior calendar year (CPI-adjusted for 2025 and 2026, next adjustment 1 January 2027; revenue counts worldwide), or
- buys, sells or shares personal information of 100,000 or more consumers or households per year, or
- earns 50% or more of annual revenue from selling or sharing personal information.

"Sharing" means disclosing for cross-context behavioural advertising, which covers most ad pixels.

## Duties the checks use

| Duty | Where | Check |
|---|---|---|
| Notice at collection, at or before the point of collection | 1798.100, regs 7012 | SP.PRIVACY.US-NOTICE |
| Privacy policy with categories, sources, purposes, recipients, retention, rights, updated at least every 12 months | 1798.130, regs 7011 | SP.PRIVACY.US-NOTICE |
| Rights: know, delete, correct, opt out of sale or sharing, limit use of sensitive personal information, no discrimination | 1798.100 to 1798.125 | SP.PRIVACY.RIGHTS |
| "Do Not Sell or Share My Personal Information" link and, where sensitive data is used beyond allowed purposes, "Limit the Use of My Sensitive Personal Information" link (or one combined alternative opt-out link) | 1798.135, regs 7013-7015 | SP.PRIVACY.US-OPTOUT |
| Honour opt-out preference signals such as Global Privacy Control as a valid opt-out, and since 1 January 2026 show whether the signal was processed | regs 7025 | SP.CONSENT.GPC |
| Two methods to submit requests (one can be online for online-only businesses) | 1798.130, regs 7020 | SP.PRIVACY.RIGHTS |
| Contracts with service providers and contractors | 1798.100(d), regs 7051 | SP.PRIVACY.DPA |
| Reasonable security | 1798.150 (private right of action for breaches) | SP.TLS.*, SP.ACCESS.*, SP.INFRA.ENCRYPT |

## Regulations effective 1 January 2026

Approved September 2025. Staggered dates:
- Risk assessments: required for qualifying processing from 1 January 2026. Attestation and summary to the CPPA by 1 April 2028 for 2026-2027 assessments.
- Automated decisionmaking technology (ADMT) used for significant decisions: comply from 1 January 2027 (pre-use notice, opt-out, access).
- Cybersecurity audits: first certification due 1 April 2028 (revenue above USD 100 million), 1 April 2029 (USD 50 to 100 million), 1 April 2030 (below USD 50 million).

These are process duties. The skill reports them as `needs_manual` under SP.CERT readiness only when CCPA applies.

## Other US states

About 20 US states have comprehensive privacy laws with similar opt-out rights and, in many, a duty to honour opt-out preference signals. Hamu checks California only. Mention in the report that other state laws may apply when `users_in` is `US`.
