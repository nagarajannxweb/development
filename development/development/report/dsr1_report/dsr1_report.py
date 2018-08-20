# Copyright (c) 2013, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import flt, cint, getdate, now
from frappe import msgprint, _



def execute(filters=None):
	if not filters: filters = frappe._dict({})
	

	invoice_list = get_invoices(filters)
	columns = get_columns()
	
	if not invoice_list:
		msgprint(_("No record found"))
	data  = []

	for inv in invoice_list:
		
		row = [
			#inv[0], inv[1], inv[2], inv[3],inv[4],inv[5]
			inv.name, inv.date,inv.warehouse
		
			]
		
		
		row +=    [inv.brand_sales_target,inv.total_pos_sale,inv.virtaul_store_sale,inv.walkin_conversion,inv.target_achievement,inv.abv,inv.abq,inv.target_achievement] 

		data.append(row)
	
	return columns, data



def get_columns():
	#return columns#

	columns = [
		_("DSR1")+":Link/Item:100",
		_("Date1")+"::150",
		_("Warehouse1")+":Link/Warehouse:100",
		_("Brand Sales Target1")+":Link/Item Group:100",
		_("Total POS Sale1")+":Link/Brand:90",
		_("Virtaul Store Sale1")+"::140",
		_("Walkin Conversion")+"::100",
		_("ABV")+"::100",
		_("ABQ")+"::100",
		_("Target Achievement")+"::100",
		 ]
		

	return columns



def get_conditions(filters):
	conditions = ""


	if filters.get("from_date"): conditions += " and date >= %(from_date)s"
	if filters.get("to_date"): conditions += " and date <= %(to_date)s"

	if filters.get("warehouse"): conditions += " and warehouse = %(warehouse)s"

	return conditions


def get_invoices(filters):
	conditions = get_conditions(filters)
	return frappe.db.sql("""
		select name, date, warehouse, brand_sales_target, total_pos_sale, 
		virtaul_store_sale,walkin_conversion,abv,abq,target_achievement
		from `tabDSR`
		where docstatus = 1  %s order by name desc """ %
		conditions, filters, as_dict=1)



	


