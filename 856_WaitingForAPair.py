'''
Joe Walter

difficulty: 20%
run time:   0:00
answer:     17.09661501

	***

856 Waiting For A Pair

A standard 52-card deck comprises 13 ranks in four suits. A pair is a set of two cards of the same rank.

Cards are drawn, without replacement, from a well shuffled 52-card deck waiting for consecutive cards that form a pair. For example, the probability of finding a pair in the first two draws is 1/17.

Cards are drawn until either such a pair is found or the pack is exhausted waiting for one. In the latter case we say that all 52 cards were drawn.

Find the expected number of cards that were drawn. Give your answer rounded to eight places after the decimal point.
'''

from math import factorial as f
from collections import Counter

no_pairs = [0]*53 # count ways to draw cards without getting a pair
pair     = [0]*53 # count ways to get a pair on the i-th draw
start_state = tuple([-1]+[4]*13) # [last rank drawn + remaining in each rank]
path_counts = Counter()
path_counts[start_state] += 1
for drawn in range(1,53):
	new_path_counts = Counter()
	for path,path_count in path_counts.items():
		last, remaining = path[0], list(path[1:])
		for i,choice_count in enumerate(remaining):
			if choice_count > 0:
				if i == last:
					pair[drawn] += choice_count*path_count
				else:
					remaining[i] -= 1
					new_remaining = sorted(remaining)
					new_last = [new_remaining.index(choice_count-1)]
					new_path_counts[tuple(new_last+new_remaining)] += choice_count*path_count
					remaining[i] += 1
	path_counts = new_path_counts
	no_pairs[drawn] = sum(path_counts.values())


ev = 0
for drawn in range(1,53):
	ev += drawn * (pair[drawn]/(f(52)//f(52-drawn)))
ev += 52 * no_pairs[52]/f(52)

print(f"{ev:.8f}")
