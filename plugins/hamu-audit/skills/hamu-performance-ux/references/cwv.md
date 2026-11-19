---
framework: CWV
name: Core Web Vitals (LCP, INP, CLS) and supporting metrics
last_verified: 2026-11-19
sources:
  - https://web.dev/articles/vitals
  - https://web.dev/articles/defining-core-web-vitals-thresholds
  - https://developer.chrome.com/docs/crux/
  - https://developers.google.com/search/docs/appearance/core-web-vitals
  - https://developer.chrome.com/blog/lighthouse-13-0
status: verified; claims of a 2026 INP threshold change found only in unreliable secondary sources and not adopted
---

# Core Web Vitals

## Metrics and thresholds (p75 of page loads, per device type)

| Metric | Good | Needs improvement | Poor | Measures |
|---|---|---|---|---|
| LCP Largest Contentful Paint | at most 2.5 s | 2.5 to 4.0 s | above 4.0 s | Loading of the main content |
| INP Interaction to Next Paint | at most 200 ms | 200 to 500 ms | above 500 ms | Responsiveness to all interactions (replaced FID in March 2024) |
| CLS Cumulative Layout Shift | at most 0.1 | 0.1 to 0.25 | above 0.25 | Visual stability |

A page passes Core Web Vitals when all three are good at p75. No new Core Web Vital has been added since INP.

Supporting metrics (diagnostic, not Core Web Vitals): TTFB (good at most 0.8 s), FCP (good at most 1.8 s), TBT in the lab (lab proxy for INP, good below 200 ms on Lighthouse mobile).

## Field vs lab

| Source | What | Use for | Access |
|---|---|---|---|
| CrUX (Chrome UX Report) | Real Chrome users, rolling 28 days, origin and URL level, only with enough traffic | The pass or fail verdict | CrUX API (free key), PageSpeed Insights, CrUX History API for trends |
| PageSpeed Insights | CrUX field data plus a Lighthouse lab run | Both, in the Claude app via the browser | pagespeed.web.dev, PSI API |
| Lighthouse 13 (October 2025) | Lab run, simulated mid-range mobile on slow 4G | Causes, before-launch sites, sites without field data | `npx lighthouse <url> --form-factor=mobile --output=json` (Node 22.19 or newer) |
| RUM in the site (web-vitals library) | Own field data | Owners who have it | Owner shares data |

Lighthouse 13 merged its performance audits into "insights" shared with DevTools (for example `lcp-discovery-insight`, `render-blocking-insight`, `cls-culprits-insight`, `third-parties-insight`, `image-delivery-insight`). Scoring did not change. Use the insight ids in evidence.

## Search

Core Web Vitals are part of Google's page experience signals. They count, but relevance counts far more. The report never promises ranking gains from speed work. SEO links to PX findings and does not measure them again.

## Report rules

- State the source and date of every number ("CrUX, 28 days to 2026-11-15, mobile p75").
- Lab numbers vary between runs. Run Lighthouse 3 times per page and report the median.
- Name the element and the cause, not only the number ("LCP is the hero image, discovered late because it is a CSS background").
