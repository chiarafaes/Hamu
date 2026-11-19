---
framework: EU-CONSUMER
name: EU consumer law for online sales (CRD, Omnibus, UCPD, Price Indication, Geo-blocking, ODR repeal)
last_verified: 2026-11-19
sources:
  - https://eur-lex.europa.eu/eli/dir/2011/83/oj
  - https://eur-lex.europa.eu/eli/dir/2019/2161/oj
  - https://eur-lex.europa.eu/eli/dir/2005/29/oj
  - https://eur-lex.europa.eu/eli/dir/1998/6/oj
  - https://eur-lex.europa.eu/eli/dir/2023/2673/oj
  - https://eur-lex.europa.eu/eli/reg/2018/302/oj
  - https://eur-lex.europa.eu/eli/reg/2024/3228/oj
status: verified for EU instruments and dates; national transposition details marked verify
---

# EU-CONSUMER

Applies to B2C online sales to consumers in the EU. Belgian transposition sits in the Code of Economic Law, Book VI (see `be-cel.md`). Owner of the legal check is SP. PX notes conversion impact (ownership matrix).

## Instruments

| Instrument | What the checks use | Check |
|---|---|---|
| Consumer Rights Directive 2011/83/EU (CRD) | Art. 6 pre-contract information for distance contracts. Art. 6a extra information on online marketplaces (added by Omnibus). Art. 8(2) order button must say the order implies payment. Art. 9 to 16 withdrawal right of 14 days, model form (Annex I(B)), exceptions (Art. 16). Art. 22 no pre-ticked boxes for extra payments. | SP.CONSUMER.PRE-INFO, .BUTTON, .WITHDRAWAL, .MARKETPLACE, .DARK |
| Directive (EU) 2023/2673, new CRD Art. 11a | Online withdrawal function for distance contracts concluded through an online interface. Clearly labelled, available during the whole withdrawal period, followed by a confirmation step, with an acknowledgement on a durable medium. Applies from **19 June 2026**. | SP.CONSUMER.WITHDRAW-FN |
| Omnibus Directive (EU) 2019/2161 | Amends CRD, UCPD, Price Indication Directive. Applies since 28 May 2022. | several |
| Price Indication Directive 98/6/EC, Art. 6a | A price reduction must show the lowest price applied in the prior 30 days or more. | SP.CONSUMER.PRICE |
| Unfair Commercial Practices Directive 2005/29/EC (UCPD) | Art. 7(6) information on whether and how reviews are verified. Annex I points 23b and 23c: claiming reviews are from real buyers without checks, and fake reviews, are always unfair. Annex I point 11a: paid ranking must be disclosed. Misleading and aggressive practices in general, which cover most dark patterns. | SP.CONSUMER.REVIEWS, .ADS, .DARK |
| Geo-blocking Regulation (EU) 2018/302 | No blocking or automatic redirect based on nationality or residence, no discrimination in payment conditions. | SP.CONSUMER.GEOBLOCK |
| Regulation (EU) 2024/3228 | Repeals the ODR Regulation 524/2013 with effect from 20 July 2025 and discontinues the ODR platform. The duty to link to it ended. An old link is now a dead link and confusing for consumers. | SP.LEGAL.ODR |

## Withdrawal function: what to look for

1. A function labelled "withdraw from contract here" or an equally clear wording in the site language.
2. Reachable during the whole 14-day period, for example in the account area, order confirmation email and footer.
3. A confirmation step ("confirm withdrawal").
4. An acknowledgement sent on a durable medium with date and time.

Belgian transposition: reported as adopted by the Law of 19 July 2026 (verify the Staatsblad text, article numbers and exact wording required in Dutch and French). Until verified, findings carry `legal_review: true`.

## Not covered here

- Digital content and services conformity (Directive 2019/770) and sale of goods (Directive 2019/771): the skill does not test conformity. It only checks that the legal guarantee is mentioned (SP.CONSUMER.PRE-INFO).
- Proposed Digital Fairness Act: not law. Do not check. Mention in the report only if the user asks about future rules.
