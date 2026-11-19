---
framework: WAD, EAA
name: Accessibility statement content and draft template
last_verified: 2026-11-19
sources:
  - https://eur-lex.europa.eu/eli/dec_impl/2018/1523/oj
  - https://eur-lex.europa.eu/eli/dir/2019/882/oj
  - https://www.w3.org/WAI/planning/statements/
  - https://bosa.belgium.be/en/accessibility-statement
status: WAD model statement verified; EAA Annex V wording paraphrased
---

# Accessibility statement

## What the law asks

| Item | WAD (public sector, Implementing Decision 2018/1523) | EAA (private B2C services, Annex V) |
|---|---|---|
| Where | Linked from every page (often the footer), in an app: store page or in-app | In the general terms and conditions or an equivalent place, in an accessible format, kept as long as the service runs |
| Conformance status | Fully, partially or not compliant with EN 301 549 / WCAG | General description of the service in accessible formats, and how it meets the accessibility requirements |
| Non-accessible content | List, with reason: non-compliance, disproportionate burden, or out of scope. Accessible alternatives where they exist | Disproportionate burden claims, when relied on |
| Preparation | Date of preparation and last review, method (self-assessment or third party) | - |
| Feedback | Contact to report barriers and to request inaccessible content | Support services give accessibility information (Annex I) |
| Enforcement | Link to the enforcement procedure | Name of the market surveillance authority is good practice (FPS Economy in Belgium) |
| Review | At least once a year | Keep up to date |

## How the skill drafts a statement

Only when the user asks. The draft is a starting point, never a legal declaration.

1. Conformance status from findings: any open `fail` on an A or AA criterion means "partially compliant". Many failures on core journeys means "not compliant". "Fully compliant" only after a full manual audit, so Hamu never writes it on its own.
2. List non-accessible content grouped by page type, in plain language, with the planned fix date if the user gives one.
3. Method: "Self-assessment with automated tools and manual checks (Hamu audit, date)." Name the tools.
4. Ask the user for the feedback contact and, for public bodies, the enforcement link of their level (federal, region, community).
5. Write it in the language(s) of the site.

## Template (fill in, keep plain language)

```markdown
# Accessibility statement

<Organisation> wants <website or app name> to be usable by everyone. This statement covers <URL or app name>.

## How accessible is this website?
This website is <fully / partially / not> compliant with the European standard EN 301 549 and WCAG 2.2 level AA.

## What is not accessible yet?
- <Problem in plain words>. <Who it affects>. We plan to fix this by <date>.
- ...

## Alternatives
If you cannot use part of this website, contact us at <email / phone> and we will give you the information another way.

## How we checked
We checked this website on <date> with <method: self-assessment, automated tools and manual tests / external audit by ...>. We last reviewed this statement on <date>.

## Feedback and contact
Did you find a barrier we do not mention? Tell us at <contact>. We answer within <n> working days.

## Enforcement
<Public sector: link to the enforcement procedure of the competent authority.>
<Private sector: The authority for accessibility of products and services in Belgium is the FPS Economy.>
```

Check id for the draft: none. The draft is an output, the related checks are A11Y.STATEMENT.*.
