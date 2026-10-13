import frappe

def execute(filters=None):
    cols=[{"label":"Forecast","fieldname":"name","fieldtype":"Link","width":160},{"label":"Scenario","fieldname":"scenario","fieldtype":"Data","width":160},{"label":"Currency","fieldname":"currency","fieldtype":"Data","width":160},{"label":"Revenue","fieldname":"total_revenue","fieldtype":"Currency","width":160},{"label":"Costs","fieldname":"total_cost","fieldtype":"Currency","width":160},{"label":"Net","fieldname":"net_projection","fieldtype":"Currency","width":160}]
    data=frappe.get_list("Financial Forecast", fields=["name","scenario","currency","total_revenue","total_cost","net_projection"], limit_page_length=0, order_by="modified desc")
    return cols,data
