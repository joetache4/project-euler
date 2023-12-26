'''
Joe Walter

difficulty: 15%
run time:   1:40
answer:     694687

	***

504 Square On The Inside

Let ABCD be a quadrilateral whose vertices are lattice points lying on the coordinate axes as follows:

A(a, 0), B(0, b), C(−c, 0), D(0, −d), where 1 ≤ a, b, c, d ≤ m and a, b, c, d, m are integers.

It can be shown that for m = 4 there are exactly 256 valid ways to construct ABCD. Of these 256 quadrilaterals, 42 of them strictly contain a square number of lattice points.

How many quadrilaterals ABCD strictly contain a square number of lattice points for m = 100?

	***

Observations

The following ideas are used:

Pick's Theorem
A = i + b/2 - 1
i = number of interior points
b = number of boundary points

Area of a Quadrilateral from diagonal lengths
A = 0.5*L1*L2

Number of integer-coordinate points between two endpoints (A,0) and (0,B)
gcd(A, B)-1
'''


from math import gcd, isqrt

def solve(m):
	ans = 0
	for a in range(1, m+1):
		for b in range(1, m+1):
			for c in range(1, m+1):
				for d in range(1, m+1):
					A = 0.5*(a+c)*(b+d)
					B = 0
					B += gcd(a, b)
					B += gcd(b, c)
					B += gcd(c, d)
					B += gcd(d, a)
					I = A - B/2 + 1
					if I == isqrt(int(I))**2:
						ans += 1
	return ans

assert solve(4) == 42

print(solve(100))
