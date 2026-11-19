# Changelog

## 0.5.0 (2026-11-19) Phase 3: hamu-performance-ux

- `references/checks.md`: 76 `PX.` checks over 15 domains. Performance checks with measured thresholds (CWV, loading, images, third parties, server). UX checks scored with a fixed 0 to 2 rubric, confidence at most medium unless measured. CRO ideas as `info` with hypothesis and metric. Brand checks only with a brand kit. Field data first rule.
- References: Core Web Vitals (thresholds unchanged: LCP 2.5 s, INP 200 ms, CLS 0.1; Lighthouse 13 insight audits), performance method and budgets per site type, usability heuristics in own words, conversion patterns, store listing quality. Rubric examples for every rubric check.
- `SKILL.md`: audit steps (sample, field data, lab runs, screenshots at 375, 768, 1280 px, rubric pass) and guardrails mode.
- CI: `scripts/check-content.py` fails when a rubric check has no rubric examples.
- Shared: new framework id `UXH` (Hamu usability heuristics, best practice) in `applicability-matrix.md`. No schema change.

## 0.4.0 (2026-11-19) Phase 2: hamu-accessibility

- `references/checks.md`: 81 `A11Y.` checks over 15 domains. Every WCAG 2.2 level A and AA criterion (55) has a check, with level, WCAG version, default severity, axe-core rule ids and test method. AAA as advisory. Framework mapping rule per law version (EN 301 549 v3.2.1 / v4.1.1, ADA, Section 508). Guardrails pointers per build task.
- References: WCAG 2.2, EN 301 549 (v4.1.1 published September 2026, v3.2.1 still the harmonised version), EAA (Belgian micro-enterprise rule unresolved, treated as likely), WAD (Belgian federal law and BOSA), ADA (Title II dates extended to 2027 and 2028), Section 508.
- `statement.md`: what WAD and EAA ask of an accessibility statement, and a draft template.
- `manual-test-script.md`: page sample and scripts for keyboard, screen reader, zoom and reflow, colour, media, motion, forms.
- `SKILL.md`: audit steps and guardrails mode.
- CI: `scripts/check-content.py` fails when a WCAG 2.2 A/AA criterion has no check.
- Shared: A11Y rows of `applicability-matrix.md` verified and extended. No schema change.

## 0.3.0 (2026-11-19) Phase 1b: hamu-security-privacy readiness and global privacy

- Readiness references (ids and own words only): ISO/IEC 27001:2022, SOC 2 Trust Services Criteria, ISO/IEC 42001:2023, NIST CSF 2.0, HIPAA (current Security Rule, proposed update noted as projected July 2027). Each has a manual checklist for process controls.
- Global privacy references: CCPA/CPRA (thresholds, 2026 regulations on risk assessments, ADMT and cybersecurity audits, GPC display duty), COPPA (2025 amendments, compliance 22 April 2026), PIPEDA (Bill C-36 noted, not law), LGPD, POPIA, Apple and Google Play privacy rules.
- `checks.md`: 9 new checks (SP.CONSENT.GPC, SP.PRIVACY.US-NOTICE, SP.PRIVACY.US-OPTOUT, SP.PRIVACY.COPPA, SP.PRIVACY.LOCAL-OFFICER, SP.MOBILE.ATT, SP.MOBILE.MANIFEST, SP.CERT.NIST-CSF, SP.CERT.CCPA-PROC), 146 in total. Readiness mapping table from Hamu domains to ISO 27001, SOC 2, NIST CSF, HIPAA and ISO 42001 ids, and the steps to build a readiness view.
- `SKILL.md`: reference table and readiness step.
- Shared: `PIPEDA / LGPD / POPIA` split into three framework ids in `applicability-matrix.md`. No schema change.

## 0.2.0 (2026-11-19) Phase 1a: hamu-security-privacy, EU, Belgium and baseline

- `hamu-security-privacy/references/checks.md`: check catalogue with 137 `SP.` checks over 23 domains, with frameworks, default severity, passive/active/code/manual mode, how to test per runtime, guardrails pointers per build task and pointers to other skills.
- Framework reference files with `last_verified` and primary sources: GDPR, GDPR-K, EPRIVACY-BE, GDPR-TRANSFER, BE-CEL, EU-CONSUMER, GPSR, DSA, AI Act, CRA, PLD, Data Act, NIS2-BE, DORA, PSD2, PCI DSS, MDR, ASVS 5.0, OWASP Top 10 (Web 2025, API 2023, Mobile 2024, LLM 2025), MASVS, CIS. Items that could only be checked against secondary sources are marked `verify`.
- `SKILL.md`: audit steps and guardrails mode.
- Shared: SP rows of `applicability-matrix.md` verified (CCPA thresholds, NIS2 size and size-independent cases, CRA scope for SaaS, PLD date, EAA micro definition). Belgian cookie article in `findings.example.json` confirmed (Art. 10/2 Law of 30 July 2018). No schema change.
- Not yet: readiness views (ISO 27001, SOC 2, ISO 42001, HIPAA, NIST CSF) and global privacy laws (CCPA, COPPA, PIPEDA, LGPD, POPIA, app stores). Planned for phase 1b.

## 0.1.0 (2026-11-19) Phase 0: foundation

- Repository set up as a Claude Code plugin marketplace (`hamu`) with one plugin (`hamu-audit`).
- Shared contract: intake (permission question, auto-detection, three scoping questions, guardrails mode), applicability matrix, ownership matrix with overlap decisions, severity and scoring, run protocol with runtime fallbacks, layered report template.
- JSON Schemas for `.audit/context.json` and `.audit/findings/<skill>.json`, with validated examples.
- Scaffolds for five skills: security-privacy, accessibility, performance-ux, seo-visibility, audit-rollup.
- `scripts/sync-shared.sh` to copy the shared contract into each skill, with `--check` for CI.
