'''
Joe Walter

difficulty: 50%
run time:   0:00
answer:     21384

	***

106 Special Subset Sums: Meta-Testing

Let S(A) represent the sum of elements in set A of size n. We shall call it a special sum set if for any two non-empty disjoint subsets, B and C, the following properties are true:

    S(B) ≠ S(C); that is, sums of subsets cannot be equal.
    If B contains more elements than C then S(B) > S(C).

For this problem we shall assume that a given set contains n strictly increasing elements and it already satisfies the second rule.

Surprisingly, out of the 25 possible subset pairs that can be obtained from a set for which n = 4, only 1 of these pairs need to be tested for equality (first rule). Similarly, when n = 7, only 70 out of the 966 subset pairs need to be tested.

For n = 12, how many of the 261625 subset pairs that can be obtained need to be tested for equality?

NOTE: This problem is related to Problem 103 and Problem 105.
'''

from lib.array import subsets

def dominates(a, b):
	if all(x < y for x,y in zip(a, b)):
		return True
	return False

def solve(length):
	arr = set(range(length))
	total = 0
	for a in subsets(arr, 2, len(arr)//2):
		complement = arr - a
		a = sorted(a)
		for b in subsets(complement, len(a), len(a)):
			b = sorted(b)
			# first test below prevents checking all subset pairs twice
			if a[0] < b[0] and not dominates(a, b):
				total += 1
	return total

assert solve(4) == 1
assert solve(7) == 70

print(solve(12))
