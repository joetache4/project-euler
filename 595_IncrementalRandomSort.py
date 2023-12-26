'''
Joe Walter

difficulty: 35%
run time:   0:00
answer:     54.17529329

	***

595 Incremental Random Sort

A deck of cards numbered from 1 to n is shuffled randomly such that each permutation is equally likely.

The cards are to be sorted into ascending order using the following technique:

    Look at the initial sequence of cards. If it is already sorted, then there is no need for further action. Otherwise, if any subsequences of cards happen to be in the correct place relative to one another (ascending with no gaps), then those subsequences are fixed by attaching the cards together. For example, with 7 cards initially in the order 4123756, the cards labelled 1, 2 and 3 would be attached together, as would 5 and 6.

    The cards are 'shuffled' by being thrown into the air, but note that any correctly sequenced cards remain attached, so their orders are maintained. The cards (or bundles of attached cards) are then picked up randomly. You should assume that this randomisation is unbiased, despite the fact that some cards are single, and others are grouped together.

    Repeat steps 1 and 2 until the cards are sorted.

Let S(n) be the expected number of shuffles needed to sort the cards. Since the order is checked before the first shuffle, S(1) = 0. You are given that S(2) = 1, and S(5) = 4213/871.

Find S(52), and give your answer rounded to 8 decimal places.
'''

from math import factorial, comb
from functools import cache

@cache
def count(n, m):
	'''Count the permutations of n cards with m consecutive cards.'''
	if m == 0:
		return factorial(n) - sum(count(n, k) for k in range(1, n))
	return comb(n-1, m) * count(n-m, 0)

def S(n):
	if n == 1:
		return 0
	@cache
	def _S(n):
		# {# of card groups -> count of such permutations}
		# so, transition probabilities * total number of permutations
		# keys range from 1 to n (inclusive)
		P = {n-m: count(n, m) for m in range(n)}
		# solve S(k) = 1 + P(k)S(k) + P(k-1)S(k-1) + ... P(2)S(2)
		# skip S(1) since S(1) = 0
		f = factorial(n)
		return (1 + sum(P[k]*_S(k) for k in range(2, n))/f)/(1-P[n]/f)
	# _S() assumes the n cards start with no consecutives, which may not be the case
	# since the initial permutation is actually random, subtract 1 -- it's like we got a free shuffle
	return _S(n)-1

assert S(1) == 0
assert S(2) == 1
assert S(5) == 4213/871

print(f"{S(52):.8f}")
