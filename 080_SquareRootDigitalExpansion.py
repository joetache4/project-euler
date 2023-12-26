'''
Joe Walter

difficulty: 20%
run time:   0:00
answer:     40886

	***

080 Square Root Digital Expansion

It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal expansion of such square roots is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.

	***

Solution Method

Babylonian Method
https://en.wikipedia.org/wiki/Methods_of_computing_square_roots
The number of correct digits of the approximation roughly doubles with each iteration.

Also, this problem can be trivially solved with the sqrt() method in the Decimal class.
'''

from math import isqrt
from decimal import getcontext, Decimal as D

getcontext().prec = 110

def nonsquare(m):
	n = 2
	while n < m:
		if isqrt(n)**2 != n:
			yield n
		n += 1

def sqrt(n):
	a = D(n)/2
	for i in range(10):
		a = (a + n/a)/2
	return a

def val(n):
	return sum(int(d) for d in str(n).replace(".","")[:100])

ans = sum(val(sqrt(n)) for n in nonsquare(101))
print(ans)
