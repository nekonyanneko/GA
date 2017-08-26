# -*- coding: utf-8 -*-

class Employee(object):
	"""This class means employees"""
	def __init__(
		self, employee_id, name, days, manager, wills
		):
		"""
		INPUT:
			Same as variables.
		
		VARIABLE:employee_id
			Employee's Number
		VARIABLE:name
			Employee's name
		VARIABLE:days
			Employee's work days
		VARIABLE:manager
			Is Employee manager?
			Input variable "True" or "False"
		VARIABLE:wills
			Employee preferred shift
			Input variable list
			The format of the list elements is as follows
			-> DEFINE VARIABLE of Shift class

		RETURN:
			noting
		"""
		self.employee_id = employee_id
		self.name        = name
		self.days        = days
		self.manager     = manager
		self.wills       = wills
	def is_applicated(self, box_name):
		"""
		This method is answer that employee preferred shift satisfy.
		Input:
			Whether an box_name element exists in Employee's valiable of wills.

		RETURN:
			Employee's variable of wills
		"""
		return (box_name in self.wills)

