'''
Joe Walter

difficulty: 50%
run time:   0:07
answer:     10057761

	***

139 Pythagorean Tiles

Let (a, b, c) represent the three sides of a right angle triangle with integral length sides. It is possible to place four such triangles together to form a square with length c.

For example, (3, 4, 5) triangles can be placed together to form a 5 by 5 square with a 1 by 1 hole in the middle and it can be seen that the 5 by 5 square can be tiled with twenty-five 1 by 1 squares.

https://projecteuler.net/resources/images/0139.png?1678992052

However, if (5, 12, 13) triangles were used then the hole would measure 7 by 7 and these could not be used to tile the 13 by 13 square.

Given that the perimeter of the right triangle is less than one-hundred million, how many Pythagorean triangles would allow such a tiling to take place?
'''

from math import isqrt

def farey(n):
	'''Use Farey sequences to generate coprime pairs <= n.'''
	a, b, c, d = 0, 1, 1, n
	while c <= n:
		k = (n+b)//d
		a, b, c, d = c, d, (k*c-a), (k*d-b)
		if a == 1 and b == 1:
			break
		yield (a,b)

def seed_vals(p_max):
	'''Create inputs for Euclid's method from coprime numbers.'''
	# calculate the Farey order needed so that only a few triplets are generated with perimeter > p_max
	order = isqrt(p_max // 2) + 1
	# inputs must be coprime and have opposite parity
	for (n, m) in farey(order):
		if m%2 != n%2:
			yield (n, m)

def triplet(m, n):
	'''Use Euclid's method to generate primitive Pythagorean triplets.'''
	if m < n:
		m, n = n, m
	a = m*m - n*n
	b = 2*m*n
	c = m*m + n*n
	if b < a:
		a, b = b, a
	return (a, b, c)

N   = 100*10**6
ans = 0

for (n, m) in seed_vals(N):
	a, b, c = triplet(m, n)
	p = a + b + c
	if p >= N:
		continue
	s = c/abs(a-b)
	if int(s) == s:
		ans += N//p

print(ans)
