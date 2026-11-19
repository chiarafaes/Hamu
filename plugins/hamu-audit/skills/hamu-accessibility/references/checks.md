---
last_verified: 2026-11-19
owner: hamu-accessibility
prefix: A11Y.
---

# Check catalogue: hamu-accessibility

Every check this skill owns. Ids follow `ownership-matrix.md` (`A11Y.DOMAIN.CHECK`). The target is WCAG 2.2 level AA. AAA criteria are reported as `info` advisories.

Attribution for reports: "Success criterion numbers and names from W3C WCAG 2.2, https://www.w3.org/TR/WCAG22/. Copyright W3C."

## How to read this file

| Column | Meaning |
|---|---|
| Id | `check_id` written to the finding. |
| Check | What passes. |
| SC | WCAG 2.2 success criterion number(s). |
| Lvl | A, AA or AAA. |
| Since | WCAG version that added the criterion (2.0, 2.1, 2.2). Decides which laws it maps to, see below. |
| Sev | Default severity before modifiers in `severity.md`. |
| Auto | axe-core rule ids that test it (partly or fully). `-` = no reliable rule, use the manual method. |
| How | `A` = automated, `H` = heuristic on DOM or screenshot, `M` = manual (`needs_manual` with a script from `manual-test-script.md`). |

## Framework mapping rule (applies to every check)

Write these to `frameworks[]`, only for frameworks with status `applies` or `likely`:

| Framework | Ref | Relation | Condition |
|---|---|---|---|
| WCAG22 | the SC number, level in `level` | requirement for A and AA, best_practice for AAA | always |
| EN301549 | `9.<SC>` for web content, `10.<SC>` for non-web documents, `11.<SC>` for native software and apps | requirement | EAA or WAD applies. v3.2.1 maps to WCAG 2.1: SC with Since 2.2 map only to v4.1.1, see `en301549.md` |
| EAA | `Annex I` | requirement | EAA applies |
| WAD | `Art. 4` | requirement | WAD applies |
| ADA | `Title III` or `Title II (28 CFR 35.200)` | requirement for Title II, best_practice for Title III | ADA applies and Since is 2.0 or 2.1 |
| S508 | `E205.4` | requirement | S508 applies and Since is 2.0 |

Rules:
- A failing A or AA criterion with a law that `applies` is at least `medium` (severity modifier).
- One finding per check per pattern. Thirty images without alt in the same template is one finding, with sample locations.
- Automated tools find roughly a third of issues. Always add the manual checks for the main user journey. Never report "no issues" from axe alone.
- Low-confidence heuristic findings go to "Needs confirmation".

---

## STRUCT: structure, semantics, page level

| Id | Check | SC | Lvl | Since | Sev | Auto | How |
|---|---|---|---|---|---|---|---|
| A11Y.STRUCT.TITLE | Each page has a unique, descriptive `<title>`. | 2.4.2 | A | 2.0 | medium | document-title | A |
| A11Y.STRUCT.LANDMARK | Page uses landmarks (header, nav, main, footer). One `main`. Content sits inside landmarks. | 1.3.1, 2.4.1 | A | 2.0 | medium | landmark-one-main, region, landmark-unique | A |
| A11Y.STRUCT.SKIP | A skip link or landmarks let keyboard users bypass repeated blocks. The skip link is visible on focus and works. | 2.4.1 | A | 2.0 | medium | bypass | A + M |
| A11Y.STRUCT.HEADINGS | Headings exist, describe their section, and their levels reflect the structure. | 1.3.1, 2.4.6 | A, AA | 2.0 | medium | empty-heading, heading-order (best practice), page-has-heading-one (best practice) | A + H |
| A11Y.STRUCT.SEMANTICS | Lists, tables, quotes and similar content use real markup. Data tables have header cells. Layout tables are not used. | 1.3.1 | A | 2.0 | medium | list, listitem, td-headers-attr, th-has-data-cells, definition-list | A |
| A11Y.STRUCT.ORDER | The reading order in the DOM matches the visual order. | 1.3.2 | A | 2.0 | medium | - | H |
| A11Y.STRUCT.SENSORY | Instructions do not rely only on shape, size, position or sound ("click the round button on the right"). | 1.3.3 | A | 2.0 | low | - | H |
| A11Y.STRUCT.ORIENTATION | Content works in portrait and landscape. | 1.3.4 | AA | 2.1 | medium | css-orientation-lock | A |
| A11Y.STRUCT.RESIZE | Text can be zoomed to 200% without loss of content or function. Viewport does not block zoom. | 1.4.4 | AA | 2.0 | medium | meta-viewport, meta-viewport-large | A + M |
| A11Y.STRUCT.REFLOW | At 320 CSS px wide (400% zoom of 1280 px) content reflows without horizontal scrolling, except content that needs two dimensions. | 1.4.10 | AA | 2.1 | high | - | M (resize to 320 px and screenshot) |
| A11Y.STRUCT.SPACING | No loss of content when line height 1.5, paragraph spacing 2, letter spacing 0.12 and word spacing 0.16 times the font size are applied. | 1.4.12 | AA | 2.1 | low | - | H (inject spacing CSS, compare) |
| A11Y.STRUCT.LINK-NAME | Link text, alone or with its context, says where the link goes. No bare "click here" or "read more" without context. | 2.4.4 | A | 2.0 | medium | link-name | A + H |
| A11Y.STRUCT.MULTI-WAY | More than one way to find a page (navigation, search, sitemap), except for steps in a process. | 2.4.5 | AA | 2.0 | low | - | H |
| A11Y.STRUCT.CONSISTENT-NAV | Repeated navigation keeps the same order across pages. | 3.2.3 | AA | 2.0 | low | - | H (compare 3 pages) |
| A11Y.STRUCT.CONSISTENT-ID | Components with the same function have the same name and icon across pages. | 3.2.4 | AA | 2.0 | low | - | H |
| A11Y.STRUCT.FRAME | Iframes have a title that describes them. | 4.1.2 | A | 2.0 | low | frame-title | A |

## IMG: images and graphics

| Id | Check | SC | Lvl | Since | Sev | Auto | How |
|---|---|---|---|---|---|---|---|
| A11Y.IMG.ALT | Informative images have a text alternative that conveys the same information. Decorative images have empty alt or are CSS. | 1.1.1 | A | 2.0 | high | image-alt, role-img-alt, svg-img-alt, area-alt, input-image-alt, object-alt | A + H (judge quality of alt text) |
| A11Y.IMG.ICON | Icon-only buttons and links have an accessible name. | 1.1.1, 4.1.2 | A | 2.0 | high | button-name, link-name | A |
| A11Y.IMG.COMPLEX | Charts, maps and infographics have a long description or data table nearby. | 1.1.1 | A | 2.0 | medium | - | H |
| A11Y.IMG.TEXT | No images of text where real text could be used (logos excepted). | 1.4.5 | AA | 2.0 | low | - | H |
| A11Y.IMG.CAPTCHA | A CAPTCHA offers an alternative in another modality, or a non-CAPTCHA option. | 1.1.1 | A | 2.0 | high | - | H |

## MEDIA: audio and video

| Id | Check | SC | Lvl | Since | Sev | Auto | How |
|---|---|---|---|---|---|---|---|
| A11Y.MEDIA.ALT | Prerecorded audio-only has a transcript. Video-only has a transcript or audio track. | 1.2.1 | A | 2.0 | medium | - | H |
| A11Y.MEDIA.CAPTION | Prerecorded video with sound has synchronised captions. | 1.2.2 | A | 2.0 | high | video-caption | A + M |
| A11Y.MEDIA.DESCRIPTION | Prerecorded video has audio description where visual information is not in the soundtrack. | 1.2.3, 1.2.5 | A, AA | 2.0 | medium | - | M |
| A11Y.MEDIA.LIVE | Live video with sound has live captions. | 1.2.4 | AA | 2.0 | medium | - | M |
| A11Y.MEDIA.AUTOPLAY | Audio that plays for more than 3 seconds can be paused or stopped, or its volume set independently. | 1.4.2 | A | 2.0 | medium | no-autoplay-audio | A |

## COLOR: colour and contrast

| Id | Check | SC | Lvl | Since | Sev | Auto | How |
|---|---|---|---|---|---|---|---|
| A11Y.COLOR.CONTRAST | Text contrast at least 4.5:1, or 3:1 for large text (24 px, or 18.66 px bold). | 1.4.3 | AA | 2.0 | medium | color-contrast | A + H (text on images and gradients) |
| A11Y.COLOR.NON-TEXT | UI component boundaries, focus indicators, icons and chart parts needed to understand content have 3:1 against adjacent colours. | 1.4.11 | AA | 2.1 | medium | - | H |
| A11Y.COLOR.ONLY | Colour is not the only way to convey information (errors, required fields, links in text, chart series). | 1.4.1 | A | 2.0 | medium | link-in-text-block | A + H |
| A11Y.COLOR.ENHANCED | Text contrast at least 7:1 (advisory). | 1.4.6 | AAA | 2.0 | info | color-contrast-enhanced | A |

## KBD: keyboard

| Id | Check | SC | Lvl | Since | Sev | Auto | How |
|---|---|---|---|---|---|---|---|
| A11Y.KBD.ACCESS | Every function works with a keyboard alone: menus, dialogs, carousels, custom selects, cookie banner, checkout. | 2.1.1 | A | 2.0 | high | scrollable-region-focusable, nested-interactive | M (tab through the main journey) |
| A11Y.KBD.TRAP | Focus never gets stuck. Dialogs and embeds can be left with standard keys. | 2.1.2 | A | 2.0 | high | - | M |
| A11Y.KBD.SHORTCUT | Single-character shortcuts can be turned off, remapped, or only work on focus. | 2.1.4 | A | 2.1 | low | - | H (look for keydown handlers on document) |
| A11Y.KBD.NATIVE | Interactive elements are native (`button`, `a href`, `input`) or have role, tabindex and key handlers. No click handlers on `div` without them. | 2.1.1, 4.1.2 | A | 2.0 | high | - | H, code review in Claude Code |

## FOCUS: focus and context changes

| Id | Check | SC | Lvl | Since | Sev | Auto | How |
|---|---|---|---|---|---|---|---|
| A11Y.FOCUS.VISIBLE | The keyboard focus is always visible. No `outline: none` without a replacement. | 2.4.7 | AA | 2.0 | high | - | M + H (CSS search for outline removal) |
| A11Y.FOCUS.ORDER | Focus order follows a logical order. No positive `tabindex`. | 2.4.3 | A | 2.0 | medium | tabindex | A + M |
| A11Y.FOCUS.OBSCURED | The focused element is not fully hidden by sticky headers, cookie banners or chat widgets. | 2.4.11 | AA | 2.2 | medium | - | M |
| A11Y.FOCUS.DIALOG | Opening a dialog moves focus into it. Closing returns focus to the trigger. | 2.4.3 | A | 2.0 | medium | - | M |
| A11Y.FOCUS.ON-FOCUS | Focusing an element does not change context (no automatic navigation or submit). | 3.2.1 | A | 2.0 | medium | - | M |
| A11Y.FOCUS.ON-INPUT | Changing a setting does not change context unless the user was told (for example a select that navigates). | 3.2.2 | A | 2.0 | medium | - | M |
| A11Y.FOCUS.HOVER | Content shown on hover or focus (tooltips, menus) can be dismissed, hovered and stays until dismissed. | 1.4.13 | AA | 2.1 | low | - | M |
| A11Y.FOCUS.APPEARANCE | Focus indicator is at least as large as a 2 px perimeter with 3:1 change of contrast (advisory). | 2.4.13 | AAA | 2.2 | info | - | H |

## FORM: forms and errors

| Id | Check | SC | Lvl | Since | Sev | Auto | How |
|---|---|---|---|---|---|---|---|
| A11Y.FORM.LABEL | Every field has a visible label tied to it in code. Placeholder alone is not a label. | 1.3.1, 3.3.2, 4.1.2 | A | 2.0 | high | label, select-name, form-field-multiple-labels | A + H |
| A11Y.FORM.REQUIRED | Required fields are indicated in text or with a marker explained on the page, and in code (`required` or `aria-required`). | 3.3.2 | A | 2.0 | medium | - | H |
| A11Y.FORM.GROUP | Related controls (radio groups, date parts) are grouped with `fieldset` and `legend` or a group role with a name. | 1.3.1 | A | 2.0 | medium | - | H |
| A11Y.FORM.AUTOCOMPLETE | Fields for user data have a correct `autocomplete` value. | 1.3.5 | AA | 2.1 | low | autocomplete-valid | A |
| A11Y.FORM.ERROR | Errors are identified in text, next to the field, linked with `aria-describedby`, and announced. | 3.3.1 | A | 2.0 | high | - | M (submit an empty form on staging or with consent; passive: inspect validation code) |
| A11Y.FORM.SUGGEST | Error messages suggest how to fix when known ("Enter a date as DD/MM/YYYY"). | 3.3.3 | AA | 2.0 | medium | - | M |
| A11Y.FORM.PREVENT | Legal, financial or data-changing submissions can be reviewed, corrected or reversed. | 3.3.4 | AA | 2.0 | medium | - | M |
| A11Y.FORM.REDUNDANT | Information already entered in the same process is filled in or selectable, not asked again. | 3.3.7 | A | 2.2 | low | - | M |
| A11Y.FORM.AUTH | Login does not need a cognitive function test (memorising, transcribing, puzzles) without an alternative. Paste and password managers work. | 3.3.8 | AA | 2.2 | high | - | M + H (look for `onpaste` blocking, split OTP fields without paste) |

## ARIA: names, roles, values, status

| Id | Check | SC | Lvl | Since | Sev | Auto | How |
|---|---|---|---|---|---|---|---|
| A11Y.ARIA.NAME | Every interactive element has an accessible name, role and state that assistive tech can read (buttons, toggles, tabs, accordions). | 4.1.2 | A | 2.0 | high | button-name, aria-command-name, aria-toggle-field-name, aria-input-field-name | A |
| A11Y.ARIA.VALID | ARIA attributes and roles are valid, allowed and complete. No `aria-hidden` on focusable content. | 4.1.2 | A | 2.0 | medium | aria-valid-attr, aria-valid-attr-value, aria-required-attr, aria-allowed-attr, aria-roles, aria-hidden-focus, aria-required-children, aria-required-parent | A |
| A11Y.ARIA.LABEL-IN-NAME | The accessible name contains the visible label text. | 2.5.3 | A | 2.1 | medium | label-content-name-mismatch (experimental) | A + H |
| A11Y.ARIA.STATUS | Status messages (added to cart, search results count, form saved) are announced without moving focus. | 4.1.3 | AA | 2.1 | medium | - | M + H (look for `role="status"` or `aria-live`) |
| A11Y.ARIA.DUPLICATE-ID | Ids referenced by ARIA or labels are unique. | 1.3.1, 4.1.2 | A | 2.0 | low | duplicate-id-aria | A |

## TARGET: pointer and touch

| Id | Check | SC | Lvl | Since | Sev | Auto | How |
|---|---|---|---|---|---|---|---|
| A11Y.TARGET.SIZE | Targets are at least 24 by 24 CSS px, or have enough spacing, with the exceptions in the SC. Use axe `target-size`, not raw element sizes: links inside a sentence are exempt, and a raw size check flags them falsely. | 2.5.8 | AA | 2.2 | medium | target-size | A |
| A11Y.TARGET.GESTURE | Multipoint or path gestures (pinch, swipe) have a single-pointer alternative. | 2.5.1 | A | 2.1 | medium | - | M |
| A11Y.TARGET.CANCEL | Actions fire on release (up event), not on press, or can be aborted. | 2.5.2 | A | 2.1 | low | - | H |
| A11Y.TARGET.DRAG | Dragging has a single-pointer alternative (buttons, inputs). | 2.5.7 | AA | 2.2 | medium | - | M |
| A11Y.TARGET.ENHANCED | Targets at least 44 by 44 CSS px (advisory). | 2.5.5 | AAA | 2.1 | info | - | H |

## MOTION: time, movement, flashing

| Id | Check | SC | Lvl | Since | Sev | Auto | How |
|---|---|---|---|---|---|---|---|
| A11Y.MOTION.PAUSE | Moving, blinking or auto-updating content that lasts over 5 seconds (carousels, tickers, background video) can be paused, stopped or hidden. | 2.2.2 | A | 2.0 | medium | blink, marquee | A + M |
| A11Y.MOTION.TIMING | Time limits (session timeout, timed offers in checkout) can be turned off, adjusted or extended. | 2.2.1 | A | 2.0 | medium | meta-refresh | A + M |
| A11Y.MOTION.FLASH | Nothing flashes more than three times per second. | 2.3.1 | A | 2.0 | high | - | M |
| A11Y.MOTION.ACTUATION | Functions triggered by device motion (shake, tilt) have a UI alternative and can be turned off. | 2.5.4 | A | 2.1 | low | - | M |
| A11Y.MOTION.REDUCED | Non-essential animation respects `prefers-reduced-motion` (advisory, SC 2.3.3 AAA). | 2.3.3 | AAA | 2.1 | info | - | H (CSS search) |

## LANG: language

| Id | Check | SC | Lvl | Since | Sev | Auto | How |
|---|---|---|---|---|---|---|---|
| A11Y.LANG.PAGE | `<html lang>` is set and valid, and matches the main language of the page. | 3.1.1 | A | 2.0 | medium | html-has-lang, html-lang-valid, html-xml-lang-mismatch | A |
| A11Y.LANG.PARTS | Passages in another language have their own `lang` (for example an English quote on a Dutch page, or the French version link). | 3.1.2 | AA | 2.0 | low | valid-lang | A + H |

## DOC: documents (PDF, Office)

| Id | Check | SC | Lvl | Since | Sev | Auto | How |
|---|---|---|---|---|---|---|---|
| A11Y.DOC.TAGGED | Downloadable PDFs that users need (forms, terms, price lists) are tagged, have a title, language, reading order and alt text. | 1.1.1, 1.3.1, 2.4.2, 3.1.1 | A | 2.0 | medium | - | A in Claude Code (`npx` PDF checker or `pdfinfo`, if the user agrees), else M |
| A11Y.DOC.ALTERNATIVE | Important documents are also available as accessible HTML, or the statement lists them as exceptions. WAD exempts many office files published before 23 September 2018. | 1.1.1 | A | 2.0 | low | - | H |

## MOBILE: native apps

| Id | Check | SC | Lvl | Since | Sev | Auto | How |
|---|---|---|---|---|---|---|---|
| A11Y.MOBILE.LABELS | Controls have accessibility labels (`accessibilityLabel`, `contentDescription`, `Semantics`). | 1.1.1, 4.1.2 | A | 2.0 | high | - | Code review, or Accessibility Inspector / Accessibility Scanner (M) |
| A11Y.MOBILE.DYNAMIC-TYPE | Text scales with system font size (Dynamic Type, sp units) without clipping. | 1.4.4 | AA | 2.0 | medium | - | Code review + M |
| A11Y.MOBILE.SCREENREADER | Main journey works with VoiceOver and TalkBack: order, names, states, no unlabelled custom views. | 1.3.1, 2.4.3, 4.1.2 | A | 2.0 | high | - | M |
| A11Y.MOBILE.TOUCH | Touch targets meet the 24 px rule (platform guidance: 44 pt iOS, 48 dp Android, advisory). | 2.5.8 | AA | 2.2 | medium | - | Code review |

## STATEMENT: accessibility statement and feedback

| Id | Check | SC | Lvl | Since | Sev | Auto | How |
|---|---|---|---|---|---|---|---|
| A11Y.STATEMENT.EXISTS | An accessibility statement is published and linked from every page (WAD), or the EAA information on how the service meets the accessibility requirements is available (EAA Annex V). | - | - | - | medium | - | H |
| A11Y.STATEMENT.CONTENT | The statement has the required content (see `statement.md`): conformance status, non-accessible content with reasons, date and method of assessment, feedback mechanism, enforcement procedure. | - | - | - | medium | - | H |
| A11Y.STATEMENT.FEEDBACK | A working feedback channel lets users report barriers and ask for content in another format. | - | - | - | medium | - | H |
| A11Y.STATEMENT.HELP | Help (contact, chat, FAQ) appears in the same relative place on pages that offer it. | 3.2.6 | A | 2.2 | low | - | H |

For STATEMENT checks, `frameworks` maps to WAD (`Art. 7`) or EAA (`Annex V`, `Art. 13`), not to a WCAG SC (except A11Y.STATEMENT.HELP).

## COG: cognitive access

| Id | Check | SC | Lvl | Since | Sev | Auto | How |
|---|---|---|---|---|---|---|---|
| A11Y.COG.PLAIN | Key content (terms, errors, instructions) uses plain language. Advisory, SC 3.1.5 is AAA. Required in spirit by EAA Annex I for service information. | 3.1.5 | AAA | 2.0 | info | - | H (readability score per language, sentence length) |
| A11Y.COG.ABBREV | Abbreviations and jargon are explained on first use (advisory). | 3.1.4 | AAA | 2.0 | info | - | H |
| A11Y.COG.CONSISTENT | Error messages and instructions are short and placed where users look. Linked with A11Y.FORM.* | - | - | - | info | - | H |

Readability for search is owned by SEO (`SEO.READ.*`). This skill owns plain language for cognitive access only.

---

## Coverage check

Every WCAG 2.2 level A and AA criterion (55) is covered by at least one check above. 4.1.1 Parsing is obsolete in WCAG 2.2 and is not tested. `scripts/check-content.py` fails CI when a criterion loses its check.

## Guardrails pointers by build task

At most 5 pointers, highest severity first, as concrete rules.

| Build task | Checks to draw from |
|---|---|
| Button, link, icon | A11Y.ARIA.NAME, A11Y.IMG.ICON, A11Y.KBD.NATIVE, A11Y.FOCUS.VISIBLE, A11Y.TARGET.SIZE |
| Form | A11Y.FORM.LABEL, A11Y.FORM.ERROR, A11Y.FORM.REQUIRED, A11Y.FORM.AUTOCOMPLETE, A11Y.ARIA.STATUS |
| Login and signup | A11Y.FORM.AUTH, A11Y.FORM.LABEL, A11Y.FORM.ERROR, A11Y.IMG.CAPTCHA, A11Y.MOTION.TIMING |
| Modal, dialog, cookie banner | A11Y.FOCUS.DIALOG, A11Y.KBD.TRAP, A11Y.KBD.ACCESS, A11Y.FOCUS.OBSCURED, A11Y.ARIA.NAME |
| Navigation and menu | A11Y.KBD.ACCESS, A11Y.STRUCT.SKIP, A11Y.STRUCT.LANDMARK, A11Y.FOCUS.HOVER, A11Y.STRUCT.CONSISTENT-NAV |
| Images and media | A11Y.IMG.ALT, A11Y.MEDIA.CAPTION, A11Y.MEDIA.AUTOPLAY, A11Y.MOTION.PAUSE, A11Y.IMG.TEXT |
| Colours, theme, design tokens | A11Y.COLOR.CONTRAST, A11Y.COLOR.NON-TEXT, A11Y.COLOR.ONLY, A11Y.FOCUS.VISIBLE |
| Layout and responsive | A11Y.STRUCT.REFLOW, A11Y.STRUCT.RESIZE, A11Y.STRUCT.ORDER, A11Y.STRUCT.SPACING, A11Y.TARGET.SIZE |
| Carousel, animation | A11Y.MOTION.PAUSE, A11Y.MOTION.REDUCED, A11Y.KBD.ACCESS, A11Y.MOTION.FLASH |
| Drag and drop, gestures | A11Y.TARGET.DRAG, A11Y.TARGET.GESTURE, A11Y.KBD.ACCESS |
| Mobile app screen | A11Y.MOBILE.LABELS, A11Y.MOBILE.DYNAMIC-TYPE, A11Y.MOBILE.TOUCH, A11Y.MOBILE.SCREENREADER |

## Pointers to other skills

| Observation | Owner check |
|---|---|
| Alt text missing also hurts image search | This skill owns it (A11Y.IMG.ALT). SEO links it. |
| Layout breaks at tablet or desktop sizes (not 320 px reflow) | PX.RESP.* |
| Form has too many fields or friction | PX.FORMUX.* |
| Cookie banner tracks before consent | SP.CONSENT.* |
| Slow pages, layout shift | PX.CWV.* |
| Readability for search intent | SEO.READ.* |
