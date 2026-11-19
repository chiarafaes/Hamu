---
framework: EPRIVACY-BE
name: ePrivacy Directive as applied in Belgium, with GBA/APD cookie guidance
last_verified: 2026-11-19
sources:
  - https://eur-lex.europa.eu/eli/dir/2002/58/oj
  - https://www.dataprotectionauthority.be/publications/cookie-checklist.pdf
  - https://www.ejustice.just.fgov.be/ (Law of 30 July 2018, Art. 10/2)
  - https://www.ejustice.just.fgov.be/ (Law of 21 December 2021 transposing the European Electronic Communications Code)
status: partly verified, see verify markers
---

# EPRIVACY-BE: cookies and similar technologies

## Legal basis

- EU: ePrivacy Directive 2002/58/EC, Art. 5(3). Storing or reading information on a user's device needs prior consent, unless strictly necessary for the service the user asked for or only for transmitting a communication.
- Belgium: the cookie rule used to sit in Art. 129 of the Law of 13 June 2005 on electronic communications. The Law of 21 December 2021 (transposing the European Electronic Communications Code) moved it to **Art. 10/2 of the Law of 30 July 2018**. The substance did not change. (Cross-checked with law firm commentary. Exact entry into force date: verify in the Belgian Official Gazette.)
- Consent has the GDPR meaning (Art. 4(11) and Art. 7 GDPR).
- Supervisor: GBA/APD.

## GBA/APD cookie checklist (2023)

The GBA/APD published a cookie checklist in 2023. It is not exhaustive and adds no new obligations, but it is how the authority reads the rules. Points the checks use:

| Point | Check |
|---|---|
| Non-essential cookies only after consent | SP.CONSENT.PRE-TRACK |
| A "reject all" option on the first layer, next to "accept all", without extra clicks | SP.CONSENT.REJECT |
| Buttons do not steer the choice by colour, contrast or size | SP.CONSENT.REJECT, SP.CONSUMER.DARK |
| First layer names the purposes and the parties placing cookies | SP.CONSENT.INFO |
| No pre-ticked boxes, consent per purpose | SP.CONSENT.GRANULAR |
| Scrolling or continuing to browse is not consent | SP.CONSENT.PRE-TRACK |
| Withdrawing is as easy as giving consent | SP.CONSENT.WITHDRAW |
| Consent can be proven | SP.CONSENT.RECORD |

Enforcement: the GBA/APD ordered Belgian news sites in 2024-2025 to add a reject button on the first layer after complaints by noyb. Use this as context in the executive layer, not as a fine prediction.

Open items (verify before use in a finding):
- Maximum consent validity and maximum cookie lifetime: the checklist asks for a "limited period" and for the duration of each cookie to be listed, without a fixed number in the sources checked (2026-11-19). Report long lifetimes (over 13 months) as `warn` with `legal_review: true`, never as a hard rule.
- Whether audience measurement cookies can be exempt from consent in Belgium. Default: treat analytics as needing consent.

## Strictly necessary (no consent needed)

Session cookies for a cart or login, load balancing, security (CSRF, fraud prevention), the consent cookie itself, user interface preferences the user set (language). Not exempt: analytics, A/B testing, ads, social plugins, chat widgets that track before use, session replay.

## Direct marketing by email

Belgian rule on electronic direct marketing (opt-in for emails to natural persons, with a soft opt-in for existing customers for similar products): Code of Economic Law, Book XII, and Royal Decree of 4 April 2003 (verify articles). Used by SP.PRIVACY.FORMS for the marketing checkbox.

## Other member states

When `users_in` has EU countries other than Belgium, apply the Belgian reading as the Hamu default, and note that national authorities (CNIL, AP, DSK) may differ in detail.
