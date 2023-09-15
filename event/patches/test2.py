import frappe
from frappe.utils import nowdate
from datetime import datetime

def execute():
    custom_type_docs = frappe.get_all("Custom Type", filters={}, fields=["name", "date_of_birth", "age"])
    for doc in custom_type_docs:
        date_of_birth_str = doc.date_of_birth
        today = datetime.now().date()
        birth_date = frappe.utils.getdate(date_of_birth_str)
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        frappe.db.set_value("Custom Type", doc.name, "age", age)
