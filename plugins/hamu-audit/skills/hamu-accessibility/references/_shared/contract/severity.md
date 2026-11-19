---
last_verified: 2026-11-19
---

# Severity, confidence and scoring

## Severity

Pick the highest level whose description fits. Severity is about consequence, not effort.

| Level | Meaning | Examples |
|---|---|---|
| critical | Active exploitability with real impact, or a clear legal breach likely to cause enforcement or claims now. Fix before launch / immediately. | Exposed secrets or admin panel, SQL injection, card data on own server without PCI scope, health data over plain HTTP, no consent mechanism at all with ad pixels firing |
| high | Serious risk or clear non-compliance with a law that applies. | Tracking before consent, missing withdrawal info on B2C shop, keyboard trap in checkout, missing privacy policy, outdated component with known exploited CVE |
| medium | Weakness or partial non-compliance, needs a specific condition to hurt. | Missing HSTS or CSP, contrast failures on secondary text, LCP 2.5-4 s, missing accessibility statement, canonical errors on some pages |
| low | Best-practice gap, small impact. | Missing security.txt, meta description too long, minor heading order issue |
| info | Observation or opportunity, no requirement broken. | A/B test idea, schema type that could be added, GEO mention opportunity |

Modifiers:
- **Legal applies**: a finding mapped as `requirement` to a framework with status `applies` cannot be lower than `medium`.
- **Readiness only**: a finding that only maps to a `readiness_only` certification is capped at `high`.
- **Scale**: if the issue affects the main conversion path (checkout, signup, contact) raise one level, max high unless it already qualifies as critical.

## Confidence

| Level | Use when |
|---|---|
| high | Directly observed with evidence (header, request, code line, tool output) |
| medium | Strong indication, one assumption (e.g. detected from a sample of pages) |
| low | Heuristic or inferred, needs human confirmation |

Low-confidence findings never count as `fail` in scoring. They go to "Needs confirmation" in the report.

## Method

- `automated`: tool or deterministic check.
- `heuristic`: judgement by the model on observed content (content quality, CTA clarity).
- `code_review`: read from source code.
- `manual_required`: cannot be verified by the skill (screen reader flow, process controls, contracts with processors). Report as a task for a human, with a short test script.

## Scoring (used by skills alone and by the roll-up)

Per skill, per area, start at 100 and subtract per `fail` finding with confidence medium or high:

| Severity | Points |
|---|---|
| critical | 25 |
| high | 10 |
| medium | 4 |
| low | 1 |
| info | 0 |

`warn` counts half. Floor at 0. Report the score with the number of checks run and not tested, so a high score on few checks does not look like a clean bill of health.

## Go / no-go (roll-up and pre-launch goal)

- **No-go**: any open critical, or any high mapped as `requirement` to a framework with status `applies`.
- **Go with conditions**: open highs that are best practice or readiness only, with an owner and date.
- **Go**: no criticals, no legal highs.

Always state: "This is a readiness check, not legal advice or a certification."
