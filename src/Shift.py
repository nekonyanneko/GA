# -*- coding: utf-8 -*-
import Enum as enu

class Shift(object):
	"""
	This class define Shift.
	Shift instance has Employee objects by list.
		DEFINE VARIABLE:SHIFT_BOXES
			"The day of the week" and "_", "a or b"
			ex.mon_a
		DEFINE VARIABLE:NEED_PEOPLE
			Number of people required for that day
	"""
	SHIFT_BOXES = [
	'mon_a', 'mon_b',
	'tue_a', 'tue_b',
	'wed_a', 'wed_b',
	'thu_a', 'thu_b',
	'fri_a', 'fri_b',
	'sat_a', 'sat_b',
	'sun_a', 'sun_b'
	]
	NEED_PEOPLE = [
	3,2,
	3,2,
	3,2,
	3,2,
	3,2,
	3,2,
	3,2
	]

	def __init__(self, list):
		"""
		Input is lists of employee instance.
		"""
		if list == None:
			self.make_sample()
		else:
			self.list = list
		self.employees = []

	# ランダムなデータを生成
	def make_sample(self):
		"""
		Random 
		"""
		sample_list = []
		for num in range(enu.INDIVIDUAL_NUM):
			sample_list.append(random.randint(0, 1))
		self.list = tuple(sample_list)

	# タプルを1ユーザ単位に分割
	def slice(self):
		sliced = []
		start = 0
		for num in range(enu.EMPLOYEE_NUM):
			sliced.append(self.list[start:(start + enu.SHIFT_ALL_NUM)])
			start = start + enu.SHIFT_ALL_NUM
		return tuple(sliced)

	# ユーザ別にアサインコマ名を出力する
	def print_inspect(self):
		user_no = 0
		for line in self.slice():
			print "ユーザ%d" % user_no
			print line
			user_no = user_no + 1

			index = 0
			for e in line:
				if e == 1:
					print self.SHIFT_BOXES[index]
				index = index + 1

	# CSV形式でアサイン結果の出力をする
	def print_csv(self):
		for line in self.slice():
			print ','.join(map(str, line))

	# TSV形式でアサイン結果の出力をする
	def print_tsv(self):
		for line in self.slice():
			print "\t".join(map(str, line))

	# ユーザ番号を指定してコマ名を取得する
	def get_boxes_by_user(self, user_no):
		line = self.slice()[user_no]
		return self.line_to_box(line)

	# 1ユーザ分のタプルからコマ名を取得する
	def line_to_box(self, line):
		result = []
		index = 0
		for e in line:
			if e == 1:
				result.append(self.SHIFT_BOXES[index])
			index = index + 1
		return result

	# コマ番号を指定してアサインされているユーザ番号リストを取得する
	def get_user_nos_by_box_index(self, box_index):
		user_nos = []
		index = 0
		for line in self.slice():
			if line[box_index] == 1:
				user_nos.append(index)
			index += 1
		return user_nos

	# コマ名を指定してアサインされているユーザ番号リストを取得する
	def get_user_nos_by_box_name(self, box_name):
		box_index = self.SHIFT_BOXES.index(box_name)
		return self.get_user_nos_by_box_index(box_index)

	# 想定人数と実際の人数の差分を取得する
	def abs_people_between_need_and_actual(self):
		result = []
		index = 0
		for need in self.NEED_PEOPLE:
			actual = len(self.get_user_nos_by_box_index(index))
			result.append(abs(need - actual))
			index += 1
		return result

	# 応募していないコマにアサインされている件数を取得する
	def not_applicated_assign(self):
		count = 0
		for box_name in self.SHIFT_BOXES:
			user_nos = self.get_user_nos_by_box_name(box_name)
			for user_no in user_nos:
				e = self.employees[user_no]
				if not e.is_applicated(box_name):
					count += 1
		return count

	# アサインが応募コマ数の指定された%に満たないユーザを取得
	def few_work_user(self):
		result = []
		for user_no in range(enu.EMPLOYEE_NUM):
			e = self.employees[user_no]
			ratio = float(len(self.get_boxes_by_user(user_no))) / float(len(e.wills))
			if ratio < enu.PROBABIRITY:
				result.append(e)
		return result

	# 管理者が1人もいないコマ
	def no_manager_box(self):
		result = []
		for box_name in self.SHIFT_BOXES:
			manager_included = False
			user_nos = self.get_user_nos_by_box_name(box_name)
			for user_no in user_nos:
				e = self.employees[user_no]
				if e.manager:
					manager_included = True
			if not manager_included:
				result.append(box_name)
		return result

	# 1日1人3コマの日を返却
	def three_box_per_day(self):
		result = []
		for user_no in range(enu.EMPLOYEE_NUM):
			boxes = self.get_boxes_by_user(user_no)
			wdays = []
			for box in boxes:
				wdays.append(box.split('_')[0])
			wday_names = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
			for wday_name in wday_names:
				if wdays.count(wday_name) == enu.DAY_VARIATION_NUM:
					result.append(wday_name)
		return result

	# 必須出勤日数の取得
	def get_work_day_num(self):
		result = []
		work_day = []
                for line in self.slice():
                        work_day.append(sum(line))
		for user_no in range(enu.EMPLOYEE_NUM):
			result.append( work_day[user_no] / float(self.employees[user_no].days))
		return float(sum(result)) / enu.EMPLOYEE_NUM

