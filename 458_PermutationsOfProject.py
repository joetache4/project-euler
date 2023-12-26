'''
Joe Walter

difficulty: 30%
run time:   0:00
answer:     423341841

	***

458 Permutations of Project

Consider the alphabet A made out of the letters of the word "project": A = {c,e,j,o,p,r,t}.
Let T(n) be the number of strings of length n consisting of letters from A that do not have a substring that is one of the 5040 permutations of "project".

T(7) = 7^7 - 7! = 818503.

Find T(10^12). Give the last 9 digits of your answer.

	***

By Euler's Theorem:
7^(10^12) = 7^(2500*phi(10^9)) = 1^2500 = 1 (mod 10^9)
'''

import numpy as np
from lib.matrix import mpow

def T(n, mod=None):
	A = np.matrix([
	[0,7,0,0,0,0,0,0],
	[0,1,6,0,0,0,0,0],
	[0,1,1,5,0,0,0,0],
	[0,1,1,1,4,0,0,0],
	[0,1,1,1,1,3,0,0],
	[0,1,1,1,1,1,2,0],
	[0,1,1,1,1,1,1,1],
	[0,0,0,0,0,0,0,7],
	], np.uint64)
	p = pow(7, n, mod)
	f = mpow(A, n, mod)[0, 7]
	if mod is None:
		val = p-f
	else:
		val = (p-f) % mod
	return int(val)

assert pow(7, 10**12, 10**9) == 1
assert T(7) == 818503

print(T(10**12, 10**9))
