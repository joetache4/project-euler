'''
Joe Walter

difficulty: 25%
run time:   0:07
answer:     17427258

	***

187 Semiprimes

A composite is a number containing at least two prime factors. For example, 15 = 3 × 5; 9 = 3 × 3; 12 = 2 × 2 × 3.

There are ten composites below thirty containing precisely two, not necessarily distinct, prime factors: 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

How many composite integers, n < 10^8, have precisely two, not necessarily distinct, prime factors?
'''

from lib.num import get_primes

N = 10**8

primes = get_primes(N)

ans = 0
i = 0
j = len(primes) - 1
while i < j:
	p = primes[i]
	p2 = primes[j]
	while p*p2 >= N:
		j -= 1
		p2 = primes[j]
	ans += (j - i + 1)
	i += 1

print(ans)
