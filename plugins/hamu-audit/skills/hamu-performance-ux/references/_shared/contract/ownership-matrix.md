---
last_verified: 2026-11-19
---

# Ownership matrix

One owner per check. The owner checks it fully and writes the finding. Other skills may **mention** it, but only as a short pointer, and when they run alone they write a finding with `reported_by` set to themselves and `owner_skill` set to the owner. The roll-up merges those into the owner's finding by `check_id`.

## Check id prefixes

| Prefix | Skill |
|---|---|
| `SP.` | hamu-security-privacy |
| `A11Y.` | hamu-accessibility |
| `PX.` | hamu-performance-ux |
| `SEO.` | hamu-seo-visibility |

Format: `PREFIX.DOMAIN.CHECK` in capitals, hyphens allowed, e.g. `SP.CONSENT.PRE-TRACK`, `A11Y.FORM.LABEL`, `PX.CWV.INP`, `SEO.SCHEMA.VALID`.

## Domains per skill

| Skill | Domains |
|---|---|
| SP | `TLS`, `HDR` (security headers), `COOKIE` (flags), `CONSENT`, `PRIVACY` (policy, rights, retention), `TRANSFER`, `LEGAL` (imprint, terms, BE-CEL), `CONSUMER`, `AUTH`, `ACCESS`, `INPUT` (injection, XSS), `DEPS` (vulnerable components, SBOM), `SECRETS`, `API`, `LLM`, `MOBILE`, `INFRA`, `DNS` (SPF, DKIM, DMARC, DNSSEC), `DISCLOSE` (security.txt, CVD), `LOG`, `RESIL` (backup, DR, uptime), `AI` (AI Act), `CERT` (readiness per certification) |
| A11Y | `STRUCT` (landmarks, headings, semantics), `IMG`, `MEDIA` (captions, transcripts), `COLOR` (contrast), `KBD`, `FOCUS`, `FORM`, `ARIA`, `TARGET` (target size), `MOTION`, `LANG`, `DOC` (PDFs), `MOBILE` (native a11y), `STATEMENT` (accessibility statement + feedback), `COG` (cognitive, readability for a11y) |
| PX | `CWV`, `LOAD` (resources, minification, caching, compression), `IMGPERF`, `3P` (third-party script cost), `SERVER` (TTFB, uptime, HTTP/2/3), `RESP` (responsive layout), `NAV`, `HIER` (visual hierarchy), `FORMUX`, `CTA`, `TRUST`, `FLOW` (funnels, drop-off), `BRAND`, `CRO` (A/B opportunities), `STORE` (app store listing quality) |
| SEO | `CRAWL` (robots, sitemap, status codes, redirects), `INDEX` (noindex, canonical), `I18N` (hreflang), `META`, `HEAD` (H1-H3), `URL`, `LINK` (internal links, orphans), `SCHEMA`, `RENDER` (JS rendering), `CONTENT` (quality, freshness, gaps), `EEAT`, `SPAM`, `CITE`, `READ` (readability for search), `AEO`, `GEO`, `AIO`, `SXO`, `LOCAL`, `AICRAWL` (AI bots), `OFFPAGE`, `MEASURE` (Search Console, Bing, AI referrals) |

## Overlap decisions

These topics appear in more than one source list. This table is binding.

| Topic | Owner | Others do |
|---|---|---|
| Image alt text | A11Y (`A11Y.IMG.ALT`) | SEO notes it as an image SEO factor and links the finding |
| Video captions / transcripts | A11Y (`A11Y.MEDIA.CAPTION`) | SEO links it for content indexing |
| Image weight, formats (WebP/AVIF), lazy loading | PX (`PX.IMGPERF.*`) | SEO links it |
| Core Web Vitals, page speed | PX (`PX.CWV.*`) | SEO and SXO link it, never measure it again |
| Mobile responsiveness (layout) | PX (`PX.RESP.*`) | A11Y owns reflow at 320 px (`A11Y.STRUCT.REFLOW`), SEO links |
| Tap target size | A11Y (`A11Y.TARGET.SIZE`) | PX links |
| Form labels, errors, required fields | A11Y (`A11Y.FORM.*`) | PX owns friction and field count (`PX.FORMUX.*`) |
| Form security (CSRF, validation, rate limiting) | SP (`SP.INPUT.*`, `SP.AUTH.*`) | - |
| Cookie banner and consent before tracking | SP (`SP.CONSENT.*`) | SEO checks that analytics measurement still works under consent (`SEO.MEASURE.*`), PX checks banner layout shift via CLS |
| Cookie banner accessibility | A11Y (`A11Y.KBD.*`, `A11Y.FOCUS.*`) | - |
| Dark patterns in consent or checkout | SP (`SP.CONSUMER.DARK`) | PX notes CRO impact |
| CTAs | PX (`PX.CTA.*`) | SEO's SXO links it |
| Trust signals, reviews, proof | PX (`PX.TRUST.*`) | SEO owns review schema and third-party review presence (`SEO.GEO.REVIEWS`) |
| Fake or unverified reviews | SP (`SP.CONSUMER.REVIEWS`, Omnibus) | PX links |
| Navigation usability | PX (`PX.NAV.*`) | SEO owns crawlable link structure (`SEO.LINK.*`), A11Y owns keyboard and landmarks |
| Site architecture | SEO (`SEO.LINK.ARCH`) | PX links for findability |
| Robots.txt and sitemaps | SEO | SP checks robots.txt does not expose admin paths (`SP.INFRA.EXPOSE`) |
| AI crawlers in robots.txt | SEO (`SEO.AICRAWL.*`) | SP notes data-use policy only if user asks |
| HTTPS / TLS | SP (`SP.TLS.*`) | SEO links for ranking signal |
| Server response time (TTFB) | PX (`PX.SERVER.TTFB`) | SP owns server hardening |
| Uptime | PX (`PX.SERVER.UPTIME`) | SP owns backup/DR (`SP.RESIL.*`) |
| Readability | SEO (`SEO.READ.*`) for search intent | A11Y owns plain language for cognitive access (`A11Y.COG.*`) |
| Author bios, AI-use disclosure | SEO (`SEO.EEAT.*`) for trust | SP owns legally required AI disclosure (`SP.AI.DISCLOSE`, AI Act) |
| Affiliate / sponsored disclosure | SP (`SP.CONSUMER.ADS`) | SEO checks `rel="sponsored"` (`SEO.LINK.REL`) |
| Lang attribute | A11Y (`A11Y.LANG.PAGE`) | SEO owns hreflang |
| Brand consistency | PX (`PX.BRAND.*`) | - |
| App store privacy labels | SP (`SP.MOBILE.LABELS`) | PX owns listing quality |

## Adding a check

1. Pick the owner with this table. If no row fits, the owner is the skill whose framework is the legal or technical requirement (law beats best practice).
2. Add the check to the owner's `references/checks.md` with id, frameworks, method, severity default.
3. If another skill would naturally notice it, add a row above.
