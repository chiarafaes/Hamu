---
framework: WAD
name: Web Accessibility Directive (Directive (EU) 2016/2102) and Belgian transposition
last_verified: 2026-11-19
sources:
  - https://eur-lex.europa.eu/eli/dir/2016/2102/oj
  - https://eur-lex.europa.eu/eli/dec_impl/2018/1523/oj
  - https://eur-lex.europa.eu/eli/dec_impl/2018/1524/oj
  - https://www.w3.org/WAI/policies/belgium/
  - https://bosa.belgium.be/en/accessibility-statement
status: directive and implementing decisions verified; Belgian federal law and control body verified with official statements; regional decree dates verify
---

# Web Accessibility Directive

## Scope

Websites and mobile apps of public sector bodies: state, regional and local authorities, bodies governed by public law, and associations of them. Bodies governed by public law can include subsidised organisations, schools and hospitals (check case by case, `legal_review: true`).

Exceptions (Art. 1(4)): office file formats published before 23 September 2018 unless needed for active administrative processes, prerecorded time-based media published before 23 September 2020, live media, online maps if the information is also given in an accessible way, third-party content not funded or controlled by the body, reproductions of heritage collections, extranets and intranets published before 23 September 2019 until substantially revised, archived content no longer updated.

## Belgium

- Federal: Law of 19 July 2018 on the accessibility of websites and mobile applications of public sector bodies. Control body: FPS BOSA accessibility department (Royal Decree of 5 September 2019).
- Regions and communities have their own decrees for their administrations (Flemish, French and German-speaking Communities, Walloon and Brussels-Capital Regions, French Community Commission). Exact decree dates: verify per region before citing.
- BOSA provides an accessibility check tool and a statement generator for federal bodies.

## Duties the checks use

| Duty | Where | Check |
|---|---|---|
| Websites and apps perceivable, operable, understandable, robust | Art. 4 | all WCAG-based checks via EN 301 549 |
| Accessibility statement, detailed, comprehensive, clear, kept up to date, linked from every page (apps: in the store or app) | Art. 7(1), Implementing Decision (EU) 2018/1523 | A11Y.STATEMENT.EXISTS, A11Y.STATEMENT.CONTENT |
| Feedback mechanism to report non-compliance and request inaccessible content | Art. 7(1)(b) | A11Y.STATEMENT.FEEDBACK |
| Link to the enforcement procedure | Art. 7(1)(c), Art. 9 | A11Y.STATEMENT.CONTENT |
| Monitoring by the member state (simplified and in-depth) | Art. 8, Implementing Decision (EU) 2018/1524 | context only |

Statement content: see `statement.md`.
