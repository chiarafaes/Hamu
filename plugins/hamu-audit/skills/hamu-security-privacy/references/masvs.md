---
framework: MASVS
name: OWASP Mobile Application Security Verification Standard v2 (with MASTG for test methods)
last_verified: 2026-11-19
sources:
  - https://mas.owasp.org/MASVS/
  - https://mas.owasp.org/MASTG/
status: control groups verified; current minor version (2.1) cross-checked with secondary sources
licence_note: OWASP MAS is CC BY-SA 4.0. Control ids and own-words summaries only.
---

# MASVS v2

Applies when `platforms` has `ios` or `android`. Relation `best_practice`. Needs the app source (Claude Code) for most checks. With only a store listing, the skill can check SP.MOBILE.LABELS and SP.MOBILE.DELETE from public information and writes the rest as `not_tested`.

Attribution line for reports: "Control ids from OWASP MASVS, CC BY-SA 4.0, mas.owasp.org."

## Control groups

| Group | Topic | Hamu checks |
|---|---|---|
| MASVS-STORAGE | Sensitive data at rest, leakage through logs, backups, clipboard | SP.MOBILE.STORAGE |
| MASVS-CRYPTO | Strong primitives, proper key management | SP.MOBILE.STORAGE, code review |
| MASVS-AUTH | Authentication and authorisation, local biometrics, step-up for sensitive actions | SP.AUTH.* |
| MASVS-NETWORK | Secure traffic, pinning for own endpoints where the threat model needs it | SP.MOBILE.NETWORK |
| MASVS-PLATFORM | IPC, WebViews, UI exposure of sensitive data | code review |
| MASVS-CODE | Up-to-date platform, forced updates, input handling, dependencies | SP.DEPS.* |
| MASVS-RESILIENCE | Anti-tampering, anti-reverse engineering | only for high-value apps, `info` otherwise |
| MASVS-PRIVACY | Data minimisation, no tracking without consent, transparency | SP.MOBILE.PERMS, SP.MOBILE.SDK, SP.MOBILE.LABELS |

## Files to read in a codebase

- iOS: `Info.plist` (ATS, usage descriptions), `PrivacyInfo.xcprivacy` (privacy manifest), Keychain usage.
- Android: `AndroidManifest.xml` (permissions, `usesCleartextTraffic`, exported components), `network_security_config.xml`, `EncryptedSharedPreferences` or Keystore use.
- React Native, Flutter, Expo: `app.json` / `app.config.*`, AsyncStorage use, SDK init in the app entry.
