---
name: hamu-seo-visibility
description: Audit a website for search and AI visibility: technical SEO, content and E-E-A-T, structured data, AEO, GEO, AIO, SXO, local SEO and AI crawler access. Use for an SEO audit, AI visibility or GEO check, or for SEO pointers while building.
---

# hamu-seo-visibility

Search and AI visibility checks. Owns every check with prefix `SEO.`. Technical checks come from a polite crawl. Content, trust and AI visibility use a fixed 0 to 2 rubric.

> Status: 0.9.0. Tested on a real website in Claude Code and in the Claude app (security and privacy skill). Write this version as `skill_version` in the findings file.

Never promise rankings, traffic or citations by AI assistants. Search engine rules are not law.

## Always read first

- `references/_shared/contract/intake.md`
- `references/_shared/contract/run-protocol.md`
- `references/_shared/contract/severity.md`
- `references/_shared/contract/report-template.md`
- `references/_shared/contract/applicability-matrix.md`
- `references/_shared/contract/ownership-matrix.md`
- `references/checks.md` (catalogue and rubric rules)

| Topic | Reference |
|---|---|
| Crawl limits, order, runtimes | `references/crawl-method.md` |
| Search Essentials, spam policies, Bing | `references/google-search.md` |
| Structured data rules and phase-outs | `references/schema.md` |
| AEO, GEO, AIO, SXO, AI crawlers, llms.txt | `references/ai-search.md` |
| Rubric examples | `references/content-rubric.md` |
| Local search and Belgian specifics | `references/local-seo.md` (only for local businesses) |
| AI visibility prompt set and sheet | `references/geo-prompt-set.md` |

## Pick the mode

- **Audit mode**: the user asks for an SEO, AI visibility or GEO audit.
- **Guardrails mode**: the user is building or migrating. When unsure, ask: "Full audit, or pointers for what you are building now?"

## Audit mode

1. **Intake** per `intake.md`. Reuse `.audit/context.json`. Ask at most two extra questions when missing: main services and region (for the prompt set and local checks), and the owner's choice on AI crawlers (allow training, AI search, user fetches).
2. **Environment.** Detect: `curl`, Playwright, browser tools, web search tool. Ask whether the owner can share Search Console, Bing Webmaster Tools or analytics exports. Record `tools_used` and `tools_missing`.
3. **Crawl** per `crawl-method.md` (max 200 URLs, 1 per second). Render a sample and diff raw vs rendered.
4. **Automated checks** on the crawl: CRAWL, INDEX, I18N, META, HEAD, URL, LINK, SCHEMA, RENDER, AICRAWL, and the automated parts of SPAM, CONTENT and MEASURE.
5. **Rubric pass** on a sample (home, top landing pages, one per template, 3 articles): CONTENT, EEAT, CITE, READ, AEO, GEO, SXO, LOCAL. Score against `content-rubric.md`, quote the evidence.
6. **Owner data.** If shared: coverage, queries, links, AI referrals. Else write those checks as `not_tested`.
7. **AI visibility.** Write the prompt set and empty sheet per `geo-prompt-set.md`. Optional search proxy run with confidence `low`.
8. **Write findings** to `.audit/findings/hamu-seo-visibility.json` per `finding.schema.json`. Group by template. Link owner checks of other skills (alt text, CWV, TLS) as pointers only when running alone.
9. **Write the report** `.audit/reports/hamu-seo-visibility.md` per `report-template.md`. Add an AI crawler table (bot, purpose, current rule, matches owner choice) and the template-level issue table.
10. **Update** `context.json` `runs[]` and tell the user: score, top 3 actions, what needs their data, report path. Suggest the other Hamu skills once, in one line.

### Severity reminders

- Anything that stops indexing of important pages (robots block, noindex, broken rendering, JS-only links) is `high`.
- Spam policy risks are `high`, hidden text or hacked content `critical`.
- Raise one level for the home page and top landing pages.
- GEO, CITE and AEO findings are opportunities: mostly `low` or `info`.

## Guardrails mode

1. Read `.audit/context.json`, or run intake once and store it.
2. Pick the build task in "Guardrails pointers by build task" in `checks.md`.
3. Give at most 5 concrete rules with check ids, highest impact first. Prefer code: for example "Render the product name, price and description in the server HTML, not only after hydration (SEO.RENDER.CONTENT)."
4. For migrations, always include redirects, robots.txt and noindex on staging.
5. No report files. On "is this OK now?", fetch the page raw and rendered and run the related checks.

## Overlaps

Follow `ownership-matrix.md`. This skill links but never re-measures: Core Web Vitals and image weight (PX), alt text and captions (A11Y), HTTPS (SP), legally required AI disclosure and affiliate disclosure (SP). It owns hreflang, review schema, third-party review presence, site architecture, robots.txt and AI crawler rules, and readability for search.
