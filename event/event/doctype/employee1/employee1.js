// Copyright (c) 2023, frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Employee1', {
	before_save: function (frm) {
		
		if (frm.doc.is_active) {
			frm.doc.status = 'Active';
		} else {
			frm.doc.status = 'Inactive';
		}
	}
});
