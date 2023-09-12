from frappe import _
import frappe

def validate(doc):

   
    if not doc.date_of_birth:
        frappe.throw("Date of Birth is required.")

   
    dob = doc.date_of_birth
    today = frappe.utils.nowdate()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

   
    if age < 18:
        frappe.throw("custom type must be at least 18 years old.")
