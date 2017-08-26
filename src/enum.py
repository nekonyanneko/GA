# -*- coding: utf-8 -*-
import Employee as emp
import evalShift as eva

"""
Define Employee
e0:朝だけ
e1:月・水・金
e2:週末だけ
e3:どこでもOK
e4:夜だけ
e5:平日のみ
e6:金土日
e7:昼のみ
e8:夜のみ
e9:木金土日
"""
e0 = emp.Employee(0, "山田", 40, False, ['mon_1', 'tue_1', 'wed_1', 'thu_1', 'fri_1', 'sat_1', 'sun_1'])
e1 = emp.Employee(1, "鈴木", 21, False, ['mon_1', 'mon_2', 'mon_3', 'wed_1', 'wed_2', 'wed_3', 'fri_1', 'fri_2', 'fri_3'])
e2 = emp.Employee(2, "佐藤", 18, False, ['sat_1', 'sat_2', 'sat_3', 'sun_1', 'sun_2', 'sun_3'])
e3 = emp.Employee(3, "田中", 35, True, ['mon_1', 'mon_2', 'mon_3', 'tue_1', 'tue_2', 'tue_3','wed_1', 'wed_2', 'wed_3','thu_1', 'thu_2', 'thu_3','fri_1', 'fri_2', 'fri_3','sat_1', 'sat_2', 'sat_3', 'sun_1', 'sun_2', 'sun_3'])
e4 = emp.Employee(4, "山口", 19, False, ['mon_3', 'tue_3', 'wed_3', 'thu_3', 'fri_3', 'sat_3', 'sun_3'])
e5 = emp.Employee(5, "加藤", 43, True, ['mon_1', 'mon_2', 'mon_3', 'tue_1', 'tue_2', 'tue_3','wed_1', 'wed_2', 'wed_3','thu_1', 'thu_2', 'thu_3','fri_1', 'fri_2', 'fri_3'])
e6 = emp.Employee(6, "川口", 25, False, ['fri_1', 'fri_2', 'fri_3', 'sat_1', 'sat_2', 'sat_3', 'sun_1', 'sun_2', 'sun_3'])
e7 = emp.Employee(7, "野口", 22, False, ['mon_2', 'tue_2', 'wed_2', 'thu_2', 'fri_2', 'sat_2', 'sun_2'])
e8 = emp.Employee(8, "棚橋", 18, False, ['mon_3', 'tue_3', 'wed_3', 'thu_3', 'fri_3', 'sat_3', 'sun_3'])
e9 = emp.Employee(9, "小山", 30, True, ['thu_1', 'thu_2', 'thu_3', 'fri_1', 'fri_2', 'fri_3', 'sat_1', 'sat_2', 'sat_3', 'sun_1', 'sun_2', 'sun_3'])

EMPLOYEES = [e0, e1, e2, e3, e4, e5, e6, e7, e8, e9]

"""
These enum are evaluation
"""
EVA_1 = 210.0
EVA_2 = 210.0
EVA_3 = 10.0
EVA_4 = 21.0
EVA_5 = 70.0

