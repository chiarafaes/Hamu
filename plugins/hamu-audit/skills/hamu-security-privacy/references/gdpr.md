---
framework: GDPR
name: EU General Data Protection Regulation (Regulation (EU) 2016/679)
last_verified: 2026-11-19
sources:
  - https://eur-lex.europa.eu/eli/reg/2016/679/oj
  - https://www.dataprotectionauthority.be/
  - https://www.gegevensbeschermingsautoriteit.be/
status: verified for article numbers below; national items marked verify
---

# GDPR

Applies since 25 May 2018. Supervisory authority for Belgium: Gegevensbeschermingsautoriteit / Autorité de protection des données (GBA/APD). Belgian implementing law: Law of 30 July 2018 on the protection of natural persons with regard to the processing of personal data.

## Articles the checks use

| Art. | Topic | Used by |
|---|---|---|
| 4(11) | Definition of consent: freely given, specific, informed, unambiguous | SP.CONSENT.GRANULAR |
| 5 | Principles: lawfulness, purpose limitation, data minimisation (5(1)(c)), storage limitation (5(1)(e)), integrity and confidentiality (5(1)(f)) | SP.PRIVACY.FORMS, SP.PRIVACY.RETENTION, SP.PRIVACY.PII-URL, SP.LOG.PII |
| 6 | Legal bases | SP.CONSENT.PRE-TRACK |
| 7 | Conditions for consent: proof (7(1)), withdrawal as easy as giving (7(3)), not conditional on unneeded data (7(4)) | SP.CONSENT.* |
| 8 | Child's consent for information society services. Member states set 13 to 16. See `gdpr-k.md` | SP.PRIVACY.CHILDREN |
| 9 | Special categories of data | SP.PRIVACY.SPECIAL |
| 12 | Transparent, concise, plain language | SP.PRIVACY.LANG |
| 13, 14 | Information to give (collected from the person / not from the person) | SP.PRIVACY.CONTENT |
| 15-22 | Rights: access, rectification, erasure, restriction, portability, objection, automated decisions | SP.PRIVACY.RIGHTS |
| 25 | Data protection by design and by default | SP.PRIVACY.FORMS, SP.HDR.REFERRER |
| 28 | Processor contracts | SP.PRIVACY.DPA, SP.LLM.DATA |
| 30 | Records of processing activities | SP.PRIVACY.ROPA |
| 32 | Security of processing (encryption, confidentiality, resilience, restore, testing) | SP.TLS.*, SP.ACCESS.*, SP.INFRA.ENCRYPT, SP.RESIL.BACKUP |
| 33 | Breach notification to the authority within 72 hours | SP.PRIVACY.BREACH |
| 34 | Breach communication to the people affected when high risk | SP.PRIVACY.BREACH |
| 35 | Data protection impact assessment | SP.PRIVACY.DPIA |
| 37 | Data protection officer | SP.PRIVACY.CONTENT |
| 44-49 | Transfers. See `gdpr-transfer.md` | SP.TRANSFER.* |
| 77 | Right to lodge a complaint with a supervisory authority | SP.PRIVACY.CONTENT |
| 87 | National identification numbers | SP.PRIVACY.RRN |

## Privacy notice checklist (Art. 13, used by SP.PRIVACY.CONTENT)

1. Identity and contact details of the controller (and EU representative if established outside the EU).
2. DPO contact, if a DPO is appointed.
3. Purposes and legal basis per purpose. For legitimate interest: which interest.
4. Recipients or categories of recipients.
5. Transfers outside the EEA and the safeguard used.
6. Retention period or the criteria to set it.
7. Rights (access, rectification, erasure, restriction, objection, portability).
8. Right to withdraw consent at any time.
9. Right to complain to a supervisory authority (GBA/APD for Belgium, with link).
10. Whether providing data is a legal or contractual requirement, and what happens if not.
11. Automated decision-making and profiling, with meaningful information on the logic.

Score: missing items 1, 3 or 7 is `high`. Other gaps are `medium`. Method `heuristic`, confidence medium.

## DPIA triggers (Art. 35, used by SP.PRIVACY.DPIA)

Flag as likely needed when two or more apply: systematic monitoring, special category data at scale, profiling with significant effects, data on vulnerable people (children, patients, employees), new technology such as AI on personal data, combining datasets, large scale. The GBA/APD publishes its own list of processing types that require a DPIA (verify current version on the GBA site).

## Belgian specifics

- Digital age of consent: 13 (Law of 30 July 2018, Art. 7). See `gdpr-k.md`.
- National register number (rijksregisternummer / numéro de registre national): use is restricted by Belgian law. Treat any collection by a private website as `high` with `legal_review: true` unless a legal basis is shown. Exact statute: Law of 8 August 1983 on the National Register, Art. 8 (verify).
- Complaint authority: GBA/APD, rue de la Presse 35, 1000 Brussels. Link: https://www.dataprotectionauthority.be/citizen/actions/lodge-a-complaint (verify path).

## Fines (for the executive layer)

Up to EUR 20 million or 4% of worldwide annual turnover for the most serious breaches (Art. 83(5)), and up to EUR 10 million or 2% for others (Art. 83(4)). Mention only in the executive layer, never as a prediction.
