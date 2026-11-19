---
framework: OWASP-T10
name: OWASP Top 10 lists (Web 2025, API Security 2023, Mobile 2024, LLM Applications 2025)
last_verified: 2026-11-19
sources:
  - https://owasp.org/Top10/2025/
  - https://owasp.org/API-Security/editions/2023/en/0x11-t10/
  - https://owasp.org/www-project-mobile-top-10/
  - https://genai.owasp.org/llm-top-10/
status: web 2025 list verified with OWASP and press coverage; API, Mobile, LLM editions verify exact titles
licence_note: OWASP content is CC BY-SA 4.0. Ids and short own-words names only.
---

# OWASP Top 10

Awareness lists, not standards. Relation is always `best_practice`. Use them to label findings so developers recognise them. ASVS is the testable standard behind them.

Attribution line for reports: "Category ids from the OWASP Top 10 projects, CC BY-SA 4.0, owasp.org."

## Web, 2025 edition

Presented November 2025 (release candidate), final text published by early 2026.

| Id | Short name | Hamu checks |
|---|---|---|
| A01:2025 | Broken access control (now includes SSRF) | SP.ACCESS.*, SP.HDR.CORS |
| A02:2025 | Security misconfiguration | SP.HDR.*, SP.SECRETS.ENV, SP.INFRA.* |
| A03:2025 | Software supply chain failures (new, wider than "vulnerable components") | SP.DEPS.* |
| A04:2025 | Cryptographic failures | SP.TLS.*, SP.SECRETS.CLIENT, SP.INFRA.ENCRYPT |
| A05:2025 | Injection | SP.INPUT.SQL, SP.INPUT.XSS |
| A06:2025 | Insecure design | manual, design review |
| A07:2025 | Authentication failures | SP.AUTH.* |
| A08:2025 | Software or data integrity failures | SP.DEPS.SRI, SP.INPUT.DESERIAL, SP.AUTH.TOKEN |
| A09:2025 | Security logging and alerting failures | SP.LOG.* |
| A10:2025 | Mishandling of exceptional conditions (new) | SP.INPUT.ERRORS |

## API Security, 2023 edition

| Id | Short name | Hamu checks |
|---|---|---|
| API1:2023 | Broken object level authorisation | SP.ACCESS.IDOR, SP.API.OBJECT |
| API2:2023 | Broken authentication | SP.API.AUTH |
| API3:2023 | Broken object property level authorisation | SP.API.OBJECT |
| API4:2023 | Unrestricted resource consumption | SP.API.RATE |
| API5:2023 | Broken function level authorisation | SP.ACCESS.SERVER |
| API6:2023 | Unrestricted access to sensitive business flows | manual |
| API7:2023 | Server-side request forgery | SP.ACCESS.SSRF |
| API8:2023 | Security misconfiguration | SP.HDR.CORS |
| API9:2023 | Improper inventory management | SP.API.DOCS |
| API10:2023 | Unsafe consumption of APIs | code review |

## Mobile, 2024 edition

M1 improper credential usage, M2 inadequate supply chain security, M3 insecure authentication and authorisation, M4 insufficient input and output validation, M5 insecure communication, M6 inadequate privacy controls, M7 insufficient binary protections, M8 security misconfiguration, M9 insecure data storage, M10 insufficient cryptography. (Verify exact titles.) Used as labels next to MASVS on SP.MOBILE.*.

## LLM Applications, 2025 edition

| Id | Short name | Hamu checks |
|---|---|---|
| LLM01:2025 | Prompt injection | SP.LLM.INJECT |
| LLM02:2025 | Sensitive information disclosure | SP.LLM.DATA |
| LLM03:2025 | Supply chain | SP.DEPS.* |
| LLM04:2025 | Data and model poisoning | manual |
| LLM05:2025 | Improper output handling | SP.LLM.OUTPUT |
| LLM06:2025 | Excessive agency | SP.LLM.INJECT |
| LLM07:2025 | System prompt leakage | SP.LLM.DATA |
| LLM08:2025 | Vector and embedding weaknesses | SP.LLM.DATA |
| LLM09:2025 | Misinformation | not checked |
| LLM10:2025 | Unbounded consumption | SP.LLM.KEY |

(Verify LLM titles against genai.owasp.org before citing a full title.)
