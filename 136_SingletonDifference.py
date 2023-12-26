'''
Joe Walter

difficulty: 50%
run time:   0:03
answer:     2544559

	***

136 Singleton Difference

The positive integers, x, y, and z, are consecutive terms of an arithmetic progression. Given that n is a positive integer, the equation, x^2 − y^2 − z^2 = n, has exactly one solution when n = 20:

13^2 − 10^2 − 7^2 = 20

In fact there are twenty-five values of n below one hundred for which the equation has a unique solution.

How many values of n less than fifty million have exactly one solution?

	***

Observations

(x+y)^2 - x^2 - (x-y)^2 = n, so 4xy - x^2 = n
x is a divisor of n
y = (n+x^2)/(4x) is an int

*** If n has  >1 solution, then sn has  >1 solution, where s is a square.
*** If n has >=1 solution, then sn has >=1 solution, where s is a square.
		Each sqrt(s)x is a solution to sn

*** n has 0 solutions iff. n=3 (mod 4) or n=4 (mod 8) or n=0 (mod 16).

n prime -> n has 0 or 1 solutions

n odd prime -> 4n has exactly 1 solution

n odd prime -> (4^k)n for k>2 has more than 1 solution

n odd composite -> 4n has >1 solutions

n has more than 1 odd divisor and n has more than 0 solutions -> n has more than solution

*** n has exactly 1 solution iff. n=(4^k)p where k in {0,1,2} and p is odd prime or n=4,16

As n increases, it is more likely the case that: n has 1 solution -> n is prime.
Alternatively, large composite numbers are unlikely to have exactly 1 solution.
'''

from lib.num import get_primes

def solve(N):
	primes = get_primes(N)
	del primes[0]
	ans = 0
	for p in primes:
		if p%4 == 3:
			ans += 1
		if 16*p < N:
			ans += 2
		elif 4*p < N:
			ans += 1
	ans += 2 # for n=4,16
	return ans

assert solve(100) == 25

print(solve(50*10**6))


# shows patterns
'''
from math import isqrt
from lib.num import get_primes, divisors, factor

N = 50*10**6

primes = get_primes(isqrt(N)+1)
for n in range(1, N):
	div = divisors(n, primes)
	num_sol = 0
	for x in div:
		q, r = divmod(n+x*x, 4*x)
		if r == 0:
			if q >= x:
				continue
			num_sol += 1
	print(f'count({n}) = {num_sol}')
	#if num_sol == 1:
	#	print(factor(n, primes))
#'''


# slightly faster, much less memory used
'''
from math import isqrt
from itertools import cycle
from lib.num import get_primes, divisors, factor

N = 50*10**6
T = True
F = False

primes = get_primes(isqrt(N)+1)
gt1 = [None] * N # n with 'greater than one' solutions
ans = 0
for n, gt0 in zip(range(1, N), cycle([F,F,T,T,F,F,T,F,F,F,T,T,F,F,T,T])): # zeros come in a pattern
	if gt0 and not gt1[n]:
		num_sol = 0
		for d in divisors(n, primes):
			q, r = divmod(n+d*d, 4*d)
			if q < d and r == 0:
				num_sol += 1
				if num_sol > 1:
					# all sn have >=1 solution where s is a square
					k = 2
					m = n*k*k
					while m < N:
						gt1[m] = True
						k += 1
						m = n*k*k
					break
		if num_sol == 1:
			ans += 1

print(ans)
#'''


# Original solution - slow and uses a ton of memory
'''
N = 50*10**6

def list_divisors(n):
	div = [[1] for x in range(n+1)]
	div[0] = []
	for d in range(2, n+1):
		for m in range(d, n+1, d):
			div[m].append(d)
	return div

ans = 0
for n,div in enumerate(list_divisors(N)):
	num_sol = 0
	for x in div:
		q, r = divmod(n+x*x, 4*x)
		if r == 0:
			if q >= x:
				continue
			num_sol += 1
			if num_sol > 1:
				break
	if num_sol == 1:
		ans += 1

print(ans)
'''
