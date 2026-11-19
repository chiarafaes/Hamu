---
framework: GOOGLE-SEARCH, BING-WMG
name: Google Search Essentials (technical requirements, spam policies, key best practices) and Bing Webmaster Guidelines
last_verified: 2026-11-19
sources:
  - https://developers.google.com/search/docs/essentials
  - https://developers.google.com/search/docs/essentials/spam-policies
  - https://developers.google.com/search/docs/fundamentals/creating-helpful-content
  - https://developers.google.com/search/blog/2024/03/core-update-spam-policies
  - https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a
status: structure verified on Google Search Central; 2026 enforcement changes cross-checked with secondary sources only
---

# Google Search Essentials and Bing

## Search Essentials has three parts

1. **Technical requirements**: Googlebot is not blocked, the page returns HTTP 200, and the page has indexable content. Checks: SEO.CRAWL.*, SEO.INDEX.NOINDEX, SEO.RENDER.*.
2. **Spam policies**: breaking them can lower rankings or remove pages (manual actions or automated systems). Checks: SEO.SPAM.*, SEO.LINK.REL, SEO.SCHEMA.REVIEWS.
3. **Key best practices**: helpful, reliable, people-first content, words people search for, crawlable links, images and video best practices, structured data. Checks: CONTENT, EEAT, META, HEAD, LINK, SCHEMA.

## Spam policies the skill checks

Own-words summaries:
- Cloaking, doorway pages, hidden text and links, sneaky redirects, keyword stuffing.
- Link spam: buying or selling links that pass ranking credit, excessive link exchanges.
- Scaled content abuse: many pages made mainly to rank, by any method (AI, templates, people), with little value. Introduced March 2024.
- Site reputation abuse: third-party pages published on a site to profit from its ranking signals. Introduced March 2024.
- Expired domain abuse: buying an expired domain to rank low-value content on its old reputation. Introduced March 2024.
- Hacked content, user-generated spam, thin affiliate pages, machine-generated traffic, misleading functionality, scraping.

Reported 2026 changes (verify on Search Central before quoting): changes to site reputation enforcement in the EEA from 30 August 2026, and spam updates in June and September 2026.

## Helpful content

Since March 2024 helpfulness is part of the core ranking systems, not a separate classifier. Google's self-assessment questions (own words): Is the content original? Does it fully answer the question? Would a reader trust it? Does it show first-hand experience? Was it made mainly for people or for search engines?

## AI features

Google's guidance (2025, clarified June 2026): the same SEO best practices apply to AI Overviews and AI Mode. No special markup, AI files or markdown pages are needed. Pages need to be indexed and snippet-eligible. See `ai-search.md`.

## Bing Webmaster Guidelines

Similar principles. Bing supports IndexNow for fast change notification. Bing's index also feeds Microsoft Copilot and several other search and AI products, so Bing visibility matters for AI search. Checks: SEO.CRAWL.INDEXNOW, SEO.MEASURE.BING.

## Report rules

- Never promise rankings, traffic or AI citations.
- Ranking claims point to Google or Bing documentation, not to third-party studies.
- Core updates and spam updates are context, not a diagnosis. Without the owner's Search Console data, do not attribute a traffic drop to an update.
