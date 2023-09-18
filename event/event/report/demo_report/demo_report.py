# Copyright (c) 2023, frappe and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    labels = []
    values = []
    for k in data:
        labels.append(k['date_of_birth'])
        values.append(k['age'])
        chart = {
        "type": "bar",
        "data": {
			"labels": labels,
			"datasets": [
				    {"values": values},	
        	],
        },
    }
    return columns, data, "demo report", chart


def get_columns():
    columns = [
        {
            'fieldname': 'date_of_birth',
            'label': 'Date_Of_Birth',
            'fieldtype': 'Date',
        },
        {
            'fieldname': 'age',
            'label': 'Age',
            'fieldtype': 'Data',
        },
    ]
    return columns

def get_data(filters):
    data = frappe.db.get_all("Custom Type", filters=filters, fields=["date_of_birth", "age"])
    return data
