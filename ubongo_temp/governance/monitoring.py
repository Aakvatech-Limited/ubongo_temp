import frappe
from frappe.utils import today, add_days

def check_governance_alerts():
    """Daily desk notifications, idempotent per recipient/document/day."""
    now = today()
    soon = add_days(now, 30)
    rules = (
        ("Governance Contract", "renewal_notice_date", ["Active", "Executed"], "contract_owner", "Contract renewal notice"),
        ("Compliance Requirement", "due_date", ["Active"], "owner", "Compliance review due"),
        ("Governance Risk", "review_date", ["Open", "Treating", "Monitoring"], "owner", "Risk review due"),
        ("IP License", "valid_until", ["Active"], "owner", "IP license expiry"),
        ("IP Asset", "expiry_date", ["Active", "Registered"], "owner", "IP registration expiry"),
    )
    for doctype, date_field, states, owner_field, subject in rules:
        status_field = "stage" if doctype == "Governance Contract" else "status"
        records = frappe.get_all(doctype, filters={status_field: ["in", states], date_field: ["between", [now, soon]]},
            fields=["name", owner_field, date_field])
        for row in records:
            recipient = row.get(owner_field)
            if not recipient or recipient == "Administrator":
                continue
            # Notification Log stores recipient, document and subject; dedup by notification date.
            if frappe.db.exists("Notification Log", {"for_user": recipient, "document_type": doctype,
                    "document_name": row.name, "subject": subject + ": " + row.name,
                    "creation": [">=", now]}):
                continue
            frappe.get_doc({"doctype": "Notification Log", "for_user": recipient, "type": "Alert",
                "document_type": doctype, "document_name": row.name,
                "subject": subject + ": " + row.name}).insert(ignore_permissions=True)
