---
framework: PLD
name: Product Liability Directive (Directive (EU) 2024/2853)
last_verified: 2026-11-19
sources:
  - https://eur-lex.europa.eu/eli/dir/2024/2853/oj
status: verified for EU text; Belgian transposition verify
---

# PLD

- Adopted 23 October 2024. Member states transpose by **9 December 2026**. Applies to products placed on the market after that date. The old Directive 85/374/EEC keeps applying to older products.
- Software, including AI systems and software delivered as a service when it is part of a product, counts as a product. Free and open source software developed or supplied outside a commercial activity is excluded.
- A product can be defective because of missing security updates or a lack of cybersecurity that the law requires (link with CRA).
- Belgian transposition law: verify status.

## How the skill uses it

No separate checks. PLD raises the stakes of existing findings. When PLD applies, add `PLD` as `evidence_for` on:
- SP.DEPS.VULN and SP.DEPS.EOL (unpatched known vulnerabilities),
- SP.DISCLOSE.CVD (no way to receive vulnerability reports),
- SP.AI.* for AI features in products.

Executive layer wording: "Since December 2026, software defects, including security gaps, can lead to product liability claims." Always with `legal_review: true`.
