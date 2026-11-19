# Changelog

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
