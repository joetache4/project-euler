'''
Joe Walter

difficulty: 45%
run time:   0:00
answer:     1118049290473932

	***

138 Special Isosceles Triangles

Consider the isosceles triangle with base length, b = 16, and legs, L = 17.

https://projecteuler.net/resources/images/0138.png?1678992052

By using the Pythagorean theorem it can be seen that the height of the triangle, h = sqrt(17^2 - 8^2) = 15, which is one less than the base length.

With b = 272 and L = 305, we get h = 273, which is one more than the base length, and this is the second smallest isosceles triangle with the property that h = b +- 1.

Find sum(L) for the twelve smallest isosceles triangles for which h = b +- 1 and b, L are positive integers.
'''

# First couple of Ls - the ratio approaches some number just under 18
'''
17
305
5473
98209
1762289
'''

from itertools import count
from math import sqrt

solve = lambda a,b,c: (sqrt(b*b - 4*a*c) - b)/(2*a)

Ls, L, r, prev_L  = [], 17, -1, 1

while len(Ls) < 12:
	b1 = solve(5,  8, 4 - 4*L*L) # h = b+1
	b2 = solve(5, -8, 4 - 4*L*L) # h = b-1
	if int(b1)==b1 or int(b2)==b2:
		Ls.append(L)
		r, prev_L = L/prev_L, L
		L = int(r*L) # L is always odd but it's unnecessary to account for this
	else:
		L += 1

print(sum(Ls))
