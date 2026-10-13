import re
import frappe
from frappe.utils import flt, getdate

def validate_forecast(doc, method=None):
    pattern = r"^\\d{4}-(0[1-9]|1[0-2])$"
    if not re.fullmatch(pattern, doc.from_period or "") or not re.fullmatch(pattern, doc.to_period or "") or doc.from_period > doc.to_period:
        frappe.throw("Invalid forecast period range")
    if not doc.get("lines"):
        frappe.throw("Forecast needs at least one line")
    revenue = cost = 0
    for row in doc.lines:
        if not re.fullmatch(pattern, row.period or "") or not doc.from_period <= row.period <= doc.to_period:
            frappe.throw("Line period outside forecast range")
        row.forecast_amount = flt(flt(row.baseline) * (1 + flt(row.adjustment_percent) / 100) + flt(row.manual_adjustment), 2)
        if row.category == "Revenue":
            revenue += row.forecast_amount
        else:
            cost += row.forecast_amount
    doc.total_revenue, doc.total_cost = flt(revenue, 2), flt(cost, 2)
    doc.net_projection = flt(revenue - cost, 2)

def validate_bva(doc, method=None):
    if getdate(doc.period_from) > getdate(doc.period_to):
        frappe.throw("Invalid BVA date range")
    if not doc.get("lines"):
        frappe.throw("BVA needs at least one line")
    budget = actual = 0
    for row in doc.lines:
        row.variance = flt(flt(row.actual) - flt(row.budget), 2)
        row.variance_percent = flt(100 * row.variance / flt(row.budget), 2) if flt(row.budget) else 0
        row.favourability = "On Budget" if row.variance == 0 else ("Favourable" if ((row.category == "Revenue") == (row.variance > 0)) else "Unfavourable")
        budget += flt(row.budget)
        actual += flt(row.actual)
    doc.total_budget, doc.total_actual, doc.total_variance = flt(budget, 2), flt(actual, 2), flt(actual-budget, 2)

def validate_bank_feed(doc, method=None):
    if frappe.db.exists("Bank Feed Entry", {"connection": doc.connection, "external_id": doc.external_id, "name": ["!=", doc.name]}):
        frappe.throw("Duplicate transaction identifier for this bank connection")
    if doc.status == "Imported" and not doc.bank_transaction:
        frappe.throw("Imported status requires ERPNext Bank Transaction reference")
