---
framework: GDPR-K
name: GDPR rules for children, with Belgian digital age of consent
last_verified: 2026-11-19
sources:
  - https://eur-lex.europa.eu/eli/reg/2016/679/oj
  - https://www.ejustice.just.fgov.be/ (Law of 30 July 2018, Art. 7)
  - https://www.dataprotectionauthority.be/
status: verified for GDPR articles; Belgian article number cross-checked against secondary sources
---

# GDPR-K: children

## Rules

- GDPR Art. 8: when consent is the legal basis for an information society service offered directly to a child, consent below the national age needs parental authorisation. The controller makes reasonable efforts to verify it.
- Belgium sets the age at 13 (Law of 30 July 2018, Art. 7).
- Recital 38: children merit specific protection, especially for marketing and profiling.
- Art. 12(1): information for children must be in language a child can understand.
- DSA Art. 28: online platforms accessible to minors must ensure a high level of privacy, safety and security, and may not show ads based on profiling to users they know are minors. See `dsa.md`.

## How the skill applies it

| Situation | Status |
|---|---|
| `product.children_targeted = true` | applies |
| Content plausibly attractive to under 16 (games, school, youth sport, toys) | likely, ask in follow-up |
| Adult-only service with a real age gate | not_applicable |

Checks: SP.PRIVACY.CHILDREN, SP.CONSENT.*, SP.CONSUMER.DARK (dark patterns weigh heavier for minors).

Users in other member states: the age differs per country (13 to 16). Apply the strictest age among the target markets, and say which one was used.
