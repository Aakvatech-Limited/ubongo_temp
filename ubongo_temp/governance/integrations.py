"""Configuration-only provider and bank integration layer, not a live connector."""
import frappe

def preview_connection(name):
    if not frappe.has_permission("Integration Connection", "read"):
        frappe.throw("Insufficient permission", frappe.PermissionError)
    c=frappe.get_doc("Integration Connection", name)
    return {"provider":c.provider,"enabled":bool(c.enabled),"status":c.last_sync_status,"message":"Adapter not implemented; external API disabled."}
