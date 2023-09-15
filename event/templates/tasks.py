import frappe
import string
import random

def cron():

    print("/n/n New Note Inserted /n/n")
    letters = string.ascii_letters
    note = " ".join(random.choice(letters) for i in range(5))

    new_note = frappe.get_doc({"doctype": "Note",
                               "title": note
                               })
    new_note.insert()
    frappe.db.commit()