'''
Joe Walter

difficulty: 40%
run time:   0:01
answer:     7526965179680

	***

231 The Prime Factorisation of Binomial Coefficients

The binomial coefficient (10,3) = 120.
120 = 2^3 * 3 * 5 = 2 * 2 * 2 * 3 * 5, and
2 + 2 + 2 + 3 + 5 = 14.

So the sum of the terms in the prime factorisation of (10,3) is 14.

Find the sum of the terms in the prime factorisation of (20000000,15000000).
'''

from lib.num import get_primes

# given p, sums prime power factors p^k for all numbers up to n
def sum_pk(n, p):
	count = 0
	x = n//p
	while x > 0:
		count += x
		x //= p
	return count*p

# sums all prime power factors for all numbers up to n
def sum_all_pk(n, primes):
	s = 0
	for p in primes:
		if p > n:
			break
		s += sum_pk(n, p)
	return s

def solve(a, b):
	primes = get_primes(a+1)
	return sum_all_pk(a, primes) - sum_all_pk(b, primes) - sum_all_pk(a-b, primes)

assert solve(10, 3) == 14

print(solve(20*10**6, 15*10**6))
