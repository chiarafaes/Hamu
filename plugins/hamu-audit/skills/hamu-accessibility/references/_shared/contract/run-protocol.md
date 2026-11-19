---
last_verified: 2026-11-19
---

# Run protocol

How every Hamu skill runs, stores output and degrades when tools are missing.

## Folder layout

All state lives in `.audit/` at the project root (codebase) or the working folder (URL audit). Add `.audit/` to `.gitignore` unless the user wants reports in version control.

```
.audit/
  context.json                 shared scope, written by the first skill (context.schema.json)
  findings/
    hamu-security-privacy.json (finding.schema.json)
    hamu-accessibility.json
    hamu-performance-ux.json
    hamu-seo-visibility.json
  evidence/<skill>/            screenshots, raw tool output, HAR excerpts (redacted)
  reports/
    <skill>.md                 standalone report per skill
    hamu-audit.md              roll-up (markdown)
    hamu-audit.html            roll-up dashboard
    hamu-audit.docx / .pdf     roll-up client deliverable
  history/<audit_id>/          previous findings, for re-audit diffs
```

Before a new run of the same skill, move the previous findings file to `history/<old audit_id>/`. The roll-up uses it to show fixed / new / still open.

## Steps (every skill)

1. **Intake** per `intake.md`. Reuse `context.json` when valid.
2. **Environment check.** Detect runtime and available tools. Record `tools_used` and `tools_missing`.
3. **Freshness check.** Read `last_verified` from every reference file the run uses. If older than 12 months, set `stale: true` and add a line to the report: "Reference X last verified on DATE. Rules may have changed."
4. **Checks.** Run the skill's checks for applicable frameworks only. Owner checks fully, non-owner checks as pointers (see `ownership-matrix.md`).
5. **Write findings** to `.audit/findings/<skill>.json`. Validate against `finding.schema.json` when a validator is available (Python `jsonschema`, or `ajv`). Fix and rewrite on errors.
6. **Write report** `.audit/reports/<skill>.md` per `report-template.md`.
7. **Update** `context.json` `runs[]`.
8. **Tell the user**: score, go/no-go if relevant, top 3 actions, where the report is. Suggest the other Hamu skills only once, in one line, if they have not run.

## Runtimes and degradation

| Capability | Claude Code (local) | Claude app / cloud | Fallback |
|---|---|---|---|
| Fetch pages and headers | `curl`, Playwright | Browser tools (Claude in Chrome, built-in browser), WebFetch | Ask the user to paste headers or HTML |
| Lighthouse / CWV lab data | `npx lighthouse` | Browser + PageSpeed Insights page | Mark `PX.CWV.*` as not_tested, explain how to run |
| Field CWV (CrUX) | PSI API / CrUX API if key available | PageSpeed Insights page in browser | not_tested |
| Accessibility engine | `@axe-core/cli` or axe via Playwright, pa11y | Inject axe-core via browser JS tool if allowed | Manual checks from DOM, lower confidence |
| Dependency vulnerabilities | `npm audit`, `pip-audit`, `osv-scanner` | Read lockfiles, match against known advisories with lower confidence | not_tested |
| Static analysis | `semgrep`, `gitleaks` / `trufflehog` | Pattern search in code | Lower confidence |
| TLS details | `openssl s_client`, `testssl.sh` | Browser security info, SSL Labs page in browser | Header-level checks only |
| DNS (SPF, DKIM, DMARC) | `dig` | Web DNS lookup page in browser | not_tested |
| AI visibility (GEO) | Prompt set run by the user or via connected tools | Same | Provide the prompt set and a tracking sheet |

Rules:
- Never install tools without telling the user. Prefer `npx` / `pipx run` so nothing stays installed.
- In the cloud workspace, shell network access is usually restricted to package registries. Use browser tools for the target site; do not retry blocked requests with other commands.
- Every check that could not run because of a missing tool is written as a finding with `status: not_tested`, so the report's coverage is honest.

## Safety

- Passive by default. Active tests only with `permission.active_testing_allowed=true`, and then never against production without explicit scope.
- Respect rate limits: max 1 request per second on a target unless the owner allows more. Crawl cap 200 URLs by default.
- Never submit real forms on production (no orders, no contact form spam). Inspect them.
- Evidence is redacted: no passwords, tokens, API keys, session ids, full personal data. Show the first 4 characters of a secret and its location only.
- No copyrighted control text from ISO, AICPA, PCI SSC. Ids and own-words paraphrase only.

## Guardrails mode

When the user is building, not auditing:
1. Read `context.json` (run intake once if missing).
2. For the current task, pick the relevant checks from the skill's `checks.md` by domain.
3. Give at most 5 pointers, highest severity first, as concrete code or design rules. No report files.
4. If the user asks "is this OK now?", run only the related checks in audit mode.
