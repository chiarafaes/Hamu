---
framework: CIS
name: CIS Benchmarks and CIS Controls (ids only)
last_verified: 2026-11-19
sources:
  - https://www.cisecurity.org/cis-benchmarks
  - https://www.cisecurity.org/controls
status: verified for structure; benchmark versions change often, cite the version the user runs
licence_note: CIS Benchmarks are licensed for non-commercial use with terms of their own. Hamu cites benchmark names and section numbers only and never copies recommendation text.
---

# CIS

Applies when the audit includes a codebase or infrastructure config (Dockerfile, Kubernetes manifests, Terraform, server config). For URL-only audits, CIS checks are `not_tested`.

## What the skill checks

| Area | Example rules (own words) | Hamu check |
|---|---|---|
| Docker (CIS Docker Benchmark) | Run as non-root user, use trusted and pinned base images, no secrets in image layers, add a health check | SP.INFRA.CONTAINER |
| Kubernetes (CIS Kubernetes Benchmark) | No privileged containers, read-only root filesystem where possible, resource limits, network policies | SP.INFRA.CONTAINER |
| Cloud (CIS AWS / Azure / GCP Foundations) | No public storage buckets, no admin ports open to the internet, logging enabled, encryption at rest | SP.INFRA.IAC, SP.INFRA.ENCRYPT |
| Web server | No version banners, no directory listing, TLS hardening | SP.HDR.LEAK, SP.INFRA.EXPOSE, SP.TLS.VERSION |
| Email domain | SPF, DMARC, DKIM | SP.DNS.* |

## Tools (Claude Code)

Only with the user's agreement, run without installing permanently: `pipx run checkov -d .` for IaC, `npx` or Docker-based `trivy config .` if available. Without tools: pattern search with lower confidence.

Relation is always `best_practice`. CIS Controls v8 ids may be added as `evidence_for` when the user asks for a CIS Controls view (phase 1b readiness work).
