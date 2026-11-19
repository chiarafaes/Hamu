# Changelog

## 0.1.0 (2026-11-19) Phase 0: foundation

- Repository set up as a Claude Code plugin marketplace (`hamu`) with one plugin (`hamu-audit`).
- Shared contract: intake (permission question, auto-detection, three scoping questions, guardrails mode), applicability matrix, ownership matrix with overlap decisions, severity and scoring, run protocol with runtime fallbacks, layered report template.
- JSON Schemas for `.audit/context.json` and `.audit/findings/<skill>.json`, with validated examples.
- Scaffolds for five skills: security-privacy, accessibility, performance-ux, seo-visibility, audit-rollup.
- `scripts/sync-shared.sh` to copy the shared contract into each skill, with `--check` for CI.
