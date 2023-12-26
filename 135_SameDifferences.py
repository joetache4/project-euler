'''
Joe Walter

difficulty: 45%
run time:   0:10
answer:     4989

	***

135 Same Difference

Given the positive integers, x, y, and z, are consecutive terms of an arithmetic progression, the least value of the positive integer, n, for which the equation, x2 − y2 − z2 = n, has exactly two solutions is n = 27:

34^2 − 27^2 − 20^2 = 12^2 − 9^2 − 6^2 = 27

It turns out that n = 1155 is the least value which has exactly ten solutions.

How many values of n less than one million have exactly ten distinct solutions?
'''

from collections import Counter
from lib.num import FactorRange, divisors_from_factors

def count_sols(n, divs):
	s = 0
	for div in divs:
		a, b = -div, -n//div
		if (a+b)%4 != 0:
			continue
		d = -(a+b)//4
		x = d-a
		if 0 < 2*d < x < 5*d:
			s += 1
	return s

assert count_sols(1155, divisors_from_factors([3,5,7,11])) == 10
assert count_sols(27, divisors_from_factors([3,3,3])) == 2

N = 10**6
C = 10

fac = FactorRange(N)
fac = [fac.factor(n) for n in range(N)]
div = [divisors_from_factors(f) for f in fac]
cnt = [count_sols(n,d) for n,d in enumerate(div)]
cnt = sum(1 for c in cnt if c == C)

print(cnt)
