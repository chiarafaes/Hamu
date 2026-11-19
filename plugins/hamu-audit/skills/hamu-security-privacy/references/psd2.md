---
framework: PSD2
name: Payment Services Directive 2 (Directive (EU) 2015/2366) and RTS on strong customer authentication (Delegated Regulation (EU) 2018/389)
last_verified: 2026-11-19
sources:
  - https://eur-lex.europa.eu/eli/dir/2015/2366/oj
  - https://eur-lex.europa.eu/eli/reg_del/2018/389/oj
status: verified for current law; successor package (PSD3 / PSR) not yet checked, verify
---

# PSD2

## Who

- `applies`: the organisation is a payment service provider (payment institution, e-money institution, account information or payment initiation service).
- `not_applicable`: merchants that use a PSP such as Mollie, Stripe, Adyen or PayPal. The PSP handles strong customer authentication (SCA). The merchant must not break it, for example by storing card data or bypassing 3-D Secure.

## What the skill checks

- For merchants: nothing under PSD2. Card handling goes to `pci-dss.md`.
- For PSPs: SP.AUTH.MFA mapped to the SCA RTS (two of knowledge, possession, inherence, dynamic linking for remote payments). Everything else is out of scope for a website audit and goes to `needs_manual`.

## Future

The EU agreed a new Payment Services Regulation and PSD3 package. Do not check against it until it is published in the Official Journal and its application date is known (verify).
