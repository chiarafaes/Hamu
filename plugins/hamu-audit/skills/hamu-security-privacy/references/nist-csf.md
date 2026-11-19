---
framework: NIST-CSF
name: NIST Cybersecurity Framework 2.0 (with SP 800-53 Rev. 5 as control catalogue)
last_verified: 2026-11-19
sources:
  - https://www.nist.gov/cyberframework
  - https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf
  - https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final
status: verified
licence_note: NIST publications are US government works and not subject to copyright in the US. Hamu still uses ids and short labels.
---

# NIST CSF 2.0 readiness

Readiness only. Published 26 February 2024. Voluntary. Used by US clients and as a common language for security programmes. CSF 2.0 added the Govern function and covers organisations of every size.

## Functions and Hamu evidence

| Function | Categories the checks feed | Evidence from Hamu checks |
|---|---|---|
| GV Govern | GV.OC context, GV.RM risk strategy, GV.RR roles, GV.PO policy, GV.OV oversight, GV.SC supply chain | SP.RESIL.SUPPLIER, manual |
| ID Identify | ID.AM asset management, ID.RA risk assessment, ID.IM improvement | SP.DEPS.SBOM, SP.TRANSFER.MAP, manual |
| PR Protect | PR.AA identity and access, PR.AT awareness, PR.DS data security, PR.PS platform security, PR.IR infrastructure resilience | SP.AUTH.*, SP.ACCESS.*, SP.TLS.*, SP.INFRA.*, SP.HDR.*, SP.RESIL.BACKUP |
| DE Detect | DE.CM continuous monitoring, DE.AE adverse event analysis | SP.LOG.* |
| RS Respond | RS.MA management, RS.AN analysis, RS.CO reporting and communication, RS.MI mitigation | SP.RESIL.INCIDENT |
| RC Recover | RC.RP recovery plan execution, RC.CO communication | SP.RESIL.BACKUP, manual |

Cite categories (for example `PR.AA`) as `evidence_for`. Cite SP 800-53 controls (for example `AC-3`, `IA-2`) only when the user asks for an 800-53 view.

## Manual checklist (needs_manual)

1. Current and target profile, or at least a list of priorities.
2. Named owner for cybersecurity risk at management level.
3. Asset and data inventory.
4. Incident response plan tested in the last 12 months.
5. Recovery objectives (RTO, RPO) for critical services.
