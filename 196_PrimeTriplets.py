'''
Joe Walter

difficulty: 65%
run time:   0:18
answer:     322303240771079935

	***

196 Prime Triplets

Build a triangle from all positive integers in the following way:

 1
 2  3
 4  5  6
 7  8  9 10
11 12 13 14 15
16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31 32 33 34 35 36
37 38 39 40 41 42 43 44 45
46 47 48 49 50 51 52 53 54 55
56 57 58 59 60 61 62 63 64 65 66
. . .

Each positive integer has up to eight neighbours in the triangle.

A set of three primes is called a prime triplet if one of the three primes has the other two as neighbours in the triangle.

For example, in the second row, the prime numbers 2 and 3 are elements of some prime triplet.

If row 8 is considered, it contains two primes which are elements of some prime triplet, i.e. 29 and 31.
If row 9 is considered, it contains only one prime which is an element of some prime triplet: 37.

Define S(n) as the sum of the primes in row n which are elements of any prime triplet.
Then S(8)=60 and S(9)=37.

You are given that S(10000)=950007619.

Find S(5678027) + S(7208785).
'''

from collections import Counter
from lib.num import get_primes235 as get_primes

primes = get_primes(6*10**6) # max_prime**2 must be >

def sieve_range(n, m, primes):
	is_prime = [True] * (m-n)
	for p in primes:
		if p*p >= m:
			break
		for i in range((-n%p)%p, m-n, p):
			is_prime[i] = False
	return {i+n for i,p in enumerate(is_prime) if p}

def sieve_row(row, primes):
	return sieve_range(first_in_row(row), first_in_row(row+1), primes)

def first_in_row(row):
	return 1 + row*(row-1)//2

def upper_odds(row, n):
	# assumes n is odd
	if row%2 == 0:
		#Y
		if n == first_in_row(row):
			return [n-row+2]
		elif first_in_row(row+1)-n <= 2:
			return [n-row]
		else:
			return [n-row, n-row+2]
	else:
		#inverted-Y
		if n == first_in_row(row+1)-1:
			return []
		else:
			return [n-(row-1)]

def lower_odds(row, n):
	# assumes n is odd
	if row%2 == 0:
		return [n+row]
	else:
		if n == first_in_row(row):
			return [n+row+1]
		else:
			return [n+row-1, n+row+1]

def upper_primes(row, n, range_primes):
	return (p for p in upper_odds(row, n) if p in range_primes)

def lower_primes(row, n, range_primes):
	return (p for p in lower_odds(row, n) if p in range_primes)

def S(row):
	if row == 1: return 0
	if row in [2,3]: return 5 # special cases involving prime 2
	P1 = sieve_row(row-2, primes)
	P2 = sieve_row(row-1, primes)
	P3 = sieve_row(row+0, primes)
	P4 = sieve_row(row+1, primes)
	P5 = sieve_row(row+2, primes)
	C = Counter()
	for p in P2:
		upper = list(upper_primes(row-1,p,P1))
		lower = list(lower_primes(row-1,p,P3))
		n = len(upper) + len(lower)
		for q in lower:
			C[q] += n
	for p in P4:
		upper = list(upper_primes(row+1,p,P3))
		lower = list(lower_primes(row+1,p,P5))
		n = len(upper) + len(lower)
		for q in upper:
			C[q] += n
	return sum(p for p in P3 if C[p] >= 2)

assert S(1) == 0
assert S(2) == 5
assert S(3) == 5
assert S(4) == 7
assert S(5) == 24
assert S(6) == 36
assert S(7) == 23
assert S(8) == 60
assert S(9) == 37
assert S(10) == 47
assert S(10000) == 950007619

print(S(5678027)+S(7208785))
