# -*- coding: utf-8 -*-
# Copyright (c) 2018, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt


class DSR(Document):   
	def validate_calculation(self):

		total_pos_sale = self.pos_cash_sale+self.pos_card_sale+self.pos_other_mode_sale
		
		self.total_pos_sale = total_pos_sale  

		cash_deposit_amount = self.pos_cash_sale + self.advance_cash
		self.cash_deposit_amount = cash_deposit_amount

		card_realisation_amount = self.pos_card_sale+ self.advance_card
		self.card_realisation_amount = card_realisation_amount
		
		walkin_conversion = flt(self.bill)/flt(self.walkin)*100 
 		self.walkin_conversion = walkin_conversion
		
		target_achievement = flt(self.total_pos_sale)/flt(self.sales_target)*100
 		self.target_achievement = target_achievement
		
		abv = flt(self.total_pos_sale)/flt(self.bill)
 		self.abv = abv
		
		abq = flt(self.qty)/flt(self.bill)
		self.abq = abq
		



	def validate_duplicate_record(self):
			res = frappe.db.sql("""select name from `tabDSR` where warehouse = %s and date = %s
				and name != %s and docstatus = 1""",
				(self.warehouse, self.date, self.name))
			if res:
				frappe.throw(_("Entry for the date for {0} is already existed").format(self.warehouse))

				



	def validate(self):

		self.validate_calculation()
		self.validate_duplicate_record()


