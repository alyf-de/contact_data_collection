// Copyright (c) 2020, ALYF GmbH and contributors
// For license information, please see license.txt

frappe.ui.form.on('Contact Data', {
	refresh: function (frm) {
		if (!frm.is_new()) {
			frm.add_custom_button(__('Who was there at the same time?'), () => {
				frappe.set_route('query-report', 'People By Time', {
					from_time: frm.doc.present_from,
					to_time: frm.doc.present_to
				});
			});
		}
	}
});
