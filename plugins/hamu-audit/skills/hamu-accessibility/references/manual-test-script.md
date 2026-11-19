---
framework: WCAG22
name: Manual test scripts for needs_manual accessibility findings
last_verified: 2026-11-19
sources:
  - https://www.w3.org/WAI/test-evaluate/
  - https://www.w3.org/WAI/WCAG22/Understanding/
  - https://www.w3.org/WAI/test-evaluate/conformance/wcag-em/
status: method based on W3C WAI evaluation guidance (WCAG-EM); scripts are own words
---

# Manual test scripts

Use these when a check is `M`. Run them yourself where the runtime allows (Playwright keyboard events, browser tools, resize), else give them to the user as a task. Each script fits in the `needs_manual` finding's `detail_technical`.

## Sample (WCAG-EM style)

Test the same set of pages for every script:
1. Home page.
2. One page per template (product, article, category, search results, contact).
3. Every step of the main journey (signup, checkout, booking, contact form), up to the point where a real transaction would happen.
4. Pages with special content: video, forms, maps, PDFs that users must use.
5. Accessibility statement, privacy and terms pages.

Default 10 to 15 pages. Note the list in the report.

## Keyboard (A11Y.KBD.*, A11Y.FOCUS.*)

1. Put the mouse away. Reload the page.
2. Press Tab. The first stop should be a skip link or the first menu item. Focus must be visible on every stop.
3. Tab through the whole page. Write down any element you cannot reach, any stop where focus is invisible, and any jump in an illogical order.
4. Open every menu, dialog, accordion, tab panel and custom select with Enter or Space. Close dialogs with Escape. Focus should go into the dialog and come back to the trigger.
5. Check that nothing traps focus. Shift+Tab must also work.
6. Check that sticky headers, cookie banners and chat buttons never fully cover the focused element.
7. Complete the main journey with keyboard only.

In Claude Code: Playwright `page.keyboard.press("Tab")` in a loop, record `document.activeElement` and a screenshot per stop.

## Screen reader (A11Y.ARIA.*, A11Y.MOBILE.SCREENREADER)

Quick pass with one combination per platform: VoiceOver with Safari (macOS, iOS), NVDA with Firefox or Chrome (Windows), TalkBack with Chrome (Android).
1. Listen to the page title and the first heading.
2. Navigate by headings (VoiceOver rotor, NVDA H key). Is the outline logical?
3. Navigate by landmarks. Is there one main?
4. Tab to each button and link. Is the name clear without seeing the screen? Do toggles announce their state?
5. Fill in a form. Is every field announced with its label and required state? Submit with an error. Is the error announced?
6. Trigger a status change (add to cart, filter results). Is it announced without moving focus?

Claude cannot run a screen reader. Always `needs_manual`, confidence for related automated findings stays as measured.

## Zoom and reflow (A11Y.STRUCT.RESIZE, A11Y.STRUCT.REFLOW, A11Y.STRUCT.SPACING)

1. Set the viewport to 1280 px wide and zoom the browser to 200%. All text readable, nothing cut off, all functions usable.
2. Set the viewport to 320 CSS px wide (equal to 400% zoom). No horizontal scrolling for text content. Menus still usable.
3. Apply this CSS and check nothing is cut off or overlaps:
   `* { line-height: 1.5 !important; letter-spacing: 0.12em !important; word-spacing: 0.16em !important; } p { margin-bottom: 2em !important; }`

In Claude Code or the Claude app: resize the browser and screenshot. This part can run automatically, then confidence is medium.

## Colour (A11Y.COLOR.*)

1. Check text on images, gradients and hover states, which tools miss.
2. Check focus rings, input borders and icons against their background: 3:1.
3. View the page in greyscale. Is any information lost (errors, required fields, chart series, links in text)?

## Media (A11Y.MEDIA.*)

1. Play each video with sound. Are there captions, in sync and complete?
2. Is visual information that matters (text on screen, actions) also spoken or described?
3. Does any audio start on its own? Can it be stopped?

## Motion and time (A11Y.MOTION.*)

1. Watch the page for 10 seconds. Does anything move, blink or update on its own? Is there a pause button?
2. Is there a session timeout or timer in the journey? Is the user warned and can they extend?
3. Does anything flash? If in doubt, mark as fail with confidence low and ask for a PEAT check.

## Forms and authentication (A11Y.FORM.*)

1. Only on staging or with the owner's permission: submit each form empty, then with wrong data. Are errors in text, next to the field, and do they say how to fix?
2. In a multi-step flow, are you asked for the same information twice?
3. On login: can you paste a password and a one-time code? Is there a puzzle or memory test without an alternative?

Passive mode (no permission): inspect the validation code or HTML attributes instead, and mark confidence medium.
