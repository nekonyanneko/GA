# -*- coding: utf-8 -*-
import Shift as shi
import Enum as enu

def evalShift(individual):
	"""
	This method is grobal method.
	This method is evaluation.

	If you need new evaluation method, you must define it as follows. 

	RETURN:
		evaluation values
	"""
	shift           = shi.Shift(individual) # Get indiviaual of shift
	shift.employees = enu.EMPLOYEES # Get employees list

	# 想定人数とアサイン人数の差
	people_count_sub_sum = sum(shift.abs_people_between_need_and_actual()) / enu.EVA_1

	# 応募していない時間帯へのアサイン数
	not_applicated_count = shift.not_applicated_assign() / enu.EVA_2

	# アサイン数が応募数の半分以下の従業員数
	few_work_user        = len(shift.few_work_user()) / enu.EVA_3

	# 管理者が1人もいないコマ数
	no_manager_box       = len(shift.no_manager_box()) / enu.EVA_4

	# a,bの全部にアサインされている
	three_box_per_day    = len(shift.three_box_per_day()) / enu.EVA_5
	
	return (
		not_applicated_count,
		people_count_sub_sum,
		few_work_user,
		no_manager_box,
		three_box_per_day
		)

