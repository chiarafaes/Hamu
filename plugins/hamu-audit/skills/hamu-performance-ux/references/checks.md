---
last_verified: 2026-11-19
owner: hamu-performance-ux
prefix: PX.
---

# Check catalogue: hamu-performance-ux

Every check this skill owns. Ids follow `ownership-matrix.md` (`PX.DOMAIN.CHECK`). Performance checks use measured thresholds. UX checks use a fixed 0 to 2 rubric so two runs on the same site give the same answer.

## How to read this file

| Column | Meaning |
|---|---|
| Id | `check_id` written to the finding. |
| Check | What passes. For rubric checks: what a 2 looks like. |
| Frameworks | `CWV`, `UXH` (Hamu usability heuristics, `ux-heuristics.md`), `GOOGLE-SEARCH` (page experience, evidence only), `APPLE-ASRG` / `GOOGLE-PLAY` (store listing). Relation is `best_practice` unless stated. |
| Sev | Default severity before modifiers. Raised one level on the main conversion path (`severity.md`). |
| How | `A` automated (tool or measurement), `R` rubric (0 to 2, see below), `M` manual. |
| Test | `CC` Claude Code, `APP` Claude app, `FB` fallback. If no route works, `not_tested`. |

## Rubric for `R` checks

| Score | Status | Meaning |
|---|---|---|
| 2 | pass | Meets the check on all sampled pages. |
| 1 | warn | Meets it partly, or fails on secondary pages only. |
| 0 | fail | Fails on the main journey or on most sampled pages. |

Rules:
- Each `R` check in `ux-heuristics.md` or `conversion.md` has examples of 0, 1 and 2. Score against those, not against taste.
- Confidence for `R` checks is at most `medium`. Use `high` only when the evidence is a count or a measurement (number of fields, target size, word count).
- Every `R` finding includes a screenshot with the problem marked in `evidence`.
- CRO checks are ideas, not defects: status `warn` or `pass`, severity `info`, with a hypothesis and a metric to test.

## Field data first

Core Web Vitals in the report come from field data (CrUX, 28-day p75) when available. Lab data (Lighthouse) explains causes. Always state which one a number comes from. A site with too little traffic has no CrUX data: then use lab data, say so, and set confidence `medium`.

---

## CWV: Core Web Vitals

Thresholds at the 75th percentile of page loads, per device type. See `cwv.md`.

| Id | Check | Frameworks | Sev | How | Test |
|---|---|---|---|---|---|
| PX.CWV.LCP | Largest Contentful Paint at most 2.5 s (good). 2.5 to 4 s is warn, above 4 s is fail. | CWV, GOOGLE-SEARCH E | medium | A | CC: CrUX API or PSI API if a key is set, else `npx lighthouse --form-factor=mobile`. APP: open PageSpeed Insights in the browser. FB: `not_tested`. |
| PX.CWV.INP | Interaction to Next Paint at most 200 ms. 200 to 500 ms warn, above 500 ms fail. | CWV, GOOGLE-SEARCH E | medium | A | Field data only (CrUX). Lab: Total Blocking Time as a proxy, confidence low. |
| PX.CWV.CLS | Cumulative Layout Shift at most 0.1. 0.1 to 0.25 warn, above 0.25 fail. Name the shifting elements (cookie banner, ads, images without size, late fonts). | CWV, GOOGLE-SEARCH E | medium | A | Lighthouse `cls-culprits-insight`, PSI field data. |
| PX.CWV.ORIGIN | Origin-level CrUX for mobile passes all three metrics. | CWV | medium | A | CrUX origin data. Report the share of good, needs improvement and poor. |
| PX.CWV.MOBILE-GAP | Mobile is not far behind desktop (LCP or INP more than 1.5 times worse). | CWV | low | A | Compare form factors. |

## LOAD: loading and delivery

| Id | Check | Frameworks | Sev | How | Test |
|---|---|---|---|---|---|
| PX.LOAD.LCP-RESOURCE | The LCP element is in the initial HTML, not lazy loaded, and has `fetchpriority="high"` or is preloaded when it is an image. | CWV | medium | A | Lighthouse `lcp-discovery-insight`, HTML inspection. |
| PX.LOAD.RENDER-BLOCK | No render-blocking CSS or sync JS in the head beyond what the first view needs. | CWV | medium | A | Lighthouse `render-blocking-insight`. |
| PX.LOAD.JS-WEIGHT | Mobile JS transfer within the budget for the site type (see `performance-method.md`). Unused JS below 30% on the main pages. | CWV | medium | A | Lighthouse network requests and unused JS. |
| PX.LOAD.CSS-WEIGHT | CSS within budget, unused CSS below 50% on the main pages. | CWV | low | A | Lighthouse. |
| PX.LOAD.COMPRESS | Text resources are compressed (Brotli or gzip). | CWV | medium | A | `curl -sI -H "Accept-Encoding: br,gzip"`. |
| PX.LOAD.CACHE | Static assets have long cache lifetimes with fingerprinted file names. HTML has a sensible revalidation policy. | CWV | low | A | Response headers on assets. |
| PX.LOAD.FONTS | Web fonts are subset, self-hosted or preconnected, use `font-display: swap` or optional, and at most 4 font files on first view. | CWV | low | A | Network log and CSS. |
| PX.LOAD.REDIRECTS | No redirect chains before the main document (max 1 hop). | CWV | low | A | `curl -sIL`. |
| PX.LOAD.BFCACHE | Pages are eligible for the back/forward cache (no `unload` handlers, no blocking `Cache-Control: no-store` on normal pages). | CWV | low | A | CC: Playwright plus `notRestoredReasons` API in Chrome. APP: DevTools not available, `not_tested`. |
| PX.LOAD.PREFETCH | Likely next navigations are prefetched or prerendered (Speculation Rules or link prefetch). Advisory: Chrome-only today, so a progressive enhancement. | CWV | info | A | Look for `<script type="speculationrules">`. |
| PX.LOAD.DOM-SIZE | DOM stays under about 1,500 elements on key pages. | CWV | low | A | Lighthouse `dom-size-insight`. |

## IMGPERF: image performance

| Id | Check | Frameworks | Sev | How | Test |
|---|---|---|---|---|---|
| PX.IMGPERF.FORMAT | Photos use AVIF or WebP with a fallback where needed. | CWV | low | A | Content types in network log. |
| PX.IMGPERF.SIZE | Images are not served much larger than displayed (responsive `srcset` / `sizes`). | CWV | medium | A | Lighthouse `image-delivery-insight`. |
| PX.IMGPERF.LAZY | Below-the-fold images are lazy loaded. Above-the-fold images are not. | CWV | low | A | `loading` attribute vs position. |
| PX.IMGPERF.DIMENSIONS | Images and embeds have width and height (or aspect-ratio) to prevent layout shift. | CWV | medium | A | Lighthouse, HTML. |
| PX.IMGPERF.VIDEO | Background and hero videos are compressed, have a poster, and do not autoload on mobile data where avoidable. | CWV | low | A | Network log. |

## 3P: third-party scripts

| Id | Check | Frameworks | Sev | How | Test |
|---|---|---|---|---|---|
| PX.3P.COST | Third-party scripts block the main thread less than 250 ms on mobile in total. List the top 5 by cost. | CWV | medium | A | Lighthouse `third-parties-insight`. |
| PX.3P.COUNT | No more than about 10 third-party origins on first view. Duplicate tags (two analytics tools doing the same job) are flagged. | CWV | low | A | Network log grouped by origin. |
| PX.3P.FACADE | Heavy embeds (chat widgets, video players, maps) load on interaction or with a facade. | CWV | low | A | Network log before interaction. |
| PX.3P.CONSENT-COST | The consent tool itself does not delay LCP by more than 0.5 s. | CWV | low | A | Lighthouse with and without the CMP script blocked (CC only). Legal consent checks are SP's. |

## SERVER

| Id | Check | Frameworks | Sev | How | Test |
|---|---|---|---|---|---|
| PX.SERVER.TTFB | Time to First Byte at p75 at most 0.8 s (field) or below 0.6 s in lab from a nearby region. | CWV | medium | A | CrUX TTFB, `curl -w "%{time_starttransfer}"` (5 runs, median). |
| PX.SERVER.PROTOCOL | HTTP/2 or HTTP/3 is used for the main origin and static assets. | CWV | low | A | `curl --http2 -sI`, `alt-svc` header for h3. |
| PX.SERVER.CDN | Static assets are served from a CDN or edge close to the main market (EU for Belgian sites). | CWV | info | A | Response headers (`server`, `via`, `cf-ray`, `x-cache`). |
| PX.SERVER.UPTIME | Uptime monitoring exists. Known downtime in the last 30 days is reported if the owner shares it. | - | low | M | `needs_manual`. Backups and disaster recovery belong to SP. |
| PX.SERVER.ERRORS | No 5xx and no broken 4xx resources on the sampled pages. | - | medium | A | Network log status codes. |

## RESP: responsive layout

Screenshots at 375, 768 and 1280 px wide. Reflow at 320 px is owned by A11Y (`A11Y.STRUCT.REFLOW`).

| Id | Check | Frameworks | Sev | How | Test |
|---|---|---|---|---|---|
| PX.RESP.VIEWPORT | Correct viewport meta. No horizontal scroll at 375 px. | UXH | medium | A | Playwright or browser resize, compare `scrollWidth` with viewport. |
| PX.RESP.LAYOUT | Layout adapts at each width: no overlapping elements, no cut-off text, no tiny columns. | UXH | medium | R | Screenshots at three widths. |
| PX.RESP.READABLE | Body text at least 16 px on mobile, line length about 45 to 90 characters on desktop. | UXH | low | A | Computed styles. |
| PX.RESP.STICKY | Sticky headers, banners and chat buttons together cover less than 25% of the mobile viewport. | UXH | medium | A | Measure fixed elements at 375 by 812. |
| PX.RESP.INPUTS | Inputs use the right mobile keyboard (`type="email"`, `tel`, `inputmode="numeric"`). | UXH | low | A | Input attributes. |

## NAV: navigation and findability

| Id | Check | Frameworks | Sev | How | Test |
|---|---|---|---|---|---|
| PX.NAV.CLARITY | Main menu labels are clear and in the user's words. At most about 7 top-level items. | UXH | medium | R | Menu inspection. |
| PX.NAV.LOCATION | Users can tell where they are: active state in the menu, breadcrumbs on deep pages, clear page titles. | UXH | low | R | Screenshots. |
| PX.NAV.SEARCH | Sites with more than about 50 products or articles have a search that handles typos and empty results helpfully. | UXH | medium | R + M | Try 3 queries (one with a typo) in passive mode, this is normal browsing. |
| PX.NAV.MOBILE | The mobile menu is easy to open and close and shows the main tasks first. | UXH | medium | R | 375 px screenshots. |
| PX.NAV.404 | The 404 page helps users on (search, main links) and returns status 404. | UXH | low | A + R | Request a non-existing URL. |
| PX.NAV.TASKS | The top 3 tasks of the site (from intake goal or the home page) are reachable within 3 clicks from home. | UXH | medium | R | Click paths. |

## HIER: visual hierarchy and content

| Id | Check | Frameworks | Sev | How | Test |
|---|---|---|---|---|---|
| PX.HIER.ABOVE-FOLD | The first mobile screen says what the site offers and to whom, and shows the main action. | UXH | medium | R | 375 px first-view screenshot. |
| PX.HIER.SCAN | Pages are scannable: headings, short paragraphs, lists, enough white space. | UXH | low | R | Screenshots plus word count per paragraph. |
| PX.HIER.FOCUS | One primary visual focus per screen. No competing banners, popups or equal-weight buttons. | UXH | medium | R | Screenshots. |
| PX.HIER.POPUPS | No popups or interstitials that cover content on entry, especially on mobile. Newsletter popups wait for engagement. | UXH, GOOGLE-SEARCH E | medium | A + R | First-load screenshot after 5 s. The cookie banner is not counted. |
| PX.HIER.MICROCOPY | Buttons and labels say what happens ("Get a quote", not "Submit"). Error and empty states are helpful. | UXH | low | R | Button text inventory. |

## FORMUX: form friction

Labels, errors and required markers are A11Y's (`A11Y.FORM.*`). This domain covers effort.

| Id | Check | Frameworks | Sev | How | Test |
|---|---|---|---|---|---|
| PX.FORMUX.FIELDS | Forms ask only what is needed. Contact forms at most about 5 fields, checkout at most about 12 visible fields. | UXH | medium | A | Count visible fields. Confidence high. |
| PX.FORMUX.GUEST | Checkout allows guest purchase. Account creation is offered after the order. | UXH | high | R | Checkout entry inspection. |
| PX.FORMUX.INLINE | Validation happens inline after the field is left, not only on submit, and does not clear entered data. | UXH | low | R + M | Code or behaviour on staging. |
| PX.FORMUX.AUTOFILL | Address, email and payment fields support browser autofill and address lookup where available. | UXH | low | A | `autocomplete` values (shared evidence with A11Y.FORM.AUTOCOMPLETE). |
| PX.FORMUX.PROGRESS | Multi-step forms show progress and allow going back without losing data. | UXH | low | R | Flow inspection. |
| PX.FORMUX.CAPTCHA | No CAPTCHA unless abuse requires it. Prefer invisible or proof-of-work checks. | UXH | low | R | Look for reCAPTCHA, hCaptcha, Turnstile. Accessibility of CAPTCHA is A11Y's. |

## CTA: calls to action

| Id | Check | Frameworks | Sev | How | Test |
|---|---|---|---|---|---|
| PX.CTA.PRIMARY | Each key page has one clear primary CTA, visible without scrolling on mobile. | UXH | medium | R | Screenshots. |
| PX.CTA.LABEL | CTA text is specific and action-led. | UXH | low | R | Text inventory. |
| PX.CTA.CONTRAST | The primary CTA stands out from secondary actions (colour, size, weight), within the brand palette. | UXH | low | R | Screenshots. Colour contrast for accessibility is A11Y's. |
| PX.CTA.CONTACT | A direct contact route (phone, email, form, chat) is easy to find on every page for service businesses. | UXH | medium | R | Header and footer. |

## TRUST: trust signals

Review schema and third-party review presence belong to SEO. Fake reviews are SP's (legal).

| Id | Check | Frameworks | Sev | How | Test |
|---|---|---|---|---|---|
| PX.TRUST.PROOF | Real proof near decisions: reviews with source and date, client logos, cases, certifications. | UXH | medium | R | Product, pricing and contact pages. |
| PX.TRUST.PRICE | Prices, delivery costs and timelines are visible before checkout. No surprises at the last step. | UXH | high | R | Product and cart. Legal price information is SP's (SP.CONSUMER.PRE-INFO). |
| PX.TRUST.ABOUT | An about page shows real people, location and story. | UXH | low | R | About page. |
| PX.TRUST.SECURITY | Payment page shows recognisable payment methods and a clear secure context. No outdated "secure" badges without meaning. | UXH | low | R | Checkout entry. |
| PX.TRUST.FRESH | No visibly stale content on key pages (old copyright year, "upcoming" events in the past, dead news section). | UXH | low | A + R | Dates on pages. |

## FLOW: funnels and journeys

| Id | Check | Frameworks | Sev | How | Test |
|---|---|---|---|---|---|
| PX.FLOW.STEPS | The main journey (buy, book, request) has no unneeded steps or detours. | UXH | medium | R | Walk the journey up to payment. Count steps and page loads. |
| PX.FLOW.DEAD-ENDS | No dead ends: every page has a next step. Confirmation pages tell what happens next. | UXH | medium | R | Journey walk. |
| PX.FLOW.ANALYTICS | Funnel steps are measurable (events on key steps), so drop-off can be found. Consent-dependent measurement is SEO's. | - | low | A + C | Event names in tag manager or code. |
| PX.FLOW.DROP-OFF | If the owner shares analytics, the biggest drop-off step is named with a likely cause. | - | info | M | Owner data only. |

## BRAND: brand consistency

Run only when a brand kit is available (in the project, in `.audit/context.json`, or provided by the user). Without one: `not_tested` with the note "No brand kit provided." Never invent brand rules.

| Id | Check | Frameworks | Sev | How | Test |
|---|---|---|---|---|---|
| PX.BRAND.COLOR | Colours used match the brand palette or design tokens. List off-palette colours with count. | - | low | A | Computed styles vs tokens. |
| PX.BRAND.TYPE | Fonts and type scale match the brand kit. | - | low | A | Computed font families and sizes. |
| PX.BRAND.VOICE | Copy follows the tone of voice and language rules of the brand kit (for example formal or informal address). | - | low | R | Sample of headings, CTAs, errors. |
| PX.BRAND.ASSETS | Logo, favicon and social share image are present, sharp and current. | - | low | A + R | Head tags and assets. |

## CRO: conversion ideas

Always severity `info`. Each finding has a hypothesis ("If we ..., then ... because ..."), the metric to watch, and an effort estimate.

| Id | Check | Frameworks | Sev | How | Test |
|---|---|---|---|---|---|
| PX.CRO.TEST-IDEAS | Up to 5 test ideas on the main journey, ranked by expected impact and effort. | - | info | R | From the other PX findings. |
| PX.CRO.SOCIAL-PROOF | Placement of proof near the primary CTA. | - | info | R | Screenshots. |
| PX.CRO.URGENCY | Any urgency or scarcity is real. Fake urgency is a legal issue owned by SP (SP.CONSUMER.DARK). | - | info | R | Pointer only. |

## STORE: app store listing quality

Privacy labels and store policy compliance are SP's (SP.MOBILE.*).

| Id | Check | Frameworks | Sev | How | Test |
|---|---|---|---|---|---|
| PX.STORE.LISTING | Title, subtitle and first lines of the description say what the app does and for whom. | APPLE-ASRG, GOOGLE-PLAY | low | R | Public store page. |
| PX.STORE.SCREENSHOTS | Screenshots show the main tasks, are current, readable on a phone, and localised for main markets. | APPLE-ASRG, GOOGLE-PLAY | low | R | Public store page. |
| PX.STORE.RATING | Rating and recent reviews are monitored and answered. Common complaints are named. | - | info | R | Public store page. |
| PX.STORE.SIZE | App download size and startup time are reasonable for the category (owner data or store page). | - | info | M | `needs_manual` unless the build is available. |

---

## Guardrails pointers by build task

At most 5 pointers, highest severity first, as concrete rules.

| Build task | Checks to draw from |
|---|---|
| Hero or landing section | PX.LOAD.LCP-RESOURCE, PX.IMGPERF.DIMENSIONS, PX.HIER.ABOVE-FOLD, PX.CTA.PRIMARY, PX.IMGPERF.FORMAT |
| Images and media | PX.IMGPERF.SIZE, PX.IMGPERF.LAZY, PX.IMGPERF.DIMENSIONS, PX.IMGPERF.FORMAT, PX.IMGPERF.VIDEO |
| Adding a script or widget | PX.3P.COST, PX.3P.FACADE, PX.3P.COUNT, PX.LOAD.RENDER-BLOCK |
| Fonts and CSS | PX.LOAD.FONTS, PX.LOAD.RENDER-BLOCK, PX.LOAD.CSS-WEIGHT, PX.CWV.CLS |
| Interactive component (filters, cart, search) | PX.CWV.INP, PX.LOAD.JS-WEIGHT, PX.NAV.SEARCH |
| Form or checkout | PX.FORMUX.FIELDS, PX.FORMUX.GUEST, PX.TRUST.PRICE, PX.FORMUX.INLINE, PX.FLOW.STEPS |
| Navigation and menu | PX.NAV.CLARITY, PX.NAV.MOBILE, PX.NAV.TASKS, PX.RESP.STICKY |
| Layout and responsive | PX.RESP.VIEWPORT, PX.RESP.LAYOUT, PX.RESP.READABLE, PX.RESP.STICKY |
| Deploy and hosting | PX.LOAD.COMPRESS, PX.LOAD.CACHE, PX.SERVER.PROTOCOL, PX.SERVER.TTFB, PX.LOAD.REDIRECTS |
| Copy and microcopy | PX.HIER.MICROCOPY, PX.CTA.LABEL, PX.BRAND.VOICE |

## Pointers to other skills

| Observation | Owner check |
|---|---|
| Layout breaks at 320 px | A11Y.STRUCT.REFLOW |
| Tap targets too small | A11Y.TARGET.SIZE |
| Form labels or errors missing | A11Y.FORM.* |
| CTA colour contrast too low | A11Y.COLOR.CONTRAST |
| Fake urgency, hidden costs, pre-ticked add-ons | SP.CONSUMER.DARK |
| Missing legal price or delivery information | SP.CONSUMER.PRE-INFO |
| Review schema, third-party review presence | SEO.GEO.REVIEWS |
| Crawlable link structure, site architecture | SEO.LINK.* |
| Backups and disaster recovery | SP.RESIL.* |
