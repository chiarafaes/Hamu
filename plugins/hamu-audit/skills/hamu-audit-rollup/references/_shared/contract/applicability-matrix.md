---
last_verified: 2026-11-19
status: draft, thresholds and dates are verified per framework in each skill's references (phase 1-4)
---

# Applicability matrix

Maps `.audit/context.json` to frameworks. Each rule gives a status: `applies`, `likely`, `readiness_only`, `not_applicable` or `unknown`.

Rules of thumb:
- When in doubt between `applies` and `not_applicable`, use `likely` and say what would decide it.
- Legal thresholds and dates live in the skill reference files, each with its own `last_verified` date. This file only says *when* a framework is in scope.
- Voluntary standards (SOC 2, ISO 27001, ISO 42001) are `readiness_only` unless the user named them. Baseline technical standards (OWASP, WCAG, CIS) always run as `best_practice` evidence.

## Framework ids

| Id | Name | Owner skill(s) |
|---|---|---|
| GDPR | EU General Data Protection Regulation | SP |
| GDPR-K | GDPR rules for children (BE digital age of consent: 13) | SP |
| EPRIVACY-BE | ePrivacy Directive as applied in Belgium + GBA/APD cookie guidance | SP |
| GDPR-TRANSFER | International transfers (Chapter V, EU-US DPF) | SP |
| EU-CONSUMER | Consumer Rights Directive, Omnibus, UCPD (dark patterns), withdrawal function, Geo-blocking | SP, PX |
| BE-CEL | Belgian Code of Economic Law: mandatory information society and e-commerce disclosures | SP |
| GPSR | General Product Safety Regulation (online sellers of physical products) | SP |
| DSA | Digital Services Act | SP |
| AIACT-50 | AI Act transparency obligations (chatbots, generated content) | SP |
| AIACT | AI Act other obligations (high-risk, prohibited practices) | SP |
| DATA-ACT | EU Data Act | SP |
| CRA | Cyber Resilience Act | SP |
| PLD | Product Liability Directive (software as product) | SP |
| NIS2-BE | NIS2 as transposed in Belgium (CCB, CyberFundamentals) | SP |
| DORA | Digital Operational Resilience Act | SP |
| PSD2 | Payment Services Directive 2 / SCA | SP |
| PCI-DSS | Payment Card Industry Data Security Standard | SP |
| MDR | EU Medical Device Regulation (software as a medical device) | SP |
| EAA | European Accessibility Act (via EN 301 549) | A11Y |
| WAD | Web Accessibility Directive (public sector, EN 301 549) | A11Y |
| EN301549 | EN 301 549 harmonised standard | A11Y |
| WCAG22 | WCAG 2.2 (A, AA; AAA advisory) | A11Y |
| ADA | Americans with Disabilities Act (Title III, case law aligns with WCAG AA) | A11Y |
| S508 | Section 508 (US federal) | A11Y |
| ASVS5 | OWASP ASVS 5.0 | SP |
| OWASP-T10 | OWASP Top 10 (Web, API, Mobile, LLM) | SP |
| MASVS | OWASP MASVS / MASTG | SP |
| CIS | CIS Benchmarks | SP |
| ISO27001 | ISO/IEC 27001:2022 + 27002 (ids only, no control text) | SP |
| ISO42001 | ISO/IEC 42001 AI management system (ids only) | SP |
| SOC2 | AICPA Trust Services Criteria (ids only) | SP |
| NIST-CSF | NIST CSF 2.0 / SP 800-53 | SP |
| HIPAA | US HIPAA Security and Privacy Rules | SP |
| CCPA | California CCPA / CPRA | SP |
| COPPA | US Children's Online Privacy Protection Act | SP |
| PIPEDA / LGPD / POPIA | Canada / Brazil / South Africa privacy laws | SP |
| APPLE-ASRG | Apple App Store Review Guidelines | SP, PX |
| GOOGLE-PLAY | Google Play Developer Program Policies | SP, PX |
| CWV | Core Web Vitals (LCP, INP, CLS) | PX |
| GOOGLE-SEARCH | Google Search Essentials, spam policies, helpful content | SEO |
| SCHEMA | schema.org structured data | SEO |

SP = hamu-security-privacy, A11Y = hamu-accessibility, PX = hamu-performance-ux, SEO = hamu-seo-visibility.

## Rules

### Privacy and consumer

| Framework | applies when | likely when | not_applicable when |
|---|---|---|---|
| GDPR | established_in has an EU/EEA country, OR users_in has BE/EU and the site processes any personal data (forms, accounts, tracking, logs) | users_in is GLOBAL and EU users cannot be excluded | no EU establishment and no EU users targeted |
| GDPR-K | GDPR applies AND (children_targeted OR data_categories has children) | content plausibly attractive to under-16s | otherwise |
| EPRIVACY-BE | users_in has BE or established_in has BE, AND cookies/local storage/pixels detected | users_in has EU (apply the member state rules of the main market; BE rules as Hamu default) | no non-essential storage or tracking detected |
| GDPR-TRANSFER | GDPR applies AND any processor/script sends data outside the EEA (US analytics, fonts, chat widgets, hosting) | third-party scripts with unknown hosting | all processing in EEA |
| EU-CONSUMER | audience B2C or both AND users_in has BE/EU | B2B shop that does not block consumers | B2B only with consumer purchase technically blocked |
| BE-CEL | established_in has BE AND site offers any online service or advertising (disclosure duties apply to almost every business site) | - | not established in BE (check own national equivalent) |
| GPSR | sells_online AND physical consumer products AND users_in has EU | - | services or digital only |
| DSA | intermediary is not none | user-generated content or third-party listings detected | intermediary none |
| CCPA | users_in has US-CA or US AND organisation meets CCPA thresholds (verify in reference) | US users and size unknown | no US users |
| COPPA | users_in has US AND (children_targeted OR actual knowledge of under-13 users) | - | otherwise |
| PIPEDA / LGPD / POPIA | users_in has CA / BR / ZA | GLOBAL | otherwise |

### Security, resilience and product

| Framework | applies when | likely when | not_applicable when |
|---|---|---|---|
| ASVS5, OWASP-T10 | always (best_practice baseline) | - | - |
| MASVS | platforms has ios or android | - | web only |
| CIS | codebase or infra config present (Dockerfile, IaC, server config) | - | URL-only audit (mark not_tested) |
| NIS2-BE | established_in has BE AND sector in NIS2 Annex I/II AND size medium or large; OR role supplier_to_regulated_entity (supply chain expectations, contractual) | sector fits but size unknown | micro/small outside special cases (DNS, TLD, trust services, public electronic comms: verify) |
| DORA | sector has finance/banking/insurance AND users_in EU; OR role supplier_to_regulated_entity with financial clients | - | otherwise |
| CRA | connected_product true, OR software is placed on the EU market as a product (downloadable app, desktop software, SDK) | mobile apps sold or distributed in EU: check whether pure SaaS front-end | pure SaaS / website without a product with digital elements |
| PLD | software is placed on the EU market as a product (including apps and SaaS-linked products) | - | non-commercial or purely B2B services: verify |
| PSD2 | product is a payment service provider or initiates payments itself | - | merchants using a PSP (the PSP handles SCA) |
| PCI-DSS | payments is direct_card or embedded_fields | payments is hosted_redirect (reduced scope, likely SAQ A) | payments none |
| DATA-ACT | connected_product true, OR product is a cloud/data processing service customers may switch away from | - | otherwise |
| AIACT-50 | ai is chatbot or generates_content AND users_in has EU | ai_features (check whether users interact directly with AI) | ai none |
| AIACT | ai is high_risk_use | ai in hiring, credit, education scoring, biometric or similar | ai none or low-risk |
| MDR | medical_purpose true | health vocabulary with diagnostic/therapeutic claims | otherwise |
| HIPAA | users_in has US AND data_categories has health AND organisation is a covered entity or business associate | US health data, role unclear | otherwise |
| ISO27001, SOC2, ISO42001, NIST-CSF, CyFun-BE | user named it in certification_targets (status readiness_only) | - | otherwise: findings still carry ids as evidence_for, no separate section |
| APPLE-ASRG / GOOGLE-PLAY | platforms has ios / android | - | otherwise |

### Accessibility

| Framework | applies when | likely when | not_applicable when |
|---|---|---|---|
| WCAG22 | always (AA as target, AAA reported as advisory) | - | - |
| EN301549 | EAA or WAD applies | - | - |
| EAA | users_in has BE/EU AND audience B2C or both AND product is a service in EAA scope (e-commerce, banking, transport, e-books, electronic communications, audiovisual access) AND NOT (micro AND service-only) | B2C service, scope category unclear | B2B only; micro-enterprise providing services |
| WAD | public_sector true AND established_in EU | body governed by public law (e.g. subsidised org): verify | otherwise |
| ADA | users_in has US AND audience B2C or both | - | otherwise |
| S508 | US federal agency or federal contractor | - | otherwise |

### Performance and search

| Framework | applies when |
|---|---|
| CWV | always for web targets |
| GOOGLE-SEARCH, SCHEMA | always for public web targets; skip for logged-in-only apps |

## Output

Write the result to `applicable_frameworks[]`. Every `likely` or `unknown` entry needs a `reason` that names the deciding fact, so the report can tell the reader what to confirm.
