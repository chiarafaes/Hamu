---
framework: AI-SEARCH
name: AI visibility prompt set and tracking sheet
last_verified: 2026-11-19
sources:
  - https://developers.google.com/search/docs/appearance/ai-features
  - https://docs.perplexity.ai/guides/bots
status: Hamu method
---

# AI visibility prompt set (SEO.GEO.PROMPTS)

Claude cannot log in to ChatGPT, Perplexity, Gemini or Copilot on the user's behalf, and answers vary per user, location and day. So Hamu gives a repeatable test the owner can run, plus a sheet to track it.

## Build the prompt set (10 to 20 prompts)

From the intake (services, region, audience) write prompts in the language customers use, in four groups:

| Group | Example (tattoo studio in Ghent) |
|---|---|
| Category, local | "Best tattoo studio in Ghent for fine line work?" |
| Problem | "How do I take care of a new tattoo the first week?" |
| Comparison | "Fine line vs traditional tattoo, which ages better?" |
| Brand | "What do people say about <brand> in Ghent?" |

Rules: no brand name in the first three groups. Use Dutch and French prompts for Belgian markets. Keep the set fixed so results compare over time.

## Run

For each prompt and each assistant (ChatGPT, Perplexity, Gemini, Copilot, Claude, Google AI Overviews or AI Mode): new chat, no login history if possible, note the date.

Optional proxy in Claude: run the prompts through the available web search tool and record which domains appear. Confidence `low`, label as "search proxy, not the assistant's answer".

## Tracking sheet columns

| Column | Values |
|---|---|
| Date | YYYY-MM-DD |
| Assistant | ChatGPT, Perplexity, Gemini, Copilot, Claude, AI Overviews, AI Mode |
| Prompt id | P01 to P20 |
| Brand mentioned | yes / no |
| Brand cited with link | yes / no |
| Position | first, in list, footnote only, not present |
| Competitors mentioned | names |
| Sources cited | domains |
| Sentiment | positive, neutral, negative |
| Notes | wrong facts, outdated info |

Hamu writes the prompt set and an empty sheet (CSV) to `.audit/reports/hamu-geo-prompts.csv`. A re-audit compares filled sheets.
