'''
Joe Walter

difficulty: 65%
run time:   0:10
answer:     1096883702440585

	***

266 Pseudo Square Root

The divisors of 12 are: 1,2,3,4,6 and 12.
The largest divisor of 12 that does not exceed the square root of 12 is 3.
We shall call the largest divisor of an integer n that does not exceed the square root of n the pseudo square root (PSR) of n.
It can be seen that PSR(3102)=47.

Let p be the product of the primes below 190.
Find PSR(p) mod 10^16.

	***

Solution Method

Meet-in-the-middle
https://en.wikipedia.org/wiki/Knapsack_problem#Meet-in-the-middle
'''

from math import prod
from bisect import bisect
from lib.num import get_primes, factor
from lib.array import subsets

primes = get_primes(190) # sorted low to high
n      = prod(primes)
target = n**0.5

A      = primes[:len(primes)//2]
B      = primes[len(primes)//2:]
A      = sorted(prod(s) for s in subsets(A, 0)) # prod([]) = 1

psr = 0
for b in subsets(B, 0):
	b = prod(b)
	if b > target:
		continue
	a_target = target/b     # a_target >= 1
	i = bisect(A, a_target) # so, i >= 1, as A[0] = 1
	psr = max(psr, b*A[i-1])
ans = psr % (10**16)

print(f"  n = {n}")
print(f"PSR = {psr}")
print(f"fac = {factor(psr, primes)}")
print(f"dif = {n - psr**2}")
print(f"ans = {ans}")






'''
# pseudo-polynomial time approximation

import math
from decimal import Decimal, getcontext
from lib.num import get_primes, factor

getcontext().prec = 80

primes = [Decimal(p) for p in get_primes(190 - 1)]
target = Decimal(prod(primes))

# https://en.wikipedia.org/wiki/Subset_sum_problem
# also, take log() of both sides to convert from multiplication to addition
t = target.sqrt().ln()
x = [p.ln() for p in primes]
c = Decimal(0.001) # error term
n = len(x)
S = {0}

for i in range(n):
	T = {x[i] + y for y in S}
	U = T.union(S)
	U = sorted(U)
	y = U[0]
	S = {y}
	for z in U:
		# Trim the list by eliminating numbers close to one another
		# and throw out elements greater than s.
		if y + c*t/n < z and z <= t:
			y = z
			S.add(z)


sum = sorted(S)[-1]
psr = round(sum.exp())
factors = factor(psr)
ans = psr % (10**16)

print(f"target   = {target}")
print(f"best sum = {sum}")
print(f"PSR	  = {psr}")
print(f"ans	  = {ans}")
print(f"diff	 = {target - psr**2}")
print(f"PSR factorization: {factors}")
print(f"PSR | target:	  {target % psr == 0}")


# return S contains a number between (1 − c)s and s
'''
