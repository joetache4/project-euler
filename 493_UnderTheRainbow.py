'''
Joe Walter

difficulty: 10%
run time:   0:00
answer:     6.818741802

	***

493 Under The Rainbow

70 coloured balls are placed in an urn, 10 for each of the seven rainbow colours.

What is the expected number of distinct colours in 20 randomly picked balls?

Give your answer with nine digits after the decimal point (a.bcdefghij).
'''

from math import comb, prod, factorial as f
from collections import Counter
from lib.num import partitions

def count_permutations(arr):
	c = Counter(arr)
	return f(len(arr)) / prod(f(c[x]) for x in c)

ans = 0
for p in partitions(20, range(1, 11)):
	if len(p) > 7:
		continue
	num_unique = len(p)
	while len(p) < 7:
		p.append(0)
	num_perms = count_permutations(p)
	prob = prod(comb(10, b) for b in p) / comb(70, 20)
	ans += num_unique * num_perms * prob

print(f"{ans:.9f}")