---
framework: AI-SEARCH
name: AI answer engines, AI crawlers and Hamu definitions of AEO, GEO, AIO and SXO
last_verified: 2026-11-19
sources:
  - https://developers.google.com/search/docs/appearance/ai-features
  - https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers
  - https://platform.openai.com/docs/bots
  - https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler
  - https://docs.perplexity.ai/guides/bots
  - https://llmstxt.org/
status: crawler names cross-checked with several sources; vendor pages change often, re-check user agents before each run
---

# AI search

## Hamu definitions

| Term | Hamu meaning | Main checks |
|---|---|---|
| AEO, answer engine optimisation | Content shaped so an engine can lift a direct answer (featured snippets, voice, AI answers). | SEO.AEO.* |
| GEO, generative engine optimisation | Being mentioned and cited by generative assistants (ChatGPT, Claude, Perplexity, Gemini, Copilot). Depends on entity clarity, third-party mentions and citable content. | SEO.GEO.*, SEO.CITE.* |
| AIO, AI Overviews optimisation | Visibility in Google AI Overviews and AI Mode. Same basics as Google Search, plus snippet eligibility. | SEO.AIO.* |
| SXO, search experience optimisation | The path from result to conversion. | SEO.SXO.*, links to PX |

These terms are industry labels, not standards. The report explains them in one plain sentence each.

## What is known about how AI answers pick sources

- Google AI Overviews and AI Mode draw on the Google index. Google says no special optimisation, markup or AI files are needed, and that pages must be indexed and eligible for snippets.
- ChatGPT search, Claude and Perplexity use their own crawlers and search partners, and fetch pages live for user questions. Many of these fetchers do not run JavaScript, so content in the raw HTML is safer.
- Copilot and several others build on Bing's index.
- Third-party mentions (reviews, media, forums, comparison sites) appear often in AI answers about brands and products.

Hamu never claims a check will produce citations. GEO findings are opportunities with low or medium confidence.

## AI crawler table

Purpose decides the robots.txt advice. Ask the owner once: allow training? allow AI search? allow user-triggered fetches?

| Operator | User agent | Purpose | Respects robots.txt |
|---|---|---|---|
| OpenAI | GPTBot | Model training | yes |
| OpenAI | OAI-SearchBot | ChatGPT search index | yes |
| OpenAI | ChatGPT-User | Live fetch for a user request | OpenAI says robots.txt may not apply to user-initiated fetches (verify) |
| Anthropic | ClaudeBot | Model training | yes |
| Anthropic | Claude-SearchBot | Search index for Claude | yes |
| Anthropic | Claude-User | Live fetch for a user request | yes (per Anthropic) |
| Perplexity | PerplexityBot | Search index | yes |
| Perplexity | Perplexity-User | Live fetch for a user request | may not (verify) |
| Google | Google-Extended | Control token for Gemini model training and grounding, not a separate crawler. Does not affect Google Search or AI Overviews | yes |
| Google | Googlebot | Search, AI Overviews, AI Mode | yes |
| Apple | Applebot-Extended | Control token for Apple model training | yes |
| Common Crawl | CCBot | Open web dataset used by many models | yes |
| Meta | Meta-ExternalAgent | Model training | reported yes (verify) |
| ByteDance | Bytespider | Model training | reported to ignore robots.txt at times (verify) |

Old tokens `anthropic-ai` and `Claude-Web` are deprecated.

Common mistake: blocking all bots in a WAF or bot-protection tool (Cloudflare "block AI bots" setting) also blocks AI search and live fetch, not only training. SEO.AICRAWL.SEARCH-OPEN checks this with one request per user agent.

## llms.txt

A proposed plain-text index for language models at `/llms.txt`. Google said in 2026 that it does not use such files for Search or its AI features. Adoption studies show most files get few or no requests. Useful for developer documentation read by coding agents. Hamu reports it as `info` only.
