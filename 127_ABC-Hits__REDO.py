'''
Joe Walter

difficulty: 50%
run time:   0:59
answer:     18407904

	***

127 ABC-Hits

The radical of n, rad(n), is the product of distinct prime factors of n. For example, 504 = 23 × 32 × 7, so rad(504) = 2 × 3 × 7 = 42.

We shall define the triplet of positive integers (a, b, c) to be an abc-hit if:

    GCD(a, b) = GCD(a, c) = GCD(b, c) = 1
    a < b
    a + b = c
    rad(abc) < c

For example, (5, 27, 32) is an abc-hit, because:

    GCD(5, 27) = GCD(5, 32) = GCD(27, 32) = 1
    5 < 27
    5 + 27 = 32
    rad(4320) = 30 < 32

It turns out that abc-hits are quite rare and there are only thirty-one abc-hits for c < 1000, with ∑c = 12523.

Find ∑c for c < 120000.
'''

from math import gcd, prod
from lib.num import FactorRange

M = 120000
#M = 1000

fr = FactorRange(M)
R = [prod(set(fr.factor(a))) for a in range(M)]
S = 0

for c in range(3, M):
	if c == R[c]:
		continue
	d = 2 if c%2==0 else 1
	for a in range(1,(c+1)//2, d):
		b = c - a
		# rad(abc)=rad(a)rad(b)rad(c) if a,b,c are pairwise coprime
		if R[a]*R[b]*R[c] >= c:
			continue
		if gcd(a,b) > 1 or gcd(a*b,c) > 1:
			continue
		S += c

print(S)
