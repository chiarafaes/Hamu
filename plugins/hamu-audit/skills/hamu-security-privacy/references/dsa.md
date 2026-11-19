---
framework: DSA
name: Digital Services Act (Regulation (EU) 2022/2065)
last_verified: 2026-11-19
sources:
  - https://eur-lex.europa.eu/eli/reg/2022/2065/oj
  - https://www.bipt.be/ (Belgian Digital Services Coordinator)
status: verified for articles; Belgian coordinator role verify
---

# DSA

Applies to all intermediary services since 17 February 2024. Duties grow by layer: intermediary, hosting, online platform, marketplace, very large platform. Belgian Digital Services Coordinator: BIPT/IBPT (verify current designation).

## Which layer (from `context.product.intermediary`)

| Layer | Example | Articles the checks use |
|---|---|---|
| Intermediary (all) | Hosting, caching, mere conduit | Art. 11 point of contact for authorities, Art. 12 point of contact for users, Art. 14 terms explain moderation |
| Hosting | Sites that store user content (comments, uploads) | + Art. 16 notice and action, Art. 17 statement of reasons |
| Online platform | Forums, social features, marketplaces | + Art. 20 complaint handling, Art. 25 no dark patterns in the interface, Art. 26 ad transparency, Art. 27 recommender transparency, Art. 28 protection of minors |
| Marketplace | Third-party sellers to consumers | + Art. 30 trader traceability, Art. 31 compliance by design, Art. 32 right to information |

## Small company exemption

Art. 19: micro and small enterprises (per Recommendation 2003/361/EC) are exempt from the platform duties in Section 3 (Art. 20 to 28) and Section 4 (Art. 29 to 32), unless they are very large online platforms. Art. 11 to 18 still apply. Record the size from intake. When size is unknown, run the checks and mark status `warn` with a note.

## Checks

SP.CONSUMER.DSA-NOTICE (Art. 11, 12, 14, 16), SP.CONSUMER.MARKETPLACE (Art. 30-32), SP.CONSUMER.ADS (Art. 26), SP.CONSUMER.DARK (Art. 25), SP.PRIVACY.CHILDREN (Art. 28).
