# -*- coding: utf-8 -*-
import Employee as emp
import EvalShift as eva

"""
Define Employee
"""
e0  = emp.Employee(1, "abe", 20, False, [
	'mon_a', 'tue_a', 'wed_a', 'thu_a', 'fri_a', 'sat_a', 'sun_a'])
e1  = emp.Employee(1, "chiba", 35, True, [
	'mon_a', 'tue_b', 'wed_a', 'thu_b', 'fri_a', 'sat_b', 'sun_a'])
e2  = emp.Employee(2, "takahashi", 25, False, [
	'mon_a', 'mon_b', 'tue_a', 'tue_b', 'wed_a', 'wed_b', 'thu_a', 'thu_b', 'fri_a', 'fri_b', 'sat_a', 'sat_b', 'sun_a', 'sun_b'])
e3  = emp.Employee(3, "suzuki", 32, True, [
	'mon_a',  'tue_a', 'tue_b', 'wed_a', 'wed_b', 'thu_b', 'fri_a', 'fri_b', 'sat_a', 'sat_b', 'sun_a', 'sun_b'])
e4  = emp.Employee(4, "hayashi", 32, True, [
	'mon_a', 'mon_b', 'tue_a', 'tue_b', 'wed_b', 'thu_a', 'thu_b', 'fri_a', 'fri_b', 'sat_b', 'sun_a', 'sun_b'])
e5  = emp.Employee(5, "ota", 22, False, [
	'mon_a', 'mon_b', 'tue_a', 'tue_b', 'wed_a', 'wed_b', 'thu_a', 'thu_b', 'fri_a', 'fri_b'])
e6  = emp.Employee(6, "kato", 21, False, [
	'mon_a', 'mon_b', 'tue_a', 'tue_b', 'wed_a', 'wed_b', 'thu_a', 'sat_a', 'sat_b', 'sun_a', 'sun_b'])
e7  = emp.Employee(7, "pika", 23, False, [
	'mon_a', 'mon_b', 'tue_a', 'thu_a', 'thu_b', 'fri_a', 'fri_b', 'sat_a', 'sat_b', 'sun_a', 'sun_b'])
e8  = emp.Employee(8, "komori", 25, False, [
	'mon_a', 'mon_b', 'tue_a', 'wed_b', 'thu_a', 'thu_b', 'fri_a', 'sat_b', 'sun_a', 'sun_b'])
e9  = emp.Employee(9, "kobayashi", 30, True, [
	'tue_b', 'wed_a', 'wed_b', 'thu_a', 'thu_b', 'fri_a', 'fri_b', 'sat_a', 'sat_b', 'sun_a', 'sun_b'])
e10 = emp.Employee(10, "tanaka", 29, False, [
	'mon_a', 'mon_b', 'tue_a', 'tue_b', 'wed_a', 'wed_b', 'thu_a', 'thu_b', 'fri_a', 'fri_b', 'sat_a', 'sat_b', 'sun_a', 'sun_b'])

EMPLOYEES = [e0, e1, e2, e3, e4, e5, e6, e7, e8, e9, e10]
EMPLOYEE_NUM = len(EMPLOYEES)
DAY_VARIATION_NUM = 2
WEEK_OF_DAY = 7
SHIFT_ALL_NUM = WEEK_OF_DAY * DAY_VARIATION_NUM # 7 days * 2(a or b)
PROBABIRITY = 0.5

"""
These enum are evaluation
"""
EVA_1 = float(EMPLOYEE_NUM * WEEK_OF_DAY)
EVA_2 = float(EMPLOYEE_NUM * WEEK_OF_DAY)
EVA_3 = float(EMPLOYEE_NUM)
EVA_4 = float(WEEK_OF_DAY * DAY_VARIATION_NUM)
EVA_5 = float(EMPLOYEE_NUM * WEEK_OF_DAY)

