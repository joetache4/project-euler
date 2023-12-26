'''
Joe Walter

difficulty: 5%
run time:   0:00
answer:     31875000

	***

009 Special Pythagorean Triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2.

For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.

Find the product abc.
'''

from bisect import bisect

def solve():
	squares = [x*x for x in range(1000)]
	for a in range(1, 500):
		for b in range(a+1, 501):
			a2 = a*a
			b2 = b*b
			c2 = a2 + b2
			c = bisect(squares, c2)-1
			if squares[c] == c2 and a + b + c == 1000:
				return a*b*c

print(solve())
