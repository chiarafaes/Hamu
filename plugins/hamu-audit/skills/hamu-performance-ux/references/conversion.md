---
framework: UXH
name: Conversion patterns and rubric examples (FORMUX, CTA, TRUST, FLOW, CRO, BRAND voice)
last_verified: 2026-11-19
sources:
  - https://www.gov.uk/service-manual/design/designing-good-questions
  - https://web.dev/learn/forms/
  - https://www.nngroup.com/topic/e-commerce/
  - https://baymard.com/research/checkout-usability
status: Hamu own-words patterns; external research cited by name only, numbers from paid research are not reproduced
licence_note: Baymard Institute and Nielsen Norman Group research is copyrighted. Hamu cites sources by name and writes its own guidance.
---

# Conversion patterns

Conversion work is about removing friction and doubt on the main journey. Legal limits come first: dark patterns, fake urgency and hidden costs are SP findings (SP.CONSUMER.*), not growth tactics.

## Patterns behind the checks

- **Ask less.** Every extra field costs completions. Drop "how did you hear about us", split name only if needed, ask for phone only when it is used.
- **Guest checkout first.** Forced account creation is one of the most cited reasons for checkout abandonment in published checkout research.
- **No surprises.** Show delivery cost and time early. Unexpected costs at the last step drive abandonment.
- **Proof near the decision.** Reviews and guarantees next to the price or primary button, not only on a testimonials page.
- **Clear next step.** Confirmation pages and emails say what happens next and when.
- **Local trust for Belgian sites.** Bancontact as payment method (check current local wallet options, they change), Dutch and French content, Belgian address and enterprise number visible.

## Rubric examples

| Check | 2 | 1 | 0 |
|---|---|---|---|
| PX.FORMUX.GUEST | Guest checkout is the default, account offered after the order. | Guest option exists but is less visible than "create account". | Account required to buy. |
| PX.FORMUX.INLINE | Inline validation after leaving a field, data kept on error. | Validation only on submit, data kept. | Data lost on error, or validation fires while typing every key. |
| PX.FORMUX.PROGRESS | Steps shown, back works without data loss. | Steps shown, back loses some data. | No progress, back breaks the flow. |
| PX.FORMUX.CAPTCHA | No CAPTCHA, or an invisible check. | Checkbox CAPTCHA. | Image puzzle CAPTCHA on every submit. |
| PX.CTA.PRIMARY | One primary CTA in the first mobile screen of each key page. | CTA present but below the fold, or two equal CTAs. | No clear CTA on a key page. |
| PX.CTA.LABEL | Specific verb and object ("Book a free intro call"). | Generic but clear ("Contact us"). | Vague ("Submit", "Go", "Learn more" as the only CTA). |
| PX.CTA.CONTRAST | Primary CTA clearly heavier than secondary actions. | Same weight as one other action. | Primary CTA looks like a secondary link. |
| PX.CTA.CONTACT | Contact route in header or sticky element on every page. | Only in the footer. | Only on a contact page buried in a menu. |
| PX.TRUST.PROOF | Dated reviews with source, near the CTA, plus cases or logos. | Proof exists but only on a separate page, or undated. | No proof at all on a site that asks for money or data. |
| PX.TRUST.PRICE | Price and delivery cost and time on the product page. | Delivery cost only in the cart. | Costs appear only at the last step. |
| PX.TRUST.ABOUT | Real people, photos, location, story. | Generic text, stock photos. | No about information. |
| PX.TRUST.SECURITY | Known payment logos, clean payment step. | Missing logos or mixed styles. | Payment step looks like another site without explanation. |
| PX.TRUST.FRESH | Content dates are current. | One stale item on a key page. | Several stale signals (old year, past events, dead blog). |
| PX.FLOW.STEPS | Journey has no detours, about 3 to 5 steps to complete. | One unneeded step or page reload. | Many detours, forced registration, or repeated questions. |
| PX.FLOW.DEAD-ENDS | Every page leads on, confirmation says what happens next. | Some pages without a next step. | Confirmation page is blank or generic. |
| PX.BRAND.ASSETS | Logo, favicon and share image present, sharp, current. | One missing or blurry asset. | Old logo, missing favicon and no share image. |
| PX.BRAND.VOICE | Copy matches the brand kit in tone and address form throughout. | Mostly matches, a few off-brand pages or mixed address forms. | Tone clearly differs from the brand kit on key pages. |

## CRO idea format

Each PX.CRO finding:
- Hypothesis: "If we <change>, then <metric> will <go up or down>, because <reason from a finding>."
- Metric: the event or conversion to watch.
- Effort: S, M or L.
- Evidence: the finding ids it builds on.
Rank by impact divided by effort. At most 5 ideas.
