---
name: hamu-performance-ux
description: Audit a website or app for performance, UX and conversion: Core Web Vitals, loading, responsive layout, navigation, visual hierarchy, forms, CTAs, trust signals and funnels. Use for a speed, UX, CRO or Core Web Vitals audit, or for performance and UX pointers while building.
---

# hamu-performance-ux

Performance, usability and conversion checks. Owns every check with prefix `PX.`. Performance is measured against thresholds. UX is scored with a fixed 0 to 2 rubric, so results are repeatable.

> Status: 0.9.0. Tested on a real website in Claude Code and in the Claude app (security and privacy skill). Write this version as `skill_version` in the findings file.

Speed and UX findings are best practice, not legal requirements. Legal issues seen on the way (dark patterns, hidden costs) go to hamu-security-privacy.

## Always read first

- `references/_shared/contract/intake.md`
- `references/_shared/contract/run-protocol.md`
- `references/_shared/contract/severity.md`
- `references/_shared/contract/report-template.md`
- `references/_shared/contract/applicability-matrix.md`
- `references/_shared/contract/ownership-matrix.md`
- `references/checks.md` (catalogue, rubric rules, field-data-first rule)

| Topic | Reference |
|---|---|
| Core Web Vitals, field vs lab | `references/cwv.md` |
| Page sample, lab settings, budgets, screenshots | `references/performance-method.md` |
| Usability heuristics, rubric for RESP, NAV, HIER | `references/ux-heuristics.md` |
| Conversion patterns, rubric for FORMUX, CTA, TRUST, FLOW, BRAND, CRO format | `references/conversion.md` |
| App store listing | `references/store-listing.md` (only when `platforms` has ios or android) |

## Pick the mode

- **Audit mode**: the user asks for a speed, UX, CRO or Core Web Vitals audit.
- **Guardrails mode**: the user is building. When unsure, ask: "Full audit, or pointers for what you are building now?"

## Audit mode

1. **Intake** per `intake.md`. Reuse `.audit/context.json`. Ask one extra question only if missing: "What is the main thing visitors should do on the site?" It decides the main journey. If a brand kit exists in the project or the user gives one, note its path in the context.
2. **Environment.** Detect: Playwright, `npx lighthouse` (Node 22.19+), CrUX or PSI API key, `curl`, browser tools. Record `tools_used` and `tools_missing`.
3. **Sample** per `performance-method.md` (6 to 10 URLs including the main journey up to payment).
4. **Field data.** Fetch CrUX for origin and sampled URLs (API, or PageSpeed Insights in the browser). Record the date range.
5. **Lab data.** Lighthouse mobile, 3 runs per URL, median. Keep the JSON in `.audit/evidence/hamu-performance-ux/`.
6. **Headers and network.** Compression, caching, protocol, redirects, third-party origins, status codes.
7. **Screenshots** at 375, 768 and 1280 px, first view and full page, for every sampled URL.
8. **Rubric pass.** Score every `R` check from the screenshots and DOM against the examples in `ux-heuristics.md` and `conversion.md`. Mark the problem area on the screenshot when possible. Walk the main journey up to the payment step without submitting.
9. **Brand.** Run PX.BRAND.* only with a brand kit. Else write them as `not_tested` with "No brand kit provided."
10. **Write findings** to `.audit/findings/hamu-performance-ux.json` per `finding.schema.json`. Rubric score goes into `detail_technical` ("Rubric 1 of 2: ..."). CRO ideas as `info` with hypothesis, metric and effort.
11. **Write the report** `.audit/reports/hamu-performance-ux.md` per `report-template.md`. Add a CWV table (metric, field p75, lab median, status, source and date) and a screenshot strip per width.
12. **Update** `context.json` `runs[]` and tell the user: CWV verdict, score, top 3 actions, report path. Suggest the other Hamu skills once, in one line.

### Severity reminders

- Raise one level when the issue is on the main conversion path.
- CWV "poor" on mobile for the main landing page is `high`. "Needs improvement" is `medium`.
- Rubric score 0 on the main journey is `medium` or `high` per the check default. Score 1 is `warn`.
- CRO is always `info`.

## Guardrails mode

1. Read `.audit/context.json`, or run intake once and store it.
2. Pick the build task in "Guardrails pointers by build task" in `checks.md`.
3. Give at most 5 concrete rules with check ids, highest impact first. Prefer code: for example "Add `width`, `height` and `fetchpriority="high"` to the hero image and do not lazy load it (PX.LOAD.LCP-RESOURCE, PX.IMGPERF.DIMENSIONS)."
4. Use the project's design tokens and brand kit when giving visual advice. Never invent colours or fonts.
5. No report files. On "is this fast enough now?", run Lighthouse on that page only and compare with the previous run.

## Overlaps

Follow `ownership-matrix.md`. Use "Pointers to other skills" in `checks.md`: reflow at 320 px and tap target size are A11Y's, dark patterns and legal price information are SP's, review schema and crawlable links are SEO's. SEO links to PX for Core Web Vitals and never measures them again.
