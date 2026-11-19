---
framework: DATA-ACT
name: EU Data Act (Regulation (EU) 2023/2854)
last_verified: 2026-11-19
sources:
  - https://eur-lex.europa.eu/eli/reg/2023/2854/oj
  - https://digital-strategy.ec.europa.eu/en/policies/data-act
status: verified
---

# Data Act

## Timeline

| Date | What applies |
|---|---|
| 12 Sep 2025 | Most obligations: user access to data from connected products and related services (Art. 4, 5), data holder duties, cloud switching (Chapter VI), unfair contract terms in data sharing (Art. 13) |
| 12 Sep 2026 | Art. 3(1) access by design for connected products and related services placed on the market after this date |
| 12 Jan 2027 | Switching charges must be fully removed (reduced cost only until then) |
| 12 Sep 2027 | Unfair terms rules extend to certain long-term contracts concluded on or before 12 Sep 2025 (Art. 50, verify conditions) |

## Who it hits

- Makers of connected products and providers of related services (apps that control a device): users must get access to the data their use generates.
- Data processing services (cloud, SaaS, PaaS, IaaS): customers must be able to switch provider, with a maximum notice period and transition period, and no obstacles.

## How the skill uses it

Applies only when `connected_product = true` or the product is a data processing service. Checks are mostly `needs_manual`:
- Is there a way for users to get the data from their connected product? (SP.PRIVACY.RIGHTS extended, mapped to DATA-ACT Art. 4.)
- For SaaS: is data export documented and do the terms allow switching? Mapped to DATA-ACT Chapter VI.

These are reported under `SP.PRIVACY.RIGHTS` with `DATA-ACT` as an extra framework, not as new check ids, to keep the catalogue small.
