// Copyright (c) 2023, frappe and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["demo report"] = {
	"filters": [
		{
		'fieldname' : 'date_of_birth',
		'label' : 'Date_Of_Birth',
		'fieldtype' : 'Date'
		},

		{
			'fieldname':'age',
			'label':'Age',
			'fieldtype':'Data'
		},

	]
};
