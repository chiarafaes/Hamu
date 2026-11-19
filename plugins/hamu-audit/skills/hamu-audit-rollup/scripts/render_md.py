"""Render a Hamu roll-up dict as Markdown, following report-template.md."""

SKILL_NAMES = {
    "hamu-security-privacy": "Security and privacy",
    "hamu-accessibility": "Accessibility",
    "hamu-performance-ux": "Performance and UX",
    "hamu-seo-visibility": "SEO and AI visibility",
}
VERDICT_TEXT = {"go": "Go", "go_with_conditions": "Go with conditions", "no_go": "No-go"}
DISCLAIMER = (
    "This is a readiness check, not legal advice or a certification. "
    'Items marked "legal review" need confirmation by a lawyer.'
)


def cell(value):
    """Make a value safe inside a Markdown table cell."""
    text = "" if value is None else str(value)
    return text.replace("\\", "\\\\").replace("|", "\\|").replace("\n", " ").strip()


def inline(value):
    text = "" if value is None else str(value)
    return text.replace("\n", " ").strip()


def fw_label(fw):
    parts = [fw.get("id", "")]
    if fw.get("ref"):
        parts.append(fw["ref"])
    label = " ".join(parts)
    return f"{label} ({fw.get('relation', '')})"


def render(r):
    t = r.get("target", {})
    o = r["overall"]
    lines = []
    add = lines.append

    add(f"# {inline(t.get('name') or 'Target')}: Hamu audit report")
    add("")
    mode = "active" if r["testing"].get("active_testing_allowed") else "passive"
    add(f"Audit id: {r['audit_id']} · Generated: {r['generated_at']} · Mode: {mode}")
    add("")
    add(f"> {DISCLAIMER}")
    add("")

    # 1. Summary
    add("## 1. Summary")
    add("")
    add(f"**Verdict:** {VERDICT_TEXT[o['verdict']]} · **Overall score:** {o['score'] if o['score'] is not None else 'n/a'}")
    add("")
    for reason in o["reasons"][:5]:
        add(f"- {inline(reason)}")
    add("")
    add("| Area | Score | Critical | High | Medium | Low | Checks run | Not tested |")
    add("|---|---|---|---|---|---|---|---|")
    for s in r["skills"]:
        if not s["ran"]:
            add(f"| {SKILL_NAMES[s['skill']]} | not run | | | | | | |")
            continue
        sev = s["open_by_severity"]
        add(
            f"| {SKILL_NAMES[s['skill']]} | {s['score'] if s['score'] is not None else 'n/a'} | "
            f"{sev['critical']} | {sev['high']} | {sev['medium']} | {sev['low']} | {s['checks_run']} | {s['not_tested']} |"
        )
    add("")
    add("Scores start at 100 per area and drop per open finding (critical 25, high 10, medium 4, low 1, warn counts half). "
        "Low-confidence findings are not scored. A high score on few checks is not a clean bill of health.")
    add("")

    # 2. Top actions
    add("## 2. Top actions")
    add("")
    if not r["top_actions"]:
        add("No open findings above info level.")
    for i, a in enumerate(r["top_actions"], 1):
        effort = a["effort"] or "?"
        add(f"{i}. {inline(a['fix'] or a['title'])} ({a['severity']}, {effort}) · {a['id']}")
    add("")

    # 3. Scope
    add("## 3. Scope")
    add("")
    urls = ", ".join(t.get("urls", []) or []) or "n/a"
    add(f"- Target: {inline(t.get('name'))} ({t.get('type', 'n/a')}), {inline(urls)}")
    if t.get("languages"):
        add(f"- Languages: {', '.join(t['languages'])}")
    add(f"- Testing: {mode}, owner confirmed: {'yes' if r['testing'].get('owner_confirmed') else 'no'}")
    add("")
    add("| Framework | Status | Reason |")
    add("|---|---|---|")
    for fw in r["frameworks"]:
        add(f"| {cell(fw['id'])} | {cell(fw['status'])} | {cell(fw['reason'])} |")
    add("")

    # 4. Findings
    add("## 4. Findings")
    add("")
    shown = [f for f in r["findings"] if f["status"] in ("fail", "warn") and f["confidence"] != "low"]
    if not shown:
        add("No open findings.")
    for skill in SKILL_NAMES:
        group = [f for f in shown if f["owner_skill"] == skill]
        if not group:
            continue
        add(f"### {SKILL_NAMES[skill]}")
        add("")
        for f in group:
            add(f"#### {inline(f['title'])} · {f['severity']} · {f['status']}")
            add("")
            add(f"**What this means:** {inline(f['summary_plain'])}")
            add("")
            add(f"**Technical detail:** {inline(f['detail_technical'])}")
            add("")
            for e in f.get("evidence", [])[:5]:
                snippet = f": `{inline(e['snippet'])[:200]}`" if e.get("snippet") else ""
                add(f"- Evidence ({e['type']}) {inline(e['location'])}{snippet}")
            if f.get("evidence"):
                add("")
            if f.get("frameworks"):
                add("**Frameworks:** " + " · ".join(inline(fw_label(x)) for x in f["frameworks"]))
                add("")
            fix = f.get("fix") or {}
            if fix:
                add(f"**Fix:** {inline(fix.get('summary'))} · Effort: {fix.get('effort', '?')}")
                for step in fix.get("steps", []):
                    add(f"- {inline(step)}")
                add("")
            flags = []
            if f.get("legal_review"):
                flags.append("legal review")
            if len(f.get("reported_in", [])) > 1:
                flags.append("also reported by " + ", ".join(s for s in f["reported_in"] if s != f["owner_skill"]))
            add(f"Id: {f['id']} · Confidence: {f['confidence']} · Method: {f['method']}"
                + (" · " + "; ".join(flags) if flags else ""))
            add("")

    # 5. Needs confirmation
    add("## 5. Needs confirmation")
    add("")
    by_id = {f["id"]: f for f in r["findings"]}
    if not r["needs_confirmation"]:
        add("Nothing to confirm.")
    for fid in r["needs_confirmation"]:
        f = by_id[fid]
        add(f"- **{inline(f['title'])}** ({f['status']}, confidence {f['confidence']}) · {fid}")
        add(f"  {inline(f['detail_technical'])[:600]}")
    add("")

    # 6. Framework coverage
    add("## 6. Framework coverage")
    add("")
    add("| Framework | Status | Findings | Pass | Fail | Warn | Manual | Not tested |")
    add("|---|---|---|---|---|---|---|---|")
    for fw in r["frameworks"]:
        add(f"| {cell(fw['id'])} | {fw['status']} | {fw['findings']} | {fw['pass']} | {fw['fail']} | {fw['warn']} | {fw['needs_manual']} | {fw['not_tested']} |")
    add("")

    # 7. Not tested and limitations
    lim = r["limitations"]
    add("## 7. Not tested and limitations")
    add("")
    add(f"- Skills not run: {', '.join(lim['skills_not_run']) or 'none'}")
    add(f"- Tools missing: {', '.join(lim['tools_missing']) or 'none'}")
    for ref in lim["stale_references"]:
        add(f"- Reference {ref['file']} last verified on {ref['last_verified']}. Rules may have changed.")
    not_tested = [f for f in r["findings"] if f["status"] == "not_tested"]
    for f in not_tested[:30]:
        add(f"- Not tested: {inline(f['title'])} · {f['id']}")
    add("")

    # 8. Changes since last audit
    d = r.get("diff")
    if d:
        add("## 8. Changes since last audit")
        add("")
        add(f"Compared with audit {d['previous_audit_id']}.")
        add("")
        for label, key in (("Fixed", "fixed"), ("New", "new"), ("Still open", "still_open"), ("Not rechecked", "not_rechecked")):
            add(f"**{label} ({len(d[key])})**")
            add("")
            for row in d[key]:
                add(f"- {inline(row['title'])} · {row['id']}")
            add("")

    # 9. Cross-skill overview
    add("## 9. Cross-skill overview")
    add("")
    if not r["cross_skill"]:
        add("No finding was reported by more than one skill.")
    for row in r["cross_skill"]:
        add(f"- {inline(row['title'])}: reported in {', '.join(row['reported_in'])} · {row['id']}")
    add("")

    add("## Appendix")
    add("")
    for s in r["skills"]:
        if s["ran"]:
            add(f"- {s['skill']} {s['skill_version'] or ''}".rstrip())
    add("")
    add("Standards are referenced by id. Hamu does not reproduce ISO, AICPA or PCI SSC text. "
        "WCAG criteria: Copyright W3C. OWASP ids: CC BY-SA 4.0, owasp.org.")
    add("")
    return "\n".join(lines)
