'''
Joe Walter

difficulty: 20%
run time:   0:04
answer:     788626351539895

	***

713 Turan's Water Heating System

Turan has the electrical water heating system outside his house in a shed. The electrical system uses two fuses in series, one in the house and one in the shed. (Nowadays old fashioned fuses are often replaced with reusable mini circuit breakers, but Turan's system still uses old fashioned fuses.) For the heating system to work both fuses must work.

Turan has N fuses. He knows that m of them are working and the rest are blown. However, he doesn't know which ones are blown. So he tries different combinations until the heating system turns on.
We denote by T(N,m) the smallest number of tries required to ensure the heating system turns on.
T(3,2) = 3 and T(8,4) = 7.

Let L(N) be the sum of all T(N,m) for 2 <= m <= N.
L(10^3) = 3281346

Find L(10^7).

	***

The best way to check the fuses is to separate them into m-1 groups so that, by the pigeonhole principle, there exists a group with 2 working fuses. Then the worst case scenario is that all bad pairs of fuses are tested before, finally, a good pair is found.
'''

from math import comb

def T(N,m):
	# separate into m-1 groups
	# some will be bigger by 1 due to remainder
	count       = m-1                # number of groups
	count_big   = N%count            # number of smaller groups
	count_small = count-count_big    # number of bigger groups
	size        = N//(m-1)           # size of smaller groups
	return comb(size+1,2)*count_big + comb(size,2)*count_small

assert T(3,2) == 3
assert T(8,4) == 7

def L(N):
	return sum(T(N,m) for m in range(2, N+1))

assert L(10**3) == 3281346

print(L(10**7))


# this helped me find the best way to choose fuses
'''
from itertools import combinations
def is_subset(a, b):
	return all(x in b for x in a)
# all pairs
pairs = list(combinations(range(8), 2))
# all 7-length lists of pairs
methods = list(combinations(pairs, 7))
# find method that always works (has a valid pair for every permutation of fuses)
for method in methods:
	if all(any(is_subset(m, valid) for m in method) for valid in combinations(range(8),4)):
		print(method)

def T_slow(N, M):
	# partition N into group_size such that, by the pigeonhole principle, there will be a group with at least 2 working fuses
	group_count = min(M-1, N//2)
	group_size = [N//group_count] * group_count
	# distribute excess into last (or first, it doesn't matter) bunch of groups
	n = N % group_count #N - sum(group_size)
	group_size[:n] = [group_size[0]+1]*n
	#if n > 0:
	#	group_size[-n:] = [group_size[0]+1]*n
	# put at least one working fuse in each group, and put the rest in the last bunch of group_size
	valid = [1] * group_count
	valid[-1] = 2
	m = M - group_count - 1
	i = -1
	while m > 0:
		if valid[i] < group_size[i]:
			valid[i] += 1
			m -= 1
		else:
			i -= 1
	# the worst case scenario is every bad pair tested before the first good pair
	ans = 1
	for g,v in zip(group_size, valid):
		if v >= 2:
			ans += comb(g-v, 2)
			ans += (g-v)*v
			break
		else:
			ans += comb(g, 2)
	return ans
'''
