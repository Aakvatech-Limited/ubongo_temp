import frappe

def execute(filters=None):
    filters = filters or {}
    columns = [
        {"label": "Requirement", "fieldname": "requirement", "fieldtype": "Link", "options": "Compliance Requirement", "width": 240},
        {"label": "Functional Area", "fieldname": "functional_area", "fieldtype": "Data", "width": 160},
        {"label": "Assessment Date", "fieldname": "assessment_date", "fieldtype": "Date", "width": 120},
        {"label": "Result", "fieldname": "result", "fieldtype": "Data", "width": 160},
        {"label": "Action Status", "fieldname": "action_status", "fieldtype": "Data", "width": 140},
        {"label": "Target Date", "fieldname": "target_date", "fieldtype": "Date", "width": 120},
    ]
    query_filters = {}
    if filters.get("functional_area"):
        query_filters["functional_area"] = filters["functional_area"]
    if filters.get("result"):
        query_filters["result"] = filters["result"]
    data = frappe.get_list("Compliance Assessment", filters=query_filters,
        fields=["requirement", "functional_area", "assessment_date", "result", "action_status", "target_date"],
        order_by="assessment_date desc", limit_page_length=0)
    return columns, data
