---
last_verified: 2026-11-19
owner: hamu-seo-visibility
prefix: SEO.
---

# Check catalogue: hamu-seo-visibility

Every check this skill owns. Ids follow `ownership-matrix.md` (`SEO.DOMAIN.CHECK`). Technical checks are automated from a crawl. Content, trust and AI visibility checks use the same fixed 0 to 2 rubric as hamu-performance-ux, with examples in `content-rubric.md`.

## How to read this file

| Column | Meaning |
|---|---|
| Id | `check_id` written to the finding. |
| Check | What passes. |
| Frameworks | `GOOGLE-SEARCH` (Search Essentials, spam policies, `google-search.md`), `BING-WMG` (Bing Webmaster Guidelines), `SCHEMA` (schema.org and rich result rules, `schema.md`), `AI-SEARCH` (AI answer engines, `ai-search.md`). `R` = requirement of that search engine's own rules, `B` = best_practice. |
| Sev | Default severity. Raised one level for the home page and top landing pages. |
| How | `A` automated from the crawl or a fetch, `R` rubric 0 to 2, `M` manual or owner data. |
| Test | `CC` Claude Code, `APP` Claude app, `FB` fallback. If no route works, `not_tested`. |

Rubric rules are the same as in hamu-performance-ux: 2 pass, 1 warn, 0 fail, confidence at most `medium` unless measured, a screenshot or quote as evidence, and examples in `content-rubric.md`.

Search engine rules are not law. "Requirement" here means the engine says breaking it can stop indexing or trigger a manual action. The report never promises rankings or AI citations.

Crawl defaults (`crawl-method.md`): max 200 URLs, 1 request per second, respect robots.txt for the Hamu crawler itself, compare raw and rendered HTML on a sample.

---

## CRAWL: crawlability

| Id | Check | Frameworks | Sev | How | Test |
|---|---|---|---|---|---|
| SEO.CRAWL.ROBOTS | `robots.txt` exists, returns 200, is valid, and does not block important sections, CSS or JS. | GOOGLE-SEARCH R, BING-WMG R | high | A | Fetch and parse. Test key URLs against rules for Googlebot and Bingbot. |
| SEO.CRAWL.SITEMAP | An XML sitemap exists, is referenced in robots.txt, has only canonical 200 URLs, and `lastmod` is accurate. | GOOGLE-SEARCH B, BING-WMG B | medium | A | Fetch, sample 50 URLs, check status and canonical. |
| SEO.CRAWL.STATUS | No 4xx or 5xx on internally linked URLs. Soft 404s (200 with "not found" content) are flagged. | GOOGLE-SEARCH R | medium | A | Crawl. |
| SEO.CRAWL.REDIRECTS | Redirects are 301 or 308, single hop, no loops, no internal links pointing at redirects. | GOOGLE-SEARCH B | low | A | Crawl. |
| SEO.CRAWL.HTTPS-CANON | One preferred host: HTTP and non-preferred www or non-www variants redirect to it. TLS itself is SP's. | GOOGLE-SEARCH B | medium | A | Fetch the four variants. |
| SEO.CRAWL.PARAMS | Faceted navigation and URL parameters do not create endless crawlable duplicates. | GOOGLE-SEARCH B | medium | A | Count parameter URLs in the crawl. |
| SEO.CRAWL.INDEXNOW | Site pings IndexNow (Bing, Yandex and others) on content changes, or submits sitemaps to Bing Webmaster Tools. | BING-WMG B | info | A | Look for the IndexNow key file or CMS plugin. |

## INDEX: indexing controls

| Id | Check | Frameworks | Sev | How | Test |
|---|---|---|---|---|---|
| SEO.INDEX.NOINDEX | No `noindex` (meta or `X-Robots-Tag`) on pages that should rank. Staging and thin utility pages are noindexed. | GOOGLE-SEARCH R | high | A | Crawl headers and meta. |
| SEO.INDEX.CANONICAL | Every indexable page has a self-referencing or correct canonical. No canonical to a redirect, 404 or noindex page. | GOOGLE-SEARCH B | medium | A | Crawl. |
| SEO.INDEX.DUPLICATE | No near-duplicate pages competing for the same query without canonical or consolidation. | GOOGLE-SEARCH B | medium | A | Compare titles, H1 and content hashes. |
| SEO.INDEX.COVERAGE | Search Console coverage shows no large group of important pages "crawled, not indexed" or "discovered, not indexed". | GOOGLE-SEARCH B | medium | M | Owner shares Search Console export. Else `not_tested`. |
| SEO.INDEX.STAGING | Staging, preview and test hosts are not indexable (auth or noindex). | GOOGLE-SEARCH B | high | A | Check hosts linked from the site or named by the owner. |

## I18N: languages and regions

Important for Belgium: Dutch, French, often German and English versions.

| Id | Check | Frameworks | Sev | How | Test |
|---|---|---|---|---|---|
| SEO.I18N.HREFLANG | Language versions have reciprocal `hreflang` (for example `nl-BE`, `fr-BE`, `en`) plus `x-default`, pointing at canonical 200 URLs. | GOOGLE-SEARCH B | medium | A | Crawl, validate pairs. |
| SEO.I18N.URLS | Each language has its own URL (subfolder or subdomain). No language switch by cookie or IP only. | GOOGLE-SEARCH B | medium | A | Compare URLs per language. |
| SEO.I18N.TRANSLATED | Translated pages are fully translated (title, meta, content, alt, schema), not machine-translated boilerplate with mixed languages. | GOOGLE-SEARCH B | medium | R | Sample pages per language. `lang` attribute itself is A11Y's. |
| SEO.I18N.REDIRECT | Visitors are not force-redirected by IP or browser language. A suggestion banner is fine. | GOOGLE-SEARCH B | low | A | Fetch with different `Accept-Language`. |

## META: titles and descriptions

| Id | Check | Frameworks | Sev | How | Test |
|---|---|---|---|---|---|
| SEO.META.TITLE | Every page has a unique, descriptive title with the main topic first and the brand last, roughly 30 to 60 characters. | GOOGLE-SEARCH B | medium | A | Crawl. Length is a guide, not a rule. |
| SEO.META.DESCRIPTION | Key pages have a unique meta description that summarises the page and invites the click, roughly 70 to 160 characters. | GOOGLE-SEARCH B | low | A | Crawl. |
| SEO.META.SOCIAL | Open Graph and Twitter card tags give a title, description and share image on key pages. | - | low | A | Head tags. |
| SEO.META.FAVICON | A favicon is set and crawlable (shown in Google results). | GOOGLE-SEARCH B | info | A | Head link and fetch. |

## HEAD: headings

| Id | Check | Frameworks | Sev | How | Test |
|---|---|---|---|---|---|
| SEO.HEAD.H1 | One H1 per page that states the topic and matches search intent. | GOOGLE-SEARCH B | low | A | Crawl. Heading structure for assistive tech is A11Y's. |
| SEO.HEAD.OUTLINE | H2 and H3 describe sections in words people search for, so pages answer sub-questions. | GOOGLE-SEARCH B | low | R | Sample pages. |

## URL

| Id | Check | Frameworks | Sev | How | Test |
|---|---|---|---|---|---|
| SEO.URL.READABLE | URLs are short, lowercase, use words and hyphens, and are stable. No session ids. | GOOGLE-SEARCH B | low | A | Crawl. |
| SEO.URL.CHANGES | URL changes keep 301 redirects from old URLs. | GOOGLE-SEARCH B | medium | M | Owner shares old URL list, or check common old paths. |

## LINK: internal links and architecture

| Id | Check | Frameworks | Sev | How | Test |
|---|---|---|---|---|---|
| SEO.LINK.CRAWLABLE | Navigation and content links are real `<a href>` links, not JS click handlers. | GOOGLE-SEARCH R | high | A | Raw HTML link extraction. |
| SEO.LINK.ARCH | Important pages are within 3 clicks of the home page. Hubs link to their children and back. | GOOGLE-SEARCH B | medium | A | Click depth from the crawl. |
| SEO.LINK.ORPHANS | No important pages without internal links (in sitemap but not linked). | GOOGLE-SEARCH B | medium | A | Sitemap vs crawl. |
| SEO.LINK.ANCHOR | Anchor text describes the target. Not all "read more". | GOOGLE-SEARCH B | low | A | Anchor inventory. |
| SEO.LINK.BROKEN-EXT | No broken outbound links on key pages. | - | low | A | HEAD requests at 1 per second. |
| SEO.LINK.REL | Paid and affiliate links have `rel="sponsored"`, user content links `rel="ugc"`. The legal disclosure is SP's. | GOOGLE-SEARCH R | medium | A | Detect affiliate patterns and UGC areas. |

## SCHEMA: structured data

| Id | Check | Frameworks | Sev | How | Test |
|---|---|---|---|---|---|
| SEO.SCHEMA.VALID | Structured data parses without errors (JSON-LD preferred) and matches visible content. | SCHEMA R, GOOGLE-SEARCH R | medium | A | Parse JSON-LD. CC: schema validation. APP: Rich Results Test in the browser. |
| SEO.SCHEMA.ORG | Home page has `Organization` (or `LocalBusiness`) with name, logo, url, sameAs, contact. `WebSite` with name. | SCHEMA B, AI-SEARCH B | medium | A | JSON-LD. |
| SEO.SCHEMA.TYPES | Page types use fitting, still-supported types (`Product` with offers, `Article`, `BreadcrumbList`, `Event`, `LocalBusiness`, `Recipe`, `JobPosting`, `VideoObject`). | SCHEMA B | low | A | Compare with the supported list in `schema.md`. |
| SEO.SCHEMA.DEPRECATED | No effort spent on types Google no longer shows (see `schema.md`). Advisory: keep them only if other consumers use them. | SCHEMA B | info | A | Detect deprecated types. |
| SEO.SCHEMA.REVIEWS | Review and rating markup follows the rules: no self-serving reviews on the business's own LocalBusiness or Organization, ratings match visible reviews. | SCHEMA R, GOOGLE-SEARCH R | medium | A | JSON-LD vs visible content. |

## RENDER: JavaScript rendering

| Id | Check | Frameworks | Sev | How | Test |
|---|---|---|---|---|---|
| SEO.RENDER.CONTENT | Main content, links, title, canonical and structured data are in the raw HTML or reliably rendered. Content that only appears after interaction is flagged. | GOOGLE-SEARCH B, AI-SEARCH R | high | A | Compare `curl` HTML with Playwright rendered DOM. Many AI crawlers do not run JS, so raw HTML matters more for AI-SEARCH. |
| SEO.RENDER.BLOCKED | Resources needed to render (JS, CSS, API) are not blocked by robots.txt. | GOOGLE-SEARCH R | medium | A | robots.txt vs resource URLs. |
| SEO.RENDER.SPA | Client-side routes return real URLs with server status codes (no hash routing for indexable pages, 404 for missing). | GOOGLE-SEARCH B | medium | A | Fetch unknown route, check status. |

## CONTENT: quality and coverage

| Id | Check | Frameworks | Sev | How | Test |
|---|---|---|---|---|---|
| SEO.CONTENT.HELPFUL | Key pages are written for people: they answer the visitor's question fully, show first-hand knowledge, and are not padded. | GOOGLE-SEARCH B | medium | R | Sample of top pages. |
| SEO.CONTENT.THIN | No large group of thin or near-empty pages (tag pages, empty categories, placeholder pages) in the index. | GOOGLE-SEARCH B | medium | A | Word counts and templates. |
| SEO.CONTENT.INTENT | Each key page matches one search intent (know, do, buy, go). | GOOGLE-SEARCH B | low | R | Title, H1 and content vs likely query. |
| SEO.CONTENT.GAPS | Main services or products each have a dedicated page. Common customer questions are answered somewhere. | GOOGLE-SEARCH B | low | R | Services list vs pages, FAQ coverage. |
| SEO.CONTENT.FRESH | Time-sensitive pages show a visible updated date and are current. | GOOGLE-SEARCH B | low | A + R | Dates on pages. |
| SEO.CONTENT.CANNIBAL | No two pages target the same main topic and compete. | GOOGLE-SEARCH B | low | A | Title and H1 similarity. |
| SEO.CONTENT.IMAGES | Images that carry meaning have descriptive file names and sit near related text. Alt text is A11Y's (A11Y.IMG.ALT), linked here. | GOOGLE-SEARCH B | info | A | File names. |
| SEO.CONTENT.VIDEO | Important videos have a watch page, a transcript or captions, and `VideoObject` markup. Captions are A11Y's. | GOOGLE-SEARCH B | info | A | Video embeds. |

## EEAT: experience, expertise, authority, trust

| Id | Check | Frameworks | Sev | How | Test |
|---|---|---|---|---|---|
| SEO.EEAT.AUTHOR | Articles and advice pages show who wrote or reviewed them, with a bio and credentials where relevant (health, money, law). | GOOGLE-SEARCH B, AI-SEARCH B | medium | R | Article sample. |
| SEO.EEAT.ABOUT | About and contact pages make the organisation real: people, address, enterprise number, history. Legal identity details are SP's. | GOOGLE-SEARCH B, AI-SEARCH B | low | R | About page. |
| SEO.EEAT.EXPERIENCE | Content shows first-hand experience: own photos, cases, data, process. | GOOGLE-SEARCH B | low | R | Sample. |
| SEO.EEAT.AI-USE | Where AI helped create content, how it was used is explained when readers would expect it. Legally required AI disclosure is SP's (SP.AI.LABEL). | GOOGLE-SEARCH B | info | R | Look for AI-use notes. |
| SEO.EEAT.YMYL | Pages on health, money, safety or legal topics cite sources and show review by a qualified person. | GOOGLE-SEARCH B | high | R | Only when YMYL topics are present. |

## SPAM: spam policy risks

| Id | Check | Frameworks | Sev | How | Test |
|---|---|---|---|---|---|
| SEO.SPAM.SCALED | No large set of templated or AI-generated pages with little unique value (city by city pages with swapped names, auto-generated glossaries). | GOOGLE-SEARCH R | high | A + R | Template similarity across the crawl. |
| SEO.SPAM.REPUTATION | No third-party content hosted to borrow the site's reputation (coupon sections, sponsored directories unrelated to the business). | GOOGLE-SEARCH R | high | R | Sections unrelated to the main topic. |
| SEO.SPAM.HIDDEN | No hidden text or links, cloaking, sneaky redirects or doorway pages. | GOOGLE-SEARCH R | critical | A | Compare rendered text with visible text, user agent comparison (Googlebot UA vs browser UA, one fetch each). |
| SEO.SPAM.LINKS | No signs of link schemes: sitewide paid footer links, link exchange pages. | GOOGLE-SEARCH R | medium | A + R | Outbound link patterns. |
| SEO.SPAM.HACKED | No injected spam (pharma, casino, foreign-language pages) on the domain. | GOOGLE-SEARCH R | critical | A | `site:` style sampling via sitemap and crawl, odd language pages. Security cause goes to SP. |
| SEO.SPAM.EXPIRED | If the domain was recently bought or repurposed, the new content fits the domain's history. | GOOGLE-SEARCH R | medium | M | Owner question. |

## CITE: citability

| Id | Check | Frameworks | Sev | How | Test |
|---|---|---|---|---|---|
| SEO.CITE.FACTS | Key pages contain concrete, checkable facts (numbers, prices, dates, specs) in text, not only in images. | AI-SEARCH B | medium | R | Sample. |
| SEO.CITE.SOURCES | Claims cite their sources with links. | AI-SEARCH B, GOOGLE-SEARCH B | low | R | Sample. |
| SEO.CITE.ORIGINAL | The site publishes something others would cite: original data, research, tools, clear definitions. | AI-SEARCH B | info | R | Content inventory. |
| SEO.CITE.QUOTABLE | Important statements are self-contained sentences that make sense when quoted alone. | AI-SEARCH B | low | R | Sample paragraphs. |

## READ: readability for search

Plain language for cognitive access is A11Y's (A11Y.COG.*).

| Id | Check | Frameworks | Sev | How | Test |
|---|---|---|---|---|---|
| SEO.READ.LEVEL | Readability fits the audience (B1 level for consumer pages in Dutch and French). | GOOGLE-SEARCH B | low | A | Readability score per language (sentence length, word length). |
| SEO.READ.STRUCTURE | Answers come first, then detail (inverted pyramid). Lists and tables for steps and comparisons. | GOOGLE-SEARCH B, AI-SEARCH B | low | R | Sample. |

## AEO: answer engine optimisation

Being the direct answer (featured snippets, voice, AI answers).

| Id | Check | Frameworks | Sev | How | Test |
|---|---|---|---|---|---|
| SEO.AEO.QUESTIONS | Pages target real questions in headings, each followed by a direct 40 to 60 word answer. | AI-SEARCH B, GOOGLE-SEARCH B | medium | R | Headings and following paragraph. |
| SEO.AEO.FAQ | FAQ sections answer real customer questions (not keyword stuffing). FAQ rich results are limited by Google, so value is for users and AI answers, not stars. | AI-SEARCH B | low | R | FAQ pages. |
| SEO.AEO.DEFINITIONS | Key terms of the business are defined clearly once, on a page that can be cited. | AI-SEARCH B | low | R | Sample. |

## GEO: generative engine optimisation

Being mentioned and cited by AI assistants (ChatGPT, Claude, Perplexity, Gemini, Copilot).

| Id | Check | Frameworks | Sev | How | Test |
|---|---|---|---|---|---|
| SEO.GEO.ENTITY | The brand is a clear entity: same name, description and facts across site, schema (`sameAs`), Google Business Profile, LinkedIn, Wikidata where relevant. | AI-SEARCH B | medium | A + R | Compare sources. |
| SEO.GEO.MENTIONS | The brand is mentioned on third-party sites that AI assistants often cite (industry media, comparison sites, directories, forums). | AI-SEARCH B | medium | M | Owner data or web search, confidence low. |
| SEO.GEO.REVIEWS | The brand has recent reviews on third-party platforms (Google, Trustpilot, sector platforms). Review markup on the own site is SEO.SCHEMA.REVIEWS. | AI-SEARCH B | low | M + A | Public profiles. |
| SEO.GEO.PROMPTS | A prompt set of 10 to 20 buyer questions is defined, and the brand's presence in AI answers is tracked over time. | AI-SEARCH B | info | M | `geo-prompt-set.md`. Claude produces the set and sheet. Runs by the user. Optional proxy run with available search tools, confidence low. |
| SEO.GEO.COMPARE | Comparison and "best X in Y" questions about the category have a fair, factual page on the site (with competitors named honestly). | AI-SEARCH B | info | R | Content inventory. |

## AIO: Google AI Overviews and AI Mode

| Id | Check | Frameworks | Sev | How | Test |
|---|---|---|---|---|---|
| SEO.AIO.ELIGIBLE | Pages are indexable and snippet-eligible (no `nosnippet` or very low `max-snippet` on pages that should be shown). Google says no special markup or files are needed for AI features. | GOOGLE-SEARCH R, AI-SEARCH B | medium | A | Meta robots and headers. |
| SEO.AIO.EXTENDED | `Google-Extended` in robots.txt is set on purpose (it controls Gemini model use, not Search or AI Overviews). | AI-SEARCH B | info | A | robots.txt. |

## SXO: search experience

From search result to conversion. PX owns the UX checks, SXO links them.

| Id | Check | Frameworks | Sev | How | Test |
|---|---|---|---|---|---|
| SEO.SXO.MATCH | The landing page delivers what the title and description promised. | GOOGLE-SEARCH B | medium | R | Top landing pages. |
| SEO.SXO.NEXT | Search landing pages have a clear next step. Links PX.CTA.* and PX.CWV.*. | - | low | R | Pointer to PX findings. |

## LOCAL: local search

Only when the business serves customers in a region or has a location.

| Id | Check | Frameworks | Sev | How | Test |
|---|---|---|---|---|---|
| SEO.LOCAL.GBP | A verified Google Business Profile exists with correct category, hours, photos, services and website link. | GOOGLE-SEARCH B, AI-SEARCH B | high | M + A | Public profile in browser or owner confirmation. |
| SEO.LOCAL.NAP | Name, address and phone are identical on the site, GBP, Bing Places, Apple Business Connect and main Belgian directories. | GOOGLE-SEARCH B | medium | A + M | Compare public listings. |
| SEO.LOCAL.PAGES | Each location has its own page with address, map, hours, local content and `LocalBusiness` schema. No doorway city pages. | GOOGLE-SEARCH B | medium | R | Location pages. |
| SEO.LOCAL.REVIEWS | Reviews on GBP are recent and answered. | GOOGLE-SEARCH B | low | M | Public profile. |

## AICRAWL: AI crawler access

| Id | Check | Frameworks | Sev | How | Test |
|---|---|---|---|---|---|
| SEO.AICRAWL.POLICY | robots.txt rules for AI crawlers match the owner's choice per purpose: training, search indexing, user-triggered fetch (see crawler table in `ai-search.md`). | AI-SEARCH B | medium | A | Parse robots.txt per user agent. Ask the owner's intent once. |
| SEO.AICRAWL.SEARCH-OPEN | If the owner wants AI search visibility: search and user-fetch bots (OAI-SearchBot, ChatGPT-User, Claude-SearchBot, Claude-User, PerplexityBot) are not blocked by robots.txt, WAF or bot protection. | AI-SEARCH B | high | A | robots.txt plus a fetch with each user agent string (one request each), compare status. |
| SEO.AICRAWL.LLMSTXT | `llms.txt` is optional. Google does not use it for Search or AI features. Useful mainly for developer documentation read by coding agents. | AI-SEARCH B | info | A | Fetch `/llms.txt`. Never a fail. |

## OFFPAGE

| Id | Check | Frameworks | Sev | How | Test |
|---|---|---|---|---|---|
| SEO.OFFPAGE.LINKS | The site has relevant links from real sites in its field and region. | GOOGLE-SEARCH B | info | M | Owner data from Search Console links report or a backlink tool. |
| SEO.OFFPAGE.PROFILES | Social and directory profiles link to the site and use the same brand facts. | AI-SEARCH B | low | A + M | `sameAs` targets. |

## MEASURE: measurement

| Id | Check | Frameworks | Sev | How | Test |
|---|---|---|---|---|---|
| SEO.MEASURE.GSC | Google Search Console is verified for the domain property. | GOOGLE-SEARCH B | medium | M + A | Verification meta tag or DNS record, or owner confirms. |
| SEO.MEASURE.BING | Bing Webmaster Tools is verified (also feeds Copilot and other engines that use Bing). | BING-WMG B | low | M + A | Verification tag or owner. |
| SEO.MEASURE.ANALYTICS | Analytics measures organic traffic under the consent setup (consent-mode pings or cookieless analytics), so reports are not blind after "reject". Consent legality is SP's. | - | medium | A | Network log after reject vs accept. |
| SEO.MEASURE.AI-REFERRALS | Traffic from AI assistants is tracked (referrers such as chatgpt.com, perplexity.ai, claude.ai, copilot.microsoft.com, gemini.google.com) in a separate channel. | AI-SEARCH B | low | A + M | Analytics config or owner. |

---

## Guardrails pointers by build task

| Build task | Checks to draw from |
|---|---|
| New page or template | SEO.META.TITLE, SEO.HEAD.H1, SEO.INDEX.CANONICAL, SEO.RENDER.CONTENT, SEO.SCHEMA.TYPES |
| Site launch or migration | SEO.CRAWL.ROBOTS, SEO.INDEX.NOINDEX, SEO.CRAWL.SITEMAP, SEO.URL.CHANGES, SEO.INDEX.STAGING |
| Multilingual site | SEO.I18N.HREFLANG, SEO.I18N.URLS, SEO.I18N.TRANSLATED, SEO.I18N.REDIRECT |
| JS framework or SPA | SEO.RENDER.CONTENT, SEO.RENDER.SPA, SEO.LINK.CRAWLABLE, SEO.RENDER.BLOCKED |
| Blog post or article | SEO.CONTENT.HELPFUL, SEO.EEAT.AUTHOR, SEO.AEO.QUESTIONS, SEO.CITE.FACTS, SEO.CITE.SOURCES |
| Local business site | SEO.LOCAL.GBP, SEO.LOCAL.NAP, SEO.SCHEMA.ORG, SEO.LOCAL.PAGES |
| Navigation and menus | SEO.LINK.CRAWLABLE, SEO.LINK.ARCH, SEO.LINK.ANCHOR |
| robots.txt or bot protection change | SEO.CRAWL.ROBOTS, SEO.AICRAWL.POLICY, SEO.AICRAWL.SEARCH-OPEN, SEO.RENDER.BLOCKED |
| Affiliate or sponsored content | SEO.LINK.REL, SEO.SPAM.REPUTATION |

## Pointers to other skills

| Observation | Owner check |
|---|---|
| Missing alt text | A11Y.IMG.ALT |
| Missing captions | A11Y.MEDIA.CAPTION |
| Slow pages, CWV | PX.CWV.* |
| Image weight and formats | PX.IMGPERF.* |
| Mobile layout | PX.RESP.* |
| HTTPS and TLS | SP.TLS.* |
| robots.txt exposes admin paths | SP.INFRA.EXPOSE |
| Legally required AI disclosure | SP.AI.DISCLOSE, SP.AI.LABEL |
| Affiliate disclosure text | SP.CONSUMER.ADS |
| Hacked content security cause | SP.INPUT.*, SP.DEPS.* |
| Trust signals and CTAs on landing pages | PX.TRUST.*, PX.CTA.* |
| Lang attribute | A11Y.LANG.PAGE |
