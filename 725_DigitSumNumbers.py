'''
Joe Walter

difficulty: 10%
run time:   0:00
answer:     4598797036650685

	***

725 Digit Sum Numbers

A number where one digit is the sum of the other digits is called a digit sum number or DS-number for short. For example, 352, 3003 and 32812 are DS-numbers.

We define S(n) to be the sum of all DS-numbers of n digits or less.

You are given S(3) = 63270 and S(7) = 85499991450.

Find S(2020). Give your answer modulo 10**16.
'''

from math import comb, factorial, prod
from collections import Counter
from lib.num import partitions

def S(n, m=16):
	ans = 0
	for D in range(1, 10):							# for each summed digit
		for parts in partitions(D):					# for each way to get this sum
			if len(parts)+1 > n:
				continue
			parts.append(D)
			for d in set(parts):					# for each nonzero digit
				others = parts.copy()
				others.remove(d)
				# perms = number of ways to permute the other digits into n-1 places
				perms   = comb(n-1, len(others))
				perms  *= factorial(len(others))
				perms //= prod(factorial(c) for c in Counter(others).values())
				for i in range(min(n,m)):			# for each place to put this digit
					ans += d * 10**i * perms
	ans %= 10**m
	return ans

assert S(2) == 495
assert S(3) == 63270
assert S(7) == 85499991450

print(S(2020))
