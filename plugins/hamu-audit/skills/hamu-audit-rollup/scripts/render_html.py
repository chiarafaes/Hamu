"""Render a Hamu roll-up dict as one self-contained, accessible HTML dashboard.

No external requests: inline CSS and JS only, guarded by a strict CSP.
Every value from findings is escaped with html.escape. Filters work with
JavaScript; without it every finding is shown. Print CSS gives a clean PDF.
"""
import html
import json

from render_md import DISCLAIMER, SKILL_NAMES, VERDICT_TEXT

SEVERITIES = ("critical", "high", "medium", "low", "info")
STATUS_TEXT = {
    "fail": "Fail", "warn": "Warning", "pass": "Pass", "needs_manual": "Needs manual check",
    "not_tested": "Not tested", "not_applicable": "Not applicable",
}

CSS = """
:root{--bg:#ffffff;--surface:#f5f6f8;--text:#1a1a1a;--muted:#4a4f57;--border:#c9ced6;--focus:#1f5fbf;--link:#1a4fa0;
--crit-bg:#fde2e2;--crit-fg:#7a1010;--high-bg:#ffe6cc;--high-fg:#6e3600;--med-bg:#fff2b8;--med-fg:#574500;
--low-bg:#e1ecff;--low-fg:#1d3f73;--info-bg:#eceff3;--info-fg:#33373d;--go:#1e6b34;--cond:#7a4b00;--nogo:#9b1c1c;
--space-1:4px;--space-2:8px;--space-3:16px;--space-4:24px;--space-5:40px;--radius:8px;
--font:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;--mono:ui-monospace,SFMono-Regular,Menlo,monospace}
@media (prefers-color-scheme:dark){:root{--bg:#14161a;--surface:#1d2026;--text:#eceef1;--muted:#b4bac3;--border:#3a3f48;
--focus:#8ab4ff;--link:#9cc0ff;--crit-bg:#4a1717;--crit-fg:#ffd2d2;--high-bg:#4a2c10;--high-fg:#ffdcb8;--med-bg:#3f3610;
--med-fg:#fff0a8;--low-bg:#172a4a;--low-fg:#cfe0ff;--info-bg:#2a2e35;--info-fg:#dde1e6;--go:#7fd99a;--cond:#ffcc80;--nogo:#ff9c9c}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--text);font:16px/1.5 var(--font)}
a{color:var(--link)}
:focus-visible{outline:3px solid var(--focus);outline-offset:2px}
.skip{position:absolute;left:-9999px}.skip:focus{left:var(--space-3);top:var(--space-3);background:var(--bg);padding:var(--space-2)}
header,main,footer{max-width:1100px;margin:0 auto;padding:var(--space-3)}
h1{font-size:1.75rem;margin:var(--space-3) 0 var(--space-2)}h2{font-size:1.35rem;margin-top:var(--space-5)}h3{font-size:1.1rem}
.meta{color:var(--muted);font-size:.9rem}
.note{border-left:4px solid var(--border);padding:var(--space-2) var(--space-3);background:var(--surface)}
.verdict{display:flex;flex-wrap:wrap;gap:var(--space-3);align-items:center;padding:var(--space-3);border:1px solid var(--border);border-radius:var(--radius);background:var(--surface)}
.verdict strong{font-size:1.4rem}.v-go{color:var(--go)}.v-go_with_conditions{color:var(--cond)}.v-no_go{color:var(--nogo)}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:var(--space-3);margin-top:var(--space-3)}
.card{border:1px solid var(--border);border-radius:var(--radius);padding:var(--space-3)}
.card .score{font-size:2rem;font-weight:700}
table{border-collapse:collapse;width:100%;margin:var(--space-2) 0}
th,td{border-bottom:1px solid var(--border);padding:var(--space-2);text-align:left;vertical-align:top}
caption{text-align:left;font-weight:600;padding:var(--space-2) 0}
.table-wrap{overflow-x:auto}
.badge{display:inline-block;padding:2px var(--space-2);border-radius:999px;font-size:.8rem;font-weight:600}
.sev-critical{background:var(--crit-bg);color:var(--crit-fg)}.sev-high{background:var(--high-bg);color:var(--high-fg)}
.sev-medium{background:var(--med-bg);color:var(--med-fg)}.sev-low{background:var(--low-bg);color:var(--low-fg)}
.sev-info{background:var(--info-bg);color:var(--info-fg)}
form.filters{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:var(--space-3);padding:var(--space-3);border:1px solid var(--border);border-radius:var(--radius)}
label{display:block;font-weight:600;margin-bottom:var(--space-1)}
select,input{width:100%;min-height:44px;padding:var(--space-2);font:inherit;color:var(--text);background:var(--bg);border:1px solid var(--muted);border-radius:6px}
button{min-height:44px;padding:var(--space-2) var(--space-3);font:inherit;border:1px solid var(--muted);border-radius:6px;background:var(--surface);color:var(--text);cursor:pointer}
article.finding{border:1px solid var(--border);border-radius:var(--radius);padding:var(--space-3);margin:var(--space-3) 0}
article.finding h4{margin:0 0 var(--space-2);font-size:1.05rem}
.tags{display:flex;flex-wrap:wrap;gap:var(--space-2);margin-bottom:var(--space-2)}
details summary{cursor:pointer;font-weight:600;min-height:44px;display:flex;align-items:center}
code,pre{font-family:var(--mono);font-size:.85rem;white-space:pre-wrap;word-break:break-word}
.visually-hidden{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
[hidden]{display:none!important}
@media print{.skip,form.filters,#count,.no-print{display:none!important}
body{font-size:11pt;background:#fff;color:#000}article.finding{break-inside:avoid}
details>*{display:block}a{color:#000}h2{break-before:page}h2:first-of-type{break-before:auto}}
"""

JS = """
(function(){
  var form=document.getElementById('filters');if(!form)return;
  var items=[].slice.call(document.querySelectorAll('article.finding'));
  var count=document.getElementById('count');
  function apply(){
    var sev=form.sev.value,skill=form.skill.value,fw=form.fw.value,status=form.status.value,q=form.q.value.toLowerCase().trim();
    var shown=0;
    items.forEach(function(el){
      var ok=(!sev||el.dataset.sev===sev)&&(!skill||el.dataset.skill===skill)&&(!status||el.dataset.status===status)
        &&(!fw||(' '+el.dataset.fw+' ').indexOf(' '+fw+' ')>-1)&&(!q||el.textContent.toLowerCase().indexOf(q)>-1);
      el.hidden=!ok;if(ok)shown++;
    });
    document.querySelectorAll('section.skill-group').forEach(function(s){
      s.hidden=!s.querySelector('article.finding:not([hidden])');
    });
    count.textContent=shown+' of '+items.length+' findings shown';
  }
  form.addEventListener('input',apply);form.addEventListener('change',apply);
  form.addEventListener('reset',function(){setTimeout(apply,0)});
  form.addEventListener('submit',function(e){e.preventDefault();apply()});
  window.addEventListener('beforeprint',function(){document.querySelectorAll('details').forEach(function(d){d.open=true})});
  apply();
})();
"""


def e(value):
    return html.escape("" if value is None else str(value), quote=True)


def badge(sev):
    return f'<span class="badge sev-{e(sev)}">{e(sev.capitalize())}<span class="visually-hidden"> severity</span></span>'


def options(values, labels=None):
    out = ['<option value="">All</option>']
    for v in values:
        out.append(f'<option value="{e(v)}">{e((labels or {}).get(v, v))}</option>')
    return "".join(out)


def finding_html(f):
    fws = " ".join(sorted({x.get("id", "") for x in f.get("frameworks", [])}))
    fw_list = " · ".join(
        e(" ".join(p for p in (x.get("id"), x.get("ref")) if p)) + f" ({e(x.get('relation'))})"
        for x in f.get("frameworks", [])
    )
    ev_rows = "".join(
        f"<li><strong>{e(ev.get('type'))}</strong> {e(ev.get('location'))}"
        + (f"<br><code>{e(str(ev.get('snippet'))[:300])}</code>" if ev.get("snippet") else "")
        + "</li>"
        for ev in f.get("evidence", [])[:8]
    )
    fix = f.get("fix") or {}
    steps = "".join(f"<li>{e(s)}</li>" for s in fix.get("steps", []))
    code = f"<pre><code>{e(fix['code_example'])}</code></pre>" if fix.get("code_example") else ""
    flags = []
    if f.get("legal_review"):
        flags.append('<span class="badge sev-info">Legal review</span>')
    if len(f.get("reported_in", [])) > 1:
        flags.append('<span class="badge sev-info">Found by several skills</span>')
    return f"""
<article class="finding" data-sev="{e(f['severity'])}" data-skill="{e(f['owner_skill'])}" data-status="{e(f['status'])}" data-fw="{e(fws)}" aria-labelledby="t-{e(f['id'])}">
  <h4 id="t-{e(f['id'])}">{e(f['title'])}</h4>
  <div class="tags">{badge(f['severity'])}<span class="badge sev-info">{e(STATUS_TEXT.get(f['status'], f['status']))}</span>{''.join(flags)}</div>
  <p><strong>What this means:</strong> {e(f['summary_plain'])}</p>
  {f'<p><strong>Fix:</strong> {e(fix.get("summary"))} (effort {e(fix.get("effort", "?"))})</p>' if fix.get("summary") else ''}
  <details>
    <summary>Technical detail</summary>
    <p>{e(f['detail_technical'])}</p>
    {f'<p><strong>Frameworks:</strong> {fw_list}</p>' if fw_list else ''}
    {f'<ul>{ev_rows}</ul>' if ev_rows else ''}
    {f'<ol>{steps}</ol>' if steps else ''}{code}
    <p class="meta">Id {e(f['id'])} · Confidence {e(f['confidence'])} · Method {e(f['method'])}</p>
  </details>
</article>"""


def render(r):
    t = r.get("target", {})
    o = r["overall"]
    lang = e(r.get("report_language") or "en")
    title = f"{t.get('name') or 'Target'}: Hamu audit"
    findings = r["findings"]
    visible = [f for f in findings if f["status"] not in ("pass", "not_applicable")]
    frameworks = sorted({x.get("id", "") for f in visible for x in f.get("frameworks", [])})
    statuses = [s for s in STATUS_TEXT if any(f["status"] == s for f in visible)]

    cards = []
    for s in r["skills"]:
        if not s["ran"]:
            cards.append(f'<div class="card"><h3>{e(SKILL_NAMES[s["skill"]])}</h3><p>Not run.</p></div>')
            continue
        sev = s["open_by_severity"]
        cards.append(
            f'<div class="card"><h3>{e(SKILL_NAMES[s["skill"]])}</h3>'
            f'<p class="score">{e(s["score"] if s["score"] is not None else "n/a")}<span class="visually-hidden"> out of 100</span></p>'
            f'<p class="meta">{sev["critical"]} critical, {sev["high"]} high, {sev["medium"]} medium open. '
            f'{s["checks_run"]} checks run, {s["not_tested"]} not tested.</p></div>'
        )

    actions = "".join(
        f"<li>{badge(a['severity'])} {e(a['fix'] or a['title'])} <span class=\"meta\">(effort {e(a['effort'] or '?')}, {e(a['id'])})</span></li>"
        for a in r["top_actions"]
    ) or "<li>No open findings above info level.</li>"

    fw_rows = "".join(
        f"<tr><th scope=\"row\">{e(fw['id'])}</th><td>{e(fw['status'])}</td><td>{fw['pass']}</td><td>{fw['fail']}</td>"
        f"<td>{fw['warn']}</td><td>{fw['needs_manual']}</td><td>{fw['not_tested']}</td><td>{e(fw['reason'])}</td></tr>"
        for fw in r["frameworks"]
    )

    groups = []
    for skill, name in SKILL_NAMES.items():
        items = [f for f in visible if f["owner_skill"] == skill]
        if items:
            groups.append(f'<section class="skill-group" aria-labelledby="g-{e(skill)}"><h3 id="g-{e(skill)}">{e(name)}</h3>'
                          + "".join(finding_html(f) for f in items) + "</section>")

    diff_html = ""
    d = r.get("diff")
    if d:
        parts = []
        for label, key in (("Fixed", "fixed"), ("New", "new"), ("Still open", "still_open"), ("Not rechecked", "not_rechecked")):
            rows = "".join(f"<li>{e(x['title'])} <span class=\"meta\">{e(x['id'])}</span></li>" for x in d[key])
            parts.append(f"<h3>{label} ({len(d[key])})</h3><ul>{rows or '<li>None</li>'}</ul>")
        diff_html = f'<h2 id="changes">Changes since last audit</h2><p>Compared with audit {e(d["previous_audit_id"])}.</p>' + "".join(parts)

    lim = r["limitations"]
    lim_items = [f"<li>Skills not run: {e(', '.join(lim['skills_not_run']) or 'none')}</li>",
                 f"<li>Tools missing: {e(', '.join(lim['tools_missing']) or 'none')}</li>"]
    lim_items += [f"<li>Reference {e(x['file'])} last verified {e(x['last_verified'])}. Rules may have changed.</li>"
                  for x in lim["stale_references"]]

    data_json = json.dumps({"audit_id": r["audit_id"], "generated_at": r["generated_at"]}).replace("</", "<\\/")
    mode = "active" if r["testing"].get("active_testing_allowed") else "passive"

    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'unsafe-inline'; script-src 'unsafe-inline'; img-src data:">
<meta name="referrer" content="no-referrer">
<title>{e(title)}</title>
<style>{CSS}</style>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header>
  <p class="meta">Hamu audit report</p>
  <h1>{e(t.get('name') or 'Target')}</h1>
  <p class="meta">Audit {e(r['audit_id'])} · Generated {e(r['generated_at'])} · Testing {e(mode)}</p>
</header>
<main id="main">
  <p class="note">{e(DISCLAIMER)}</p>
  <h2 id="summary">Summary</h2>
  <div class="verdict"><span>Verdict</span><strong class="v-{e(o['verdict'])}">{e(VERDICT_TEXT[o['verdict']])}</strong>
  <span>Overall score <strong>{e(o['score'] if o['score'] is not None else 'n/a')}</strong><span class="visually-hidden"> out of 100</span></span></div>
  <ul>{''.join(f'<li>{e(x)}</li>' for x in o['reasons'][:5])}</ul>
  <div class="cards">{''.join(cards)}</div>
  <h2 id="actions">Top actions</h2>
  <ol>{actions}</ol>
  <h2 id="findings">Findings</h2>
  <form id="filters" class="filters no-print" aria-label="Filter findings">
    <div><label for="f-sev">Severity</label><select id="f-sev" name="sev">{options(SEVERITIES)}</select></div>
    <div><label for="f-skill">Area</label><select id="f-skill" name="skill">{options(list(SKILL_NAMES), SKILL_NAMES)}</select></div>
    <div><label for="f-fw">Framework</label><select id="f-fw" name="fw">{options(frameworks)}</select></div>
    <div><label for="f-status">Status</label><select id="f-status" name="status">{options(statuses, STATUS_TEXT)}</select></div>
    <div><label for="f-q">Search</label><input id="f-q" name="q" type="search" autocomplete="off"></div>
    <div><button type="reset" style="margin-top:28px">Reset filters</button></div>
  </form>
  <p id="count" role="status" aria-live="polite"></p>
  {''.join(groups) or '<p>No findings to show.</p>'}
  <h2 id="coverage">Framework coverage</h2>
  <div class="table-wrap"><table>
    <caption>Findings per applicable framework</caption>
    <thead><tr><th scope="col">Framework</th><th scope="col">Status</th><th scope="col">Pass</th><th scope="col">Fail</th><th scope="col">Warn</th><th scope="col">Manual</th><th scope="col">Not tested</th><th scope="col">Reason</th></tr></thead>
    <tbody>{fw_rows}</tbody>
  </table></div>
  {diff_html}
  <h2 id="limits">Not tested and limitations</h2>
  <ul>{''.join(lim_items)}</ul>
</main>
<footer><p class="meta">Standards are referenced by id. Hamu does not reproduce ISO, AICPA or PCI SSC text. WCAG criteria: Copyright W3C. OWASP ids: CC BY-SA 4.0.</p></footer>
<script type="application/json" id="hamu-meta">{data_json}</script>
<script>{JS}</script>
</body>
</html>
"""
