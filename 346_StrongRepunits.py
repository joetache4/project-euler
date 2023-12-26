'''
Joe Walter

difficulty: 15%
run time:   0:01
answer:     336108797689259276

	***

346 Strong Repunits

The number 7 is special, because 7 is 111 written in base 2, and 11 written in base 6
(i.e. 7_10 = 11_6 = 111_2). In other words, 7 is a repunit in at least two bases b > 1.

We shall call a positive integer with this property a strong repunit. It can be verified that there are 8 strong repunits below 50: {1,7,13,15,21,31,40,43}.
Furthermore, the sum of all strong repunits below 1000 equals 15864.

Find the sum of all strong repunits below 10^12.

	***

Observations

Any number n > 1 can be written as 11 in base n-1. So, look for numbers that can be written as 11...1 (at least 3 1's) in some base b.
'''

from itertools import count

def solve(N):
	repunits = set([1])
	for b in count(2):
		n = 1 + b + b*b
		p = 3
		if n >= N:
			break
		while n < N:
			repunits.add(n)
			n += b**p
			p += 1
	return sum(repunits)

assert solve(50) == sum([1,7,13,15,21,31,40,43])
assert solve(1000) == 15864

print(solve(10**12))
