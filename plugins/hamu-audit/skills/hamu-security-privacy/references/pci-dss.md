---
framework: PCI-DSS
name: Payment Card Industry Data Security Standard v4.0.1 (ids only)
last_verified: 2026-11-19
sources:
  - https://www.pcisecuritystandards.org/document_library/
  - https://blog.pcisecuritystandards.org/faq-clarifies-new-saq-a-eligibility-criteria-for-e-commerce-merchants
  - https://docs.adyen.com/development-resources/pci-dss-compliance-guide/saq-a-eligibility
status: verified for versions and dates; SAQ A eligibility wording cross-checked with secondary sources
licence_note: Requirement numbers only. Never copy PCI SSC text. Descriptions below are in our own words.
---

# PCI DSS

Readiness only. The skill never states that a merchant is PCI DSS compliant. It estimates the likely self-assessment questionnaire (SAQ) and points at gaps it can see.

## Versions

- PCI DSS v4.0.1 (published June 2024) is the current version. v3.2.1 retired 31 March 2024.
- Requirements that were "future-dated" in v4.0 became mandatory on **31 March 2025**.

## SAQ estimate (from `context.product.payments`)

| Payments value | Typical SAQ | Meaning |
|---|---|---|
| hosted_redirect | SAQ A | The customer is sent to the PSP's page, or the card form is a PSP iframe. The merchant never touches card data. |
| embedded_fields | SAQ A or A-EP | PSP fields in iframes: usually A. If the merchant's own scripts can change the payment page (direct post, JS-built form): A-EP. |
| direct_card | SAQ D | The merchant's own server receives card numbers. Highest scope. |
| none | - | not_applicable |

SAQ A update (January 2025): requirements 6.4.3 (payment page script management) and 11.6.1 (change and tamper detection on payment pages) were removed from SAQ A. In return a new eligibility criterion says the merchant has confirmed its site is not susceptible to attacks from scripts that could affect its e-commerce systems. The PCI SSC FAQ explains that meeting 6.4.3 and 11.6.1, or using the PSP's script protection, are ways to confirm this. Effective with v4.0.1 from 31 March 2025.

## Requirement ids the checks map to

| Requirement | Topic (own words) | Check |
|---|---|---|
| 2 | Secure configuration, no default settings | SP.HDR.LEAK, SP.INFRA.* |
| 3 | Do not store sensitive authentication data, protect stored account data | SP.LOG.PII, code review |
| 4.2.1 | Strong cryptography for card data over public networks | SP.TLS.HTTPS, SP.TLS.VERSION |
| 6.3.3 | Patch known vulnerabilities | SP.DEPS.VULN |
| 6.4.3 | Inventory and authorise scripts on payment pages | SP.DEPS.INVENTORY |
| 8.4 | MFA for access to the cardholder data environment | SP.AUTH.MFA |
| 10 | Log and monitor access | SP.LOG.SECURITY |
| 11.6.1 | Detect unauthorised changes to payment pages | SP.DEPS.INVENTORY |

Critical finding: card numbers posted to the merchant's own server or visible in logs, when the merchant believed it was SAQ A. That is the "card data on own server without PCI scope" example in `severity.md`.
