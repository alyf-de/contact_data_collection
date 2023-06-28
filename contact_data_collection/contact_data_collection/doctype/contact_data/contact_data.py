# -*- coding: utf-8 -*-
# Copyright (c) 2020, ALYF GmbH and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
from datetime import datetime, timedelta

import frappe
from frappe.model.document import Document
from frappe.utils import validate_email_address, validate_phone_number


class ContactData(Document):

	def validate(self):
		validate_email_address(self.email_address)
		validate_phone_number(self.phone)


def delete_records(older_than: timedelta=None):
	"""Delete Contact Data that is older than the specfied timedelta.

	If `older_than` is not specified, the number of days specified in Contact
	Data Collection Settings is used.
	"""
	if not older_than:
		delete_after = frappe.db.get_single_value("Contact Data Collection Settings", "delete_contact_data_after")
		older_than = timedelta(days=delete_after)

	deletion_date = datetime.now() - older_than
	records_to_remove = frappe.get_list("Contact Data", {
		"creation": ("<=", deletion_date)
	})

	for record in records_to_remove:
		doc = frappe.get_doc("Contact Data", record.name)
		doc.delete()
