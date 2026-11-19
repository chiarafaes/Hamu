---
framework: APPLE-ASRG, GOOGLE-PLAY
name: App store listing quality (product page, not policy)
last_verified: 2026-11-19
sources:
  - https://developer.apple.com/app-store/product-page/
  - https://developer.apple.com/help/app-store-connect/reference/screenshot-specifications
  - https://support.google.com/googleplay/android-developer/answer/9866151
status: verified for structure; screenshot specifications change often, check the linked pages before giving pixel sizes
---

# Store listing quality

Policy and privacy labels are SP's (`app-stores.md` in hamu-security-privacy). This file covers how well the listing sells the app.

## Rubric examples

| Check | 2 | 1 | 0 |
|---|---|---|---|
| PX.STORE.LISTING | Name and subtitle (Apple) or short description (Google) say what the app does and for whom. The first lines of the description lead with the main benefit. | Clear name, vague subtitle or description. | Name only, description is a feature dump or marketing filler. |
| PX.STORE.SCREENSHOTS | First 3 screenshots show the main tasks with short captions, match the current app, localised for the main markets (NL and FR for Belgium). | Current but no captions, or not localised. | Outdated UI, or device frames with unreadable text. |
| PX.STORE.RATING | Recent reviews are answered, rating trend is stable or rising. | Some answers, old complaints unanswered. | Many unanswered complaints about the same issue. |

## Notes

- Apple shows up to 3 screenshots or app previews in search results, so the first ones matter most.
- Google Play has a feature graphic and a short description field (80 characters). Check that both are filled.
- Custom product pages (Apple) and custom store listings (Google) allow versions per audience or campaign. Mention as `info` for apps with paid acquisition.
