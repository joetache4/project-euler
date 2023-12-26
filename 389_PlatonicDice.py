'''
Joe Walter

difficulty: 30%
run time:   0:32
answer:     2406376.3623

	***

389 Platonic Dice

An unbiased single 4-sided die is thrown and its value, T, is noted.
T unbiased  6-sided dice are thrown and their scores are added together. The sum, C, is noted.
C unbiased  8-sided dice are thrown and their scores are added together. The sum, O, is noted.
O unbiased 12-sided dice are thrown and their scores are added together. The sum, D, is noted.
D unbiased 20-sided dice are thrown and their scores are added together. The sum, I, is noted.
Find the variance of I, and give your answer rounded to 4 decimal places.
'''

from functools import cache
from itertools import combinations
from collections import Counter

@cache
def count_possible_sums(sides, dice_count):
	if dice_count == 1:
		return Counter({s:1 for s in range(1, sides+1)})
	else:
		a = dice_count // 2
		b = dice_count - a
		a = count_possible_sums(sides, a)
		b = count_possible_sums(sides, b)
		c = Counter()
		for k1, v1 in a.items():
			for k2, v2 in b.items():
				c[k1+k2] += v1*v2
		return c

P    = Counter() # Probability of values for D
T    = count_possible_sums(4, 1)
Tsum = sum(T.values())
for t,tc in T.items():
	Pt   = tc/Tsum
	C    = count_possible_sums(6, t)
	Csum = sum(C.values())
	for c,cc in C.items():
		Pc   = cc/Csum
		O    = count_possible_sums(8, c)
		Osum = sum(O.values())
		for o,oc in O.items():
			Po   = oc/Osum
			D    = count_possible_sums(12, o)
			Dsum = sum(D.values())
			for d,dc in D.items():
				Pd    = dc/Dsum
				P[d] += Pt*Pc*Po*Pd

# Law of Total Variance
# https://en.wikipedia.org/wiki/Law_of_total_variance

# variance of the sum of d 20-sided dice
def Var(d):
	return d*399/12

# expected sum of d 20-sided dice
def E(d):
	return d*10.5

v = sum(Var(d)*P[d] for d in P.keys())           + \
	sum(E(d)**2*(1-P[d])*P[d] for d in P.keys()) + \
	-2*sum(E(d1)*P[d1]*E(d2)*P[d2] for d1,d2 in combinations(P.keys(),2))

print(f"{v:.4f}")
