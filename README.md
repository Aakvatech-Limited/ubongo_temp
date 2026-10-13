# Ubongo Governance

A new standalone Frappe v16.50+ governance app for **DARCI, enterprise risks, compliance, contract lifecycle and intellectual-property rights**.

## Included
- 9 standard DocTypes including DARCI and contract-obligation child tables
- Enforced DARCI ownership, risk scoring, basic contract and IP-license guardrails
- Cross-functional compliance assessments with corrective-action tracking
- Governance Overview workspace and Compliance Control Register report
- Daily due-date desk alerts and an explicit, repeatable demo-data loader

## Install
```sh
bench get-app https://github.com/Aakvatech-Limited/ubongo_temp --branch feat/governance-darci-risk-compliance-contract-ip
bench --site SITE install-app ubongo_temp
bench --site SITE migrate
```

To add **sample data only on a test site**:
```sh
bench --site SITE execute ubongo_temp.governance.demo.install_demo
```

See [User Guide](docs/USER_GUIDE.md), [Implementation Notes](docs/IMPLEMENTATION.md) and [Requirements Coverage](docs/REQUIREMENTS_COVERAGE.md).

> Limitations: native Frappe Version audit and Attach fields provide initial document history/storage; full contract document diffing, provider-backed e-signature, immutable approvals, external infringement detection, and live multi-domain analytics require separate integrations/workflows. No live site validation has been performed.

## Finance extension

Includes disabled integration and banking registries, staged bank entries, BVA snapshots, financial scenarios and opt-in synthetic demo seed. No real provider/bank API is implemented. See [finance notes](docs/FINANCE_AND_INTEGRATIONS.md).
