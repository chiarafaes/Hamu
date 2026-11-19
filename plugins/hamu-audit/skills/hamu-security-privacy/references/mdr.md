---
framework: MDR
name: EU Medical Device Regulation (Regulation (EU) 2017/745), software as a medical device
last_verified: 2026-11-19
sources:
  - https://eur-lex.europa.eu/eli/reg/2017/745/oj
  - https://health.ec.europa.eu/medical-devices-sector/new-regulations/guidance-mdcg-endorsed-documents-and-other-guidance_en
  - https://www.famhp.be/ (FAMHP / FAGG / AFMPS)
status: verified for articles; transition periods verify
---

# MDR

Software is a medical device when the manufacturer intends it for a medical purpose: diagnosis, prevention, monitoring, prediction, prognosis, treatment or alleviation of disease (Art. 2(1)). Wellness and lifestyle apps without a medical claim are not. Belgian authority: FAMHP (FAGG / AFMPS).

## Classification

Annex VIII, Rule 11: software that provides information used for diagnostic or therapeutic decisions is class IIa at least, IIb or III when decisions could cause serious harm or death. Software that monitors physiological processes is IIa (IIb for vital parameters where variations could mean immediate danger). Other software is class I. Guidance: MDCG 2019-11 (verify current revision).

## How the skill uses it

The skill does not assess conformity. It only flags scope:
- `applies` when `medical_purpose = true`.
- `likely` when health vocabulary appears with diagnostic or therapeutic claims ("detects", "diagnoses", "treats").

One finding under SP.PRIVACY.SPECIAL with `MDR` as framework and `legal_review: true`: "This product may be a medical device. Confirm the intended purpose with a regulatory expert." Health data also triggers GDPR Art. 9 checks.

Transition periods for legacy devices were extended by Regulation (EU) 2023/607 (verify current end dates before quoting).
