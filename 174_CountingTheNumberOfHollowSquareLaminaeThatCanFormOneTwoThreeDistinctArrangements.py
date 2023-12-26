'''
Joe Walter

difficulty: 40%
run time:   0:00
answer:     209566

	***

174 Counting The Number Of "Hollow" Square Laminae That Can Form One, Two, Three, ... Distinct Arrangements

We shall define a square lamina to be a square outline with a square "hole" so that the shape possesses vertical and horizontal symmetry.

Given eight tiles it is possible to form a lamina in only one way: 3x3 square with a 1x1 hole in the middle. However, using thirty-two tiles it is possible to form two distinct laminae.

If t represents the number of tiles used, we shall say that t = 8 is type L(1) and t = 32 is type L(2).

Let N(n) be the number of t ≤ 1000000 such that t is type L(n); for example, N(15) = 832.

What is ∑N(n) for 1 ≤ n ≤ 10?
'''

from collections import Counter

def solve():
	M = 10**6
	c = Counter()
	D = 3
	while True:
		if 4*D - 4 > M:
			break
		for d in range(D-2, 0, -2):
			size = D*D - d*d
			if size <= M:
				c[size] += 1
			else:
				break
		D += 1
	return sum(1 for v in c.values() if 1 <= v <= 10)

print(solve())
