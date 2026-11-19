# Hamu: instructions for Claude

Hamu is a Claude Code plugin marketplace with one plugin, `hamu-audit`: five skills that audit websites, web apps and mobile apps. Owner: Hamu (VAT BE 1008.566.012). Read this file before any change.

## Structure (do not change without asking)

- 4 audit skills that work alone + 1 roll-up that merges them:
  - `hamu-security-privacy` (prefix `SP.`)
  - `hamu-accessibility` (prefix `A11Y.`)
  - `hamu-performance-ux` (prefix `PX.`)
  - `hamu-seo-visibility` (prefix `SEO.`)
  - `hamu-audit-rollup` (Markdown, self-contained HTML dashboard, Word/PDF, go/no-go)
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
- [ ] Phase 2: hamu-accessibility
- [ ] Phase 3: hamu-performance-ux
- [ ] Phase 4: hamu-seo-visibility
- [ ] Phase 5: hamu-audit-rollup (merge, dedupe, scoring, re-audit diff, renderers)
- [ ] Phase 6: test on 2-3 real targets (URL and codebase, Claude Code and Claude app)
- [ ] Phase 7: publish (marketplace install test, README install line, `license` issue label)

Open items:
- `verify` markers in the hamu-security-privacy references (Belgian article numbers for the withdrawal function and Book XII, AI Omnibus OJ number, CyFun milestones, GBA/APD cookie lifetime). Check against the Belgian Official Gazette, EUR-Lex and CCB before phase 6. Phase 1b adds: LGPD incident deadline wording (business days), HHS tracking guidance status, app store guideline numbers (re-check each run).
- EAA micro-enterprise treatment in Belgium: sources conflict. Settle in phase 2.

## Working agreements

- For bigger tasks: short plan first, then build.
- Ask when information is missing instead of assuming.
- Nothing gets published or released without explicit approval from the owner.
- Work on a branch, open a PR. Do not push to `main` directly after the initial commit.
