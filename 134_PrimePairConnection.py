'''
Joe Walter

difficulty: 45%
run time:   0:01
answer:     18613426663617118

	***

134 Prime Pair Connection

Consider the consecutive primes p1 = 19 and p2 = 23. It can be verified that 1219 is the smallest number such that the last digits are formed by p1 whilst also being divisible by p2.

In fact, with the exception of p1 = 3 and p2 = 5, for every pair of consecutive primes, p2 > p1, there exist values of n for which the last digits are formed by p1 and n is divisible by p2. Let S be the smallest of these values of n.

Find ∑ S for every pair of consecutive primes with 5 ≤ p1 ≤ 1000000.
'''

from lib.num import get_primes

primes = get_primes(1000004) #1000003 is prime

ans = 0
for i in range(2, len(primes)-1):
	p1, p2 = primes[i], primes[i+1]
	offset = 10
	while offset < p1:
		offset *= 10
	k = (-p1 * pow(offset, -1, p2) % p2)
	ans += offset * k + p1

print(ans)
