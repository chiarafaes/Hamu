---
framework: SCHEMA
name: schema.org structured data and Google rich result support
last_verified: 2026-11-19
sources:
  - https://schema.org/
  - https://developers.google.com/search/docs/appearance/structured-data/search-gallery
  - https://developers.google.com/search/docs/appearance/structured-data/sd-policies
  - https://developers.google.com/search/blog/2025/06/simplifying-search-results
  - https://developers.google.com/search/blog/2025/11/update-on-our-efforts
  - https://developers.google.com/search/updates
status: phase-outs verified on Search Central blog and updates log; the full list of January 2026 removals was not published in one place, check the search gallery before each run
---

# Structured data

## Rules (Google structured data policies, own words)

- Markup must describe content that is visible on the page.
- No misleading or irrelevant markup. No markup for content hidden from users.
- Reviews and ratings: no self-serving reviews in `LocalBusiness` or `Organization` markup about the business itself. Ratings must match visible reviews.
- JSON-LD is the recommended format.
- Valid markup does not guarantee a rich result.

## Phase-outs (do not spend effort on these for Google)

| When | What |
|---|---|
| 2023 | FAQ rich results limited to authoritative government and health sites. HowTo rich results removed. |
| June to November 2025 | Course Info, Claim Review, Estimated Salary, Learning Video, Special Announcement, Vehicle Listing phased out of Search and Search Console. Book Actions was announced but later kept. |
| January 2026 | Further removals from Search Console and its API for rarely used features, including Practice Problem (documentation removed 6 January 2026). Dataset markup is used only by Dataset Search. |

Structured data still helps other consumers (Bing, AI systems that read schema, knowledge graphs). Keep valid existing markup when it describes the page. SEO.SCHEMA.DEPRECATED is `info` only.

## Types Hamu checks first

Check the Google search gallery for the current list before relying on any rich result.

| Site type | Types |
|---|---|
| Every site | `Organization` or `LocalBusiness` (name, logo, url, sameAs, contactPoint), `WebSite`, `BreadcrumbList` |
| E-commerce | `Product` with `Offer` (price, currency, availability), merchant return and shipping details, `AggregateRating` only from real reviews |
| Content | `Article` or `BlogPosting` with author (`Person` with url), dates |
| Local business | `LocalBusiness` subtype, address, geo, opening hours, telephone |
| Events | `Event` with location, dates, offers |
| Jobs | `JobPosting` |
| Video | `VideoObject` |

## Testing

- Claude Code: extract JSON-LD from raw and rendered HTML, parse, check required properties per type.
- Claude app: Google Rich Results Test and the Schema Markup Validator (validator.schema.org) in the browser.
- Compare marked-up values (price, rating, address) with visible text. Mismatch is SEO.SCHEMA.VALID fail.
