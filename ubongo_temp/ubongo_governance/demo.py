"""Explicit opt-in demo seed. Run bench --site SITE execute ubongo_temp.governance.demo.install_demo."""
import frappe
from frappe.utils import add_days, today

def _ensure(doctype, titlefield, title, values):
    filters = {titlefield: title}
    existing = frappe.db.exists(doctype, filters)
    if existing:
        return existing
    return frappe.get_doc({"doctype": doctype, titlefield: title, **values}).insert(ignore_permissions=True).name

def install_demo():
    """Clearly named SAMPLE records. Never called by install/migrate hooks."""
    user = frappe.session.user if frappe.session.user != "Guest" else "Administrator"
    p = _ensure("Governance Project", "project_title", "[DEMO] Digital Operations Governance", {
        "status": "Active", "business_unit": "Technology", "owner": user,
        "darci": [{"responsibility": r, "user": user} for r in
                  ("Driver", "Approver", "Responsible", "Consulted", "Informed")],
        "summary": "Demo DARCI allocation; replace with real staff before operational use."
    })
    _ensure("Governance Risk", "risk_title", "[DEMO] Vendor continuity risk", {
        "domain": "Operations", "project": p, "functional_area": "Procurement", "owner": user,
        "likelihood_rating": 0.6, "impact_rating": 0.8, "status": "Treating", "treatment": "Mitigate",
        "mitigation_plan": "Evaluate alternate suppliers and review quarterly.",
        "review_date": add_days(today(), 20)
    })
    requirement = _ensure("Compliance Requirement", "requirement_title", "[DEMO] Access review control", {
        "standard": "Demo Internal Policy", "functional_area": "Information Security", "owner": user,
        "frequency": "Quarterly", "due_date": add_days(today(), 20),
        "control_description": "Review privileged access quarterly.", "status": "Active"
    })
    if not frappe.db.exists("Compliance Assessment", {"requirement": requirement, "remarks": "[DEMO] Seed assessment"}):
        frappe.get_doc({"doctype": "Compliance Assessment", "requirement": requirement,
            "assessment_date": today(), "assessor": user, "result": "Compliant",
            "action_status": "Not Required", "remarks": "[DEMO] Seed assessment"}).insert(ignore_permissions=True)
    _ensure("Governance Contract", "contract_title", "[DEMO] Supplier services agreement", {
        "counterparty": "Demo Supplier", "stage": "Drafting", "contract_owner": user,
        "renewal_notice_date": add_days(today(), 25), "end_date": add_days(today(), 90),
        "obligations": [{"obligation": "Submit quarterly service report", "owner": user,
                         "due_date": add_days(today(), 30), "status": "Open"}]
    })
    a = _ensure("IP Asset", "asset_title", "[DEMO] Proprietary Training Methodology", {
        "asset_type": "Methodology", "owner": user, "status": "Active",
        "territory": "Tanzania", "rights_summary": "Demo proprietary educational method.",
        "infringement_status": "None Reported"
    })
    if not frappe.db.exists("IP License", {"asset": a, "licensee": "[DEMO] Research Team"}):
        frappe.get_doc({"doctype": "IP License", "asset": a,
            "licensee": "[DEMO] Research Team", "license_type": "Research",
            "valid_from": today(), "valid_until": add_days(today(), 45),
            "status": "Draft", "permitted_use": "Evaluation and internal research only.",
            "owner": user}).insert(ignore_permissions=True)
    frappe.db.commit()
    print("Demo governance data installed; all sample records have [DEMO] labels.")
