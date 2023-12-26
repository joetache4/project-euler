'''
Joe Walter

difficulty: 25%
run time:   0:00
answer:     34029210557338

	***

203 Squarefree Binomial Coefficients

The binomial coefficients

can be arranged in triangular form, Pascal's triangle, like this:
	1
	1		1
	1		2		1
	1		3		3		1
	1		4		6		4		1
	1		5		10		10		5		1
	1		6		15		20		15		6		1
	1		7		21		35		35		21		7		1
	.........

It can be seen that the first eight rows of Pascal's triangle contain twelve distinct numbers: 1, 2, 3, 4, 5, 6, 7, 10, 15, 20, 21 and 35.

A positive integer n is called squarefree if no square of a prime divides n. Of the twelve distinct numbers in the first eight rows of Pascal's triangle, all except 4 and 20 are squarefree. The sum of the distinct squarefree numbers in the first eight rows is 105.

Find the sum of the distinct squarefree numbers in the first 51 rows of Pascal's triangle.
'''

from math import prod
from collections import Counter
from lib.num import FactorRange

N = 51

def is_squarefree(n, k, F = FactorRange(N).factor_all()):
	'''Returns C(n,k) if C(n,k) is squarefree, otherwise 0'''
	f = []
	for i in range(n, n-k, -1):
		f += F[i]
	for i in range(k, 1, -1):
		for j in F[i]:
			f.remove(j)
	if all(p < 2 for p in Counter(f).values()):
		return prod(f)
	else:
		return 0

def ans(N):
	a = {1}
	for n in range(2, N):
		for k in range(1, n//2+1):
			a.add(is_squarefree(n, k))
	return sum(a)

assert ans(8) == 105

print(ans(N))
