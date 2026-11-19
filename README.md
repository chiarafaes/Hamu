# Hamu audit skills

Audit skills for Claude that check websites, web apps and mobile apps for security, privacy, accessibility, performance, UX and search/AI visibility. Built with EU and Belgium depth, and global frameworks on top.

Each skill works on its own. Used together they share one scope, never check the same thing twice, and merge into one layered report.

> **Status: 0.1.0, phase 0.** The shared foundation is done. The audit checks are being built. Not ready for real audits yet.

## Free to use, not for sale

Hamu is free for everyone to use for noncommercial purposes: your own site or app, learning, research, nonprofits, schools and public bodies.

You may **not**, without a separate license from Hamu:

- sell, resell, sublicense or repackage these skills or their content
- include them in a paid product, plugin, course or service
- use them to deliver paid work, such as paid audits or client reports

Want to use Hamu commercially? Open a GitHub issue with the label `license` and tell us what you have in mind.

| Part | License |
|---|---|
| Code, schemas, scripts, SKILL.md files | [PolyForm Noncommercial 1.0.0](LICENSE.md) |
| Reference content (`shared/contract/`, `references/`) | [CC BY-NC-SA 4.0](LICENSE-CONTENT.md) |

Copyright (c) 2026 Hamu (VAT BE 1008.566.012). All rights not granted by these licenses are reserved.

## Skills

| Skill | Covers |
|---|---|
| `hamu-security-privacy` | GDPR, Belgian cookie rules (GBA/APD), EU consumer law, Belgian Code of Economic Law, AI Act transparency, NIS2 (BE), CRA, DORA, PCI DSS, OWASP ASVS / Top 10 / MASVS, readiness for SOC 2, ISO 27001, ISO 42001, HIPAA |
| `hamu-accessibility` | WCAG 2.2, EN 301 549, European Accessibility Act, Web Accessibility Directive, ADA, Section 508, accessibility statement |
| `hamu-performance-ux` | Core Web Vitals, loading, responsive layout, navigation, hierarchy, forms, CTAs, trust signals, conversion |
| `hamu-seo-visibility` | Technical SEO, content and E-E-A-T, structured data, AEO, GEO, AIO, SXO, local SEO, AI crawlers |
| `hamu-audit-rollup` | Merges all findings into one report: Markdown, HTML dashboard, Word/PDF, go/no-go verdict |

## How it works

1. **Three scoping questions** (where you operate, what the product does, who you are and why you audit) plus auto-detection decide which rules apply.
2. Each skill writes findings in one shared JSON format to `.audit/`.
3. The roll-up merges them, removes duplicates and builds one report with an executive layer and a technical layer.
4. **Guardrails mode:** while you build, the skills give short, concrete pointers instead of a full audit.

Testing is **passive by default**. Active security tests only run when you confirm you own the target and allow them.

## Install

In Claude Code:

```
/plugin marketplace add <github-user>/hamu
/plugin install hamu-audit@hamu
```

## Repository layout

```
.claude-plugin/marketplace.json
plugins/hamu-audit/
  .claude-plugin/plugin.json
  shared/            source of truth: contract, schemas, examples
  skills/<skill>/    SKILL.md + references (shared contract copied into references/_shared)
scripts/sync-shared.sh
scripts/validate.py
```

Edit shared files only in `plugins/hamu-audit/shared/`, then run `scripts/sync-shared.sh`. CI runs `scripts/sync-shared.sh --check` and `scripts/validate.py`.

## Contributing and questions

Use GitHub issues for bugs, outdated rules, new checks and license requests. Contributions are welcome. By opening a pull request you agree that Hamu may include your contribution under the licenses above.

## Important

Hamu gives readiness checks, not legal advice, and not a certification. See [DISCLAIMER.md](DISCLAIMER.md).

Standards are referenced by id. Hamu does not reproduce ISO, AICPA or PCI SSC text. OWASP and W3C material is referenced and paraphrased, with attribution.
