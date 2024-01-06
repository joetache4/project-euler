'''
Joe Walter

difficulty: 15%
run time:   0:00
answer:     45009328011709400

	***

845 Prime Digit Sum

Let D(n) be the n-th positive integer that has the sum of its digits a prime.

For example, D(61) = 157 and D(10^8) = 403539364.

Find D(10^16).
'''

from math import prod, factorial as f
from collections import Counter
from functools import cache
from lib.num import is_prime

@cache
def count(target_len, current_len=0, dsum=0):
	'''Count numbers up to a given length with a prime digit sum.'''
	if current_len == target_len:
		return 1 if is_prime(dsum) else 0
	else:
		return sum(count(target_len, current_len+1, dsum+d) for d in range(10))

def D(n):
	length = 1
	while count(length) < n:
		length += 1
	digits = [0]*length
	for i in range(length):
		for _ in range(9):
			c = count(length-1-i, dsum=sum(digits))
			if c < n:
				digits[i] += 1
				n -= c
			else:
				break
	val = int("".join(str(d) for d in digits))
	return val

assert D(61) == 157
assert D(10**8) == 403539364

print(D(10**16))
