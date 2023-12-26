'''
Joe Walter

difficulty: 20%
run time:   0:21
answer:     26033

	***

060 Prime Pair Sets

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
'''

from lib.num import get_primes
from lib.array import binary_search

primes = get_primes(10**8)

def concat(x, y):
	'''
	c = 10
	while c <= y:
		c *= 10
	return c*x + y
	'''
	return int(str(x)+str(y)) # just as fast

def is_pair(a, b):
	return 	binary_search(primes, concat(a, b)) and \
			binary_search(primes, concat(b, a))

def solve(p):
	subsets = []
	# convert primes into indices & create adjacency matrix
	pairs = [[False]*len(p) for _ in p]
	for i, a in enumerate(p):
		for j, b in enumerate(p):
			if j >= i:
				break
			if is_pair(a, b):
				pairs[i][j], pairs[j][i] = True, True
				subsets.append([i, j])
	# add primes one at a time to subsets, see which are valid
	for _ in range(3):
		new_subsets = []
		for s in subsets:
			for c in range(len(pairs)):
				if c not in s and all(pairs[x][c] for x in s):
					new_subsets.append([c, *s])
		subsets = new_subsets
	#convert indices back into primes
	subsets = [[p[i] for i in s] for s in subsets]
	if subsets:
		return min(sum(s) for s in subsets)
	else:
		return float("inf")

# groups primes based on mod 3
# cannot combine primes from both sets at once (they'd be divisible by 3)
p1, p2 = [3], []
for p in primes:
	if p > 9999:
		break # assume primes are 4 digits or fewer
	if p%3 == 1:
		p1.append(p)
	else:
		p2.append(p)

print(min(solve(p1), solve(p2)))
