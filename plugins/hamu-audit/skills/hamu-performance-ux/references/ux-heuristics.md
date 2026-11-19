---
framework: UXH
name: Hamu usability heuristics and rubric examples (RESP, NAV, HIER)
last_verified: 2026-11-19
sources:
  - https://www.nngroup.com/articles/ten-usability-heuristics/
  - https://www.iso.org/standard/75258.html
  - https://www.gov.uk/service-manual/design
status: Hamu own-words heuristics; Nielsen heuristics and ISO 9241-110:2020 principles referenced by name only
licence_note: Nielsen Norman Group and ISO texts are copyrighted. Hamu names the heuristics and principles and writes its own descriptions and examples.
---

# Usability heuristics (UXH)

`UXH` is the Hamu framework id for usability findings. Relation is always `best_practice`. Each finding may cite the related heuristic in `ref`, for example `UXH ref: "H1 visibility of system status"`.

## Heuristics

| Ref | Heuristic (own words) | Related ISO 9241-110 principle |
|---|---|---|
| H1 | Show people what is going on (loading, saved, step 2 of 4). | Self-descriptiveness |
| H2 | Speak the user's language, not internal jargon. | Conformity with user expectations |
| H3 | Let people undo and leave easily. | Controllability |
| H4 | Stay consistent within the site and with common web conventions. | Conformity with user expectations |
| H5 | Prevent errors before they happen. | Use error robustness |
| H6 | Show options instead of making people remember them. | Self-descriptiveness |
| H7 | Offer shortcuts for frequent users without confusing new ones. | Suitability for the user's tasks |
| H8 | Keep screens focused, remove what does not help the task. | Suitability for the user's tasks |
| H9 | Explain errors plainly and say how to fix them. | Use error robustness |
| H10 | Give help where people need it. | Learnability |

These follow the ten usability heuristics of Jakob Nielsen (Nielsen Norman Group) and the interaction principles of ISO 9241-110:2020, in Hamu's own words.

## Rubric examples

Score 2 = pass, 1 = warn, 0 = fail. Use the example closest to what you see.

| Check | 2 | 1 | 0 |
|---|---|---|---|
| PX.RESP.LAYOUT | Clean at 375, 768, 1280. | One component overlaps or crops at one width. | Content overlaps, is cut off or unusable at 375 px. |
| PX.NAV.CLARITY | 5 to 7 plain labels that match user tasks ("Prices", "Book a session"). | Some vague labels ("Solutions", "Discover") or 8 to 10 items. | Jargon or internal names, or more than 10 top-level items without grouping. |
| PX.NAV.LOCATION | Active state plus breadcrumbs on deep pages. | Active state only, or breadcrumbs that skip levels. | No sign of where the user is. |
| PX.NAV.SEARCH | Search tolerates typos, suggests, and empty results offer alternatives. | Exact match only, or empty results are a dead end. | No search on a large site, or search is broken. |
| PX.NAV.MOBILE | Menu opens with one tap, main tasks first, easy close. | Deep nesting or tiny triggers. | Menu cannot be opened or closed reliably. |
| PX.NAV.404 | Helpful page with search and main links, status 404. | Plain message with a home link, or soft 404 (status 200). | Server error page or blank page. |
| PX.NAV.TASKS | All top 3 tasks within 3 clicks and named on the home page. | One task needs 4 or more clicks or is hidden. | A main task cannot be found from the home page. |
| PX.HIER.ABOVE-FOLD | Offer, audience and primary action visible in the first mobile screen. | Two of the three. | Only a slider, a logo or a generic slogan. |
| PX.HIER.SCAN | Headings every few paragraphs, paragraphs under about 80 words, lists for steps. | Long paragraphs on secondary pages. | Walls of text on key pages. |
| PX.HIER.FOCUS | One clear primary element per screen. | Two competing elements. | Banners, popups and buttons all compete. |
| PX.HIER.POPUPS | No entry popup, or only after clear engagement. | Popup after a delay, easy to close. | Full-screen popup on entry on mobile, hard to close. |
| PX.HIER.MICROCOPY | Every button says what happens. Errors and empty states guide the user. | Some generic labels ("Submit", "Click here"). | Most actions are generic or unclear. |
