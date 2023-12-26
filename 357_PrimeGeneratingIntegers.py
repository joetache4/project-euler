'''
Joe Walter

difficulty: 10%
run time:   0:37
answer:     1739023853137

	***

357 Prime Generating Integers

Consider the divisors of 30: 1, 2, 3, 5, 6, 10, 15, 30.
It can be seen that for every divisor d of 30, d + 30/d is prime.

Find the sum of all positive integers n not exceeding 100000000
such that for every divisor d of n, d + n/d is prime.

	***

n=1 is a prime generating integer
if n>1, then n must be even so that all d + n/d are odd
n must be one less than a prime so that 1 + n/1 is prime
n must be squarefree
'''

from lib.num import get_primes, is_prime, divisors

primes = get_primes(10**8//2)

candidates = [1] + [2*(p-2) for p in primes[1:]] # len(candidates) == 3001134
candidates = [n for n in candidates if is_prime(n+1)] # len(candidates) == 458463

ans = 0
for n in candidates:
	if all(is_prime(d + n//d) for d in divisors(n, primes)):
		# 39627 iterations
		ans += n

print(ans)
