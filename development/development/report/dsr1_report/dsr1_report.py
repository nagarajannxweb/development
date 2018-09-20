# Copyright (c) 2013, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import flt,cint, getdate, now
from frappe import msgprint, _

def execute(filters):
	#return _execute(filters)
#def _execute(filters):
	if not filters: filters = frappe._dict({})

	data_list = get_datas(filters)
	columns = get_columns()
	
	if not data_list:
		msgprint(_("No record found"))
	data  = []

	for d in data_list:
		
		row = [
			
			d.name, d.date,d.warehouse
		
			]
		
		
		row +=    [d.sales_target,d.total_pos_sale,d.virtual_store_sale,d.walkin_conversion,d.target_achievement,d.abv,d.abq] 

		data.append(row)
	
	return columns, data


def get_conditions(filters):
	conditions = ""


	if filters.get("from_date"): conditions += " and date >= %(from_date)s"
	if filters.get("to_date"): conditions += " and date <= %(to_date)s"

	if filters.get("warehouse"): conditions += " and warehouse = %(warehouse)s"

	return conditions


def get_datas(filters):
	conditions = get_conditions(filters)
	return frappe.db.sql("""
		select name, date, warehouse, sales_target, total_pos_sale, 
		virtual_store_sale,walkin_conversion,abv,abq,target_achievement
		from `tabDSR`
		where docstatus = 1  %s  """ %
		conditions, filters, as_dict=1)

def get_columns():
	#return columns#

	columns = [
		_("DSR") + ":Link/DSR:100",
		_("Date")+"::150",
		_("Warehouse")+":Link/Warehouse:100",
		_("Brand Sales Target")+ ":Float:100",
		_("Total POS Sale")+ ":Float:90",
		_("Virtual Store Sale")+ ":Float:140",
		_("Walkin Conversion")+ ":Float:100",
		_("Target Achievement")+ ":Float:100",
		_("ABV")+ ":Float:100",
		_("ABQ")+ ":Float:100",
		
		 ]
	return columns
