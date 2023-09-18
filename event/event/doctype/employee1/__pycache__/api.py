import frappe

@frappe.whitelist()
def get_custom_type_detali():
    return frappe.db.sql(f"""SELECT first_name FROM `tabCustom Type` WHERE ownr='Administrator';""", as_dict=True)