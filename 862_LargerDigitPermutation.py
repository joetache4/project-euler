'''
Joe Walter

difficulty:
run time:   0:00
answer:     6111397420935766740

	***

862 Larger Digit Permutation

For a positive integer n define T(n) to be the number of strictly larger integers which can be formed by permuting the digits of n.

Leading zeros are not allowed and so for n=2302 the total list of permutations would be:

	2023, 2032, 2203, 2230, 2302, 2320, 3022, 3202, 3220

giving T(2302) = 4.

Further define S(k) to be the sum of T(n) for all k-digit numbers n. You are given S(3)=1701.

Find S(12).
'''

from lib.num import partitions
from itertools import permutations
from math import comb, factorial as f, prod

def S(k):
	x = 0
	perms = set()
	for p in partitions(k):
		if len(p) > 10:
			continue
		for perm in permutations(p):
			# perm represents a digit multiplicity "signature"
			if perm in perms:
				continue
			else:
				perms.add(perm)
			# digit assignments w/o 0
			a = comb(9,len(perm))
			# valid permutations of digits for each assignment
			b = f(k)//prod(f(p) for p in perm)
			# digit assignments w/ 0
			c = comb(9,len(perm)-1)
			# valid permutations of digits for each assignment
			d = b - b*perm[0]//k
			x += a*(b*(b-1)//2) + c*(d*(d-1)//2)
	return x

assert S(3) == 1701

print(S(12))
