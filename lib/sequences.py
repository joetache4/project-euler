import numpy as np
from math import factorial, comb
from heapq import heappush, heappop
from lib.matrix import mpow, matrix

def fibonacci(init=(0,1)):
	a,b = init
	while True:
		yield a
		a,b = b,a+b

def nth_fibonacci(n, mod=float("inf")):
	if n == 0:
		return 0
	if n == 1:
		return 1
	mat = matrix([[1,1],[1,0]])
	return mpow(mat, n-1, mod)[0,0]

# including nth term
def fibonacci_sum(n, mod=float("inf")):
	return (nth_fibonacci(n+2, mod)-1) % mod

# less than, not including, stop
def _figurative(stop, f):
	n = 1
	while (v := f(n)) < stop:
		yield v
		n += 1

def triangular(stop=float("inf")):
	yield from _figurative(stop, lambda n: (n*n+n)>>1)

def square(stop=float("inf")):
	yield from _figurative(stop, lambda n: n*n)

def pentagonal(stop=float("inf")):
	yield from _figurative(stop, lambda n: (3*n*n-n)>>1)

def hexagonal(stop=float("inf")):
	yield from _figurative(stop, lambda n: 2*n*n-n)

def heptagonal(stop=float("inf")):
	yield from _figurative(stop, lambda n: (5*n*n-3*n)>>1)

def octagonal(stop=float("inf")):
	yield from _figurative(stop, lambda n: 3*n*n-2*n)

def pythag(primitive_only=True):
	'''
	Generate Pythagorean Triples in increasing size of hypotenuse.
	Optionally, yield primitive triples or all triples.
	Note that if (a,b,c) is yielded at some point, then (b,a,c) will NOT be.
	'''
	q = []
	visited = set()
	sides = lambda k,m,n: (k*(m*m - n*n), 2*k*m*n, k*(m*m + n*n))
	heappush(q, (5,3,4,1,2,1)) # c, a, b, k, m, n
	while True:
		c,a,b,k,m,n = heappop(q)
		yield (a,b,c)
		if not primitive_only:
			a,b,c = sides(k+1,m,n)
			if (a,b,c) not in visited:
				visited.add((a,b,c))
				heappush(q, (c,a,b,k+1,m,n))
		a,b,c = sides(k,m+1,n)
		if (a,b,c) not in visited:
			visited.add((a,b,c))
			heappush(q, (c,a,b,k,m+1,n))
		if n + 1 < m:
			a,b,c = sides(k,m,n+1)
			if (a,b,c) not in visited:
				visited.add((a,b,c))
				heappush(q, (c,a,b,k,m,n+1))

# Stirling Number: Number of ways to partition a set of size n into exactly k non-empty subsets
# Bell Number: Number of ways to partition a set of size n into any number of non-empty subsets
# Partition Function: Number of ways to partition a positive integer into positive summands, w/o regard to order

# https://jamesmccaffrey.wordpress.com/2020/07/30/computing-a-stirling-number-of-the-second-kind-from-scratch-using-python/
def stirling2(n, k):
	s = 0
	for i in range(0, k+1):
		a = (-1)**(k-i)
		b = comb(k, i)
		c = i**n
		s += a*b*c
	return s//factorial(k)
