---
framework: DORA
name: Digital Operational Resilience Act (Regulation (EU) 2022/2554)
last_verified: 2026-11-19
sources:
  - https://eur-lex.europa.eu/eli/reg/2022/2554/oj
  - https://www.nbb.be/ (National Bank of Belgium)
  - https://www.fsma.be/
status: verified
---

# DORA

Applies since **17 January 2025** to financial entities in the EU (banks, payment and e-money institutions, investment firms, insurers, crypto-asset service providers and others). Belgian supervisors: National Bank of Belgium (NBB) and FSMA.

## Who

- `applies`: the organisation is a financial entity.
- `likely` (relation `best_practice`): the organisation is an ICT third-party service provider to financial entities. Contracts must then contain the clauses of Art. 30, and the client will ask for evidence. Critical ICT providers designated by the European Supervisory Authorities have direct oversight.

## Pillars and checks

| Pillar | Articles | Check |
|---|---|---|
| ICT risk management | Art. 5 to 16 | SP.ACCESS.*, SP.AUTH.MFA, SP.TLS.*, SP.LOG.*, SP.RESIL.BACKUP |
| ICT incident reporting | Art. 17 to 23 | SP.RESIL.INCIDENT |
| Resilience testing | Art. 24 to 27 | manual. Threat-led penetration testing only for designated entities |
| Third-party risk | Art. 28 to 44 | SP.RESIL.SUPPLIER |
| Information sharing | Art. 45 | not checked |

Process duties are `needs_manual`. The skill reports the technical evidence it can see and lists the rest as a human task.
