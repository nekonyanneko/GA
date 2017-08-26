# -*- coding: utf-8 -*-

class Employee(object):
	"""This class means employees"""
	def __init__(self, employee_id, name, age, manager, wills):
		"""
		VARIABLE:employee_id
			Employee's Number
		VARIABLE:name
			Employee's name
		VARIABLE:age
			Employee's age
		VARIABLE:manager
			Is Employee manager?
			Input variable "True" or "False"
		VARIABLE:wills
			Employee preferred shift
			Input variable list
			The format of the list elements is as follows
			-> DEFINE VARIABLE of Shift class

		RETURN:noting
		"""
		self.employee_id = employee_id
		self.name        = name
		self.age         = age
		self.manager     = manager
		self.wills       = wills
	def is_applicated(self, box_name):
		"""
		"""
		return (box_name in self.wills)

