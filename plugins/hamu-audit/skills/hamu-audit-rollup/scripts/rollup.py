#!/usr/bin/env python3
"""Hamu roll-up: merge, deduplicate, score and diff Hamu findings.

Usage:
  python3 rollup.py [--audit-dir .audit] [--previous DIR] [--skills a,b] [--no-render]

Reads   <audit-dir>/context.json and <audit-dir>/findings/*.json
Writes  <audit-dir>/reports/hamu-audit.json, hamu-audit.md, hamu-audit.html

Standard library only. Python 3.9 or newer. Rules come from the shared
contract: severity.md (scoring, verdict), ownership-matrix.md (merging),
run-protocol.md (history layout).
"""
import argparse
import datetime as dt
import json
import pathlib
import sys

SEVERITY_RANK = {"critical": 0, "high": 1, "medium": 2, "low": 3, "info": 4}
SEVERITY_POINTS = {"critical": 25, "high": 10, "medium": 4, "low": 1, "info": 0}
EFFORT_RANK = {"S": 0, "M": 1, "L": 2}
OPEN = ("fail", "warn")
SKILLS = (
    "hamu-security-privacy",
    "hamu-accessibility",
    "hamu-performance-ux",
    "hamu-seo-visibility",
)


class RollupError(Exception):
    """Raised for input the roll-up must refuse (mixed audits, broken files)."""


# ---------------------------------------------------------------- loading

def load_json(path):
    try:
        return json.loads(pathlib.Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise RollupError(f"cannot read {path}: {exc}") from exc


def load_findings(findings_dir, audit_id, only_skills=None):
    """Return {skill: findings_file_dict}. Refuses files from another audit."""
    files = {}
    for path in sorted(pathlib.Path(findings_dir).glob("*.json")):
        data = load_json(path)
        skill = data.get("skill")
        if skill not in SKILLS:
            raise RollupError(f"{path}: unknown skill {skill!r}")
        if only_skills and skill not in only_skills:
            continue
        if data.get("audit_id") != audit_id:
            raise RollupError(
                f"{path}: audit_id {data.get('audit_id')!r} does not match context {audit_id!r}. "
                "Move old files to history/ before rolling up."
            )
        if skill in files:
            raise RollupError(f"two findings files for {skill}")
        files[skill] = data
    return files


# ---------------------------------------------------------------- merging

def _dedupe(items, key):
    seen, out = set(), []
    for item in items:
        k = key(item)
        if k not in seen:
            seen.add(k)
            out.append(item)
    return out


def merge_findings(files):
    """Merge pointer findings into the owner's finding with the same id.

    A pointer finding has reported_by set to a non-owner skill. Its evidence,
    frameworks, impact and related ids are added to the owner's finding. If the
    owner skill did not run, the pointer finding is kept as the finding.
    """
    by_id = {}
    order = []
    # Owner findings first so pointers merge into them.
    entries = []
    for skill, data in files.items():
        for f in data.get("findings", []):
            is_pointer = bool(f.get("reported_by")) and f.get("reported_by") != f.get("owner_skill")
            entries.append((1 if is_pointer else 0, skill, f))
    entries.sort(key=lambda e: e[0])

    for is_pointer, skill, f in entries:
        fid = f["id"]
        if fid not in by_id:
            merged = dict(f)
            merged["reported_in"] = [skill]
            merged["merged_from"] = []
            by_id[fid] = merged
            order.append(fid)
            continue
        target = by_id[fid]
        target["reported_in"] = sorted(set(target["reported_in"]) | {skill})
        target["merged_from"].append({"skill": skill, "status": f.get("status")})
        target["evidence"] = _dedupe(
            target.get("evidence", []) + f.get("evidence", []),
            lambda e: (e.get("type"), e.get("location"), e.get("snippet")),
        )
        target["frameworks"] = _dedupe(
            target.get("frameworks", []) + f.get("frameworks", []),
            lambda x: (x.get("id"), x.get("ref"), x.get("relation")),
        )
        for field in ("impact", "related"):
            if f.get(field):
                target[field] = sorted(set(target.get(field, [])) | set(f[field]))
        if f.get("legal_review"):
            target["legal_review"] = True
    return [by_id[i] for i in order]


# ---------------------------------------------------------------- scoring

def counts_as_scored(f):
    """severity.md: low-confidence findings never count as fail in scoring."""
    return f.get("confidence") != "low"


def deduction(f):
    if not counts_as_scored(f):
        return 0.0
    points = SEVERITY_POINTS[f["severity"]]
    if f["status"] == "fail":
        return float(points)
    if f["status"] == "warn":
        return points / 2.0
    return 0.0


def area_of(f):
    parts = f["check_id"].split(".")
    return parts[1] if len(parts) > 1 else "GENERAL"


def score_findings(findings):
    """Return (score, stats) for a list of findings: 100 minus deductions, floor 0."""
    stats = {s: 0 for s in ("fail", "warn", "pass", "needs_manual", "not_tested", "not_applicable")}
    sev = {s: 0 for s in SEVERITY_RANK}
    checks = set()
    total = 0.0
    for f in findings:
        stats[f["status"]] = stats.get(f["status"], 0) + 1
        if f["status"] in OPEN and counts_as_scored(f):
            sev[f["severity"]] += 1
        if f["status"] not in ("not_tested", "not_applicable"):
            checks.add(f["check_id"])
        total += deduction(f)
    score = max(0, round(100 - total))
    return score, {
        "status": stats,
        "open_by_severity": sev,
        "checks_run": len(checks),
        "not_tested": stats["not_tested"],
    }


def score_skills(findings, files):
    """Per skill: per-area scores, skill score = mean of area scores."""
    result = []
    for skill in SKILLS:
        ran = skill in files
        owned = [f for f in findings if f["owner_skill"] == skill]
        areas = {}
        for f in owned:
            areas.setdefault(area_of(f), []).append(f)
        area_rows = []
        for area in sorted(areas):
            score, stats = score_findings(areas[area])
            area_rows.append({"area": area, "score": score, **stats})
        scored_areas = [a for a in area_rows if a["checks_run"] > 0]
        skill_score = (
            round(sum(a["score"] for a in scored_areas) / len(scored_areas))
            if ran and scored_areas else None
        )
        _, totals = score_findings(owned)
        result.append({
            "skill": skill,
            "ran": ran,
            "skill_version": files[skill].get("skill_version") if ran else None,
            "score": skill_score,
            **totals,
            "areas": area_rows,
        })
    return result


# ---------------------------------------------------------------- verdict

def framework_status(context):
    return {f["id"]: f["status"] for f in context.get("applicable_frameworks", [])}


def is_legal_requirement(f, fw_status):
    return any(
        x.get("relation") == "requirement" and fw_status.get(x.get("id")) == "applies"
        for x in f.get("frameworks", [])
    )


def verdict(findings, context):
    """severity.md go / no-go rules. Only open findings with medium or high confidence count."""
    fw = framework_status(context)
    open_f = [f for f in findings if f["status"] in OPEN and counts_as_scored(f)]
    criticals = [f["id"] for f in open_f if f["severity"] == "critical"]
    legal_highs = [f["id"] for f in open_f if f["severity"] == "high" and is_legal_requirement(f, fw)]
    other_highs = [f["id"] for f in open_f if f["severity"] == "high" and f["id"] not in legal_highs]
    if criticals or legal_highs:
        return {
            "verdict": "no_go",
            "reasons": (
                [f"Open critical: {i}" for i in criticals]
                + [f"Open high on a law that applies: {i}" for i in legal_highs]
            ),
        }
    if other_highs:
        return {
            "verdict": "go_with_conditions",
            "reasons": [f"Open high (best practice or readiness): {i}" for i in other_highs],
        }
    return {"verdict": "go", "reasons": ["No open criticals and no open legal highs."]}


# ---------------------------------------------------------------- actions, coverage

def top_actions(findings, limit=10):
    open_f = [f for f in findings if f["status"] in OPEN and counts_as_scored(f)]
    open_f.sort(key=lambda f: (
        SEVERITY_RANK[f["severity"]],
        EFFORT_RANK.get((f.get("fix") or {}).get("effort"), 3),
        f["id"],
    ))
    return [{
        "id": f["id"],
        "title": f["title"],
        "severity": f["severity"],
        "effort": (f.get("fix") or {}).get("effort"),
        "owner_skill": f["owner_skill"],
        "fix": (f.get("fix") or {}).get("summary"),
    } for f in open_f[:limit] if f["severity"] != "info"]


def needs_confirmation(findings):
    return [f["id"] for f in findings if f["confidence"] == "low" or f["status"] == "needs_manual"]


def framework_coverage(findings, context):
    rows = []
    for fw in context.get("applicable_frameworks", []):
        if fw["status"] == "not_applicable":
            continue
        mapped = [f for f in findings if any(x.get("id") == fw["id"] for x in f.get("frameworks", []))]
        stats = {s: sum(1 for f in mapped if f["status"] == s) for s in ("pass", "fail", "warn", "needs_manual", "not_tested")}
        rows.append({"id": fw["id"], "status": fw["status"], "reason": fw.get("reason", ""), "findings": len(mapped), **stats})
    return rows


def limitations(files):
    tools_missing, stale = set(), []
    for skill, data in files.items():
        run = data.get("run", {})
        tools_missing.update(run.get("tools_missing", []))
        for ref in run.get("reference_freshness", []):
            if ref.get("stale"):
                stale.append({"skill": skill, **ref})
    return {
        "tools_missing": sorted(tools_missing),
        "stale_references": stale,
        "skills_not_run": [s for s in SKILLS if s not in files],
    }


# ---------------------------------------------------------------- diff

def latest_history_dir(audit_dir, current_audit_id):
    history = pathlib.Path(audit_dir) / "history"
    if not history.is_dir():
        return None
    candidates = []
    for d in history.iterdir():
        if not d.is_dir() or d.name == current_audit_id:
            continue
        starts = []
        for p in d.glob("*.json"):
            try:
                starts.append(load_json(p).get("run", {}).get("started_at", ""))
            except RollupError:
                continue
        if starts:
            candidates.append((max(starts), d))
    return max(candidates)[1] if candidates else None


def diff_against(previous_dir, findings, ran_skills, audit_dir=None):
    """Compare open findings by id. A previous finding whose owner skill did not
    run this time is 'not_rechecked', never 'fixed'."""
    prev_open, prev_audit = {}, None
    for p in sorted(pathlib.Path(previous_dir).glob("*.json")):
        data = load_json(p)
        if "findings" not in data:
            continue
        prev_audit = prev_audit or data.get("audit_id")
        for f in data["findings"]:
            if f.get("status") in OPEN:
                prev_open[f["id"]] = f
    now_open = {f["id"]: f["title"] for f in findings if f["status"] in OPEN}
    fixed, not_rechecked = [], []
    for i in sorted(prev_open):
        if i in now_open:
            continue
        row = {"id": i, "title": prev_open[i].get("title", "")}
        (fixed if prev_open[i].get("owner_skill") in ran_skills else not_rechecked).append(row)
    return {
        "previous_audit_id": prev_audit,
        "previous_dir": _relative(previous_dir, audit_dir),
        "fixed": fixed,
        "new": [{"id": i, "title": now_open[i]} for i in sorted(now_open) if i not in prev_open],
        "still_open": [{"id": i, "title": now_open[i]} for i in sorted(now_open) if i in prev_open],
        "not_rechecked": not_rechecked,
    }


def _relative(path, base):
    path = pathlib.Path(path).resolve()
    if base is not None:
        try:
            return str(path.relative_to(pathlib.Path(base).resolve()))
        except ValueError:
            pass
    return str(path)


# ---------------------------------------------------------------- build

def build_rollup(audit_dir, previous=None, only_skills=None, now=None):
    audit_dir = pathlib.Path(audit_dir)
    context = load_json(audit_dir / "context.json")
    audit_id = context["audit_id"]
    files = load_findings(audit_dir / "findings", audit_id, only_skills)
    if not files:
        raise RollupError(f"no findings files in {audit_dir / 'findings'}")
    findings = merge_findings(files)
    findings.sort(key=lambda f: (SEVERITY_RANK[f["severity"]], f["owner_skill"], f["check_id"], f["id"]))
    skills = score_skills(findings, files)
    ran_scores = [s["score"] for s in skills if s["ran"] and s["score"] is not None]
    prev_dir = pathlib.Path(previous) if previous else latest_history_dir(audit_dir, audit_id)
    generated = (now or dt.datetime.now(dt.timezone.utc)).replace(microsecond=0).isoformat()
    return {
        "schema_version": "1.0",
        "audit_id": audit_id,
        "generated_at": generated,
        "report_language": context.get("report_language", "en"),
        "target": context.get("target", {}),
        "testing": {
            "owner_confirmed": context.get("permission", {}).get("owner_confirmed", False),
            "active_testing_allowed": context.get("permission", {}).get("active_testing_allowed", False),
        },
        "goal": context.get("organisation", {}).get("goal"),
        "overall": {
            "score": round(sum(ran_scores) / len(ran_scores)) if ran_scores else None,
            **verdict(findings, context),
        },
        "skills": skills,
        "top_actions": top_actions(findings),
        "needs_confirmation": needs_confirmation(findings),
        "cross_skill": [
            {"id": f["id"], "title": f["title"], "reported_in": f["reported_in"]}
            for f in findings if len(f["reported_in"]) > 1
        ],
        "frameworks": framework_coverage(findings, context),
        "limitations": limitations(files),
        "diff": diff_against(prev_dir, findings, set(files), audit_dir) if prev_dir else None,
        "findings": findings,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--audit-dir", default=".audit")
    parser.add_argument("--previous", help="history folder to diff against (default: latest)")
    parser.add_argument("--skills", help="comma-separated skills to include (default: all found)")
    parser.add_argument("--no-render", action="store_true", help="write JSON only")
    args = parser.parse_args(argv)

    only = set(args.skills.split(",")) if args.skills else None
    try:
        rollup = build_rollup(args.audit_dir, args.previous, only)
    except RollupError as exc:
        print(f"roll-up refused: {exc}", file=sys.stderr)
        return 2

    out = pathlib.Path(args.audit_dir) / "reports"
    out.mkdir(parents=True, exist_ok=True)
    (out / "hamu-audit.json").write_text(json.dumps(rollup, indent=2, ensure_ascii=False), encoding="utf-8")
    written = ["hamu-audit.json"]
    if not args.no_render:
        sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
        import render_md
        import render_html
        (out / "hamu-audit.md").write_text(render_md.render(rollup), encoding="utf-8")
        (out / "hamu-audit.html").write_text(render_html.render(rollup), encoding="utf-8")
        written += ["hamu-audit.md", "hamu-audit.html"]
    o = rollup["overall"]
    print(f"verdict: {o['verdict']}  score: {o['score']}  findings: {len(rollup['findings'])}")
    print("written: " + ", ".join(str(out / w) for w in written))
    return 0


if __name__ == "__main__":
    sys.exit(main())
