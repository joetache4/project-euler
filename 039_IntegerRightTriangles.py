'''
Joe Walter

difficulty: 5%
run time:   0:00
answer:     840

	***

039 Integer Right Triangles

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximized?
'''

from math import isqrt
from itertools import count

def farey(n):
	'''Use Farey sequences to generate coprime numbers.'''
	a, b, c, d = 0, 1, 1, n
	while c <= n:
		k = (n+b)//d
		a, b, c, d = c, d, (k*c-a), (k*d-b)
		if a == 1 and b == 1:
			break
		yield (a,b)

def seed_vals(p_max):
	'''Create inputs for Euclid's method from coprime numbers.'''
	# calculate the Farey order needed so that only a few triplets are generated with perimeter > p_max
	f_order = isqrt(p_max // 2) + 1
	# inputs must be coprime and have opposite parity
	for (n, m) in farey(f_order):
		if m%2 != n%2:
			yield (n, m)

def triplet(m, n):
	'''Use Euclid's method to generate primitive Pythagorean triplets.'''
	if m < n:
		m, n = n, m
	a = m*m - n*n
	b = 2*m*n
	c = m*m + n*n
	if b < a:
		a, b = b, a
	return (a, b, c)

def solve(p_max):
	num_solutions = {}
	for (n, m) in seed_vals(p_max):
		a, b, c = triplet(m, n)
		for k in count(1):
			p = k*(a+b+c)
			if p > p_max:
				break
			try:
				num_solutions[p] += 1
			except KeyError:
				num_solutions[p]  = 1
	return max((v,k) for k,v in num_solutions.items())[1]

print(solve(1000))
