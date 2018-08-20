# Copyright (c) 2013, Frappe and contributors
# For license information, please see license.txt


from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import flt, cint, getdate, now
from frappe import msgprint, _

def execute(filters=None):
	if not filters: filters = frappe._dict({})
	data_list = get_data(filters)
	columns = get_columns()
	if not data_list:
		msgprint(_("No record found"))
	data  = []

	for d in data_list:
		
		row = [
			
			d.name, d.date,d.warehouse
		
			]
		
		
		row +=    [d.cash_deposit_amount,d.cash_deposit_date,d.deposit_slip,d.scratch_card_ticket,d.scratch_card_serial,d.lock_no,d.card_realisation_amount,d.card_settlement_batch]
		data.append(row)
	
	return columns, data


	
	


def get_columns():
	#return columns#

	columns = [
		_("DSR1")+":Link/Item:100",
		_("Date1")+"::150",
		_("Warehouse1")+":Link/Warehouse:100",
		_("Cash Deposit Amount1")+":Link/Item Group:100",
		_("Cash Deposit Date1")+":Link/Brand:90",
		_("Deposit Slip1#")+"::140",
		_("Scratch Card Ticket1#")+"::100",
		_("Scratch Card Serial1#")+"::100",
		_("Lock1#")+"::100",
		_("Card Realisation Amount1")+"::100",
		_("Card Settlement batch1#")+"::100",
		 ]
		

	return columns


def get_conditions(filters):
	conditions = ""


	if filters.get("from_date"): conditions += " and date >= %(from_date)s"
	if filters.get("to_date"): conditions += " and date <= %(to_date)s"

	if filters.get("warehouse"): conditions += " and warehouse = %(warehouse)s"

	return conditions


def get_data(filters):
	conditions = get_conditions(filters)
	return frappe.db.sql("""
		select name, date, warehouse,cash_deposit_amount, cash_deposit_date, 
		deposit_slip,scratch_card_ticket,scratch_card_serial,lock_no,card_realisation_amount,card_settlement_batch
		from `tabDSR`
		where docstatus = 1  %s order by name desc """ %
		conditions, filters, as_dict=1)

