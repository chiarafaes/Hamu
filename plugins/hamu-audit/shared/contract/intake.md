---
last_verified: 2026-11-19
applies_to: all Hamu skills
---

# Intake

Every Hamu skill starts here. Goal: a valid `.audit/context.json` with the fewest possible questions.

## 0. Reuse first

1. Look for `.audit/context.json` in the project root (codebase) or the current working folder (URL audit).
2. If it exists, has the same target and is less than 30 days old: reuse it. Show a one-line scope summary and ask only "Still correct?" Do not ask the three questions again.
3. If it is older than 30 days or the target differs: start a new audit id, but prefill answers from the old file.

## 1. Target and permission (always, one question)

Ask what to audit if the user did not say: URL(s), local codebase path, or both. Then ask for permission in one question:

- "Do you own this site/app or have written permission to test it?"
  - Yes, passive only (default)
  - Yes, and active tests are allowed (only on staging or with explicit scope)
  - No / auditing someone else's site

If the answer is **No**: run public, passive checks only (what any visitor sees: headers, HTML, cookies, robots.txt, sitemap, public pages). No form submissions, no login attempts, no fuzzing, no port scans. Mark `permission.owner_confirmed=false`.

Active tests (injection probes, auth testing, scanning beyond normal browsing) require `owner_confirmed=true` AND `active_testing_allowed=true`. Never infer permission from context.

## 2. Auto-detect before asking

Detect signals from the target and record them in `detected[]` with evidence. Minimum detection list:

| Signal | How to detect |
|---|---|
| Company country | Imprint/footer, VAT/company number format (BE0xxx.xxx.xxx), ccTLD, address |
| Languages | `<html lang>`, hreflang, language switcher |
| Payments | Stripe/Mollie/Adyen/PayPal scripts, checkout redirects, card input iframes vs raw `<input>` for card numbers |
| Accounts | Login/register forms, auth libraries in code |
| Tracking | GA4, GTM, Meta Pixel, Hotjar, LinkedIn Insight, TikTok pixel, consent platform |
| AI | Chatbot widgets, OpenAI/Anthropic/other LLM SDKs or API calls in code, "AI" labels |
| Health / children / finance | Vocabulary on key pages, form fields (date of birth, medical fields, IBAN), sector keywords |
| Marketplace / platform | Third-party seller listings, user-generated content, reviews by users |
| Mobile apps | App Store / Play links, `ios/` `android/` folders, React Native/Flutter config |
| Public sector | `.gov`, `.belgium.be`, `.vlaanderen.be`, `.wallonie.be`, `.brussels` domains, government branding |

## 3. The three questions

Ask only what detection did not settle with high confidence. Use the interactive question tool when available (chip options), otherwise numbered options in text. Always include "Not sure" as an option.

**Q1. Where is the organisation established and where are the users?**
Options: Belgium only · Belgium + rest of EU · EU + UK · Also US · Global
→ fills `jurisdiction.established_in`, `jurisdiction.users_in`. Follow-up only if "Also US/Global": "Any users in California, Canada, Brazil or South Africa?"

**Q2. What does the product do and what data does it handle?** (multi-select)
Options: Sells to consumers online · B2B only · Takes payments · User accounts · Health data · Financial/banking · Aimed at children · Uses AI (chatbot, generated content) · Marketplace / user content · Public sector
→ fills `product.*`. Confirm detected signals inside this question ("We detected Mollie checkout and a chatbot, correct?").

**Q3. Who is the organisation and what is this audit for?**
Size: Micro (<10 staff and <=EUR 2M turnover) · Small (<50) · Medium (<250) · Large · Not sure
Goal: Quick scan · Before launch · Preparing certification (SOC 2 / ISO 27001 / ISO 42001 / HIPAA / PCI) · Legal check · Report for a client
→ fills `organisation.*`. If goal is certification prep, ask which targets.

Maximum two follow-up questions after Q3, and only when an answer flips a framework between `applies` and `not_applicable` (for example NIS2 sector, CRA connected product, MDR medical purpose).

## 4. Resolve applicability

Run the rules in `applicability-matrix.md`. Write `applicable_frameworks[]` with status and a one-line reason. Show the user a short scope summary before running checks:

> Scope: GDPR, Belgian cookie rules, EU consumer law, EAA (WCAG 2.2 AA), AI Act transparency. Likely: PCI DSS (SAQ A). Not applicable: NIS2, HIPAA. Passive testing only.

Do not wait for approval of the scope unless the user is clearly present and the audit is large. Start the checks.

## 5. Guardrails mode (building, not auditing)

When the skill is invoked while building a site or app:
- Use the same intake, but ask it once at project start and store it.
- Do not run audits. Load the relevant checklist items as build rules for the current task only (for example a form: labels, error messages, consent, validation, CSRF).
- Keep it short: at most 5 pointers per task, highest severity first.
