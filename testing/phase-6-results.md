# Phase 6 results

Date: 2026-11-19. Runtime: Claude Code. Testing: passive only.

No personal data or target names are recorded here. Full reports stay in the git-ignored `.audit/` folder of the machine that ran the test.

## Targets

| Target | Type | Owner | Skills run |
|---|---|---|---|
| A | Public website of a small Belgian service business (10 pages, two languages) | Repository owner, permission given | all four + roll-up |
| B | This repository (Python scripts, CI workflow, no dependencies) | Repository owner | hamu-security-privacy, code checks only |
| C | Claude app run of hamu-security-privacy on target A | Repository owner | done |

## Target A in numbers

54 findings after merging: 34 pass, 2 fail, 10 warn, 5 needs manual, 3 not tested. Verdict: go, with 5 findings marked for legal review. Scores: security and privacy 86, accessibility 100, performance and UX 99, SEO and AI visibility 98, overall 96.

Site-specific issues are not listed here because this repository is public. They are in the local roll-up report and were shared with the site owner.

## Target B

No secrets (pattern search, gitleaks not installed), no unsafe Python calls, no HTML sinks, no third-party dependencies. One finding: CI actions pinned by tag, now pinned by commit SHA.

## Problems found in Hamu and what changed

| # | Problem | Kind | Fix |
|---|---|---|---|
| 1 | Roll-up skill score was the mean of area scores, so five open medium issues still gave 99 to 100 | Scoring | Skill score is now 100 minus all deductions (as `severity.md` says). Overall 100 became 96 on target A. Tests updated. |
| 2 | Verdict "go" did not mention open legal-review items | Reporting | Reasons now state how many open findings need legal review. |
| 3 | `validate.py .audit` tried to validate raw evidence files | Bug | Evidence and history folders are skipped. |
| 4 | Regex HTML parsing missed meta tags with a different attribute order | Method | `crawl-method.md` requires a real HTML parser. |
| 5 | Keyword matching of the privacy notice missed rights written in other words | Method | SP.PRIVACY.CONTENT says to read the notice in full. |
| 6 | Raw tap-target sizes flagged inline text links | False positive | A11Y.TARGET.SIZE uses axe `target-size`, which applies the inline exception. |
| 7 | Cookie banner measured during an intro animation (0 by 0 px) | False positive | SP.CONSENT.REJECT measures after the intro, `performance-method.md` covers intros. |
| 8 | LCP element was the intro SVG, not real content | Misleading metric | `cwv.md` asks to check the LCP element and report when real content shows. |
| 9 | Anonymous PageSpeed Insights API quota exhausted | Tool gap | Playwright lab fallback with CDP throttling documented. |
| 10 | Legal identity check expected legal form and RPR from a sole trader | False positive | SP.LEGAL.IDENTITY and `be-cel.md` split legal persons and natural persons. |
| 11 | HTTPS check used one severity for every case | Calibration | High only when personal data can be sent over HTTP, else medium. |
| 12 | Withdrawal check did not consider free cancellation without payment | Calibration | Warn with legal review in that case. |
| 13 | No sector value for small service businesses | Schema | Added retail, hospitality, personal_services, professional_services (non-breaking). |

## Target C: Claude app versus Claude Code

Same skill, same site, same day. The app used the built-in browser, DNS over HTTPS and the SSL Labs website. Its shell had no network access to the target, and the fixed path probe was blocked in the session. Both runs marked what they could not test.

| Area | What the comparison showed | Change in Hamu |
|---|---|---|
| Scoring | Both runs scored with the same `severity.md` rules; totals differed only because the app produced more findings | none needed |
| Verdict | The app summary said go, but the rules gave no-go because a style-only banner finding carried the default severity high | SP.CONSENT.REJECT severity for that case set to medium |
| Consent withdrawal | One runtime saw a timing-dependent result the other did not | Flow repeated with two timings, consent script read |
| Consent record | Only one run looked at the stored consent value | New passive step: date, version, expiry |
| Privacy notice | One run missed an item on the checklist | Rights and legal basis ticked one by one |
| DNSSEC | One run used a method that hides signatures | DS record at the parent, or DoH AD flag |
| Things the app could not measure (redirect with cached HSTS, path probes) | Marked needs_manual or not_tested with a test script | none needed |
| Side effects | The app cleared site storage in the user's browser and sent an analytics hit | Browser hygiene rules in the run protocol |
| Leftover data in the user's browser profile | Reported as a possible finding with low confidence | Profile leftovers are not evidence |
| skill_version | The app wrote an old version from a stale SKILL.md status line | Status lines synced, CI check added |

## Verification items resolved

- AI Omnibus: Regulation (EU) 2026/1744, Official Journal 24 July 2026, in force 27 July 2026.
- EAA micro-enterprises in Belgium: exempt until 28 June 2030.
- Belgian online withdrawal function: the earlier "Law of 19 July 2026" could not be confirmed. Secondary sources say the bill was not yet published in September 2026. References corrected.
- GBA/APD cookie lifetime: no fixed number found. Long lifetimes are a warn with legal review.

## Not covered

- Screen reader and full keyboard walk-through (needs a human).
- Field Core Web Vitals (no CrUX data for a low-traffic site).
- Google Business Profile and Search Console (need the owner).
- PDF output was generated in phase 5 but not visually inspected.
