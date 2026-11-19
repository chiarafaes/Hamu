---
framework: WCAG22
name: Web Content Accessibility Guidelines 2.2 (W3C Recommendation)
last_verified: 2026-11-19
sources:
  - https://www.w3.org/TR/WCAG22/
  - https://www.w3.org/WAI/WCAG22/Understanding/
  - https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/
  - https://www.w3.org/copyright/document-license-2023/
status: verified
licence_note: W3C documents may be referenced and quoted with attribution under the W3C Document License. Hamu uses SC numbers and short names, and paraphrases the requirement.
---

# WCAG 2.2

Published as a W3C Recommendation on 5 October 2023 (updated December 2024). Also approved as ISO/IEC 40500:2025. Backwards compatible: a page that meets 2.2 AA also meets 2.1 AA and 2.0 AA.

Attribution for reports: "WCAG 2.2 success criteria numbers and names, Copyright W3C, https://www.w3.org/TR/WCAG22/."

## Conformance

- Levels A, AA, AAA. Hamu target: AA. AAA is reported as `info`.
- Conformance applies to full pages and to complete processes. If one step of the checkout fails, the checkout fails.
- Five conformance requirements: level, full pages, complete processes, accessibility-supported ways of using technologies, non-interference.

## What changed from 2.1

New criteria (A and AA, tested): 2.4.11 Focus Not Obscured (Minimum), 2.5.7 Dragging Movements, 2.5.8 Target Size (Minimum), 3.2.6 Consistent Help, 3.3.7 Redundant Entry, 3.3.8 Accessible Authentication (Minimum).
New AAA (advisory): 2.4.12 Focus Not Obscured (Enhanced), 2.4.13 Focus Appearance, 3.3.9 Accessible Authentication (Enhanced).
Removed: 4.1.1 Parsing (obsolete, always satisfied for HTML).

## A and AA criteria (55)

| Principle | Criteria |
|---|---|
| 1 Perceivable | 1.1.1 Non-text Content (A) · 1.2.1 Audio-only and Video-only (A) · 1.2.2 Captions, Prerecorded (A) · 1.2.3 Audio Description or Media Alternative (A) · 1.2.4 Captions, Live (AA) · 1.2.5 Audio Description, Prerecorded (AA) · 1.3.1 Info and Relationships (A) · 1.3.2 Meaningful Sequence (A) · 1.3.3 Sensory Characteristics (A) · 1.3.4 Orientation (AA) · 1.3.5 Identify Input Purpose (AA) · 1.4.1 Use of Color (A) · 1.4.2 Audio Control (A) · 1.4.3 Contrast, Minimum (AA) · 1.4.4 Resize Text (AA) · 1.4.5 Images of Text (AA) · 1.4.10 Reflow (AA) · 1.4.11 Non-text Contrast (AA) · 1.4.12 Text Spacing (AA) · 1.4.13 Content on Hover or Focus (AA) |
| 2 Operable | 2.1.1 Keyboard (A) · 2.1.2 No Keyboard Trap (A) · 2.1.4 Character Key Shortcuts (A) · 2.2.1 Timing Adjustable (A) · 2.2.2 Pause, Stop, Hide (A) · 2.3.1 Three Flashes or Below Threshold (A) · 2.4.1 Bypass Blocks (A) · 2.4.2 Page Titled (A) · 2.4.3 Focus Order (A) · 2.4.4 Link Purpose, In Context (A) · 2.4.5 Multiple Ways (AA) · 2.4.6 Headings and Labels (AA) · 2.4.7 Focus Visible (AA) · 2.4.11 Focus Not Obscured, Minimum (AA) · 2.5.1 Pointer Gestures (A) · 2.5.2 Pointer Cancellation (A) · 2.5.3 Label in Name (A) · 2.5.4 Motion Actuation (A) · 2.5.7 Dragging Movements (AA) · 2.5.8 Target Size, Minimum (AA) |
| 3 Understandable | 3.1.1 Language of Page (A) · 3.1.2 Language of Parts (AA) · 3.2.1 On Focus (A) · 3.2.2 On Input (A) · 3.2.3 Consistent Navigation (AA) · 3.2.4 Consistent Identification (AA) · 3.2.6 Consistent Help (A) · 3.3.1 Error Identification (A) · 3.3.2 Labels or Instructions (A) · 3.3.3 Error Suggestion (AA) · 3.3.4 Error Prevention, Legal, Financial, Data (AA) · 3.3.7 Redundant Entry (A) · 3.3.8 Accessible Authentication, Minimum (AA) |
| 4 Robust | 4.1.2 Name, Role, Value (A) · 4.1.3 Status Messages (AA) |

## Version per law (used by the mapping rule in `checks.md`)

| Law or standard | WCAG version referenced |
|---|---|
| EN 301 549 v3.2.1 (harmonised for WAD and, until replaced, for EAA) | 2.1 A and AA |
| EN 301 549 v4.1.1 (published September 2026) | 2.2 A and AA |
| ADA Title II rule (28 CFR 35.200) | 2.1 AA |
| Section 508 (E205.4) | 2.0 AA |

Hamu tests 2.2 AA for every target, so one audit covers all of them. In the report, show which criteria are new in 2.2 so readers bound to an older version can see the difference.

## Tools

- axe-core (Deque, MPL 2.0): `npx @axe-core/cli <url>` or via Playwright (`@axe-core/playwright`). Tags: `wcag2a`, `wcag2aa`, `wcag21a`, `wcag21aa`, `wcag22aa`, `best-practice`.
- Lighthouse accessibility category uses axe-core under the hood.
- In the Claude app: inject axe-core from a CDN with the browser JS tool, only when the user allows it on that site.
