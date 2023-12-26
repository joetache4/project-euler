'''
Joe Walter

difficulty: 5%
run time:   0:00
answer:     45228

	***

032 Pandigital Products

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

ans: 45228
'''

from math import prod
from lib.num import FactorRange
from lib.array import subsets

def pandigital(a, b, c):
	digits = set(f"{a}{b}{c}")
	return '0' not in digits and len(digits) == 9

F = FactorRange(11111)
ans = 0
for n, f in F.factors():
	for subset in subsets(f, 1):
		a = subset
		b = f.copy()
		for t in a:
			b.remove(t)
		a = prod(a)
		b = prod(b)
		if pandigital(a, b, n):
			ans += n
			break

print(ans)
