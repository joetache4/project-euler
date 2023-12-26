'''
Joe Walter

difficulty: 20%
run time:   0:01
answer:     1097343

	***

087 Orime Power Triples

The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28. In fact, there are exactly four numbers below fifty that can be expressed in such a way:

28 = 22 + 23 + 24
33 = 32 + 23 + 24
49 = 52 + 23 + 24
47 = 22 + 33 + 24

How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?
'''

from math import isqrt
from lib.num import get_primes

N = 50*10**6

primes = get_primes(isqrt(N)+1)

nums = set()
for a in primes:
	n = a**2
	if n >= N: break
	for b in primes:
		n = a**2 + b**3
		if n >= N: break
		for c in primes:
			n = a**2 + b**3 + c**4
			if n >= N: break
			nums.add(n)

print(len(nums))
