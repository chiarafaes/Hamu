---
framework: GPSR
name: General Product Safety Regulation (Regulation (EU) 2023/988)
last_verified: 2026-11-19
sources:
  - https://eur-lex.europa.eu/eli/reg/2023/988/oj
status: verified
---

# GPSR

Applies since 13 December 2024 to consumer products placed on the EU market, including through online sales. Only physical products. Services and digital content are out of scope.

## Online listings (Art. 19)

Each product offer online must show clearly:

1. Name, registered trade name or trademark of the manufacturer, and postal and electronic address.
2. If the manufacturer is outside the EU: name and address of the responsible person in the EU.
3. Information to identify the product: picture, type, and any other identifier such as batch or serial number.
4. Warnings or safety information in a language consumers can easily understand, as decided by the member state where it is sold.

Used by SP.CONSUMER.GPSR. Method `heuristic` on a sample of product pages (default 10). Missing manufacturer details on most listings is `medium`. Missing warnings on products that need them (toys, electrical, cosmetics) is `high` with `legal_review: true`.

Online marketplaces have extra duties (Art. 22), such as registering in the Safety Gate portal and designing the interface so traders can give the Art. 19 information. Check only that the interface has the fields.
