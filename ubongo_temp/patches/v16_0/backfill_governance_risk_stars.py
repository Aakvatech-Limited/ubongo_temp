"""Initialize new five-star fields from existing 1–5 integer values using Query Builder."""
import frappe


def execute():
    if not frappe.db.table_exists("Governance Risk"):
        return
    if not frappe.db.has_column("Governance Risk", "likelihood_rating"):
        return
    if not frappe.db.has_column("Governance Risk", "impact_rating"):
        return

    risk = frappe.qb.DocType("Governance Risk")
    for row in frappe.get_all(
        "Governance Risk",
        fields=["name", "likelihood", "impact", "likelihood_rating", "impact_rating"],
        limit_page_length=0,
    ):
        updates = {}
        if not row.likelihood_rating and row.likelihood:
            updates["likelihood_rating"] = max(1, min(5, int(row.likelihood))) / 5
        if not row.impact_rating and row.impact:
            updates["impact_rating"] = max(1, min(5, int(row.impact))) / 5
        if updates:
            query = frappe.qb.update(risk)
            for fieldname, value in updates.items():
                query = query.set(getattr(risk, fieldname), value)
            query.where(risk.name == row.name).run()
