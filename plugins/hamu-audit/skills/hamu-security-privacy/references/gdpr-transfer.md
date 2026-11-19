---
framework: GDPR-TRANSFER
name: International transfers under GDPR Chapter V
last_verified: 2026-11-19
sources:
  - https://eur-lex.europa.eu/eli/reg/2016/679/oj
  - https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/adequacy-decisions_en
  - https://www.dataprivacyframework.gov/list
  - https://eur-lex.europa.eu/eli/dec_impl/2021/914/oj
status: verified for structure; legal challenges to the EU-US DPF marked verify
---

# GDPR-TRANSFER

## Rules

| Art. | Mechanism |
|---|---|
| 44 | General principle: transfers outside the EEA need a Chapter V basis. |
| 45 | Adequacy decision. The country (or certified company) offers equivalent protection. |
| 46 | Appropriate safeguards: Standard Contractual Clauses (Implementing Decision (EU) 2021/914), binding corporate rules, codes, certifications. |
| 49 | Derogations for specific situations (explicit consent, contract necessity). Not for routine, repeated transfers. |

## EU-US Data Privacy Framework

- Adequacy decision adopted 10 July 2023. Covers only US organisations that self-certify. Check the provider on https://www.dataprivacyframework.gov/list.
- The General Court dismissed an annulment action against the decision in 2025 (Latombe v Commission, T-553/23). An appeal to the Court of Justice may be pending (verify status before writing it in a report).
- If the provider is not certified: SCCs plus a transfer impact assessment are needed.

## How the skill checks (SP.TRANSFER.*)

1. Group all third-party requests by registrable domain.
2. Map each domain to a provider and hosting region. Use the provider's own docs. When unknown, status `warn` with confidence low.
3. For providers outside the EEA, look in the privacy notice for the transfer and its safeguard.
4. Typical examples to recognise: Google Analytics and Fonts, Meta Pixel, Hotjar, Intercom, HubSpot, Cloudflare, Vercel, AWS outside EU regions, OpenAI and Anthropic APIs.

Never decide the legal question alone. Every SP.TRANSFER.BASIS fail has `legal_review: true`.

Adequacy list: check the Commission page for the current list of countries (includes UK, Switzerland, Japan, Korea, Canada for commercial organisations, and others).
