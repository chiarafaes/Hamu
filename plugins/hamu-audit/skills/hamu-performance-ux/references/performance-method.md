---
framework: CWV
name: Hamu performance test method and budgets
last_verified: 2026-11-19
sources:
  - https://web.dev/articles/performance-budgets-101
  - https://developer.chrome.com/docs/lighthouse/performance/performance-scoring
  - https://httparchive.org/reports/page-weight
status: Hamu method; budgets are Hamu defaults based on HTTP Archive medians and web.dev guidance, not a standard
---

# Performance method

## Page sample

Same sample idea as the other skills, focused on templates:
1. Home.
2. Top landing page (from the owner, or the page ranked first for the brand name).
3. One page per template: category or listing, product or service detail, article, search results.
4. Each step of the main journey up to payment (cart, checkout start).

Default 6 to 10 URLs. Field data per URL when CrUX has it, else origin data.

## Lab settings

- Lighthouse mobile defaults (simulated throttling, Moto G Power class device, slow 4G). Do not change them, so results compare over time.
- Clean profile, no extensions, no logged-in state.
- 3 runs per URL, report the median.
- Desktop runs only when the owner asks or the audience is mainly desktop (B2B tools).

## Budgets (mobile, compressed transfer, first view)

Hamu defaults. Override with the owner's own budget when they have one.

| Site type | Total weight | JavaScript | Images | Third-party origins |
|---|---|---|---|---|
| Brochure or portfolio site | 1.0 MB | 150 KB | 600 KB | 6 |
| Content site or blog | 1.5 MB | 250 KB | 900 KB | 10 |
| E-commerce | 2.0 MB | 400 KB | 1.2 MB | 12 |
| Web app (logged in) | 2.5 MB | 600 KB | 800 KB | 8 |

Above budget is `warn`. More than 1.5 times the budget is `fail` for PX.LOAD.JS-WEIGHT and PX.LOAD.CSS-WEIGHT.

## Responsive screenshots

Widths 375, 768 and 1280 px, height 812 for mobile first view and full-page for layout review. In Claude Code use Playwright. In the Claude app use the browser resize tool. Store in `.audit/evidence/hamu-performance-ux/`.

## When tools are missing

| Missing | Effect |
|---|---|
| No CrUX access and no PSI | CWV checks from lab only, confidence medium, INP `not_tested` |
| No Lighthouse and no PSI | All CWV and LOAD lab checks `not_tested`. Header checks (compression, cache, protocol) still run with `curl` or the browser |
| No browser automation | RESP, HIER, CTA rubric checks from static HTML and screenshots the user provides, confidence low |
