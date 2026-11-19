---
last_verified: 2026-11-19
---

# Report template

Layered report: executive layer first (plain language, no jargon), technical layer below. Same structure for a single skill report and the roll-up; the roll-up adds the cross-skill sections marked (roll-up).

Writing rules:
- Report language from `context.report_language`. Framework ids and check ids stay as they are.
- Plain punctuation. No em-dashes. No filler ("It is important to note").
- Every claim in the executive layer points to a finding id in the technical layer.
- Say "readiness" and "gaps", never "compliant" or "certified".

---

```markdown
# <Target name>: <Skill or "Hamu audit"> report

Audit id: <audit_id> · Date: <date> · Mode: passive/active · Runtime: <runtime>
> This is a readiness check, not legal advice or a certification. Items marked "legal review" need confirmation by a lawyer.

## 1. Summary
<3-5 sentences in plain language: overall state, biggest risk, what to do first.>

| Area | Score | Critical | High | Medium | Low | Not tested |
|---|---|---|---|---|---|---|
| ... |

**Verdict:** Go / Go with conditions / No-go  (pre-launch and roll-up only)

## 2. Top actions
<Max 10, ordered by severity then effort. Each: one line, owner role, effort S/M/L, finding id.>

1. Block analytics until consent (high, S) · SP.CONSENT.PRE-TRACK#1a2b3c4d

## 3. Scope
- Target(s), languages, platforms
- Applicable frameworks with status and reason (table)
- Not applicable, and why
- Permission and testing mode

## 4. Findings
Grouped by area (domain), sorted by severity. For each finding:

### <title> · <severity> · <status>
**What this means:** <summary_plain>
**Technical detail:** <detail_technical>
**Evidence:** <location + snippet or artifact link>
**Frameworks:** GDPR Art. 32 (requirement) · ASVS V3.4.1 · ISO 27001 A.8.24 (evidence)
**Fix:** <summary> + steps + code example · Effort: S
**Id:** <id> · Confidence: high · Method: automated

## 5. Needs confirmation
Low-confidence and `needs_manual` items, each with a short test script a human can follow.

## 6. Framework coverage
Per applicable framework: checks run, pass, fail, not tested. Certification readiness tables (SOC 2 / ISO 27001 / ISO 42001 / HIPAA) only when requested, with the note that process controls cannot be verified from code or URL.

## 7. Not tested and limitations
Tools missing, pages not reached, checks that need access the audit did not have. Stale references.

## 8. Changes since last audit (re-audit only)
Fixed / new / still open, by finding id.

## 9. Cross-skill overview (roll-up)
Merged duplicates, findings that affect several areas, combined score and verdict.

## Appendix
Method, tools and versions, reference files with last_verified dates, glossary of framework ids.
```

## Output formats

| Format | Who writes it | Notes |
|---|---|---|
| Markdown | every skill | Always. `.audit/reports/<skill>.md` |
| JSON | every skill | Always. `.audit/findings/<skill>.json` |
| HTML dashboard | roll-up | Self-contained single file, no external requests, works offline. Filters by severity, area, framework. |
| Word / PDF | roll-up | Client deliverable from the same content. Executive layer first, findings as tables, appendix with evidence. |

A single skill can still produce HTML or Word/PDF: run the roll-up on just that skill's findings.
