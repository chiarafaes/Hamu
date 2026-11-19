---
name: hamu-security-privacy
description: Audit a website, web app, API or mobile app for security and privacy readiness: GDPR and Belgian cookie rules, EU consumer law, AI Act transparency, NIS2, CRA, PCI DSS, OWASP ASVS, plus SOC 2, ISO 27001, ISO 42001 and HIPAA readiness. Use for a security or privacy audit, compliance check, GDPR check, cookie check, or for security and privacy pointers while building.
---

# hamu-security-privacy

Security and privacy readiness checks with EU and Belgian depth. Owns every check with prefix `SP.`.

> Status: 0.3.0 (phase 1). EU and Belgian law, technical baseline, global privacy laws, app store rules and certification readiness views are in place. Not yet tested on real targets (phase 6).

This is a readiness check, not legal advice or a certification. Never write "compliant" or "certified".

## Always read first

- `references/_shared/contract/intake.md`
- `references/_shared/contract/run-protocol.md`
- `references/_shared/contract/severity.md`
- `references/_shared/contract/report-template.md`
- `references/_shared/contract/applicability-matrix.md`
- `references/_shared/contract/ownership-matrix.md`
- `references/checks.md` (the check catalogue)

Read a framework reference file only when that framework has status `applies` or `likely`.

| Framework id | Reference |
|---|---|
| GDPR | `references/gdpr.md` |
| GDPR-K | `references/gdpr-k.md` |
| EPRIVACY-BE | `references/eprivacy-be.md` |
| GDPR-TRANSFER | `references/gdpr-transfer.md` |
| BE-CEL | `references/be-cel.md` |
| EU-CONSUMER | `references/eu-consumer.md` |
| GPSR | `references/gpsr.md` |
| DSA | `references/dsa.md` |
| AIACT, AIACT-50 | `references/aiact.md` |
| CRA | `references/cra.md` |
| PLD | `references/pld.md` |
| DATA-ACT | `references/data-act.md` |
| NIS2-BE | `references/nis2-be.md` |
| DORA | `references/dora.md` |
| PSD2 | `references/psd2.md` |
| PCI-DSS | `references/pci-dss.md` |
| MDR | `references/mdr.md` |
| ASVS5 | `references/asvs5.md` |
| OWASP-T10 | `references/owasp-t10.md` |
| MASVS | `references/masvs.md` |
| CIS | `references/cis.md` |
| CCPA | `references/ccpa.md` |
| COPPA | `references/coppa.md` |
| PIPEDA | `references/pipeda.md` |
| LGPD | `references/lgpd.md` |
| POPIA | `references/popia.md` |
| APPLE-ASRG, GOOGLE-PLAY | `references/app-stores.md` |
| ISO27001 (readiness) | `references/iso27001.md` |
| SOC2 (readiness) | `references/soc2.md` |
| ISO42001 (readiness) | `references/iso42001.md` |
| NIST-CSF (readiness) | `references/nist-csf.md` |
| HIPAA | `references/hipaa.md` |

## Pick the mode

- **Audit mode**: the user asks to audit, scan, check or review an existing site, app or codebase.
- **Guardrails mode**: the user is building something and asks for security or privacy advice, or this skill is triggered while code is being written. When unsure, ask one question: "Full audit, or pointers for what you are building now?"

## Audit mode

1. **Intake.** Follow `intake.md`. Reuse `.audit/context.json` when valid. Ask the permission question. Never assume permission for active tests.
2. **Applicability.** Resolve frameworks with `applicability-matrix.md`. Show the one-line scope summary.
3. **Environment.** Detect the runtime (`claude_code` or `claude_app`) and which tools exist: `curl`, `openssl`, `dig`, `npx`, `semgrep`, `gitleaks`, `osv-scanner`, `npm audit`, Playwright, browser tools. Record `tools_used` and `tools_missing`.
4. **Freshness.** Read `last_verified` of every reference file used. Older than 12 months: mark `stale` and add the line from `run-protocol.md`. Anything marked `verify` in a reference may only be used with `legal_review: true` and confidence at most medium.
5. **Collect evidence once**, then run checks on it. Order:
   1. Fetch the home page and up to 20 key pages (legal pages, signup, checkout entry, contact, product page) at max 1 request per second. Keep headers, HTML, cookies and the network log of a clean first visit (no consent).
   2. Interact with the consent banner: reject in one clean profile, accept in another. Record requests and storage after each.
   3. Fetch public JS bundles once and scan them for secrets and library versions.
   4. DNS lookups for the apex domain.
   5. Codebase (when given): lockfiles, framework config, auth and route handlers, Dockerfile and IaC, mobile manifests.
6. **Run checks** from `checks.md`, domain by domain, for applicable frameworks plus the baseline. Skip `A` (active) checks unless `owner_confirmed` and `active_testing_allowed` are both true. Write `needs_manual` for `M` checks with a short test script for a human.
7. **Write findings** to `.audit/findings/hamu-security-privacy.json` per `finding.schema.json`:
   - `id` = `check_id` + `#` + first 8 hex characters of sha256(check_id + normalised location).
   - One finding per check per location group. Keep `pass` findings so coverage is visible.
   - Map frameworks only to those with status `applies` or `likely`. Use the relation from `checks.md`.
   - Set `legal_review: true` whenever the outcome depends on legal interpretation or on a `verify` item.
   - Every missing tool gives `not_tested` findings for the checks that needed it. No silent gaps.
   - Validate with `python3 scripts/validate.py .audit` when this repo's script and `jsonschema` are available, or with `ajv`. Fix and rewrite on errors.
8. **Write the report** `.audit/reports/hamu-security-privacy.md` per `report-template.md`: executive layer first, then technical layer. Add the OWASP attribution lines from `asvs5.md` and `owasp-t10.md` when OWASP ids are cited.
9. **Update** `context.json` `runs[]`.
10. **Readiness views.** Only for targets in `certification_targets`: follow "How a readiness view is built" in `checks.md` and the manual checklist in the matching reference file. Never write a percentage toward certification.
11. **Tell the user**: score, verdict if pre-launch, top 3 actions, report path. Suggest the other Hamu skills once, in one line.

### Severity reminders

- A finding mapped as `requirement` to a framework with status `applies` is at least `medium`.
- Readiness-only findings are capped at `high`.
- Raise one level when it hits checkout, signup or contact (max `high` unless already critical).
- Low confidence never counts as `fail` in the score.

### What this skill never does

- Submit real forms, place orders, or log in to production with real accounts.
- Scan ports, brute force, enumerate subdomains or fuzz without active permission and scope.
- Copy text from ISO/IEC, AICPA, PCI SSC or CIS documents. OWASP: ids and paraphrase only.
- Store secrets in evidence. Show the first 4 characters and the location only.

## Guardrails mode

1. Read `.audit/context.json`. If missing, run intake once (permission question skipped, it is the user's own build) and store it.
2. Match the build task to the table "Guardrails pointers by build task" in `checks.md`.
3. Give at most 5 pointers, highest severity first. Each pointer is one concrete rule for the code or design being written, with its check id. Example:
   - "Load the analytics script only after the user accepts analytics cookies, and keep it off after reject (SP.CONSENT.PRE-TRACK)."
4. No report files, no findings JSON.
5. If the user asks "is this OK now?", run only the related checks in audit mode and answer with pass or the remaining gaps.

## Overlaps

Follow `ownership-matrix.md`. When this skill notices something another skill owns (banner keyboard access, layout shift, analytics measurement), use the "Pointers to other skills" table in `checks.md` and write a pointer finding only when running alone.
