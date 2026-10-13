import frappe

def execute(filters=None):
    cols=[{"label":"Review","fieldname":"name","fieldtype":"Link","width":160},{"label":"Currency","fieldname":"currency","fieldtype":"Data","width":160},{"label":"Period From","fieldname":"period_from","fieldtype":"Date","width":160},{"label":"Period To","fieldname":"period_to","fieldtype":"Date","width":160},{"label":"Budget","fieldname":"total_budget","fieldtype":"Currency","width":160},{"label":"Actual","fieldname":"total_actual","fieldtype":"Currency","width":160},{"label":"Variance","fieldname":"total_variance","fieldtype":"Currency","width":160}]
    data=frappe.get_list("Budget Variance Review", fields=["name","currency","period_from","period_to","total_budget","total_actual","total_variance"], limit_page_length=0, order_by="modified desc")
    return cols,data
