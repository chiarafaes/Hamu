---
name: hamu-audit-rollup
description: Merge findings from the Hamu audit skills into one deduplicated report with a combined score, go/no-go verdict, HTML dashboard and Word/PDF deliverable. Use after one or more Hamu audits, or to turn a single Hamu audit into a client report.
---

# hamu-audit-rollup

Merges the findings of the Hamu audit skills into one report: deduplicated, scored, with a go / no-go verdict, a comparison with the previous audit, a Markdown report and an accessible single-file HTML dashboard. PDF comes from the dashboard. Word only on request.

> Status: 0.7.0 (phase 5). Tested on fixtures, not yet on real audits (phase 6).

The merging, scoring, verdict and diff are done by a script, not by judgement, so the same input always gives the same report. Do not recompute scores by hand.

## Always read first

- `references/_shared/contract/severity.md` (scoring and verdict rules the script implements)
- `references/_shared/contract/report-template.md` (sections the renderers follow)
- `references/_shared/contract/ownership-matrix.md` (why pointer findings merge into the owner)
- `references/_shared/contract/run-protocol.md` (`.audit/` layout and history)

## Steps

1. **Check inputs.** `.audit/context.json` and at least one file in `.audit/findings/` must exist. If not, tell the user which Hamu skill to run first. Findings from an older audit belong in `.audit/history/<audit_id>/`, the script refuses mixed audit ids.
2. **Validate** (when this repo's validator and `jsonschema` are available): `python3 scripts/validate.py .audit`. Fix the skill output before rolling up.
3. **Run the roll-up** (Python 3.9 or newer, standard library only):
   ```
   python3 <skill-dir>/scripts/rollup.py --audit-dir .audit
   ```
   Options: `--previous .audit/history/<id>` to choose the audit to compare with (default: the latest in history), `--skills a,b` to include only some skills, `--no-render` for JSON only.
   Output in `.audit/reports/`: `hamu-audit.json` (matches `rollup.schema.json`), `hamu-audit.md`, `hamu-audit.html`.
4. **Write the summary sentences.** The script fills every section except the plain-language summary paragraph. Add 3 to 5 sentences to section 1 of `hamu-audit.md`: overall state, biggest risk, what to do first. Every claim points to a finding id. Keep the verdict and scores exactly as the script wrote them.
5. **PDF** (when asked): print the HTML dashboard. It has a print stylesheet that hides filters and opens all details.
   - Claude Code with Playwright: open `hamu-audit.html`, `page.emulateMedia({ media: "print" })`, `page.pdf({ format: "A4", printBackground: true })`.
   - Claude app or no Playwright: tell the user to open the HTML file and use Print, Save as PDF.
6. **Word** (only when asked): build a `.docx` from `hamu-audit.md` with the document skill available in the environment, or with a temporary tool the user agrees to (for example `pipx run` of a Markdown to docx converter). Do not add a permanent dependency. Keep the executive layer first.
7. **Tell the user**: verdict, overall score, top 3 actions, what changed since the last audit, and where the files are. Say the score counts only what was tested, and name skills that did not run.

## How the script decides

| Topic | Rule |
|---|---|
| Merge | Findings with the same `id` are one issue. A pointer finding (`reported_by` set) merges into the owner's finding: evidence, frameworks, impact and related ids are combined, `reported_in` lists every skill that saw it. If the owner skill did not run, the pointer finding stays as the finding. |
| Area score | Per domain (`SP.CONSENT`, `A11Y.FORM` ...): 100 minus critical 25, high 10, medium 4, low 1 per open `fail`, `warn` counts half, floor 0. Low-confidence findings are not scored. |
| Skill score | Mean of its area scores. Areas with only `not_tested` findings are left out. Skills that did not run have no score. |
| Overall score | Mean of the skill scores of skills that ran. |
| Verdict | No-go: any open critical, or any open high mapped as `requirement` to a framework with status `applies`. Go with conditions: other open highs. Go: neither. Low-confidence findings never block. |
| Diff | By finding id against the previous audit: fixed, new, still open. A previous finding whose owner skill did not run this time is "not rechecked", never "fixed". |
| Top actions | Open findings (not low confidence, not info), by severity, then effort S, M, L. Max 10. |

## The dashboard

- One file, no external requests (strict Content Security Policy), works offline.
- Executive layer first: verdict, scores per area, top actions. Findings below with filters on severity, area, framework, status and a text search. Technical detail in expandable sections.
- Light and dark theme follow the system setting. Tested with axe-core (WCAG 2.2 AA) at 375 and 1280 px in both themes.
- Neutral colour tokens on `:root`. When a brand kit exists for the report owner, change only those tokens.
- UI labels are in English. Finding text is in the report language the skills used.

## A single skill as a client report

Run the roll-up with `--skills <that-skill>`. The other skills show as "not run", which is honest about coverage.
