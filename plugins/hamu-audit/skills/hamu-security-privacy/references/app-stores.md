---
framework: APPLE-ASRG, GOOGLE-PLAY
name: Apple App Store Review Guidelines and Google Play Developer Program Policies (privacy and security parts)
last_verified: 2026-11-19
sources:
  - https://developer.apple.com/app-store/review/guidelines/
  - https://developer.apple.com/help/app-review/guideline-reference/5-1-1-account-deletion
  - https://developer.apple.com/documentation/bundleresources/privacy-manifest-files
  - https://support.google.com/googleplay/android-developer/answer/10144311
  - https://support.google.com/googleplay/android-developer/answer/13327111
status: Apple account deletion verified on Apple's site; other items verified from memory of the official pages, verify guideline numbers on each run (stores update often)
---

# App store privacy rules

Applies when `platforms` has `ios` (APPLE-ASRG) or `android` (GOOGLE-PLAY). The stores are not law, but a rejection or removal stops distribution. Listing quality (screenshots, description) belongs to PX (`PX.STORE.*`).

## Apple

| Topic | Guideline | Check |
|---|---|---|
| Privacy policy link in App Store Connect and in the app | 5.1.1(i) | SP.PRIVACY.POLICY |
| Data collection needs consent, and access to data must match the app's purpose | 5.1.1(ii), (iii) | SP.MOBILE.PERMS |
| Apps that allow account creation must let users start account deletion in the app (since 30 June 2022). Deactivation is not enough. | 5.1.1(v) | SP.MOBILE.DELETE |
| App Tracking Transparency: ask permission before tracking across apps and websites of other companies | 5.1.2(i) | SP.MOBILE.ATT |
| Privacy nutrition labels in App Store Connect must match actual collection, including SDKs | App Store Connect, "App Privacy" | SP.MOBILE.LABELS |
| Privacy manifest (`PrivacyInfo.xcprivacy`) declaring collected data, tracking domains, and reasons for "required reason" APIs. Enforced for new submissions since 1 May 2024, also for listed third-party SDKs. | developer documentation | SP.MOBILE.MANIFEST |

## Google Play

| Topic | Policy | Check |
|---|---|---|
| Data safety section must be complete and accurate, including SDKs | User Data policy, Data safety | SP.MOBILE.LABELS |
| Prominent disclosure and consent before collecting personal and sensitive data not expected by users | User Data policy | SP.MOBILE.PERMS |
| Apps with account creation must offer account deletion in the app and through a web link that works without the app, listed in the Data safety form | User Data policy, account deletion | SP.MOBILE.DELETE |
| Permissions: request only what the core function needs, special rules for location, SMS, call log, all-files access | Permissions policy | SP.MOBILE.PERMS |
| Target API level requirements for new apps and updates | Target API level policy | SP.DEPS.EOL |

Severity: a store rule gap is `medium` by default, `high` when it would block release (missing account deletion, missing privacy manifest for a required reason API).
