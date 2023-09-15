
import frappe
from frappe.utils import getdate, nowdate

def execute():
    custom_type_docs = frappe.get_all("Custom Type", filters={"date_of_birth","age"}, fields=["date_of_birth","age"])

    for doc in custom_type_docs:
        
        date_of_birth = doc.date_of_birth

        
        if date_of_birth:
           
            dob = getdate(date_of_birth)

         
            today = nowdate()

            age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

            frappe.db.set_value("Custom Type", doc.name, "age", age)

    frappe.msgprint(("Age calculation completed for Custom Type documents."))

