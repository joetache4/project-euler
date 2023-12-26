'''
Joe Walter

difficulty: 15%
run time:   0:03
answer:     148693670

	***

828 Numbers Challenge

It is a common recreational problem to make a target number using a selection of other numbers. In this problem you will be given six numbers and a target number.

For example, given the six numbers 2, 3, 4, 6, 7, 25, and a target of 211, one possible solution is: 211 = (3 + 6) * 25 - (4 * 7) / 2

This uses all six numbers. However, it is not necessary to do so. Another solution that does not use the 7 is: 211 = (25 - 2) * (6 + 3) + 4

Define the score of a solution to be the sum of the numbers used. In the above example problem, the two given solutions have scores 47 and 40 respectively. It turns out that this problem has no solutions with score less than 40.

When combining numbers, the following rules must be observed:

    Each available number may be used at most once.
    Only the four basic arithmetic operations are permitted: +, -, *, /.
	All intermediate values must be positive integers, so for example (3 / 2) is never permitted as a subexpression (even if the final answer is an integer).

The attached file number-challenges.txt contains 200 problems, one per line in the format:
211:2,3,4,6,7,25

where the number before the colon is the target and the remaining comma-separated numbers are those available to be used.

Numbering the problems 1, 2, ..., 200, we let s_n be the minimum score of the solution to the n-th problem. For example, s_1 = 40, as the first problem in the file is the example given above. Note that not all problems have a solution; in such cases we take s_n = 0.

Find sum(3**n*s_n for n from 1 to 200). Give your answer modulo 1005075251.
'''


from itertools import combinations
from functools import cache
from data.p828 import get_data

def partitions(nums):
	for n in range(1, 2**len(nums)-1):
		X = []
		Y = []
		for i in range(len(nums)):
			if n & 1<<i:
				X.append(nums[i])
			else:
				Y.append(nums[i])
		yield tuple(X), tuple(Y)

@cache
def possible_targets(nums):
	if len(nums) == 1:
		return set([nums[0]])
	else:
		s = set()
		for X, Y in partitions(nums):
			for x in possible_targets(X):
				for y in possible_targets(Y):
					s.add(x+y)
					s.add(x-y)
					s.add(y-x)
					s.add(x*y)
					try:
						if x > y:
							z = x/y
						else:
							z = y/x
						if z == int(z):
							s.add(z)
					except ZeroDivisionError:
						pass
		return s

ans = 0
n   = 1
for target, nums in get_data():
	best = 0
	for count in range(1, len(nums)+1):
		for selected in combinations(nums, count):
			if best != 0 and sum(selected) >= best:
				continue
			if target in possible_targets(selected):
				if best == 0:
					best = sum(selected)
				else:
					best = min(best, sum(selected))
	ans += best * 3**n
	n   += 1
ans %= 1005075251
print(ans)
