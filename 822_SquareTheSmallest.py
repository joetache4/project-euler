'''
Joe Walter

difficulty: 15%
run time:   0:02
answer:     950591530

	***

822 Square The Smallest

A list initially contains the numbers 2, 3, ..., n.

At each round, the smallest number in the list is replaced by its square. If there is more than one such number, then only one of them is replaced.

For example, below are the first three rounds for n = 5:

[2, 3, 4, 5] -> [4, 3, 4, 5] -> [4, 9, 4, 5] -> [16, 9, 4, 5].

Let S(n, m) be the sum of all numbers in the list after m rounds.

For example, S(5, 3) = 16 + 9 + 4 + 5 = 34. Also S(10, 100) = 845339386 mod 1234567891.

Find S(10^4, 10^16). Give your answer modulo 1234567891.
'''

from math import log, floor

mod, tot = 1234567891, 1234567890

# find integer x>=0 that makes a^2^x larger than b^2^y
def exp_larger(a,b,y):
	# 2^x = log_a b^2^y = 2^y/log_b a
	# x = y - log_2 log_b a
	return max(0, floor(y - log(log(a,b),2) + 1))

# find exponents for all but the last list item such that each number has implied size larger than (len(pows)-1) ^ 2 ^ (pows[-1]-1)
def update(pows, sum_only=False, lo=0, hi=-1):
	hi = len(pows)-1
	b,y = len(pows)+1, pows[-1]-1
	if sum_only:
		def _update(lo, hi):
			val = 0
			if hi - lo < 0:
				pass
			elif hi - lo == 0:
				val += exp_larger(lo+2,b,y)
			elif hi - lo == 1:
				val += exp_larger(lo+2,b,y)
				val += exp_larger(hi+2,b,y)
			else:
				mid = (lo+hi)//2
				lo_val = exp_larger(lo+2,b,y)
				hi_val = exp_larger(hi+2,b,y)
				md_val = exp_larger(mid+2,b,y)
				val += (lo_val+hi_val+md_val)
				if lo_val == md_val:
					val += lo_val * len(range(lo+1, mid, 1))
				else:
					val += _update(lo+1, mid-1)
				if hi_val == md_val:
					val += hi_val * len(range(mid+1, hi, 1))
				else:
					val += _update(mid+1, hi-1)
			return val
	else:
		def _update(lo, hi):
			if hi - lo < 0:
				pass
			elif hi - lo == 0:
				pows[lo] = exp_larger(lo+2,b,y)
			elif hi - lo == 1:
				pows[lo] = exp_larger(lo+2,b,y)
				pows[hi] = exp_larger(hi+2,b,y)
			else:
				md = (lo+hi)//2
				lo_val = exp_larger(lo+2,b,y)
				hi_val = exp_larger(hi+2,b,y)
				md_val = exp_larger(md+2,b,y)
				pows[lo] = lo_val
				pows[hi] = hi_val
				pows[md] = md_val
				if lo_val == md_val:
					pows[lo+1:md] = [lo_val] * len(range(lo+1, md))
				else:
					_update(lo+1, md-1)
				if hi_val == md_val:
					pows[md+1:hi] = [hi_val] * len(range(md+1, hi))
				else:
					_update(md+1, hi-1)

	return _update(0, len(pows)-1)

def S(n, m):
	ans  = 0
	pows = [0]*(n-1) # index+2 = base, value = exponent, implied size is base^2^exponent

	# repeatedly find the exponent for the largest base number in the list, then remove it from the list
	# the correct exponent will be the highest number that does NOT imply too many "squaring iterations"
	# finally, set all the remaining numbers' exponents to their minimum required value
	while len(pows):
		pow_sum = sum(pows)
		# find some upper bound on largest base number's exponent
		d = 1
		lo, hi = pows[-1], pows[-1]+d
		while True:
			pows[-1] = hi
			diff = update(pows, sum_only=True) - pow_sum
			if diff > m:
				break
			else:
				d *= 2
				lo, hi = hi, hi+d
		# binary search to find exact value for the exponent
		while hi-lo > 1:
			mid = (lo+hi)//2
			pows[-1] = mid
			diff = update(pows, sum_only=True) - pow_sum
			if diff < m:
				lo = mid
			elif diff > m:
				hi = mid
			else:
				lo = mid
				break

		pows[-1] = lo
		update(pows)
		diff = sum(pows) - pow_sum

		#print((len(pows)+1, pows[-1]))
		m -= diff
		ans += pow(len(pows)+1, pow(2,pows[-1],tot), mod)
		del pows[-1]

	ans %= mod
	return ans

assert S(5, 3) == 34
assert S(10, 100) == 845339386

print(S(10**4, 10**16))




'''
from functools import cmp_to_key

def cmp_larger(a,b):
	a,x = a
	b,y = b
	return x - (y - log(log(a,b),2))

key_larger = cmp_to_key(cmp_larger)

# sign of return value indicates whether a^2^x is larger than b^2^y
def larger(a,x,b,y):
	return (y - log(log(a,b),2)) - x

def update(pows):
	b,y = len(pows)+1, pows[-1]
	y -= 1
	for i in range(len(pows)-1):
		pows[i] = exp_larger(i+2, b, y)
'''
