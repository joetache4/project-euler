'''
Joe Walter

difficulty: 65%
run time:   0:13
answer:     301

	***

152 Sum Inverse Squares

There are several ways to write the number 1/2 as a sum of inverse squares using distinct integers.

For instance, the numbers {2,3,4,5,7,12,15,20,28,35} can be used:

In fact, only using integers between 2 and 45 inclusive, there are exactly three ways to do it, the remaining two being: {2,3,4,6,7,9,10,20,28,35,36,45} and {2,3,4,6,7,9,12,15,28,30,35,36,45}.

How many ways are there to write the number 1/2 as a sum of inverse squares using distinct integers between 2 and 80 inclusive?

	***

Observations

sum(1/n**2 for n in range(3,81)) < 1/2  ->  2 must be a part of any solution set.
So, the problem becomes finding solution sets over {3...80} with a target sum of 1/4.

Use modular arithmetic to determine which numbers cannot be a part of any solution set.

Let {2, n_1, ... n_k} be a solution set.

Thats is, 1/4 = 1/n_1^2 + ... 1/n_k^2.

Primes > 80/2 cannot be in any solution set for the following reason:

Let P = prod(3...80). Let p be a prime > 40. Multiply the equation above by P and mod by p^2:

P/4 = P/n_1^2 + ... P/n_k^2  mod p^2
0   = P/p^2                  mod p^2  (because every number zero'd-out had a factor of p^2)

However P/p^2 has no factors of p, so P/p^2 mod p^2 != 0. So, p cannot be in any solution set.

A similar argument can be made for other numbers and their multiples <= 80.

Example.

See if 23, 46, or 69 is a part of any solution set. If so, then at least one of the following is nonzero (because P/4 mod (23*46*69)^2 = 0):

(P/(23^2)                          )  mod  (23*46*69)^2
(             P/(46^2)             )  mod  (23*46*69)^2
(                          P/(69^2))  mod  (23*46*69)^2
(P/(23^2)   + P/(46^2)             )  mod  (23*46*69)^2
(P/(23^2)                + P/(69^2))  mod  (23*46*69)^2
(             P/(46^2)   + P/(69^2))  mod  (23*46*69)^2
(P/(23^2)   + P/(46^2)   + P/(69^2))  mod  (23*46*69)^2

If these are all nonzero, then the 23, 46, and 69 cannot be any solution set and can be ignored.

This test is performed for all primes > 2.
'''

from math import lcm, prod
from functools import reduce
from lib.num import get_primes
from lib.array import binary_search, subsets

def solve(N):
	# find infeasible terms, those that cannot be a part of any solution set
	P = prod(n**2 for n in range(3, N+1))
	not_feasible = set()
	for n in get_primes(N+1)[1:]: # skip 2
		multiples = list(range(n, N+1, n))
		mod = prod(multiples)**2
		feasible = False
		for s in subsets(multiples, 1):
			subsum = sum(P//(n**2) for n in s)
			if subsum % mod == 0:
				feasible = True
				break
		if not feasible:
			for m in multiples:
				not_feasible.add(m)
	feasible = set(range(3, N+1)) - not_feasible

	#print(f'{not_feasible=}')
	#print(f'{feasible=}')

	# multiply by LHS and RHS by LCM, avoid imprecision in floats
	feasible = sorted(n**2 for n in feasible)
	P        = reduce(lcm, feasible)
	LHS      = P//4
	feasible = [P//n for n in feasible]

	# meet-in-the-middle algorithm
	A = feasible[:len(feasible)//2]
	B = feasible[len(feasible)//2:]
	Bsums = sorted(sum(s) for s in subsets(B, 1))
	count = sum(1 for subsum in Bsums if subsum == LHS)
	for Asub in subsets(A, 1):
		Asum = sum(Asub)
		if Asum == LHS:
			count += 1
		elif Asum < LHS:
			Bsum = LHS - Asum
			i = binary_search(Bsums, Bsum) # returns right-most match in Bsums
			if i:
				count += 1
				# some entries in B have the same sum
				for j in range(i-1, -1, -1):
					if Bsums[j] == Bsum:
						count += 1
					else:
						break

	return count

assert solve(45) == 3

print(solve(80))
