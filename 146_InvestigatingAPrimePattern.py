'''
Joe Walter

difficulty: 50%
run time:   0:18
answer:     676333270

	***

146 Investigating A Prime Pattern

The smallest positive integer n for which the numbers n^2+1, n^2+3, n^2+7, n^2+9, n^2+13, and n^2+27 are consecutive primes is 10. The sum of all such integers n below one-million is 1242490.

What is the sum of all such integers n below 150 million?

	***

Observations

n is a multiple of 2 and 5, and hence 10.
n is not a multiple of 3, 7, or 13.

(n^2+3)%7  ≠ 0 -> n%7 ≠ 2,5
(n^2+7)%7  ≠ 0 -> n%7 ≠ 0
(n^2+13)%7 ≠ 0 -> n%7 ≠ 1,6

-> n%7 = 3,4
'''

from math import prod
from sympy import isprime

PK = [1,3,7,9,13,27]
CK = [5,11,15,17,19,21,23,25]

cycles = []
primes = [3,7,11,13,17,19] # congruence classes
for p in primes:
	cycle = [True]*p
	for k in PK:
		for n in range(p):
			if (n*n+k)%p == 0:
				cycle[n] = False
	if not all(cycle):
		cycles.append(cycle)

L = prod(len(c) for c in cycles)
supercycle = [True]*L
for c in cycles:
	for i, v in enumerate(c):
		if not v:
			supercycle[i::len(c)] = (False for _ in range(i, L, len(c)))

ans = 0
for n in range(10, 150*10**6, 10):
	if supercycle[n%L]:
		if all(not isprime(n*n+k) for k in CK) and all(isprime(n*n+k) for k in PK):
			#print(n)
			ans += n
print(ans)
