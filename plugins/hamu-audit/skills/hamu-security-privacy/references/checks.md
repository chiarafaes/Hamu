---
last_verified: 2026-11-19
owner: hamu-security-privacy
prefix: SP.
---

# Check catalogue: hamu-security-privacy

Every check this skill owns. Ids follow `ownership-matrix.md` (`SP.DOMAIN.CHECK`). Framework refs point to the framework reference files in this folder, which hold the verified article numbers and dates. When a ref here and a reference file disagree, the reference file wins.

## How to read this file

| Column | Meaning |
|---|---|
| Id | `check_id` written to the finding. |
| Check | What passes. A finding is written when it does not. |
| Frameworks | Framework ids from `applicability-matrix.md`. `R` = requirement, `B` = best_practice, `E` = evidence_for. Only frameworks with status `applies` or `likely` are written to the finding. |
| Sev | Default severity before modifiers in `severity.md`. |
| Mode | `P` = passive (any visitor could see it). `A` = active (needs `owner_confirmed` and `active_testing_allowed`). `C` = codebase needed. `M` = manual (`needs_manual`). |
| How to test | `CC` = Claude Code with local tools. `APP` = Claude app with browser tools. `FB` = fallback when neither works. If no route works, write `not_tested`. |

Rules for every check:
- Run only checks whose frameworks have status `applies` or `likely`, plus all `B` baseline checks (ASVS5, OWASP-T10).
- Passive checks never submit forms, log in, or send crafted input.
- Evidence is redacted per `run-protocol.md`: first 4 characters of a secret, no session ids, no personal data.
- One finding per check per location. Same issue on 30 pages: one finding, locations listed in `evidence`.
- Non-EU privacy laws (CCPA, COPPA, PIPEDA, LGPD, POPIA) and the app store rules reuse the PRIVACY, CONSENT, TRANSFER and MOBILE checks. Their reference files list which check maps to which section. Add those frameworks to the finding when their status is `applies` or `likely`.

---

## TLS: transport security

| Id | Check | Frameworks | Sev | Mode | How to test |
|---|---|---|---|---|---|
| SP.TLS.HTTPS | Every page and asset loads over HTTPS. HTTP redirects to HTTPS with 301/308. | GDPR R (Art. 32), ASVS5 B, OWASP-T10 B (A04), PCI-DSS R (4.2.1), ISO27001 E, SOC2 E | high | P | CC: `curl -sI http://<host>/`. APP: load `http://` URL, check final URL. |
| SP.TLS.VERSION | Only TLS 1.2 and 1.3 offered. No SSLv3, TLS 1.0, 1.1. | ASVS5 B, PCI-DSS R, NIS2-BE E | medium | P | CC: `openssl s_client -connect host:443 -tls1_1` must fail, or `testssl.sh`. APP: SSL Labs page in browser. FB: `not_tested`. |
| SP.TLS.CERT | Certificate valid, matches host, chain complete, not expiring within 14 days. | ASVS5 B | high | P | CC: `openssl s_client -servername`. APP: browser security info. |
| SP.TLS.MIXED | No mixed content (HTTP scripts, iframes, images, form actions on HTTPS pages). | ASVS5 B, OWASP-T10 B | medium | P | CC/APP: scan HTML and network log for `http://` subresources. |
| SP.TLS.HSTS | `Strict-Transport-Security` with `max-age` >= 31536000. `includeSubDomains` advised. Preload advisory only. | ASVS5 B, OWASP-T10 B (A02) | medium | P | Response header on HTTPS root. |

## HDR: security headers

| Id | Check | Frameworks | Sev | Mode | How to test |
|---|---|---|---|---|---|
| SP.HDR.CSP | A Content-Security-Policy is set. No `unsafe-inline` for scripts without nonce or hash, no wildcard script sources. | ASVS5 B, OWASP-T10 B (A02, A05), PCI-DSS E (6.4.3) | medium | P | Header or `<meta http-equiv>`. Parse directives. |
| SP.HDR.FRAME | Clickjacking protection: CSP `frame-ancestors` or `X-Frame-Options`. | ASVS5 B, OWASP-T10 B (A02) | medium | P | Headers. |
| SP.HDR.NOSNIFF | `X-Content-Type-Options: nosniff`. | ASVS5 B | low | P | Headers. |
| SP.HDR.REFERRER | `Referrer-Policy` set to `strict-origin-when-cross-origin` or stricter. Full URLs with personal data in query strings never leak. | ASVS5 B, GDPR E (Art. 25) | low | P | Headers, plus check query strings for email or ids. |
| SP.HDR.PERMISSIONS | `Permissions-Policy` limits camera, microphone, geolocation, payment to what the site uses. | ASVS5 B | low | P | Headers. |
| SP.HDR.CORS | No `Access-Control-Allow-Origin: *` together with credentials. No reflected arbitrary origin on authenticated endpoints. | ASVS5 B, OWASP-T10 B (A01, A02) | high | P / A | P: read headers on public API responses. A: send `Origin: https://evil.example` and inspect. |
| SP.HDR.LEAK | No version banners (`Server: nginx/1.18.0`, `X-Powered-By`, framework debug headers). | ASVS5 B, CIS B | low | P | Headers. |

## COOKIE: cookie attributes

| Id | Check | Frameworks | Sev | Mode | How to test |
|---|---|---|---|---|---|
| SP.COOKIE.SECURE | Session and auth cookies have `Secure`. | ASVS5 B, OWASP-T10 B | medium | P | `Set-Cookie` headers, browser cookie store. |
| SP.COOKIE.HTTPONLY | Session cookies have `HttpOnly`. | ASVS5 B | medium | P | Same. |
| SP.COOKIE.SAMESITE | Session cookies have `SameSite=Lax` or `Strict`. `None` only with a CSRF defence. | ASVS5 B | low | P | Same. |
| SP.COOKIE.PREFIX | Session cookie uses `__Host-` prefix where possible. | ASVS5 B | info | P | Same. |
| SP.COOKIE.LIFETIME | Non-essential cookies do not outlive the consent period stated in the policy. Maximum consent and cookie lifetime per Belgian guidance: see `eprivacy-be.md` (verify). | EPRIVACY-BE R, GDPR R | medium | P | Compare cookie `Expires` with stated retention. |

## CONSENT: cookies and tracking consent

| Id | Check | Frameworks | Sev | Mode | How to test |
|---|---|---|---|---|---|
| SP.CONSENT.PRE-TRACK | No non-essential cookies, local storage, pixels or analytics requests before consent. | EPRIVACY-BE R, GDPR R (Art. 6, 7) | high | P | Clean profile, first load, no interaction. CC: Playwright, record requests and storage. APP: browser network log. FB: ask for a HAR file. |
| SP.CONSENT.BANNER | A consent mechanism exists when non-essential storage or tracking is present. | EPRIVACY-BE R, GDPR R | critical | P | Visual and DOM check. Critical only when ad pixels fire without any mechanism. |
| SP.CONSENT.REJECT | Refusing is as easy as accepting: a reject option on the first layer with equal prominence. | EPRIVACY-BE R, GDPR R (Art. 7), EU-CONSUMER E (UCPD) | high | P | Screenshot of first layer. Compare button style, size, colour, position. |
| SP.CONSENT.GRANULAR | Consent per purpose. No pre-ticked boxes. No bundling with terms acceptance. | EPRIVACY-BE R, GDPR R (Art. 4(11), 7) | high | P | Inspect second layer. |
| SP.CONSENT.POST-REJECT | After "reject", no non-essential requests or storage. | EPRIVACY-BE R, GDPR R | high | P | Click reject in a clean profile, reload, record requests. Clicking the banner is normal browsing, so passive. |
| SP.CONSENT.WITHDRAW | Consent can be withdrawn as easily as given, from every page (link or floating button). | GDPR R (Art. 7(3)), EPRIVACY-BE R | medium | P | Look for a persistent settings link. |
| SP.CONSENT.INFO | First layer names purposes and the parties placing cookies. A cookie list with name, purpose, duration, party is reachable. | EPRIVACY-BE R, GDPR R (Art. 13) | medium | P | Read banner and cookie policy. Compare listed cookies with observed ones. |
| SP.CONSENT.WALL | No cookie wall that blocks access unless the user accepts tracking, without a real alternative. | EPRIVACY-BE R, GDPR R (Art. 7(4)) | high | P | Reject and check access. `legal_review: true` for "pay or consent" models. |
| SP.CONSENT.MODE | Google Consent Mode or equivalent sends no identifiers before consent. Cookieless pings are noted, not failed. | EPRIVACY-BE R, GDPR R | medium | P | Inspect `gcs`/`gcd` parameters in collect requests. |
| SP.CONSENT.RECORD | Consent is logged (who, when, what version) so it can be proven. | GDPR R (Art. 7(1)) | medium | C / M | CC: look for consent log in code or CMP config. Else `needs_manual`. |
| SP.CONSENT.GPC | Opt-out preference signals (Global Privacy Control, `Sec-GPC: 1`) are honoured as an opt-out of sale and sharing, and the site shows that the signal was processed. | CCPA R (regs 7025) | high | P | CC: Playwright with `Sec-GPC: 1` header and `navigator.globalPrivacyControl = true`, compare ad and analytics requests with a run without it. APP: browser with GPC enabled if available. FB: `not_tested`. |

## PRIVACY: policy, rights, data handling

| Id | Check | Frameworks | Sev | Mode | How to test |
|---|---|---|---|---|---|
| SP.PRIVACY.POLICY | A privacy notice exists and is linked from every page footer and every form that collects data. | GDPR R (Art. 12, 13) | high | P | Crawl footer and forms. |
| SP.PRIVACY.CONTENT | Notice names controller and contact, DPO if any, purposes with legal basis, recipients, transfers, retention, rights, right to complain (GBA/APD for BE), source of data if not from the person. | GDPR R (Art. 13, 14) | medium | P | Read notice against the checklist in `gdpr.md`. `heuristic`, confidence medium. |
| SP.PRIVACY.LANG | Notice is in the language(s) of the site and readable (short sentences, layered). | GDPR R (Art. 12(1)) | low | P | Compare `<html lang>` and notice language. |
| SP.PRIVACY.FORMS | Forms collect only what the stated purpose needs. Optional fields are marked. Marketing opt-in is a separate unticked checkbox. | GDPR R (Art. 5(1)(c), 25), EPRIVACY-BE R (direct marketing) | medium | P | Inspect forms without submitting. |
| SP.PRIVACY.RIGHTS | A way to exercise rights (access, erasure, objection) is described and reachable. In code: export and delete functions exist for user accounts. | GDPR R (Art. 15-22) | medium | P / C | P: notice. C: search for delete-account and export handlers. |
| SP.PRIVACY.RETENTION | Retention periods or criteria are stated, and in code old data is deleted or anonymised. | GDPR R (Art. 5(1)(e), 13(2)(a)) | medium | P / C | Notice. Code: cron jobs, TTL indexes, cleanup tasks. |
| SP.PRIVACY.CHILDREN | If children are targeted: age check or parental consent below the Belgian digital age of consent (13), child-friendly notice. | GDPR-K R (Art. 8) | high | P | Signup flow inspection. `legal_review: true`. |
| SP.PRIVACY.SPECIAL | Special category data (health, biometrics, beliefs) has an Art. 9 condition, explicit consent where used, and stronger protection. | GDPR R (Art. 9, 35) | high | P / C | Form fields, code models. Often `needs_manual`. |
| SP.PRIVACY.DPIA | A DPIA exists when processing is high risk (large-scale special data, systematic monitoring, profiling). | GDPR R (Art. 35) | medium | M | `needs_manual` with criteria from `gdpr.md`. |
| SP.PRIVACY.ROPA | A record of processing activities exists. | GDPR R (Art. 30) | low | M | `needs_manual`. |
| SP.PRIVACY.DPA | Contracts (Art. 28 agreements) exist for every processor found in scripts and code. | GDPR R (Art. 28) | medium | M | List detected processors, ask the owner to confirm. |
| SP.PRIVACY.BREACH | A breach procedure exists that meets the 72-hour notification to the GBA/APD. | GDPR R (Art. 33, 34), NIS2-BE E | medium | M | `needs_manual`. |
| SP.PRIVACY.PII-URL | No personal data (email, name, national number) in URLs, query strings or analytics events. | GDPR R (Art. 5(1)(f), 32) | high | P / C | Network log, analytics payloads, code. |
| SP.PRIVACY.RRN | Belgian national register number (rijksregisternummer) is not collected unless a legal basis allows it. | GDPR R (Art. 87), BE law (see `gdpr.md`) | high | P / C | Form fields matching `\d{2}\.\d{2}\.\d{2}-\d{3}\.\d{2}`. `legal_review: true`. |
| SP.PRIVACY.US-NOTICE | US notices: CCPA notice at collection and privacy policy with categories, purposes, retention, rights and a "last updated" date within 12 months. COPPA online notice when children under 13 are in scope. | CCPA R, COPPA R | medium | P | Read the policy and the collection points. |
| SP.PRIVACY.US-OPTOUT | "Do Not Sell or Share My Personal Information" link (and "Limit the Use of My Sensitive Personal Information" where needed, or one combined alternative opt-out link) in the footer, and it works without creating an account. | CCPA R (1798.135) | high | P | Footer and the opt-out flow. Count as fail only when ad or cross-context tracking is detected. |
| SP.PRIVACY.COPPA | Services for children under 13: neutral age screen, verifiable parental consent before collection, separate consent before third-party disclosure or targeted ads. | COPPA R (16 CFR 312) | high | P | Signup flow inspection without creating real accounts. `legal_review: true`. |
| SP.PRIVACY.LOCAL-OFFICER | The local accountable person is named with contact: privacy officer (PIPEDA), encarregado (LGPD), information officer (POPIA). | PIPEDA R, LGPD R (Art. 41), POPIA R (s55) | medium | P | Privacy notice and footer. |

## TRANSFER: international transfers

| Id | Check | Frameworks | Sev | Mode | How to test |
|---|---|---|---|---|---|
| SP.TRANSFER.MAP | Every third-party host receiving personal data is listed with its country. | GDPR-TRANSFER R (Chapter V) | medium | P | Group network requests by domain. Map to provider and country. |
| SP.TRANSFER.BASIS | Each transfer outside the EEA has a basis: adequacy (including EU-US DPF certification), SCCs, or another Art. 46/49 ground, stated in the notice. | GDPR-TRANSFER R (Art. 44-49) | medium | P / M | Check notice. For US providers, check the DPF list. `legal_review: true`. |
| SP.TRANSFER.FONTS | Web fonts and similar assets are self-hosted or loaded only after consent, so the IP address is not sent to a third party without need. | GDPR B (Art. 5, 6), GDPR-TRANSFER E | low | P | Requests to `fonts.googleapis.com`, `fonts.gstatic.com`, CDNs. |

## LEGAL: mandatory business disclosures

| Id | Check | Frameworks | Sev | Mode | How to test |
|---|---|---|---|---|---|
| SP.LEGAL.IDENTITY | Company name, legal form, registered address, enterprise number (KBO/BCE), RPR/RPM court, email and phone are on the site. | BE-CEL R (Book XII, Book III), DSA R (Art. 11-12 for intermediaries), EU-CONSUMER R | high | P | Footer, imprint, terms. Validate the enterprise number format and checksum. |
| SP.LEGAL.VAT | VAT number shown where the business is VAT registered. | BE-CEL R | low | P | Same. |
| SP.LEGAL.REGULATED | Regulated professions show their professional body, title and rules. | BE-CEL R | medium | P | Sector keywords. `heuristic`. |
| SP.LEGAL.TERMS | Terms of sale or use exist, can be stored and printed, and are accepted before the order. | BE-CEL R, EU-CONSUMER R | medium | P | Checkout inspection without placing an order. |
| SP.LEGAL.ODR | No outdated link to the EU ODR platform (discontinued 20 July 2025). | EU-CONSUMER B | low | P | Search for `ec.europa.eu/consumers/odr`. |
| SP.LEGAL.ADR | Where required, the business names its alternative dispute resolution body (in BE: Consumer Mediation Service or sector ombudsman). | EU-CONSUMER R, BE-CEL R | low | P | Terms and footer. `verify` per sector. |

## CONSUMER: online consumer protection

| Id | Check | Frameworks | Sev | Mode | How to test |
|---|---|---|---|---|---|
| SP.CONSUMER.PRE-INFO | Before ordering: main features, total price incl. VAT and delivery, payment and delivery terms, withdrawal right, guarantee. | EU-CONSUMER R (CRD Art. 6), BE-CEL R (Book VI) | high | P | Product page and cart. Do not place orders. |
| SP.CONSUMER.BUTTON | The final order button says clearly that ordering means paying ("Order with obligation to pay" or equal). | EU-CONSUMER R (CRD Art. 8(2)) | high | P | Inspect last checkout step if reachable without payment. Else `needs_manual`. |
| SP.CONSUMER.WITHDRAWAL | 14-day withdrawal right explained, model form available, exceptions named. | EU-CONSUMER R (CRD Art. 9-16), BE-CEL R | high | P | Terms and checkout. |
| SP.CONSUMER.WITHDRAW-FN | Online withdrawal function: a clearly labelled, always available function to withdraw, with a confirmation step. | EU-CONSUMER R (CRD Art. 11a, from 19 June 2026), BE-CEL R (verify article) | high | P | Account area and footer. `legal_review: true` until BE article numbers are verified. |
| SP.CONSUMER.PRICE | Price reductions show the lowest price of the prior 30 days. | EU-CONSUMER R (Price Indication Directive Art. 6a) | medium | P | Sale labels on product and category pages. |
| SP.CONSUMER.REVIEWS | If reviews are shown: the site says whether and how it checks that reviews come from real buyers. | EU-CONSUMER R (UCPD Art. 7(6), Annex I 23b-23c) | medium | P | Review widgets and notices. |
| SP.CONSUMER.DARK | No dark patterns in checkout, signup or cancellation: fake urgency, confirmshaming, pre-ticked add-ons, hidden costs, roach motel cancellation. | EU-CONSUMER R (UCPD, CRD Art. 22), DSA R (Art. 25 for platforms) | high | P | Walk the flow, screenshot each step. `heuristic`. |
| SP.CONSUMER.SUBSCRIPTION | Subscriptions can be cancelled online as easily as they were started. Renewal terms are stated. | EU-CONSUMER R, BE-CEL R (verify) | medium | P | Account and terms. `legal_review: true`. |
| SP.CONSUMER.ADS | Ads, sponsored content and affiliate links are labelled as such. | EU-CONSUMER R (UCPD Annex I 11, 11a), DSA R (Art. 26) | medium | P | Content pages. |
| SP.CONSUMER.GEOBLOCK | Customers from other EU countries are not blocked or redirected without consent based on nationality or location. | EU-CONSUMER R (Geo-blocking Reg. 2018/302) | low | P | Look for country restrictions in checkout and terms. |
| SP.CONSUMER.GPSR | Physical products online show manufacturer, EU responsible person, product id, warnings and safety info. | GPSR R (Art. 19) | medium | P | Product pages. |
| SP.CONSUMER.MARKETPLACE | Marketplaces show whether the seller is a trader, and collect trader details (traceability). | DSA R (Art. 30-32), EU-CONSUMER R (CRD Art. 6a) | medium | P | Seller pages. |
| SP.CONSUMER.DSA-NOTICE | Hosting services and platforms have a notice-and-action mechanism, a single point of contact and terms that explain moderation. | DSA R (Art. 11, 12, 14, 16) | medium | P | Look for report buttons and contact points. |

## AUTH: authentication and sessions

| Id | Check | Frameworks | Sev | Mode | How to test |
|---|---|---|---|---|---|
| SP.AUTH.PASSWORD | Password policy follows ASVS: minimum length 8 (ASVS L1) or more, no composition rules forced, check against breached lists, paste allowed. | ASVS5 B (V6), OWASP-T10 B (A07) | medium | P / C | P: signup page hints and `minlength`. C: validation code. |
| SP.AUTH.MFA | MFA is available for users and required for admins and staff with access to personal data. | ASVS5 B (V6), NIS2-BE R (Art. 21(2)(j)), PCI-DSS R (8.4), ISO27001 E, SOC2 E | high | P / C / M | Account settings, admin login, code. |
| SP.AUTH.BRUTE | Login, signup and reset are rate limited or protected against automation. | ASVS5 B, OWASP-T10 B (A07) | medium | C / A | C: middleware. A: 10 wrong attempts on a test account. |
| SP.AUTH.ENUM | Login and reset do not reveal whether an account exists. | ASVS5 B | low | P / A | P: read messages in code or UI copy. A: compare responses. |
| SP.AUTH.RESET | Reset tokens are single-use, expire, and are not sent in URLs to third parties. | ASVS5 B | medium | C / A | Code review or test account. |
| SP.AUTH.SESSION | Session ids rotate on login, expire on idle and absolute timeout, and are invalidated on logout. | ASVS5 B (V7) | medium | C / A | Code review or test account. |
| SP.AUTH.TOKEN | JWTs: signature verified, `alg` fixed, short expiry, not stored in localStorage when an HttpOnly cookie is possible. | ASVS5 B (V9), OWASP-T10 B (A07, A08) | medium | C | Code review. |
| SP.AUTH.OAUTH | OAuth/OIDC uses PKCE, exact redirect URI match, `state` or `nonce`. | ASVS5 B (V10) | medium | C | Code and provider config. |

## ACCESS: authorisation

| Id | Check | Frameworks | Sev | Mode | How to test |
|---|---|---|---|---|---|
| SP.ACCESS.SERVER | Every protected route and API checks authorisation on the server, not only in the UI. | ASVS5 B (V8), OWASP-T10 B (A01), GDPR R (Art. 32) | critical | C / A | C: route handlers without auth middleware. A: request a protected resource without session. |
| SP.ACCESS.IDOR | Object ids in URLs or APIs are checked against the user (no IDOR). | ASVS5 B, OWASP-T10 B (A01), OWASP API1 | critical | C / A | C: queries filtered by user or tenant. A: two test accounts. |
| SP.ACCESS.ADMIN | Admin panels are not publicly reachable, or are protected by MFA and IP limits. | ASVS5 B, OWASP-T10 B (A01, A02) | high | P | Request common paths (`/admin`, `/wp-admin`, `/phpmyadmin`) at normal rate. Note status only. |
| SP.ACCESS.TENANT | Multi-tenant data is isolated (row-level security or tenant filter on every query). | ASVS5 B, ISO27001 E, SOC2 E | critical | C | Code and DB policies. |
| SP.ACCESS.SSRF | Server-side URL fetching validates targets and blocks internal addresses. | ASVS5 B, OWASP-T10 B (A01 in 2025) | high | C / A | Code review. |

## INPUT: injection and output handling

| Id | Check | Frameworks | Sev | Mode | How to test |
|---|---|---|---|---|---|
| SP.INPUT.SQL | Database access uses parameterised queries or an ORM without raw string building. | ASVS5 B, OWASP-T10 B (A05) | critical | C / A | C: Semgrep or pattern search. A: only on staging with scope. |
| SP.INPUT.XSS | User input is escaped on output. No `innerHTML`, `dangerouslySetInnerHTML`, `v-html` with user data. | ASVS5 B, OWASP-T10 B (A05) | high | C / A | C: Semgrep. P: reflected parameters visible in page source count as low-confidence warn. |
| SP.INPUT.CSRF | State-changing requests have CSRF protection (token, SameSite, or custom header check). | ASVS5 B | medium | P / C | P: forms without token and session cookie without SameSite. C: framework config. |
| SP.INPUT.UPLOAD | Uploads check type and size, are stored outside the web root, and are served with safe headers. | ASVS5 B (V5) | high | C | Code review. |
| SP.INPUT.VALIDATE | Server-side validation exists for every input. Client-side only does not pass. | ASVS5 B (V2) | medium | C | Code review: schema validation at API boundary. |
| SP.INPUT.DESERIAL | No unsafe deserialisation of untrusted data. | ASVS5 B, OWASP-T10 B (A08) | high | C | Semgrep rules for the language. |
| SP.INPUT.ERRORS | Errors do not leak stack traces, SQL, paths or versions to users. | ASVS5 B, OWASP-T10 B (A10 in 2025) | medium | P / C | P: 404 and error pages. C: error handler config. |

## DEPS: components and supply chain

| Id | Check | Frameworks | Sev | Mode | How to test |
|---|---|---|---|---|---|
| SP.DEPS.VULN | No dependencies with known vulnerabilities of high or critical severity, and none on the CISA KEV list. | OWASP-T10 B (A03 in 2025), ASVS5 B, CRA R (Annex I), NIS2-BE E, PCI-DSS R (6.3.3) | high | C | CC: `npm audit`, `pip-audit`, `osv-scanner`. APP: read lockfiles, lower confidence. FB: `not_tested`. |
| SP.DEPS.CLIENT | Client-side libraries visible in the page are not outdated with known vulnerabilities. | OWASP-T10 B (A03) | medium | P | Detect library and version from scripts. Match against OSV. Confidence medium. |
| SP.DEPS.SRI | Third-party scripts from CDNs use Subresource Integrity or are self-hosted. | ASVS5 B, OWASP-T10 B (A08), PCI-DSS E (6.4.3) | low | P | Script tags without `integrity`. |
| SP.DEPS.INVENTORY | A script inventory exists for payment pages, with authorisation and integrity checks. | PCI-DSS R (6.4.3, 11.6.1) | high | P / M | Only when PCI-DSS applies and the payment page is on the merchant's site. |
| SP.DEPS.SBOM | An SBOM can be produced (CycloneDX or SPDX) for shipped software. | CRA R (Annex I Part II), NIS2-BE E | medium | C | Lockfiles present. CC: suggest `npx @cyclonedx/cyclonedx-npm`. |
| SP.DEPS.PIN | Lockfiles committed. CI actions pinned by version or hash. | OWASP-T10 B (A03, A08) | low | C | Repo inspection. |
| SP.DEPS.EOL | Runtime and framework versions are still supported (not end of life). | OWASP-T10 B (A03), CRA E | medium | P / C | Version detection, compare with endoflife data. |

## SECRETS

| Id | Check | Frameworks | Sev | Mode | How to test |
|---|---|---|---|---|---|
| SP.SECRETS.CLIENT | No secret keys in client bundles, HTML or source maps (public keys like Stripe `pk_` are fine). | ASVS5 B, OWASP-T10 B (A04) | critical | P | Fetch JS bundles and search for key patterns. |
| SP.SECRETS.REPO | No secrets in the repository or its history. | ASVS5 B | critical | C | CC: `gitleaks` or `trufflehog`. FB: pattern search in working tree, confidence medium. |
| SP.SECRETS.SOURCEMAP | Production source maps are not public, or contain no secrets and internal paths. | ASVS5 B | low | P | Request `<bundle>.map`. |
| SP.SECRETS.ENV | `.env`, `.git/`, backup files and config dumps are not served. | ASVS5 B, OWASP-T10 B (A02) | critical | P | Request a short fixed list of paths at normal rate. Status code only. |

## API

| Id | Check | Frameworks | Sev | Mode | How to test |
|---|---|---|---|---|---|
| SP.API.AUTH | Every non-public API endpoint requires authentication. | OWASP-T10 B (API2), ASVS5 B | critical | C / A | Route inventory from code or OpenAPI. |
| SP.API.OBJECT | Object and property level authorisation (no mass assignment, no over-exposed fields). | OWASP-T10 B (API1, API3) | high | C | Serializers and DTOs. |
| SP.API.RATE | Rate limiting and payload size limits exist. | OWASP-T10 B (API4) | medium | C | Middleware config. |
| SP.API.DOCS | Public API docs and GraphQL introspection are intended, not accidental. | OWASP-T10 B (API9) | low | P | Request `/swagger`, `/openapi.json`, GraphQL introspection query only with permission. |

## LLM: AI features (security)

| Id | Check | Frameworks | Sev | Mode | How to test |
|---|---|---|---|---|---|
| SP.LLM.INJECT | Prompt injection is considered: untrusted content is separated from instructions, tools have least privilege, high-impact actions need confirmation. | OWASP-T10 B (LLM01) | high | C | Code review of prompt assembly and tool definitions. |
| SP.LLM.OUTPUT | Model output is treated as untrusted (escaped in HTML, not executed, not used in queries raw). | OWASP-T10 B (LLM05) | high | C | Code review. |
| SP.LLM.DATA | No secrets or other users' data in prompts or retrievable context. Provider data use and retention are stated. | OWASP-T10 B (LLM02), GDPR R (Art. 28, 32) | high | C / M | Code and provider settings. |
| SP.LLM.KEY | LLM API keys are server-side only, with spend limits. | ASVS5 B, OWASP-T10 B (LLM10) | critical | P / C | Client bundle search, code. |

## MOBILE

| Id | Check | Frameworks | Sev | Mode | How to test |
|---|---|---|---|---|---|
| SP.MOBILE.STORAGE | No sensitive data in plain storage (SharedPreferences, UserDefaults, AsyncStorage). Keychain or Keystore used. | MASVS B (STORAGE) | high | C | Code review. |
| SP.MOBILE.NETWORK | No cleartext traffic. ATS and Network Security Config not weakened. | MASVS B (NETWORK) | high | C | `Info.plist`, `network_security_config.xml`. |
| SP.MOBILE.PERMS | Requested permissions match features. Purpose strings are clear. | MASVS B (PRIVACY), GDPR R (Art. 5(1)(c)), APPLE-ASRG R, GOOGLE-PLAY R | medium | C | Manifest and plist. |
| SP.MOBILE.LABELS | App Store privacy labels and Play data safety form match what the code collects (SDKs included). | APPLE-ASRG R, GOOGLE-PLAY R, GDPR E | medium | C / M | Compare SDK list with declared labels. |
| SP.MOBILE.SDK | Third-party SDKs (analytics, ads) do not start before consent. | EPRIVACY-BE R, GDPR R, MASVS B | high | C | Init calls in app startup. |
| SP.MOBILE.DELETE | Users who can create an account in the app can delete it from the app. | APPLE-ASRG R, GOOGLE-PLAY R, GDPR R (Art. 17) | medium | C / P | Account screens, store listing. |
| SP.MOBILE.ATT | iOS: App Tracking Transparency prompt appears before any cross-app tracking, and tracking SDKs respect a refusal. | APPLE-ASRG R (5.1.2(i)), EPRIVACY-BE E | high | C | `NSUserTrackingUsageDescription`, `ATTrackingManager` calls before SDK init. |
| SP.MOBILE.MANIFEST | iOS: `PrivacyInfo.xcprivacy` exists, declares collected data and tracking domains, and gives reasons for required reason APIs used by the app and its SDKs. | APPLE-ASRG R | high | C | Read the manifest, compare with SDK list. |

## INFRA

| Id | Check | Frameworks | Sev | Mode | How to test |
|---|---|---|---|---|---|
| SP.INFRA.EXPOSE | robots.txt and public files do not reveal admin or internal paths. Directory listing is off. | ASVS5 B, CIS B | low | P | robots.txt, common directories. |
| SP.INFRA.CONTAINER | Containers run as non-root, use minimal pinned base images, no secrets in layers. | CIS B | medium | C | Dockerfile review. |
| SP.INFRA.IAC | IaC has no public buckets, open security groups (0.0.0.0/0 on admin ports) or disabled encryption. | CIS B, ISO27001 E, SOC2 E | high | C | CC: `semgrep`, `checkov` via `pipx run` if the user agrees. Else pattern search. |
| SP.INFRA.ENCRYPT | Personal data is encrypted at rest (database, backups, buckets). | GDPR R (Art. 32), ISO27001 E, HIPAA R, PCI-DSS R | medium | C / M | Config and IaC. Often `needs_manual`. |

## DNS: domain and email security

| Id | Check | Frameworks | Sev | Mode | How to test |
|---|---|---|---|---|---|
| SP.DNS.SPF | SPF record exists and ends in `-all` or `~all`, under 10 lookups. | NIS2-BE B (CyFun), CIS B | medium | P | CC: `dig TXT`. APP: DNS lookup page. FB: `not_tested`. |
| SP.DNS.DMARC | DMARC record with `p=quarantine` or `p=reject`. `p=none` is warn. | NIS2-BE B, CIS B | medium | P | `dig TXT _dmarc.<domain>`. |
| SP.DNS.DKIM | DKIM is set up for the sending service. | CIS B | low | P / M | Common selectors only. Unknown selector: `needs_manual`. |
| SP.DNS.CAA | CAA record limits certificate issuers. | ASVS5 B | info | P | `dig CAA`. |
| SP.DNS.DNSSEC | DNSSEC enabled (especially for `.be` domains, supported by DNS Belgium). | NIS2-BE B | info | P | `dig +dnssec`. |
| SP.DNS.TAKEOVER | No dangling CNAMEs to unclaimed cloud services on known subdomains. | ASVS5 B | high | P | Only subdomains already linked from the site. No enumeration without permission. |

## DISCLOSE: vulnerability disclosure

| Id | Check | Frameworks | Sev | Mode | How to test |
|---|---|---|---|---|---|
| SP.DISCLOSE.SECURITYTXT | `/.well-known/security.txt` exists with `Contact` and `Expires` in the future (RFC 9116). | CRA R (Annex I Part II), NIS2-BE B, ASVS5 B | low | P | Request the file. Raised to medium when CRA applies. |
| SP.DISCLOSE.CVD | A coordinated vulnerability disclosure policy is published. The CCB national CVD framework is referenced for Belgian organisations. | CRA R, NIS2-BE B | low | P | Search site for policy. |

## LOG: logging and monitoring

| Id | Check | Frameworks | Sev | Mode | How to test |
|---|---|---|---|---|---|
| SP.LOG.SECURITY | Security events (login, failed login, permission change, admin actions) are logged with time and actor. | ASVS5 B (V16), OWASP-T10 B (A09), NIS2-BE R, PCI-DSS R (10), ISO27001 E, SOC2 E | medium | C | Logger calls around auth and admin actions. |
| SP.LOG.PII | Logs do not contain passwords, tokens, full card numbers or unnecessary personal data. | GDPR R (Art. 5, 32), PCI-DSS R | high | C | Grep logger calls with request bodies. |
| SP.LOG.ALERT | Alerts exist for security events, and someone receives them. | OWASP-T10 B (A09), NIS2-BE R | medium | M | `needs_manual`. |

## RESIL: resilience

| Id | Check | Frameworks | Sev | Mode | How to test |
|---|---|---|---|---|---|
| SP.RESIL.BACKUP | Backups exist, are encrypted, kept apart from production and restore-tested. | GDPR R (Art. 32(1)(c)), NIS2-BE R, DORA R, ISO27001 E, SOC2 E | medium | M / C | Config or `needs_manual`. |
| SP.RESIL.INCIDENT | An incident response plan covers who decides and who reports (GBA/APD 72 h, CCB 24 h early warning for NIS2 entities, CRA and DORA where in scope). | NIS2-BE R, DORA R, CRA R, GDPR R | medium | M | `needs_manual`. |
| SP.RESIL.SUPPLIER | Critical suppliers are listed, with security clauses in contracts. | NIS2-BE R (Art. 21(2)(d)), DORA R | low | M | `needs_manual`. |

## AI: AI Act

| Id | Check | Frameworks | Sev | Mode | How to test |
|---|---|---|---|---|---|
| SP.AI.DISCLOSE | People are told they interact with an AI system (chatbot, voice agent) unless obvious. | AIACT-50 R (Art. 50(1)) | high | P | Open the chat widget, read the first message and labels. |
| SP.AI.LABEL | AI-generated or manipulated content is marked machine-readable. Deepfakes and AI text on public-interest topics are disclosed. | AIACT-50 R (Art. 50(2), 50(4)) | medium | P / C | Visible labels, C2PA or metadata, code. Grace period for legacy systems: see `aiact.md`. |
| SP.AI.PROHIBITED | No prohibited AI practice (manipulative techniques, social scoring, emotion recognition at work or school, untargeted face scraping). | AIACT R (Art. 5) | critical | P / C | Feature review. `legal_review: true`. |
| SP.AI.HIGH-RISK | Use cases in Annex III (hiring, credit, education, essential services) are flagged with their application date and duties. | AIACT R (Art. 6, Annex III) | high | P / M | Classification only, `legal_review: true`. |
| SP.AI.LITERACY | Staff who use or operate AI systems have AI literacy measures. | AIACT R (Art. 4) | low | M | `needs_manual`. |

## CERT: certification readiness

These findings never say "compliant" or "certified". They map existing findings to control ids as `evidence_for` and list process controls that cannot be verified from a URL or code as `needs_manual`. Capped at `high` (see `severity.md`). Only produced when the user named a target in `certification_targets`.

| Id | Check | Frameworks | Sev | Mode | How to test |
|---|---|---|---|---|---|
| SP.CERT.ISO27001 | Readiness view per Annex A theme plus the management system checklist. | ISO27001 E | info | M | `iso27001.md`. |
| SP.CERT.SOC2 | Readiness view per Trust Services category in scope plus the manual checklist. | SOC2 E | info | M | `soc2.md`. |
| SP.CERT.ISO42001 | Readiness view per Annex A area for the AI management system. | ISO42001 E | info | M | `iso42001.md`. |
| SP.CERT.NIST-CSF | Readiness view per CSF 2.0 function. | NIST-CSF E | info | M | `nist-csf.md`. |
| SP.CERT.HIPAA | Readiness view for the Security Rule safeguards. | HIPAA E | info | M | `hipaa.md`. |
| SP.CERT.PCI | SAQ type estimate and readiness for the matching requirements. | PCI-DSS E | info | M | `pci-dss.md`. |
| SP.CERT.CYFUN | Readiness for the CyberFundamentals level that matches the NIS2 classification. | NIS2-BE E | info | M | `nis2-be.md`. |
| SP.CERT.CCPA-PROC | CCPA process duties: risk assessments (from 2026), ADMT (from 2027), cybersecurity audit certification (2028 to 2030 by revenue). | CCPA R | info | M | `ccpa.md`. Only when CCPA applies. |

How a readiness view is built:
1. Take every finding of this run, and add the control ids from the mapping below as `evidence_for`.
2. Add one `needs_manual` finding per checklist item in the reference file that the owner has not confirmed.
3. In the report section "Framework coverage", show per theme or function: checks with evidence, gaps, manual items. Never a percentage "toward certification".

### Readiness mapping

Ids are written to `frameworks[].ref` with relation `evidence_for`. Copy only ids, never control text.

| Hamu domain | ISO27001 | SOC2 | NIST-CSF | HIPAA | ISO42001 |
|---|---|---|---|---|---|
| TLS | A.8.20, A.8.24 | CC6 | PR.DS | 164.312(e) | - |
| HDR, COOKIE | A.8.9, A.8.26 | CC6 | PR.PS | 164.312(c) | - |
| CONSENT, PRIVACY | A.5.34 | P1 to P8 | GV.OC | Privacy Rule | A.8 |
| TRANSFER | A.5.14 | C1, P6 | GV.SC | 164.314 | A.10 |
| LEGAL, CONSUMER | A.5.31 | CC2 | GV.OC | - | - |
| AUTH | A.5.17, A.8.5 | CC6 | PR.AA | 164.312(a), (d) | - |
| ACCESS | A.5.15, A.5.18, A.8.2, A.8.3 | CC6 | PR.AA | 164.308(a)(4), 164.312(a) | - |
| INPUT, API | A.8.26, A.8.28 | CC8 | PR.PS | 164.312(c) | - |
| DEPS | A.8.8, A.8.25 | CC7 | ID.AM, PR.PS | 164.308(a)(1) | A.4 |
| SECRETS | A.8.12, A.5.17 | CC6 | PR.DS | 164.312(a) | - |
| LLM, AI | A.8.26 | CC3 | ID.RA | - | A.5, A.6, A.7, A.9 |
| MOBILE | A.8.26 | CC6 | PR.PS | 164.312 | - |
| INFRA | A.5.23, A.8.9, A.8.24 | CC6, CC7 | PR.PS, PR.IR | 164.310, 164.312(a) | - |
| DNS | A.8.20 | CC6 | PR.PS | - | - |
| DISCLOSE | A.8.8 | CC2 | ID.IM | - | A.8 |
| LOG | A.8.15, A.8.16 | CC4, CC7 | DE.CM, DE.AE | 164.312(b) | A.6 |
| RESIL | A.5.24 to A.5.30, A.8.13, A.5.19 to A.5.22 | CC7, CC9, A1 | RS, RC, GV.SC | 164.308(a)(6), (a)(7) | A.10 |

---

## Guardrails pointers by build task

In guardrails mode pick at most 5, highest severity first. Each pointer is one concrete rule with the check id.

| Build task | Checks to draw from |
|---|---|
| Analytics, pixels, tag manager, cookie banner | SP.CONSENT.PRE-TRACK, SP.CONSENT.REJECT, SP.CONSENT.POST-REJECT, SP.CONSENT.INFO, SP.TRANSFER.MAP |
| Contact, newsletter or signup form | SP.PRIVACY.FORMS, SP.PRIVACY.POLICY, SP.INPUT.CSRF, SP.AUTH.BRUTE, SP.INPUT.VALIDATE |
| Login, accounts, password reset | SP.AUTH.PASSWORD, SP.AUTH.MFA, SP.AUTH.SESSION, SP.AUTH.ENUM, SP.PRIVACY.RIGHTS |
| Checkout and webshop | SP.CONSUMER.PRE-INFO, SP.CONSUMER.BUTTON, SP.CONSUMER.WITHDRAW-FN, SP.CONSUMER.DARK, SP.DEPS.INVENTORY |
| API endpoint | SP.ACCESS.SERVER, SP.ACCESS.IDOR, SP.API.OBJECT, SP.INPUT.VALIDATE, SP.API.RATE |
| File upload | SP.INPUT.UPLOAD, SP.ACCESS.IDOR, SP.PRIVACY.RETENTION |
| Chatbot or LLM feature | SP.AI.DISCLOSE, SP.LLM.INJECT, SP.LLM.OUTPUT, SP.LLM.KEY, SP.LLM.DATA |
| Deploy, hosting, headers | SP.TLS.HSTS, SP.HDR.CSP, SP.SECRETS.ENV, SP.HDR.LEAK, SP.SECRETS.SOURCEMAP |
| New dependency | SP.DEPS.VULN, SP.DEPS.EOL, SP.DEPS.PIN, SP.TRANSFER.MAP (if it calls home) |
| Footer, imprint, legal pages | SP.LEGAL.IDENTITY, SP.PRIVACY.CONTENT, SP.LEGAL.ODR, SP.CONSENT.WITHDRAW |
| Mobile app | SP.MOBILE.SDK, SP.MOBILE.STORAGE, SP.MOBILE.NETWORK, SP.MOBILE.LABELS, SP.MOBILE.DELETE |

## Pointers to other skills

This skill notices these but does not own them. Write a pointer finding only when running alone (`reported_by: hamu-security-privacy`, `owner_skill` set to the owner).

| Observation | Owner check |
|---|---|
| Cookie banner not keyboard operable or traps focus | A11Y.KBD.*, A11Y.FOCUS.* |
| Cookie banner causes layout shift | PX.CWV.CLS |
| Analytics no longer measures under consent | SEO.MEASURE.* |
| Dark pattern also hurts conversion | PX.CRO.* (SP keeps the legal finding) |
| `rel="sponsored"` missing on affiliate links | SEO.LINK.REL |
| Server slow or down | PX.SERVER.* |
