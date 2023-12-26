'''
Joe Walter

difficulty: 30%
run time:   0:00
answer:     180180

	***

108 Diophantine Reciprocals I

In the following equation x, y, and n are positive integers.

1/x + 1/y = 1/n

For n = 4 there are exactly three distinct solutions:

1/5 + 1/20 = 1/4
1/6 + 1/12 = 1/4
1/8 + 1/8 = 1/4

What is the least value of n for which the number of distinct solutions exceeds one-thousand?

NOTE: This problem is an easier version of Problem 110; it is strongly advised that you solve this one first.

	***

Observations

See https://mathematicalolympiads.files.wordpress.com/2012/08/an_introduction_to_diophantine_equations__a_problem_based_approach.pdf

The equation 1/x + 1/y = 1/n  is equivalent to (x-n)(y-n)=n^2. Each divisor d of n^2 suggests a solution: x-n = d and y-n = n^2/d (and then solve for x,y). So, the number of solution pairs (x,y) equals the number of divisors to n^2.

Since half of these solutions are just flipped versions of the other half (x↔y), you need to double the number of solutions you're looking for (>2000 instead of >1000). Note: There is exactly one solution where x=y.
'''

from math import prod, log
from lib.num import get_primes

def num_sol(pows):
	d = prod(2*p+1 for p in pows)	# count divisors to n^2
	return (d+1)>>1					# count unique solutions

def prime_pow(pows, primes = get_primes(100)):
	return prod(p**k for p,k in zip(primes, pows))

def min_n(M, pows, best, _start=0):
	'''For len(pows) prime factors, find the minimum n with >M solutions.'''
	pp = prime_pow(pows)
	if pp >= best:
		return best
	if num_sol(pows) > M:
		return pp
	else:
		for i in range(_start, len(pows)):
			if i == 0 or pows[i-1] > pows[i]:
				pows[i] += 1
				b    = min_n(M, pows, best, i)
				best = min(best, b)
				pows[i] -= 1
		return best

def solve(M):
	maxP = int(log(M)/log(3)+2) # maximum number of primes needed, see num_sol()
	best = float("inf")
	for pcount in range(maxP, 0, -1):
		pows = [1]*pcount
		best = min_n(M, pows, best)
		#print((k, best))
	return best

print(solve(1000))
