# Implementation and technical notes

Target: Frappe Framework 16.50+; this repository began empty. This is a first-pass application scaffold, **not a tested site export**.

Run `bench migrate` after install. Roles Governance Manager and Governance User receive basic permissions; refine them before production. The workspace is standard JSON but still needs Frappe-site round-trip export and visual QA; Sidebar and Dock should be generated in Developer Mode with **Edit Sidebar → For Your App** and **Manage Dock → Export to App**. Do not fabricate or load unvalidated v16.50 Dock/Sidebar records.

Security follow-up: apply least privilege, field-level controls for contract/IP confidentiality, private file attachments and document sharing policy. Restrict demo seeding to test sites, ensure all users assigned to DARCI are valid.

Contract electronic approvals and signatures: use Frappe Workflow and a vetted signature-provider integration; store callback verification, signer identity, immutable evidence, signature timestamps and provider envelope ID. Current provider fields are tracking metadata only. Audit Frappe Version is not immutable document-version custody.

Monitoring: `check_governance_alerts` runs daily and writes Notification Log desk alerts for key due dates within 30 days. SLA reminders for obligations and overdue escalations require additional implementation; API access and notification rules should be reviewed on an actual site.

Dashboard: Governance Overview provides navigation and the Governance Control Register provides reporting; executive KPI charts and Frappe Dashboard record exports need validation on a live v16.50 site before shipping. Suggested KPIs: open high risks (score ≥15), overdue compliance actions, contracts expiring in 30 days, overdue obligations, expiring IP licenses, project DARCI completeness.

Developer smoke tests: install, migrate, create every DocType, save valid/invalid DARCI, calculate risk score, reject unsigned Active contract, reject incomplete corrective action, reject invalid IP license dates, invoke demo loader twice, open report, run daily alert task, review ordinary-user navigation.
