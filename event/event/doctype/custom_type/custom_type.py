# # Copyright (c) 2023, frappe and contributors
# # For license information, please see license.txt

import frappe
from frappe.model.document import Document

# #on_trash event
# class CustomType(Document):
#     def on_trash(self):
#         frappe.msgprint(f"'Custom Type' {self.name} is being deleted!")
# def get_class():
#     return CustomType


# #on_cancel event
# class CustomType(Document):
#     def on_cancel(self):
#         frappe.msgprint(f"'Custom Type' {self.name} has been canceled!")

# def get_class():
#     return CustomType

# #on_submit event
# class CustomType(Document):
#     def on_submit(self):
#         frappe.msgprint(f"'Custom Type' {self.name} has been submited!")

# def get_class():
#     return CustomType

#on_trash event
class CustomType(Document):
    def on_trash(self):
        frappe.msgprint(f"'Custom Type' {self.name} is being deleted!")
def get_class():
    return CustomType


#on_cancel event
# class CustomType(Document):
#     def on_cancel(self):
#         frappe.msgprint(f"'Custom Type' {self.name} has been canceled!")


# def get_class():
#     return CustomType

