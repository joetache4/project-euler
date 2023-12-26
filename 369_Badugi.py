'''
Joe Walter

difficulty: 60%
run time:   0:02
answer:     862400558448

	***

369 Badugi

In a standard 52 card deck of playing cards, a set of 4 cards is a Badugi if it contains 4 cards with no pairs and no two cards of the same suit.

Let f(n) be the number of ways to choose n cards with a 4 card subset that is a Badugi. For example, there are 2598960 ways to choose five cards from a standard 52 card deck, of which 514800 contain a 4 card subset that is a Badugi, so f(5) = 514800.

Find ∑f(n) for 4 ≤ n ≤ 13.

	***

Solution Method

This problem is equivalent to finding the number of ways to place n stones on a 13x4 grid such that they all lie on any 3 or fewer straight lines. There is a correspondence between such configurations and card hands that CANNOT contain a Badugi subset. Count these configurations and subtract from the number of all hands, and that gives the number of hands with at least one Badugi subset.

Notes:
If a configuration is valid, then all permutations of rows and columns yield valid configurations, as well.
'''

from math import comb as C, factorial, prod
from itertools import combinations
from functools import reduce
from collections import Counter

def count_perms(nums):
	return factorial(len(nums)) // prod(factorial(v) for v in Counter(nums).values())

bitsum = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4] # OEIS A000120

def on_3_lines(rows):
	if len(rows) <= 3:
		return True
	for comb in combinations(rows, len(rows)-2):
		if bitsum[reduce(lambda x, y: x|y, comb)] <= 1:
			return True
	for comb in combinations(rows, len(rows)-1):
		if bitsum[reduce(lambda x, y: x|y, comb)] <= 2:
			return True
	return bitsum[reduce(lambda x, y: x|y, rows)] <= 3

def search(rows=[], minrow=1, count=None):
	if count is None:
		count = Counter() # number of stones -> number of 3-line configurations
	total = sum(bitsum[r] for r in rows)
	if total > 13:
		return count
	if on_3_lines(rows):
		count[total] += C(13, len(rows))*count_perms(rows) # number of ways to insert empty rows into this solution * number of ways to rearrange the rows
	else:
		return count
	for r in range(minrow, 16): # 15 = 1111, filled row
		count += search(rows+[r], r)
	return count

def ans():
	count = search()
	count = sum(C(52, n)-count[n] for n in range(4, 14))
	return count

print(ans())


# slightly faster by keeping in mind which line configurations don't need to be checked
'''
# HHH
def config3(rows):
	return len(rows) <= 3

# HHV
def config2(rows):
	for comb in combinations(rows, len(rows)-2):
		if bitsum[reduce(lambda x, y: x|y, comb)] <= 1:
			return True
	return False

# HVV
def config1(rows):
	for comb in combinations(rows, len(rows)-1):
		if bitsum[reduce(lambda x, y: x|y, comb)] <= 2:
			return True
	return False

# VVV
def config0(rows):
	return bitsum[reduce(lambda x, y: x|y, rows)] <= 3

configs = [config0, config1, config2, config3]

def count_perms(nums):
	return factorial(len(nums)) // prod(factorial(v) for v in Counter(nums).values())

def search(rows=[], max_horizontal=3, minrow=1, count=None):
	if count is None:
		count = Counter() # number of stones -> number of 3-line configurations
	total = sum(bitsum[r] for r in rows)
	if total > 13:
		return count
	while max_horizontal >= 0:
		if configs[max_horizontal](rows):
			count[total] += C(13, len(rows))*count_perms(rows)
			break
		max_horizontal -= 1
	if max_horizontal < 0:
		return count
	for r in range(minrow, 16): # 15 = 1111, filled row
		count += search(rows+[r], max_horizontal, r)
	return count
'''
