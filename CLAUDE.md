# Hamu: instructions for Claude

Hamu is a Claude Code plugin marketplace with one plugin, `hamu-audit`: five skills that audit websites, web apps and mobile apps. Owner: Hamu (VAT BE 1008.566.012). Read this file before any change.

## Structure (do not change without asking)

- 4 audit skills that work alone + 1 roll-up that merges them:
  - `hamu-security-privacy` (prefix `SP.`)
  - `hamu-accessibility` (prefix `A11Y.`)
  - `hamu-performance-ux` (prefix `PX.`)
  - `hamu-seo-visibility` (prefix `SEO.`)
  - `hamu-audit-rollup` (Markdown, self-contained HTML dashboard, Word/PDF, go/no-go)
- Roll-up logic lives in `skills/hamu-audit-rollup/scripts/` (standard library only, Python 3.9+). Change it together with `tests/rollup/` and run `python3 -m unittest discover -s tests/rollup`. Regenerate fixtures with `tests/rollup/make_fixtures.py`.
- Source of truth for shared rules: `plugins/hamu-audit/shared/`. Never edit `skills/*/references/_shared/` by hand. After changing shared files run `scripts/sync-shared.sh`, then `scripts/sync-shared.sh --check`, `python3 scripts/validate.py` and `python3 scripts/check-content.py`. CI runs the same checks on every PR.
- Every skill follows the shared contract: `intake.md`, `applicability-matrix.md`, `ownership-matrix.md`, `severity.md`, `run-protocol.md`, `report-template.md`, and writes JSON matching `finding.schema.json` / `context.schema.json`.
- One owner per check. Overlaps are decided in `ownership-matrix.md`. Add a row there before adding a check that another skill could also notice.
- Breaking schema changes bump `schema_version` and are listed in CHANGELOG.md.

## Product decisions

- Priority: EU and Belgium first (GDPR, Belgian cookie rules / GBA-APD, EU consumer law, Belgian Code of Economic Law, EAA, NIS2-BE, CRA, AI Act), then global (US, CA, BR, ZA).
- Certifications (SOC 2, ISO 27001, ISO 42001, HIPAA, PCI DSS) are **readiness** checks only. Never write "compliant" or "certified". Every report carries the disclaimer.
- Intake: permission question + auto-detection + 3 scoping questions (where, what, who/why). Reuse `.audit/context.json`.
- Passive testing by default. Active tests only with `owner_confirmed` and `active_testing_allowed`.
- Reports are layered: plain-language executive layer first, technical layer below.
- Two modes: audit and guardrails (max 5 pointers while building).
- Must work in Claude Code (local tools: Lighthouse, axe, Semgrep, npm audit, osv-scanner) and degrade in the Claude app (browser tools). Missing tools produce `not_tested` findings, never silent gaps.

## Content rules

- Every framework reference file has front matter with `last_verified` (date) and `sources` (primary URLs). Verify thresholds, dates and article numbers against primary sources (EUR-Lex, Belgian Staatsblad/Moniteur, GBA/APD, CCB, W3C, OWASP) before writing them. Mark anything unverified as `verify`.
- Never copy text from ISO/IEC, AICPA or PCI SSC documents. Ids and own-words descriptions only.
- OWASP is CC BY-SA: reference ids and paraphrase, do not copy text (our content is CC BY-NC-SA).
- WCAG: success criterion number and short name, with attribution.
- Writing style: plain punctuation, no em-dashes, no AI filler phrases, short sentences.

## License

- Code, schemas, scripts, SKILL.md: PolyForm Noncommercial 1.0.0 (`LICENSE.md`).
- Reference content: CC BY-NC-SA 4.0 (`LICENSE-CONTENT.md`).
- Free for noncommercial use. Nobody may sell, repackage, or use Hamu in paid work without a license. License requests go via GitHub issues labelled `license`.

## Phase plan

- [x] Phase 0: shared contract, schemas, scaffolds, licensing (0.1.0)
- [x] Phase 1a: hamu-security-privacy checks.md, EU/BE and baseline references, audit + guardrails steps (0.2.0)
- [x] Phase 1b: hamu-security-privacy readiness (ISO 27001, SOC 2, ISO 42001, HIPAA, NIST CSF) and global privacy (CCPA, COPPA, PIPEDA, LGPD, POPIA, app stores) (0.3.0)
- [x] Phase 2: hamu-accessibility (0.4.0)
- [x] Phase 3: hamu-performance-ux (0.5.0)
- [x] Phase 4: hamu-seo-visibility (0.6.0)
- [x] Phase 5: hamu-audit-rollup (merge, dedupe, scoring, re-audit diff, renderers) (0.7.0)
- [x] Phase 6: test on real targets in Claude Code (0.8.0). Claude app run pending, see `testing/claude-app-test.md`.
- [ ] Phase 7: publish (marketplace install test, README install line, `license` issue label)

Open items (checked 2026-11-19, phase 6):
- Belgian transposition of the online withdrawal function (Chamber doc. 56K1532): not published yet per secondary sources. Re-check the Belgian Official Gazette before citing a Belgian article.
- GBA/APD maximum cookie and consent lifetime: no fixed number found. Treated as warn plus legal review.
- CyFun milestones 2026 to 2028 and Book XII article numbers: still verify.
- EN 301 549 v4.1.1: watch for its Official Journal citation, then update `en301549.md`.
- AI crawler user agents and robots.txt behaviour change often: re-check `ai-search.md` against vendor pages before each release.

## Working agreements

- For bigger tasks: short plan first, then build.
- Ask when information is missing instead of assuming.
- Nothing gets published or released without explicit approval from the owner.
- Work on a branch, open a PR. Do not push to `main` directly after the initial commit.
