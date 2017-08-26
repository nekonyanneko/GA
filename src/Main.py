# -*- coding: utf-8 -*-
import random
from scoop import futures

from deap import base
from deap import creator
from deap import tools
from deap import cma

import Enum as enu
import Employee as emp
import Shift as shi
import EvalShift as eva

"""
deap setting
"""
creator.create("FitnessPeopleCount", base.Fitness, weights=(-10.0, -100.0, -1.0, -100.0, -10.0))
creator.create("Individual", list, fitness=creator.FitnessPeopleCount)
toolbox = base.Toolbox()
toolbox.register("map", futures.map)
toolbox.register("attr_bool", random.randint, 0, 1)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, 210)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("evaluate", eva.evalShift)
# 交叉関数を定義(二点交叉)
toolbox.register("mate", tools.cxTwoPoint)
# 変異関数を定義(ビット反転、変異隔離が5%)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
# 選択関数を定義(トーナメント選択、tournsizeはトーナメントの数)
toolbox.register("select", tools.selTournament, tournsize=3)

if __name__ == '__main__':
	# 初期集団を生成する
	pop = toolbox.population(n=300)
	CXPB, MUTPB, NGEN = 0.6, 0.5, 500 # 交差確率、突然変異確率、進化計算のループ回数

	print("進化開始")

	# 初期集団の個体を評価する
	print ("初期集団の個体数:%i" % len(pop))
	fitnesses = list(map(toolbox.evaluate, pop))
	for ind, fit in zip(pop, fitnesses):  # zipは複数変数の同時ループ
		# 適合性をセットする
		ind.fitness.values = fit

	print("  %i の個体を評価" % len(pop))

	 # 進化計算開始
	for g in range(NGEN):
		print("-- %i 世代 --" % g)

		# 選択
		# 次世代の個体群を選択
		offspring = toolbox.select(pop, len(pop))
		# 個体群のクローンを生成
		offspring = list(map(toolbox.clone, offspring))

		# 選択した個体群に交差と突然変異を適応する

		# 交叉
		# 偶数番目と奇数番目の個体を取り出して交差
		for child1, child2 in zip(offspring[::2], offspring[1::2]):
			if random.random() < CXPB:
				toolbox.mate(child1, child2)
				# 交叉された個体の適合度を削除する
				del child1.fitness.values
				del child2.fitness.values

		# 変異
		for mutant in offspring:
			if random.random() < MUTPB:
				toolbox.mutate(mutant)
				del mutant.fitness.values

		# 適合度が計算されていない個体を集めて適合度を計算
		invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
		fitnesses = map(toolbox.evaluate, invalid_ind)
		for ind, fit in zip(invalid_ind, fitnesses):
			ind.fitness.values = fit

		print("  %i の個体を評価" % len(invalid_ind))

		# 次世代群をoffspringにする
		pop[:] = offspring

		# すべての個体の適合度を配列にする
		index = 1
		for v in ind.fitness.values:
		  fits = [v for ind in pop]

		  length = len(pop)
		  mean = sum(fits) / length
		  sum2 = sum(x*x for x in fits)
		  std = abs(sum2 / length - mean**2)**0.5

		  print("* パラメータ%d") % index
		  print("  Min %s" % min(fits))
		  print("  Max %s" % max(fits))
		  print("  Avg %s" % mean)
		  print("  Std %s" % std)
		  index += 1

	print("-- 進化終了 --")

	best_ind = tools.selBest(pop, 1)[0]
	print("最も優れていた個体: %s, %s" % (best_ind, best_ind.fitness.values))
	shift = shi.Shift(best_ind)

	print("-- 出力 --")
	shift.print_csv()
	#shift.print_tsv()

