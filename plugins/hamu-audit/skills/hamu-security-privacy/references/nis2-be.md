---
framework: NIS2-BE
name: NIS2 Directive (EU) 2022/2555 as transposed in Belgium (Law of 26 April 2024), with CCB CyberFundamentals
last_verified: 2026-11-19
sources:
  - https://eur-lex.europa.eu/eli/dir/2022/2555/oj
  - https://eur-lex.europa.eu/eli/reco/2003/361/oj
  - https://ccb.belgium.be/
  - https://atwork.safeonweb.be/
  - https://ccb.belgium.be/news/nis2-18-april-2026-deadline-what-essential-entities-must-have-place
  - https://eubelius.com/en/news/entry-into-force-of-belgian-acts-transposing-nis2-what-you-need-to-know
status: dates verified with CCB and law firm sources; conformity assessment milestones marked verify
---

# NIS2-BE

## Belgian framework

- Law of 26 April 2024 establishing a framework for the cybersecurity of networks and information systems of general interest for public security, and Royal Decree of 9 June 2024. In force since **18 October 2024**.
- Authority: Centre for Cybersecurity Belgium (CCB). Registration and incident notification via the Safeonweb@Work platform.
- Registration deadline for entities in scope: 18 March 2025 (18 December 2024 for some digital sector entities). Passed. A missing registration is a finding only when the organisation clearly falls in scope.

## Scope test

1. Sector in Annex I (high criticality: energy, transport, banking, financial market infrastructure, health, drinking water, waste water, digital infrastructure, ICT service management B2B, public administration, space) or Annex II (other critical: postal, waste, chemicals, food, manufacturing of certain products, digital providers such as marketplaces, search engines and social networks, research).
2. Size per Recommendation 2003/361/EC. Medium: 50 to 249 staff, or turnover over EUR 10 million and balance sheet over EUR 10 million. Large: 250 staff or more, or turnover over EUR 50 million and balance sheet over EUR 43 million.
3. Size-independent cases: DNS service providers, TLD registries, qualified trust service providers, public electronic communications providers, sole providers of an essential service, and entities designated by the authority.
4. Essential vs important: Annex I and large is usually essential. Annex I medium, and Annex II, is usually important.

When sector fits but size is unknown: `likely`, ask the follow-up from `intake.md`.

Suppliers to NIS2 entities are not in scope by law, but often get security clauses in contracts (Art. 21(2)(d) supply chain security). Status `likely` with relation `best_practice` when `role` is supplier_to_regulated_entity.

## Measures (Directive Art. 21(2)) and checks

| Art. 21(2) | Measure | Check |
|---|---|---|
| (a) | Risk analysis and security policies | SP.CERT.CYFUN (manual) |
| (b) | Incident handling | SP.RESIL.INCIDENT, SP.LOG.* |
| (c) | Business continuity, backups, crisis management | SP.RESIL.BACKUP |
| (d) | Supply chain security | SP.RESIL.SUPPLIER, SP.DEPS.* |
| (e) | Security in acquisition, development and maintenance, including vulnerability handling | SP.DEPS.VULN, SP.DISCLOSE.CVD |
| (f) | Assessing effectiveness of measures | manual |
| (g) | Cyber hygiene and training | manual |
| (h) | Cryptography and encryption | SP.TLS.*, SP.INFRA.ENCRYPT |
| (i) | HR security, access control, asset management | SP.ACCESS.* |
| (j) | MFA, secured communications | SP.AUTH.MFA |

Management bodies must approve the measures and follow training (Art. 20).

## Incident reporting (Art. 23)

Early warning within 24 hours, incident notification within 72 hours, final report within one month, to the CCB. Checked as process only (SP.RESIL.INCIDENT, `needs_manual`).

## CyberFundamentals (CyFun) and conformity assessment

- CyFun levels: Basic, Important, Essential. Belgian NIS2 presumption of conformity is reached with CyFun or ISO/IEC 27001 certification with the right scope.
- Essential entities must undergo regular conformity assessment. Important entities may do so voluntarily.
- Milestones as reported: the CCB set **18 April 2026** as a deadline for essential entities to submit evidence. A secondary source reports a further milestone of 18 April 2027 for reaching the CyFun Essential level, with a remediation route to 18 April 2028. Verify on the CCB site before quoting.

The skill never claims CyFun conformity. SP.CERT.CYFUN gives a readiness view only.

Domain checks (SPF, DMARC, DNSSEC) map to CyFun as `best_practice`.
