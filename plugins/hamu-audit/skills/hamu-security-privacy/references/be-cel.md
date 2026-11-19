---
framework: BE-CEL
name: Belgian Code of Economic Law (Wetboek van economisch recht / Code de droit économique) and Code of Companies and Associations, website disclosures
last_verified: 2026-11-19
sources:
  - https://www.ejustice.just.fgov.be/ (Code of Economic Law, consolidated)
  - https://economie.fgov.be/
  - https://www.vlaio.be/nl/nieuws/website-facebookpagina-van-je-bedrijf-deze-gegevens-zijn-verplicht
  - https://www.cms.law/en/bel/legal-updates/belgian-consumer-law-reform-new-rules-on-online-sales-subscription-renewals-sustainability-claims-and-consumer-complaints
status: partly verified; article numbers marked verify were taken from secondary sources only
---

# BE-CEL: Belgian disclosure duties

Applies to almost every business site of an organisation established in Belgium. Supervisor: FPS Economy (FOD Economie / SPF Economie), Economic Inspection.

## Where the rules sit

| Topic | Source | Status |
|---|---|---|
| Information society service provider must show identity, address, email, enterprise number, VAT, professional details | Code of Economic Law, Book XII (transposes e-Commerce Directive 2000/31/EC Art. 5), Art. XII.6 | verify article |
| General information duties of enterprises to consumers | Code of Economic Law, Book VI, Art. VI.2 | verify article |
| Distance contracts: pre-contract information | Code of Economic Law, Book VI, Art. VI.45 | cross-checked with secondary sources |
| Withdrawal right of 14 days | Art. VI.47 | cross-checked with secondary sources |
| Online withdrawal function (Directive (EU) 2023/2673) | Belgian transposition bill (Chamber doc. 56K1532) not yet published in the Belgian Official Gazette as of September 2026 per secondary sources. Earlier reports of a "Law of 19 July 2026" could not be confirmed. Draft article numbers differ between sources (VI.47, VI.48, VI.61/1) | verify publication before citing a Belgian article |
| Company details on website (name, legal form, registered office, enterprise number, words "rechtspersonenregister"/"registre des personnes morales" with the court) | Code of Companies and Associations (WVV/CSA), Art. 2:20 | cross-checked with VLAIO and legal commentary |
| Electronic direct marketing (opt-in) | Book XII and Royal Decree of 4 April 2003 | verify |

## Checklist for SP.LEGAL.IDENTITY

Must be easy to find (footer or imprint page, reachable from every page):

1. Company name and legal form (BV/SRL, NV/SA, CommV/SComm ...).
2. Registered office address.
3. Enterprise number (KBO/BCE), format `0xxx.xxx.xxx` or `1xxx.xxx.xxx`. Checksum: the last two digits equal 97 minus (first eight digits mod 97).
4. The words "RPR" / "RPM" (rechtspersonenregister / registre des personnes morales) followed by the court of the registered office.
5. Email address and a way of direct contact.
6. VAT number where VAT registered (in Belgium usually `BE` + enterprise number).
7. For regulated professions: professional body, title, country that granted it, rules that apply.

Sanctions for missing company details exist (fines, per secondary sources EUR 156 to 30,000). Do not quote amounts in a report until verified in the statute.

## Belgium-specific consumer points

- The CMS update reports a 2026 Belgian consumer law reform touching online sales, subscription renewals, sustainability claims and complaint handling. Check the published law before adding checks beyond SP.CONSUMER.SUBSCRIPTION (verify).
- Consumer Mediation Service (Consumentenombudsdienst / Service de Médiation pour le Consommateur) is the residual ADR body for Belgian consumer disputes. Used by SP.LEGAL.ADR.
