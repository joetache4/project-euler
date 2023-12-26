'''
Joe Walter

difficulty: 5%
run time:   0:01
answer:     1412403576

	***

800 Problem 800

An integer of the form p^q*q^p with prime numbers p ≠ q is called a hybrid-integer.
For example, 800 = 2^5*5^2 is a hybrid-integer.

We define C(n) to be the number of hybrid-integers less than or equal to n.
You are given C(800) = 2 and C(800^800) = 10790

Find C(800800^800800)
'''

from math import log
from bisect import bisect
from lib.num import get_primes

primes = get_primes(20*10**6)

def C(a, b):
	ans = 0
	for i, p in enumerate(primes):
		j = bisect(primes, 0, key = lambda q: q*log(p) + p*log(q) - b*log(a)) - 1
		#assert j < len(primes)-1, "more primes are needed"
		if i >= j:
			break
		ans += j-i
	return ans

assert C(800, 1) == 2
assert C(800, 800) == 10790

print(C(800800, 800800))
