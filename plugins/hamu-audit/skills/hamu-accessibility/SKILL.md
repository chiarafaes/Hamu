---
name: hamu-accessibility
description: Audit a website or app for accessibility against WCAG 2.2, EN 301 549, the European Accessibility Act, the Web Accessibility Directive and ADA/Section 508, including the accessibility statement and a manual test script. Use for an accessibility audit, WCAG or EAA check, or for accessibility pointers while building.
---

# hamu-accessibility

Accessibility readiness checks against WCAG 2.2 level AA, with EU and Belgian law on top. Owns every check with prefix `A11Y.`.

> Status: 0.9.0. Tested on a real website in Claude Code and in the Claude app (security and privacy skill). Write this version as `skill_version` in the findings file.

This is a readiness check, not legal advice or a conformance certificate. Never write "compliant" or "WCAG certified". An automated scan alone never proves accessibility.

## Always read first

- `references/_shared/contract/intake.md`
- `references/_shared/contract/run-protocol.md`
- `references/_shared/contract/severity.md`
- `references/_shared/contract/report-template.md`
- `references/_shared/contract/applicability-matrix.md`
- `references/_shared/contract/ownership-matrix.md`
- `references/checks.md` (the check catalogue and framework mapping rule)

Read only the references for frameworks with status `applies` or `likely`:

| Framework id | Reference |
|---|---|
| WCAG22 | `references/wcag22.md` (always) |
| EN301549 | `references/en301549.md` |
| EAA | `references/eaa.md` |
| WAD | `references/wad.md` |
| ADA | `references/ada.md` |
| S508 | `references/s508.md` |
| Statement (WAD, EAA) | `references/statement.md` |
| Manual checks | `references/manual-test-script.md` |

## Pick the mode

- **Audit mode**: the user asks to audit, test or check accessibility of an existing site, app or codebase.
- **Guardrails mode**: the user is building UI. When unsure, ask: "Full audit, or pointers for what you are building now?"

## Audit mode

1. **Intake** per `intake.md`. Reuse `.audit/context.json`. Testing stays passive unless allowed (submitting forms with errors needs permission or a staging site).
2. **Applicability** with `applicability-matrix.md`. WCAG22 always applies. Show the scope line, for example: "Scope: WCAG 2.2 AA, EAA (e-commerce), EN 301 549. Not applicable: WAD, ADA."
3. **Environment.** Detect tools: Playwright, `npx @axe-core/cli`, Lighthouse, browser tools with JS injection. Record `tools_used` and `tools_missing`.
4. **Freshness.** Read `last_verified` of each reference used. Older than 12 months: mark `stale`. `verify` items force `legal_review: true`.
5. **Sample pages** per `manual-test-script.md` (10 to 15 by default, every step of the main journey up to payment).
6. **Automated pass** on each sample page:
   - Claude Code: axe via Playwright with tags `wcag2a, wcag2aa, wcag21a, wcag21aa, wcag22aa`, plus `best-practice` reported as `info`. Run at 1280 px and 320 px widths.
   - Claude app: inject axe-core with the browser JS tool when allowed, else DOM checks from `read_page` with lower confidence.
   - Map axe rule ids to Hamu checks with the "Auto" column in `checks.md`. Group nodes by check and template.
7. **Heuristic and manual pass.** Run every `H` check on the sample. Run the `M` scripts the runtime can perform (keyboard with Playwright, resize, text spacing CSS). Write the rest as `needs_manual` with the script in `detail_technical`. Always include the keyboard and screen reader scripts for the main journey.
8. **Write findings** to `.audit/findings/hamu-accessibility.json` per `finding.schema.json`. Follow the framework mapping rule in `checks.md` (version per law). Keep `pass` findings for coverage. Missing tools give `not_tested`.
9. **Write the report** `.audit/reports/hamu-accessibility.md` per `report-template.md`, with the W3C attribution line. Add a table of criteria new in WCAG 2.2 for readers bound to 2.1.
10. **Statement.** Check A11Y.STATEMENT.*. If the user asks, draft a statement with `statement.md`.
11. **Update** `context.json` `runs[]` and tell the user: score, top 3 actions, what still needs a human test, report path. Suggest the other Hamu skills once, in one line.

### Severity reminders

- Blockers on the main journey (keyboard trap, unlabelled pay button, inaccessible CAPTCHA) are `high`, or `critical` when no alternative exists at all.
- A failed A or AA criterion with a law that applies is at least `medium`.
- AAA is `info`. Best-practice axe rules are `info` or `low`.

## Guardrails mode

1. Read `.audit/context.json`, or run intake once and store it.
2. Pick the build task in "Guardrails pointers by build task" in `checks.md`.
3. Give at most 5 concrete rules, highest severity first, each with its check id. Prefer code the user can paste. Example: "Give the icon-only close button an accessible name: `<button aria-label="Close">` (A11Y.IMG.ICON)."
4. Use the project's design tokens when talking about colour and spacing. Check contrast of the token pairs used.
5. No report files. If the user asks "is this OK now?", run the related checks in audit mode on that component.

## Overlaps

Follow `ownership-matrix.md`. This skill owns alt text, captions, tap target size, reflow at 320 px, form labels and errors, keyboard and focus on the cookie banner, the lang attribute and plain language for cognitive access. Use "Pointers to other skills" in `checks.md` for the rest.
