---
framework: ASVS5
name: OWASP Application Security Verification Standard 5.0.0
last_verified: 2026-11-19
sources:
  - https://owasp.org/www-project-application-security-verification-standard/
  - https://github.com/OWASP/ASVS/tree/master/5.0/en
status: release date and chapters V1-V5, V9-V11, V15-V17 verified; V6-V8 and V12-V14 titles from the 5.0 repository, verify wording
licence_note: OWASP ASVS is CC BY-SA 4.0. Hamu references chapter and requirement ids and paraphrases. Never copy requirement text.
---

# ASVS 5.0

Released 30 May 2025 at Global AppSec EU. Three levels: L1 (baseline, testable from outside for a large part), L2 (most applications with sensitive data), L3 (high assurance). Hamu default target: L1 for every web target, L2 when the product handles accounts, payments, health or financial data.

Attribution line for reports: "Requirement ids from OWASP ASVS 5.0, CC BY-SA 4.0, owasp.org."

## Chapters and Hamu domains

| Chapter | Title | Hamu checks |
|---|---|---|
| V1 | Encoding and Sanitization | SP.INPUT.SQL, SP.INPUT.XSS |
| V2 | Validation and Business Logic | SP.INPUT.VALIDATE |
| V3 | Web Frontend Security | SP.HDR.*, SP.COOKIE.*, SP.TLS.MIXED, SP.DEPS.SRI |
| V4 | API and Web Service | SP.API.*, SP.HDR.CORS |
| V5 | File Handling | SP.INPUT.UPLOAD |
| V6 | Authentication | SP.AUTH.PASSWORD, SP.AUTH.MFA, SP.AUTH.BRUTE, SP.AUTH.ENUM, SP.AUTH.RESET |
| V7 | Session Management | SP.AUTH.SESSION |
| V8 | Authorization | SP.ACCESS.* |
| V9 | Self-contained Tokens | SP.AUTH.TOKEN |
| V10 | OAuth and OIDC | SP.AUTH.OAUTH |
| V11 | Cryptography | SP.INFRA.ENCRYPT |
| V12 | Secure Communication | SP.TLS.* |
| V13 | Configuration | SP.SECRETS.*, SP.HDR.LEAK, SP.INFRA.EXPOSE |
| V14 | Data Protection | SP.PRIVACY.PII-URL, SP.LOG.PII |
| V15 | Secure Coding and Architecture | SP.DEPS.*, SP.INPUT.DESERIAL |
| V16 | Security Logging and Error Handling | SP.LOG.*, SP.INPUT.ERRORS |
| V17 | WebRTC | only when WebRTC is detected, not in the default catalogue |

## How findings cite ASVS

Use the chapter (`V6`) when a finding covers a whole area. Use the full id (`V6.2.1`) only after reading that requirement in the official 5.0 CSV or repository, because numbering changed completely from 4.0.3. Relation is always `best_practice`.
