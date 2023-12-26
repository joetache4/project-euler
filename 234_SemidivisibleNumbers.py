'''
Joe Walter

difficulty: 50%
run time:   0:00
answer:     1259187438574927161

	***

234 Semidivisible Numbers

For an integer n ≥ 4, we define the lower prime square root of n, denoted by lps(n), as the largest prime ≤ √n and the upper prime square root of n, ups(n), as the smallest prime ≥ √n.

So, for example, lps(4) = 2 = ups(4), lps(1000) = 31, ups(1000) = 37.
Let us call an integer n ≥ 4 semidivisible, if one of lps(n) and ups(n) divides n, but not both.

The sum of the semidivisible numbers not exceeding 15 is 30, the numbers are 8, 10 and 12.
15 is not semidivisible because it is a multiple of both lps(15) = 3 and ups(15) = 5.
As a further example, the sum of the 92 semidivisible numbers up to 1000 is 34825.

What is the sum of all semidivisible numbers not exceeding 999966663333 ?
'''

from math import isqrt, ceil
from lib.num import get_primes235 as get_primes

N = 999966663333

def next_highest_prime(primes):
	n = primes[-1]
	while True:
		n += 1
		if all(n%p != 0 for p in primes):
			return n

def sum_multiples_between(a, b, m):
	a -= a%m
	k  = ceil((b-a)/m-1)
	s  = k*a + m*k*(k+1)//2
	return s

def solve(N):
	ans    = 0
	primes = get_primes(isqrt(N)+1)
	primes.append(next_highest_prime(primes))
	for i in range(len(primes)-1):
		m1   = primes[i]
		m2   = primes[i+1]
		a    = m1**2
		b    = min(N+1, m2**2)
		ans += sum_multiples_between(a, b, m1)
		ans += sum_multiples_between(a, b, m2)
		ans -= 2*sum_multiples_between(a, b, m1*m2)
	return ans

assert solve(15)   == 30
assert solve(1000) == 34825

print(solve(N))
