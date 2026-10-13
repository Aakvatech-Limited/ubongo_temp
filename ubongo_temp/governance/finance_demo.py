import frappe
from frappe.utils import today

def make(dt, field, key, attributes):
    return frappe.db.exists(dt, {field:key}) or frappe.get_doc({"doctype":dt,field:key,**attributes}).insert(ignore_permissions=True).name

def install_finance_demo():
    for provider in ("ApprovalMax", "Everhour", "Gusto", "Google Drive", "Payroll Software"):
        make("Integration Connection","connection_name","[DEMO] "+provider,{"provider":provider,"enabled":0,"notes":"Simulated configuration, no API connection"})
    for bank in ("BRA","CRDB","Stanbic"):
        conn=make("Bank Feed Connection","connection_name","[DEMO] "+bank,{"bank":bank,"account_label":"Synthetic operating account","masked_account":"****0000","enabled":0})
        if not frappe.db.exists("Bank Feed Entry",{"connection":conn,"external_id":"DEMO-"+bank+"-001"}):
            frappe.get_doc({"doctype":"Bank Feed Entry","connection":conn,"external_id":"DEMO-"+bank+"-001","posting_date":today(),"amount":1250000,"narration":"[DEMO] Simulated customer receipt"}).insert(ignore_permissions=True)
    period=today()[:7]
    for scenario,adjust in (("Base",0),("Optimistic",15),("Pessimistic",-15)):
        make("Financial Forecast","forecast_title","[DEMO] "+scenario+" Forecast",{"scenario":scenario,"currency":"TZS","from_period":period,"to_period":period,"lines":[{"period":period,"category":"Revenue","baseline":10000000,"adjustment_percent":adjust},{"period":period,"category":"Operating Expense","baseline":6500000}]})
    make("Budget Variance Review","review_title","[DEMO] Monthly BVA",{"period_from":period+"-01","period_to":today(),"currency":"TZS","lines":[{"account":"Sample Revenue","category":"Revenue","budget":10000000,"actual":9200000},{"account":"Sample Expenses","category":"Expense","budget":6500000,"actual":6750000}]})
    frappe.db.commit()
    print("Synthetic financial examples created; no external feeds or APIs connected.")
