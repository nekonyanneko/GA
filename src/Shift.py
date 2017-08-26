# -*- coding: utf-8 -*-

class Shift(object):
	"""
	This class define Shift.
	Shift instance has Employee objects by list.
		DEFINE VARIABLE:SHIFT_BOXES
			"The day of the week" and "_", "number"
			ex.mon_1
		DEFINE VARIABLE:NEED_PEOPLE
			Number of people required for that day
	"""
	SHIFT_BOXES = [
	'mon_1', 'mon_2', 'mon_3',
	'tue_1', 'tue_2', 'tue_3',
	'wed_1', 'wed_2', 'wed_3',
	'thu_1', 'thu_2', 'thu_3',
	'fri_1', 'fri_2', 'fri_3',
	'sat_1', 'sat_2', 'sat_3',
	'sun_1', 'sun_2', 'sun_3']
	NEED_PEOPLE = [
	2,3,3,
	2,3,3,
	2,3,3,
	1,2,2,
	2,3,3,
	2,4,4,
	2,4,4]

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
		for num in range(210):
			sample_list.append(random.randint(0, 1))
		self.list = tuple(sample_list)

	# タプルを1ユーザ単位に分割
	def slice(self):
		sliced = []
		start = 0
		for num in range(10):
			sliced.append(self.list[start:(start + 21)])
			start = start + 21
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

	# アサインが応募コマ数の50%に満たないユーザを取得
	def few_work_user(self):
		result = []
		for user_no in range(10):
			e = self.employees[user_no]
			ratio = float(len(self.get_boxes_by_user(user_no))) / float(len(e.wills))
			if ratio < 0.5:
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
		for user_no in range(10):
			boxes = self.get_boxes_by_user(user_no)
			wdays = []
			for box in boxes:
				wdays.append(box.split('_')[0])
			wday_names = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
			for wday_name in wday_names:
				if wdays.count(wday_name) == 3:
					result.append(wday_name)
		return result

