---
framework: EAA
name: European Accessibility Act (Directive (EU) 2019/882) and Belgian transposition
last_verified: 2026-11-19
sources:
  - https://eur-lex.europa.eu/eli/dir/2019/882/oj
  - https://economie.fgov.be/
  - https://www.ejustice.just.fgov.be/ (Code of Economic Law, consolidated)
  - https://www.craftzing.com/our-insights/articles/european-accessibility-act-in-belgium-compliance-complaints-penalties
  - https://www.lexgo.be/en/news-and-articles/14225-making-financial-services-more-accessible
  - https://www.vlaio.be/nl/nieuws/nieuwe-regels-rond-digitale-toegankelijkheid-voor-e-handelsdiensten
  - https://www.unizo.be/advies/heeft-u-een-vergunning-nodig-om-een-webshop-te-beginnen
status: directive verified; Belgian transposition law and the micro-enterprise rule conflict across secondary sources (verify)
---

# European Accessibility Act

## Dates

- Applies from **28 June 2025** to products placed on the market and services provided to consumers after that date.
- Transition (Art. 32): services may keep using products they lawfully used before 28 June 2025 until 28 June 2030. Service contracts agreed before 28 June 2025 may continue unchanged until they expire, at the latest 28 June 2030. Self-service terminals may be used until the end of their economic life, at most 20 years.

## Services in scope (Art. 2(2)) relevant to Hamu

- E-commerce services: any service at a distance, through websites and mobile apps, by electronic means, at the consumer's request, to conclude a consumer contract. In practice: B2C web shops and booking flows.
- Consumer banking services.
- Electronic communications services, and services giving access to audiovisual media services.
- Elements of air, bus, rail and waterborne passenger transport services: websites, mobile apps, e-tickets, real-time travel information.
- E-books and dedicated software.

Out of scope: B2B-only services, pure information sites that sell nothing (unless another category applies), and content of third parties not funded or controlled by the provider (Art. 2(4)).

## Exemptions

- Micro-enterprises providing services (fewer than 10 staff and annual turnover or balance sheet total at most EUR 2 million) are exempt under the directive (Art. 4(5)).
- Disproportionate burden or fundamental alteration (Art. 14): must be assessed, documented and renewed at least every 5 years, and the authority informed when relied on.

## Belgium

- Transposed through amendments to the Code of Economic Law and other laws. Secondary sources name the Law of 5 November 2023 for part of the transposition (verify title and date in the Belgian Official Gazette).
- Market surveillance and enforcement: FPS Economy (Economic Inspection).
- Micro-enterprises (fewer than 10 staff and turnover under EUR 2 million) providing services: per Unizo, VLAIO and a draft FPS Economy guideline, they are exempt until 28 June 2030, with obligations for agreements concluded after that date. One source reported 2035, which could not be confirmed. Hamu treats a Belgian micro service provider as `likely` with the reason "obligations from 28 June 2030", runs the checks as `best_practice`, and adds `legal_review: true` until the FPS Economy final guidance is checked.

## Duties the checks use

| Duty | Where | Check |
|---|---|---|
| Accessibility requirements for services, including websites and apps "in a consistent and adequate way", perceivable, operable, understandable and robust | Annex I, Section III and IV | all WCAG-based checks via EN 301 549 |
| Information on how the service meets the requirements, in the general terms and conditions or equivalent, in accessible format | Art. 13(2), Annex V | A11Y.STATEMENT.EXISTS, A11Y.STATEMENT.CONTENT |
| Support services (help desks, call centres) give information on accessibility in accessible ways | Annex I, Section III (e) | A11Y.STATEMENT.FEEDBACK |
| Identification and authentication methods, security elements and payment methods are perceivable, operable, understandable and robust | Annex I, Section IV (e-commerce, banking) | A11Y.FORM.AUTH, A11Y.KBD.ACCESS |

Presumption of conformity: EN 301 549 (see `en301549.md`).
