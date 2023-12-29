'''
Joe Walter

difficulty: 70%
run time:   0:15
answer:     785478606870985

	***

268 At Least Four Distinct Prime Factors Less Than 100

It can be verified that there are 23 positive integers less than 1000 that are divisible by at least four distinct primes less than 100.

Find how many positive integers less than 10**16 are divisible by at least four distinct primes less than 100.

	***

Inclusion-Exclusion Process

This process is simple when starting with k=1, but harder when starting with k>1.
However with k=1, you need to work on the 12650 products of subsets of size 4 and this would be much too slow.
With k=4, the factor n in front of the count is no longer +-1.

It is calculated as follows.
n_4 = 1
n_4*comb(5,4) + n_5 = 1
  (Because #s with 5 primes have been added n_4*comb(5,4) times in the prev step)
n_4*comb(6,4) + n_5*comb(6,5) + n_6 = 1
...etc. Solving these equations for n results in +- triangular numbers.
'''

from math import prod, comb
from itertools import combinations

primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
count  = 0

for k in range(4, len(primes)+1):
	n = pow(-1,k)*comb(k-1,3)
	for subset in combinations(primes, k):
		p = prod(subset)
		count += n*len(range(p,10**16,p))
print(count)
