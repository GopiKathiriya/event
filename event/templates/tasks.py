import frappe
import string
import random
from frappe.utils import now_datetime, add_days

def corn():
   
    letters = string.ascii_letters
    note = " ".join(random.choice(letters) for i in range(5))

    new_note = frappe.get_doc({"doctype": "Note",
                               "title": note
                               })
    new_note.insert()
    frappe.db.commit()


def daily():
    frappe.enqueue(send_daily_email, queue='long')

def send_daily_email():
    today = now_datetime()
    subject = "Daily Notification"
    message = "This is your daily notification email sent at {}".format(today)

    frappe.sendmail(
        recipients=["gopikathiriya2003@gmail.com"],  
        subject=subject,
        message=message,
    )
