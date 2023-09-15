// Copyright (c) 2023, frappe and contributors
// For license information, please see license.txt

//onchange event 

frappe.ui.form.on('Custom Type', {
	
		  refresh: function(frm) {
			frm.fields_dict['date_of_birth'].df.onchange = function() {
				var date_of_birth = frm.doc.date_of_birth;
				if (date_of_birth) {	
					var today = new Date();
					var birthDate = new Date(date_of_birth);
					var age = today.getFullYear() - birthDate.getFullYear();
					var monthDiff = today.getMonth() - birthDate.getMonth();
					if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < birthDate.getDate())) {
						age--;
					}	
					frm.set_value('age', age);
				}
			};
			
			frm.fields_dict['first_name'].df.onchange = function() {
				
				var first_name = frm.doc.first_name || '';
				var last_name = frm.doc.last_name || '';
				var full_name = first_name + ' ' + last_name;
				frm.set_value('full_name', full_name);
			};
			frm.fields_dict['last_name'].df.onchange = function() {
				
				var first_name = frm.doc.first_name || '';
				var last_name = frm.doc.last_name || '';
				var full_name = first_name + ' ' + last_name;
				frm.set_value('full_name', full_name);
			};
			
		}
	});

//onload event
frappe.ui.form.on('Custom Type', {
    onload: function (frm) {
        function showAlertOnLoad() {
            alert("Page is sucessfully loaded!");
        }
		 window.onload = showAlertOnLoad;
	} 
});
//validate
frappe.ui.form.on('Custom Type', {
    validate: function(frm) {
        var totalAmount = frm.doc.total_amount;
        var maximumLimit = frm.doc.maximum_limit;

        if (totalAmount > maximumLimit) {
            frappe.msgprint(__("Total amount is greater."));
		}
		else{
			frappe.msgprint(__("maximum limit is greater ."));
		}	
            frappe.validated = false; 
        }
    }
);


//refresh event
frappe.ui.form.on('Custom Type', {
    refresh: function (frm) {
        
        frm.add_custom_button('Custom Button', function () {
            
            frappe.msgprint('Custom button clicked!');
        });
    }
});

// //After save event
// frappe.ui.form.on('Custom Type', {
//     after_save: function (frm) {
//         frappe.msgprint('Custom Type document has been successfully saved....');
//     }
// });

// //on submit event
// frappe.ui.form.on('Custom Type', {
//     on_submit: function (frm) {
//         frappe.msgprint('Custom Type document has been submitted.....')
// 	}
// });


// // before cancel event
// frappe.ui.form.on('Custom Type', {
//     before_cancel: function (frm) {
//         if (frm.doc.status !== 'Draft') {
//             frappe.msgprint('Document cannot be cancelled because it is not in the "Draft" status.');
//             frappe.validated = false; // Prevent cancellation
//         }
//     }
// });

// //after cancel event
// frappe.ui.form.on('Custom Type', {
//     after_cancel: function (frm) {
//         // Code to run after a 'Custom Type' document is canceled

//         alert('Document has been canceled.');
//     }
// });

// //timeline refersh
// frappe.ui.form.on('Custom Type', {
//     refresh: function(frm) {
//         var timelineCounter = 0;
//         function refreshTimeline() {
//             timelineCounter++;
//             frm.set_value('first_name', "Timeline refreshed: " + timelineCounter)
//             frm.refresh_field('first_name');
//         }
//         setInterval(refreshTimeline, 5000);

//     }
// });

// //onload_post_render event

// frappe.ui.form.on('Custom Type', {
//     onload: function(frm) {
//        
//         msgprint("Document onload: Page has fully loaded.");

//        
//         frappe.after_ajax(function() {
//             msgprint("Rendering is complete. Post-render event triggered.");
//         });
//     }
// });



// frappe.ui.form.on('My Custom DocType', {
//     form_render: function(frm) {
//         frappe.msgprint('Form has been rendered for My Custom DocType');
//     }
//});


















	
	
	
	
	
		

