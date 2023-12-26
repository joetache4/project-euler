'''
Joe Walter

difficulty: 25%
run time:   0:00
answer:     21417

	***

124 Ordered Radicals

The radical of n, rad(n), is the product of the distinct prime factors of n. For example, 504 = 2^3 × 3^2 × 7, so rad(504) = 2 × 3 × 7 = 42.

If we calculate rad(n) for 1 ≤ n ≤ 10, then sort them on rad(n), and sorting on n if the radical values are equal, we get:

	[table]

Let E(k) be the kth element in the sorted n column; for example, E(4) = 8 and E(6) = 9.

If rad(n) is sorted for 1 ≤ n ≤ 100000, find E(10000).
'''

from math import prod
from lib.num import FactorRange

def E(M, n):
	a = FactorRange(M+1)
	a = [(prod(set(a.factor(i))), i) for i in range(1, M+1)]
	a = sorted(a)
	return a[n-1][1]

assert E(10, 4) == 8
assert E(10, 6) == 9

print(E(100000, 10000))
