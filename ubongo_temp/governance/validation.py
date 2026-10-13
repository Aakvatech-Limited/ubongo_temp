import frappe
from frappe.utils import getdate

def validate_darci(doc, method=None):
    rows = doc.get("darci") or []
    counts = {}
    seen = set()
    for row in rows:
        if not row.user or not row.responsibility:
            frappe.throw("Each DARCI assignment requires a user and role")
        key = (row.user, row.responsibility)
        if key in seen:
            frappe.throw("Duplicate DARCI user/role allocation is not allowed")
        seen.add(key)
        counts[row.responsibility] = counts.get(row.responsibility, 0) + 1
    if doc.status != "Draft":
        if counts.get("Driver", 0) != 1 or counts.get("Approver", 0) != 1:
            frappe.throw("An active project requires exactly one Driver and one Approver")
        if not counts.get("Responsible", 0):
            frappe.throw("An active project requires at least one Responsible assignment")
    if doc.start_date and doc.end_date and getdate(doc.start_date) > getdate(doc.end_date):
        frappe.throw("Project end date must not precede start date")

def validate_risk(doc, method=None):
    if not (1 <= int(doc.likelihood or 0) <= 5) or not (1 <= int(doc.impact or 0) <= 5):
        frappe.throw("Likelihood and impact must each be between 1 and 5")
    doc.risk_score = int(doc.likelihood) * int(doc.impact)
    if doc.status in ("Treating", "Monitoring") and not doc.mitigation_plan:
        frappe.throw("A mitigation plan is required while treating/monitoring a risk")

def validate_contract(doc, method=None):
    if doc.start_date and doc.end_date and getdate(doc.start_date) > getdate(doc.end_date):
        frappe.throw("Contract expiry must not precede effective date")
    if doc.stage in ("Executed", "Active") and not doc.signed_document:
        frappe.throw("Signed contract copy is required for Executed/Active stage")
    if doc.stage == "Active" and not doc.start_date:
        frappe.throw("Effective date is required for an Active contract")
    if doc.stage == "Approval Pending" and not doc.document:
        frappe.throw("Attach the contract draft before requesting approval")
    for row in doc.get("obligations") or []:
        if row.status == "Fulfilled" and not row.completed_on:
            frappe.throw("Fulfilled obligations require a completion date")

def validate_license(doc, method=None):
    if doc.valid_from and doc.valid_until and getdate(doc.valid_from) > getdate(doc.valid_until):
        frappe.throw("License end must not precede start")
    if doc.status == "Active" and not doc.agreement:
        frappe.throw("Active IP licenses require an attached permission agreement")

def validate_assessment(doc, method=None):
    if doc.result in ("Partially Compliant", "Non-Compliant"):
        if not doc.gap or not doc.action_plan or not doc.action_owner or not doc.target_date:
            frappe.throw("Non-compliance requires a documented gap, action plan, owner and target date")
    if doc.action_status == "Verified" and not doc.evidence:
        frappe.throw("Verified corrective action requires evidence")
