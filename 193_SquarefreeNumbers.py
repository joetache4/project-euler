'''
Joe Walter

difficulty: 55%
run time:   0:35
answer:     684465067343069

	***

193 Squarefree Numbers

A positive integer n is called squarefree, if no square of a prime divides n, thus 1, 2, 3, 5, 6, 7, 10, 11 are squarefree, but not 4, 8, 9, 12.

How many squarefree numbers are there below 2^50?
'''

from math import isqrt, prod
from lib.num import get_primes235 as get_primes

def subsets(nums, max_prod, arr = [], istart = 0):
	for i in range(istart, len(nums)):
		arr.append(nums[i])
		if prod(arr) >= max_prod:
			arr.pop()
			break
		yield arr
		yield from subsets(nums, max_prod, arr, i+1)
		arr.pop()

def solve(n):
	primes2 = [p*p for p in get_primes(isqrt(n)+1)]
	count = n
	for s in subsets(primes2, n):
		count += (-1)**len(s) * (n // prod(s))
	return count

print(solve(2**50))

'''
from math import pi

def approx(n):
	return int(n*6/pi**2)

def brute(n):
	primes2 = [p*p for p in get_primes(n)]
	return sum(1 for m in range(1,n) if all(m%p2!=0 for p2 in primes2))

M = 2**50

print(f"approx: {approx(M)}")
if M < 10**5:
	print(f"brute : {brute(M)}")
'''
