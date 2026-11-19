#!/usr/bin/env python3
"""Regenerate the roll-up test fixtures. Run from the repo root:
python3 tests/rollup/make_fixtures.py
Invented data only."""
import json, pathlib

ROOT = pathlib.Path(__file__).resolve().parent / "fixtures" / "audit" / ".audit"
AUDIT = "fixture-shop-20261119"
OLD = "fixture-shop-20261001"


def f(fid, owner, title, status, sev, conf="high", fws=None, reported_by=None, effort="S", ev_loc="https://shop.example.be/"):
    d = {
        "id": fid, "check_id": fid.split("#")[0], "owner_skill": owner, "title": title,
        "status": status, "severity": sev, "confidence": conf, "method": "automated",
        "summary_plain": f"Plain summary for {title}.",
        "detail_technical": f"Technical detail for {title}.",
        "frameworks": fws or [],
        "evidence": [{"type": "text", "location": ev_loc, "snippet": f"evidence {fid}"}],
        "fix": {"summary": f"Fix {title}", "steps": ["Step one"], "effort": effort},
    }
    if reported_by:
        d["reported_by"] = reported_by
    return d


def run(skill, started="2026-11-19T10:00:00+01:00", missing=None):
    return {"started_at": started, "runtime": "claude_code", "mode": "audit", "testing": "passive",
            "targets": ["https://shop.example.be"], "tools_used": ["curl"], "tools_missing": missing or []}


def write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


context = {
    "schema_version": "1.0", "audit_id": AUDIT, "created_at": "2026-11-19T09:00:00+01:00", "report_language": "en",
    "target": {"type": "url", "name": "Fixture Shop", "urls": ["https://shop.example.be"], "platforms": ["web"], "languages": ["nl", "fr"]},
    "permission": {"owner_confirmed": True, "active_testing_allowed": False},
    "jurisdiction": {"established_in": ["BE"], "users_in": ["BE", "EU"], "public_sector": False},
    "product": {"audience": "B2C", "sells_online": True, "payments": "hosted_redirect"},
    "organisation": {"size": "small", "role": "owner_of_product", "goal": "pre_launch", "certification_targets": []},
    "applicable_frameworks": [
        {"id": "GDPR", "status": "applies", "reason": "Established in BE"},
        {"id": "EPRIVACY-BE", "status": "applies", "reason": "Tracking detected, BE users"},
        {"id": "ASVS5", "status": "applies", "reason": "Baseline"},
        {"id": "WCAG22", "status": "applies", "reason": "Always"},
        {"id": "EAA", "status": "applies", "reason": "B2C e-commerce in EU"},
        {"id": "CWV", "status": "applies", "reason": "Web target"},
        {"id": "HIPAA", "status": "not_applicable", "reason": "No US health data"},
    ],
}

sp = [
    f("SP.CONSENT.PRE-TRACK#aaaaaaaa", "hamu-security-privacy", "Analytics fire before consent", "fail", "high",
      fws=[{"id": "EPRIVACY-BE", "ref": "Art. 10/2 Law of 30 July 2018", "relation": "requirement"}]),
    f("SP.HDR.CSP#bbbbbbbb", "hamu-security-privacy", "No Content-Security-Policy", "fail", "medium",
      fws=[{"id": "ASVS5", "ref": "V3", "relation": "best_practice"}], effort="M"),
    f("SP.DNS.DMARC#cccccccc", "hamu-security-privacy", "DMARC policy is none", "warn", "medium"),
    f("SP.TLS.HTTPS#dddddddd", "hamu-security-privacy", "HTTPS everywhere", "pass", "high"),
    f("SP.LOG.ALERT#eeeeeeee", "hamu-security-privacy", "Security alerts need confirmation", "needs_manual", "medium", conf="medium"),
    f("SP.DEPS.VULN#ffffffff", "hamu-security-privacy", "Dependencies not scanned", "not_tested", "high", conf="medium"),
]
a11y = [
    f("A11Y.IMG.ALT#11111111", "hamu-accessibility", "Product images without alt text", "fail", "high",
      fws=[{"id": "WCAG22", "ref": "1.1.1", "level": "A", "relation": "requirement"},
           {"id": "EAA", "ref": "Annex I", "relation": "requirement"}]),
    f("A11Y.COLOR.CONTRAST#22222222", "hamu-accessibility", "Low contrast on hero text", "fail", "medium", conf="low"),
    f("SP.CONSENT.PRE-TRACK#aaaaaaaa", "hamu-security-privacy", "Analytics fire before consent", "fail", "high",
      reported_by="hamu-accessibility", ev_loc="https://shop.example.be/products",
      fws=[{"id": "GDPR", "ref": "Art. 6", "relation": "requirement"}]),
    f("A11Y.KBD.TRAP#33333333", "hamu-accessibility", "No keyboard trap", "pass", "high"),
]
px = [
    f("PX.CWV.LCP#44444444", "hamu-performance-ux", "LCP 3.1 s on mobile", "fail", "medium", conf="medium",
      fws=[{"id": "CWV", "ref": "LCP", "relation": "best_practice"}]),
    f("PX.CTA.PRIMARY#55555555", "hamu-performance-ux", "Primary CTA below the fold", "warn", "medium", conf="medium"),
    f("SEO.LINK.REL#66666666", "hamu-seo-visibility", "Affiliate links without rel sponsored", "fail", "medium",
      reported_by="hamu-performance-ux"),
]

write(ROOT / "context.json", context)
for skill, items in (("hamu-security-privacy", sp), ("hamu-accessibility", a11y), ("hamu-performance-ux", px)):
    write(ROOT / "findings" / f"{skill}.json", {
        "schema_version": "1.0", "skill": skill, "skill_version": "0.7.0", "audit_id": AUDIT,
        "run": run(skill, missing=["osv-scanner"] if skill == "hamu-security-privacy" else []), "findings": items})

old_sp = [
    f("SP.HDR.CSP#bbbbbbbb", "hamu-security-privacy", "No Content-Security-Policy", "fail", "medium"),
    f("SP.TLS.HSTS#77777777", "hamu-security-privacy", "HSTS missing", "fail", "medium"),
]
old_seo = [f("SEO.CRAWL.ROBOTS#88888888", "hamu-seo-visibility", "robots.txt blocks CSS", "fail", "high")]
for skill, items in (("hamu-security-privacy", old_sp), ("hamu-seo-visibility", old_seo)):
    write(ROOT / "history" / OLD / f"{skill}.json", {
        "schema_version": "1.0", "skill": skill, "skill_version": "0.6.0", "audit_id": OLD,
        "run": run(skill, started="2026-10-01T10:00:00+02:00"), "findings": items})
print("fixtures written to", ROOT)
