"""Unit tests for the Hamu roll-up. Standard library only.
Run from the repo root: python3 -m unittest discover -s tests/rollup -v
"""
import datetime as dt
import html.parser
import json
import pathlib
import shutil
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "plugins/hamu-audit/skills/hamu-audit-rollup/scripts"
FIXTURE = pathlib.Path(__file__).resolve().parent / "fixtures" / "audit" / ".audit"
sys.path.insert(0, str(SCRIPTS))

import rollup  # noqa: E402
import render_html  # noqa: E402
import render_md  # noqa: E402

NOW = dt.datetime(2026, 11, 19, 12, 0, tzinfo=dt.timezone.utc)


def build(**kw):
    return rollup.build_rollup(FIXTURE, now=NOW, **kw)


class MergeTests(unittest.TestCase):
    def setUp(self):
        self.r = build()
        self.by_id = {f["id"]: f for f in self.r["findings"]}

    def test_pointer_merges_into_owner(self):
        f = self.by_id["SP.CONSENT.PRE-TRACK#aaaaaaaa"]
        self.assertEqual(f["owner_skill"], "hamu-security-privacy")
        self.assertEqual(f["reported_in"], ["hamu-accessibility", "hamu-security-privacy"])
        self.assertEqual(len(f["evidence"]), 2)
        self.assertEqual({x["id"] for x in f["frameworks"]}, {"EPRIVACY-BE", "GDPR"})

    def test_no_duplicate_ids(self):
        ids = [f["id"] for f in self.r["findings"]]
        self.assertEqual(len(ids), len(set(ids)))

    def test_pointer_kept_when_owner_did_not_run(self):
        f = self.by_id["SEO.LINK.REL#66666666"]
        self.assertEqual(f["owner_skill"], "hamu-seo-visibility")
        self.assertEqual(f["reported_by"], "hamu-performance-ux")

    def test_findings_sorted_by_severity(self):
        ranks = [rollup.SEVERITY_RANK[f["severity"]] for f in self.r["findings"]]
        self.assertEqual(ranks, sorted(ranks))

    def test_cross_skill_listed(self):
        self.assertEqual([c["id"] for c in self.r["cross_skill"]], ["SP.CONSENT.PRE-TRACK#aaaaaaaa"])


class ScoreTests(unittest.TestCase):
    def setUp(self):
        self.r = build()
        self.skills = {s["skill"]: s for s in self.r["skills"]}

    def area(self, skill, name):
        return next(a for a in self.skills[skill]["areas"] if a["area"] == name)

    def test_fail_high_costs_ten_once_after_merge(self):
        self.assertEqual(self.area("hamu-security-privacy", "CONSENT")["score"], 90)

    def test_warn_counts_half(self):
        self.assertEqual(self.area("hamu-security-privacy", "DNS")["score"], 98)

    def test_low_confidence_not_scored(self):
        self.assertEqual(self.area("hamu-accessibility", "COLOR")["score"], 100)
        self.assertEqual(self.skills["hamu-accessibility"]["open_by_severity"]["medium"], 0)

    def test_not_tested_only_area_excluded_from_skill_score(self):
        self.assertEqual(self.area("hamu-security-privacy", "DEPS")["checks_run"], 0)
        self.assertEqual(self.skills["hamu-security-privacy"]["score"], 97)

    def test_skill_not_run_has_no_score(self):
        seo = self.skills["hamu-seo-visibility"]
        self.assertFalse(seo["ran"])
        self.assertIsNone(seo["score"])

    def test_overall_is_mean_of_skills_that_ran(self):
        self.assertEqual(self.r["overall"]["score"], 97)

    def test_floor_at_zero(self):
        findings = [{"check_id": "SP.X.Y", "status": "fail", "severity": "critical", "confidence": "high"}] * 5
        score, _ = rollup.score_findings(findings)
        self.assertEqual(score, 0)


class VerdictTests(unittest.TestCase):
    def test_no_go_on_legal_highs(self):
        v = build()["overall"]
        self.assertEqual(v["verdict"], "no_go")
        joined = " ".join(v["reasons"])
        self.assertIn("SP.CONSENT.PRE-TRACK#aaaaaaaa", joined)
        self.assertIn("A11Y.IMG.ALT#11111111", joined)

    def test_go_with_conditions_for_best_practice_high(self):
        ctx = {"applicable_frameworks": [{"id": "ASVS5", "status": "applies", "reason": ""}]}
        findings = [{"id": "SP.A.B#00000000", "status": "fail", "severity": "high", "confidence": "high",
                     "frameworks": [{"id": "ASVS5", "relation": "best_practice"}]}]
        self.assertEqual(rollup.verdict(findings, ctx)["verdict"], "go_with_conditions")

    def test_low_confidence_critical_does_not_block(self):
        findings = [{"id": "SP.A.B#00000000", "status": "fail", "severity": "critical", "confidence": "low", "frameworks": []}]
        self.assertEqual(rollup.verdict(findings, {})["verdict"], "go")

    def test_likely_framework_is_not_legal(self):
        ctx = {"applicable_frameworks": [{"id": "PCI-DSS", "status": "likely", "reason": ""}]}
        findings = [{"id": "SP.A.B#00000000", "status": "fail", "severity": "high", "confidence": "high",
                     "frameworks": [{"id": "PCI-DSS", "relation": "requirement"}]}]
        self.assertEqual(rollup.verdict(findings, ctx)["verdict"], "go_with_conditions")


class DiffTests(unittest.TestCase):
    def setUp(self):
        self.d = build()["diff"]

    def ids(self, key):
        return [x["id"] for x in self.d[key]]

    def test_previous_found_automatically(self):
        self.assertEqual(self.d["previous_audit_id"], "fixture-shop-20261001")

    def test_fixed_only_when_owner_ran(self):
        self.assertEqual(self.ids("fixed"), ["SP.TLS.HSTS#77777777"])
        self.assertEqual(self.ids("not_rechecked"), ["SEO.CRAWL.ROBOTS#88888888"])

    def test_still_open_and_new(self):
        self.assertEqual(self.ids("still_open"), ["SP.HDR.CSP#bbbbbbbb"])
        self.assertIn("A11Y.IMG.ALT#11111111", self.ids("new"))
        self.assertNotIn("SP.HDR.CSP#bbbbbbbb", self.ids("new"))


class OutputTests(unittest.TestCase):
    def setUp(self):
        self.r = build()

    def test_top_actions_order(self):
        sevs = [a["severity"] for a in self.r["top_actions"]]
        self.assertEqual(sevs[:2], ["high", "high"])
        self.assertNotIn("info", sevs)

    def test_needs_confirmation(self):
        self.assertIn("SP.LOG.ALERT#eeeeeeee", self.r["needs_confirmation"])
        self.assertIn("A11Y.COLOR.CONTRAST#22222222", self.r["needs_confirmation"])

    def test_limitations(self):
        lim = self.r["limitations"]
        self.assertEqual(lim["tools_missing"], ["osv-scanner"])
        self.assertEqual(lim["skills_not_run"], ["hamu-seo-visibility"])

    def test_not_applicable_framework_left_out_of_coverage(self):
        self.assertNotIn("HIPAA", [f["id"] for f in self.r["frameworks"]])

    def test_markdown_has_all_sections_and_no_em_dash(self):
        md = render_md.render(self.r)
        for heading in ("## 1. Summary", "## 2. Top actions", "## 3. Scope", "## 4. Findings",
                        "## 5. Needs confirmation", "## 6. Framework coverage", "## 7. Not tested",
                        "## 8. Changes since last audit", "## 9. Cross-skill overview"):
            self.assertIn(heading, md)
        self.assertNotIn("—", md)
        self.assertIn("readiness check, not legal advice", md)

    def test_html_escapes_and_is_self_contained(self):
        r = json.loads(json.dumps(self.r))
        r["findings"][0]["title"] = '<script>alert("x")</script>'
        out = render_html.render(r)
        self.assertNotIn('<script>alert("x")</script>', out)
        self.assertIn("&lt;script&gt;", out)
        self.assertNotIn("http://", out.replace("http-equiv", ""))
        self.assertNotIn("src=\"http", out)
        self.assertNotIn("—", out)

    def test_html_parses_with_unique_ids(self):
        out = render_html.render(self.r)

        class P(html.parser.HTMLParser):
            def __init__(self):
                super().__init__()
                self.ids = []

            def handle_starttag(self, tag, attrs):
                for k, v in attrs:
                    if k == "id":
                        self.ids.append(v)

        p = P()
        p.feed(out)
        self.assertEqual(len(p.ids), len(set(p.ids)))
        self.assertIn('<html lang="en">', out)


class RefusalTests(unittest.TestCase):
    def test_refuses_other_audit_id(self):
        tmp = pathlib.Path(tempfile.mkdtemp())
        try:
            shutil.copytree(FIXTURE, tmp / ".audit")
            path = tmp / ".audit" / "findings" / "hamu-performance-ux.json"
            data = json.loads(path.read_text())
            data["audit_id"] = "another-audit"
            path.write_text(json.dumps(data))
            with self.assertRaises(rollup.RollupError):
                rollup.build_rollup(tmp / ".audit", now=NOW)
        finally:
            shutil.rmtree(tmp)

    def test_cli_writes_three_files(self):
        tmp = pathlib.Path(tempfile.mkdtemp())
        try:
            shutil.copytree(FIXTURE, tmp / ".audit")
            code = rollup.main(["--audit-dir", str(tmp / ".audit")])
            self.assertEqual(code, 0)
            for name in ("hamu-audit.json", "hamu-audit.md", "hamu-audit.html"):
                self.assertTrue((tmp / ".audit" / "reports" / name).exists(), name)
        finally:
            shutil.rmtree(tmp)


if __name__ == "__main__":
    unittest.main()
