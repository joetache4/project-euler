'''
Joe Walter

difficulty: 65%
run time:   0:09
answer:     142989277

	***

171 Finding Numbers For Which The Sum Of The Squares Of The Digits Is A Square

For a positive integer n, let f(n) be the sum of the squares of the digits (in base 10) of n, e.g.

f(3) = 3^2 = 9,
f(25) = 2^2 + 5^2 = 4 + 25 = 29,
f(442) = 4^2 + 4^2 + 2^2 = 16 + 16 + 4 = 36

Find the last nine digits of the sum of all n, 0 < n < 10^20, such that f(n) is a perfect square.
'''

from math import isqrt, prod, factorial as f
from collections import Counter

L      = 20
digits = [0]*L

def search(i=0, start=0, sds=0):
	if i == L:
		if isqrt(sds)**2 == sds:		
			D = Counter(digits)
			P = f(L)//prod(f(c) for c in D.values())
			# the number of permutations with digit d in some position is count(d)/L*P
			digit_sum = sum(d*c for d,c in D.items())*P//L
			# add across all L digit places
			perm_sum = digit_sum * 11111111111111111111
			return perm_sum
		else:
			return 0
	else:
		ans = 0
		for n in range(start, 10):
			digits[i] = n
			ans += search(i+1, n, sds+n*n)
		return ans

ans = search() % 10**9
print(ans)




'''
from math import prod, comb, factorial as f

# returns all partitions of int n with the following restrictions:
# 1. all parts are nonzero squares <= 9^2
# 2. there are 20 or fewer parts
def partitions(n, _arr=[]):
	if len(_arr) > 20:
		# TODO test if possible to have sum >= n by test-adding arr[-1] until length 20, raise Error if not possible
		return
	s = sum(_arr)
	if s == n:
		yield _arr
	elif s < n:
		try:
			start = int(_arr[-1]**0.5)
		except IndexError:
			start = 9
		for p in range(start, 0, -1):
			_arr.append(p**2)
			yield from partitions(n, _arr)
			del _arr[-1]

for p in partitions(900):
	print(p)
'''
