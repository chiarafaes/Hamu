---
framework: GOOGLE-SEARCH
name: Hamu crawl method
last_verified: 2026-11-19
sources:
  - https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics
  - https://www.rfc-editor.org/rfc/rfc9309
status: Hamu method; robots.txt parsing per RFC 9309
---

# Crawl method

## Limits

- Max 200 URLs by default (raise only with the owner's agreement). Max 1 request per second. Stop on repeated 429 or 5xx and report.
- The Hamu crawler identifies honestly (a normal browser user agent plus a note in the report). It respects robots.txt for itself.
- No form submissions, no logins, no parameters invented by the crawler.

## Order

1. Fetch `robots.txt` (RFC 9309 parsing) and all sitemaps it lists.
2. Start from the home page and sitemap URLs. Breadth-first, internal links only.
3. For each URL record: status, redirect chain, content type, title, meta description, meta robots, `X-Robots-Tag`, canonical, hreflang, H1, word count, internal and external links with anchors, JSON-LD blocks, `lang`, click depth.
4. Render a sample (home, one per template, top 10 by internal links) in a browser and diff against raw HTML: text, links, title, canonical, schema.
5. User-agent comparison for cloaking: fetch the home page and one template page once with a Googlebot user agent string and once with a browser user agent. Large differences are a warn, never a conclusion (real Googlebot comes from Google IPs).
6. AI crawler access: one request per AI user agent to the home page, compare status codes (SEO.AICRAWL.SEARCH-OPEN).

## Runtimes

| Runtime | How |
|---|---|
| Claude Code | `curl` for raw fetches, Playwright for rendering. A small script in the scratchpad, results to `.audit/evidence/hamu-seo-visibility/crawl.json`. |
| Claude app | Browser tools for rendering and fetches. Lower URL cap (50) because each fetch is a tool call. Say so in the report. |
| Fallback | Owner exports from Search Console or a crawler (Screaming Frog CSV). Mark confidence medium. |

## Output

Group findings by template, not by URL: "Product pages (143 URLs): canonical points to category" is one finding with sample URLs in evidence.
