# Claude app test (phase 6)

Goal: check that one Hamu skill works in the Claude app with browser tools only, and that it degrades honestly when local tools are missing.

## 1. Package the skill

From the repo root:

```bash
cd plugins/hamu-audit/skills && zip -r ~/Desktop/hamu-security-privacy.zip hamu-security-privacy -x "*.DS_Store"
```

The zip contains `SKILL.md` and `references/` including `references/_shared/`.

## 2. Install in the Claude app

1. Open Claude (web or desktop), Settings, Capabilities, Skills.
2. Upload `hamu-security-privacy.zip`.
3. Make sure the skill is switched on, and that a browser tool (Claude in Chrome or the built-in browser) is available in the chat.

## 3. Run

Start a new chat and send:

> Run a passive security and privacy audit of https://<your site>. I own the site. Passive only.

Answer the intake questions. When the skill asks for the scope, confirm it.

## 4. Fill in the log

Copy this table into your reply to Claude Code, or into an issue.

| Item | Result |
|---|---|
| Date and Claude app version | |
| Browser tool used | Claude in Chrome / built-in browser / none |
| Did the skill load (mentions Hamu, reads references)? | yes / no |
| Intake: number of questions asked | |
| Permission question asked? | yes / no |
| Scope summary shown? | yes / no |
| Consent check run in the browser (before and after reject)? | yes / no / not_tested |
| Checks marked `not_tested` because a tool was missing | list |
| Any check that claimed a result without evidence | list |
| Findings JSON produced (or offered as a file)? | yes / no |
| Report produced, executive layer first? | yes / no |
| Disclaimer present? | yes / no |
| Words "compliant" or "certified" used? | yes / no |
| Time from start to report | minutes |
| Anything confusing or wrong | free text |

## 5. Compare

Claude Code results for the same site are in `.audit/` on the machine that ran phase 6 (not in git). The app run passes when:
- the same high and medium findings appear, or are marked `not_tested` with a reason,
- no finding claims evidence the app could not collect,
- the disclaimer is present and the words "compliant" and "certified" are absent.
