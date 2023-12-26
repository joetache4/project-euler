'''
Joe Walter

difficulty: 40%
run time:   0:00
answer:     9350130049860600

	***

110 Diophantine Reciprocals II

In the following equation x, y, and n are positive integers.
1/x + 1/y = 1/n

It can be verified that when n = 1260 there are 113 distinct solutions and this is the least value of n for which the total number of distinct solutions exceeds one hundred.

What is the least value of n for which the number of distinct solutions exceeds four million?

NOTE: This problem is a much more difficult version of Problem 108 and as it is well beyond the limitations of a brute force approach it requires a clever implementation.
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

print(solve(4*10**6))
