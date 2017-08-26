# -*- coding: utf-8 -*-
import Employee as emp
import EvalShift as eva

"""
Define Employee
"""
e0  = emp.Employee(1, "abe", 3, False, [
	'mon_a', 'tue_a', 'wed_a', 'thu_a', 'fri_a', 'sat_a', 'sun_a'])
e1  = emp.Employee(1, "chiba", 4, True, [
	'mon_a', 'tue_b', 'wed_a', 'thu_b', 'fri_a', 'sat_b', 'sun_a'])
e2  = emp.Employee(2, "takahashi", 3, False, [
	'mon_a', 'mon_b', 'tue_a', 'tue_b', 'wed_a', 'wed_b', 'thu_a', 'thu_b', 'fri_a', 'fri_b', 'sat_a', 'sat_b', 'sun_a', 'sun_b'])
e3  = emp.Employee(3, "suzuki", 4, True, [
	'mon_a',  'tue_a', 'tue_b', 'wed_a', 'wed_b', 'thu_b', 'fri_a', 'fri_b', 'sat_a', 'sat_b', 'sun_a', 'sun_b'])
e4  = emp.Employee(4, "hayashi", 4, True, [
	'mon_a', 'mon_b', 'tue_a', 'tue_b', 'wed_b', 'thu_a', 'thu_b', 'fri_a', 'fri_b', 'sat_b', 'sun_a', 'sun_b'])
e5  = emp.Employee(5, "ota", 3, False, [
	'mon_a', 'mon_b', 'tue_a', 'tue_b', 'wed_a', 'wed_b', 'thu_a', 'thu_b', 'fri_a', 'fri_b'])
e6  = emp.Employee(6, "kato", 3, False, [
	'mon_a', 'mon_b', 'tue_a', 'tue_b', 'wed_a', 'wed_b', 'thu_a', 'sat_a', 'sat_b', 'sun_a', 'sun_b'])
e7  = emp.Employee(7, "pika", 3, False, [
	'mon_a', 'mon_b', 'tue_a', 'thu_a', 'thu_b', 'fri_a', 'fri_b', 'sat_a', 'sat_b', 'sun_a', 'sun_b'])
e8  = emp.Employee(8, "komori", 3, False, [
	'mon_a', 'mon_b', 'tue_a', 'wed_b', 'thu_a', 'thu_b', 'fri_a', 'sat_b', 'sun_a', 'sun_b'])
e9  = emp.Employee(9, "kobayashi", 4, True, [
	'tue_b', 'wed_a', 'wed_b', 'thu_a', 'thu_b', 'fri_a', 'fri_b', 'sat_a', 'sat_b', 'sun_a', 'sun_b'])
e10 = emp.Employee(10, "tanaka", 3, False, [
	'mon_a', 'mon_b', 'tue_a', 'tue_b', 'wed_a', 'wed_b', 'thu_a', 'thu_b', 'fri_a', 'fri_b', 'sat_a', 'sat_b', 'sun_a', 'sun_b'])

EMPLOYEES = [e0, e1, e2, e3, e4, e5, e6, e7, e8, e9, e10]
EMPLOYEE_NUM = len(EMPLOYEES)
DAY_VARIATION_NUM = 2
WEEK_OF_DAY = 7
SHIFT_ALL_NUM = WEEK_OF_DAY * DAY_VARIATION_NUM # 7 days * 2(a or b)
INDIVIDUAL_NUM = WEEK_OF_DAY * DAY_VARIATION_NUM * EMPLOYEE_NUM
PROBABIRITY = 0.8 # 休暇希望日の要求達成率

CROSS_PROBABIRTY = 0.6 # 交差確率
MULTATION_PROBABIRTY = 0.5 # 突然変異確率
LOOP_NUM = 10000 # 進化計算の回数

"""
These enum are evaluation
"""
EVA_1 = float(EMPLOYEE_NUM * WEEK_OF_DAY)
EVA_2 = float(EMPLOYEE_NUM * WEEK_OF_DAY)
EVA_3 = float(EMPLOYEE_NUM)
EVA_4 = float(WEEK_OF_DAY * DAY_VARIATION_NUM)
EVA_5 = float(EMPLOYEE_NUM * WEEK_OF_DAY)
EVA_6 = None

"""
These enum are weights evaluation
"""
EVA_WEIGHT_1 = -10.0
EVA_WEIGHT_2 = -100.0
EVA_WEIGHT_3 = -1.0
EVA_WEIGHT_4 = -100.0
EVA_WEIGHT_5 = -10.0
EVA_WEIGHT_6 = -150.0

