---
framework: AIACT, AIACT-50
name: AI Act (Regulation (EU) 2024/1689), as amended by the Digital Omnibus on AI
last_verified: 2026-11-19
sources:
  - https://eur-lex.europa.eu/eli/reg/2024/1689/oj
  - https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
  - https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/
  - https://cdp.cooley.com/digital-ai-omnibus-delays-key-deadlines-introduces-new-rules/
status: original regulation verified; Omnibus changes cross-checked with several secondary sources, Official Journal reference marked verify
---

# AI Act

## Timeline

| Date | What applies | Source status |
|---|---|---|
| 1 Aug 2024 | Entry into force | verified |
| 2 Feb 2025 | Art. 5 prohibited practices. Art. 4 AI literacy. | verified |
| 2 Aug 2025 | General-purpose AI model duties, governance, penalties | verified |
| 2 Aug 2026 | Art. 50 transparency duties | verified, not moved by the Omnibus per secondary sources |
| 2 Dec 2026 | Art. 50(2) machine-readable marking for systems already on the market before 2 Aug 2026 (grace period) | secondary sources, verify |
| 2 Dec 2027 | Annex III stand-alone high-risk systems (moved from 2 Aug 2026) | secondary sources, verify |
| 2 Aug 2028 | High-risk systems that are safety components of Annex I products (moved from 2 Aug 2027) | secondary sources, verify |

The Digital Omnibus on AI is reported as adopted as Regulation (EU) 2026/1744 and in force since 27 July 2026. Verify the number and dates on EUR-Lex before quoting them in a report. Also verify whether the Omnibus changed the Art. 4 AI literacy duty for deployers.

## Art. 50 transparency (AIACT-50)

| Para. | Duty | Who | Check |
|---|---|---|---|
| 50(1) | Tell people they interact with an AI system, unless obvious from context | Provider | SP.AI.DISCLOSE |
| 50(2) | Mark synthetic audio, image, video or text as AI-generated, machine-readable and detectable | Provider | SP.AI.LABEL |
| 50(3) | Inform people exposed to emotion recognition or biometric categorisation | Deployer | SP.AI.DISCLOSE |
| 50(4) | Disclose deepfakes, and AI-generated text published to inform the public on matters of public interest (unless human-reviewed with editorial responsibility) | Deployer | SP.AI.LABEL |

Information must be given at the latest at the first interaction, in a clear and distinguishable way, and meet accessibility requirements.

A website that embeds a third-party chatbot is usually the deployer. The provider duty in 50(1) still shows up on that site, so the skill checks the visible result either way and names who should fix it.

## Art. 5 prohibited practices (AIACT)

Check only for signals, never conclude. Every SP.AI.PROHIBITED finding has `legal_review: true`. Signals: subliminal or manipulative techniques causing harm, exploiting vulnerabilities of age or disability, social scoring, predicting crime from profiling alone, untargeted scraping of facial images, emotion recognition in workplaces or schools, biometric categorisation to infer sensitive traits, real-time remote biometric identification in public spaces for law enforcement.

## Annex III high-risk areas (AIACT)

Biometrics, critical infrastructure, education and vocational training, employment and worker management, access to essential private and public services (credit scoring, insurance pricing for life and health, emergency services), law enforcement, migration, justice and democratic processes. SP.AI.HIGH-RISK only classifies and points to the date. It does not test conformity.

## Overlap

AI-use disclosure for E-E-A-T trust is owned by SEO (`SEO.EEAT.*`). The legally required disclosure stays with SP (`SP.AI.DISCLOSE`), per the ownership matrix.
