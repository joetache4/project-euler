'''
Joe Walter

difficulty: 45%
run time:   0:00
answer:     20313839404245

	***

103 Special Subset Sums: Optimum

Let S(A) represent the sum of elements in set A of size n. We shall call it a special sum set if for any two non-empty disjoint subsets, B and C, the following properties are true:

    S(B) ≠ S(C); that is, sums of subsets cannot be equal.
    If B contains more elements than C then S(B) > S(C).

If S(A) is minimised for a given n, we shall call it an optimum special sum set. The first five optimum special sum sets are given below.

n = 1: {1}
n = 2: {1, 2}
n = 3: {2, 3, 4}
n = 4: {3, 5, 6, 7}
n = 5: {6, 9, 11, 12, 13}

It seems that for a given optimum set, A = {a1, a2, ... , an}, the next optimum set is of the form B = {b, a1+b, a2+b, ... ,an+b}, where b is the "middle" element on the previous row.

By applying this "rule" we would expect the optimum set for n = 6 to be A = {11, 17, 20, 22, 23, 24}, with S(A) = 117. However, this is not the optimum set, as we have merely applied an algorithm to provide a near optimum set. The optimum set for n = 6 is A = {11, 18, 19, 20, 22, 25}, with S(A) = 115 and corresponding set string: 111819202225.

Given that A is an optimum special sum set for n = 7, find its set string.

NOTE: This problem is related to Problem 105 and Problem 106.
'''

from queue import PriorityQueue # TODO use heapq instead
from lib.array import subsets

def cond1(arr):
	sums = set()
	for subset in subsets(arr, 1):
		s = sum(subset)
		if s in sums:
			return False
		sums.add(s)
	return True

def cond2(arr):
	#arr.sort()
	m = arr[0] # sum of lower terms
	M = 0      # sum of higher terms
	a = 1
	b = len(arr)-1
	while a < b:
		m += arr[a]
		M += arr[b]
		if m <= M:
			return False
		a += 1
		b -= 1
	return True

def solve(arr):
	q = PriorityQueue()

	a = arr[len(arr)//2]
	arr = [i+a-2 for i in arr]
	arr.insert(0, a)

	q.put((sum(arr), arr))
	visited = set()
	visited.add(tuple(arr))
	while True:
		_, arr = q.get()
		if cond2(arr) and cond1(arr):
			return "".join([str(i) for i in arr])
		for a in arr:
			b = a + 1
			while b in arr:
				b += 1
			arr2 = arr.copy()
			arr2.remove(a)
			arr2.append(b)
			arr2.sort()
			tup_arr2 = tuple(arr2)
			if tup_arr2 not in visited:
				q.put((sum(arr2), arr2))
				visited.add(tup_arr2)


assert solve([1]) == "12"
assert solve([1,2]) == "234"
assert solve([2,3,4]) == "3567"
assert solve([3,5,6,7]) == "69111213"
assert solve([6,9,11,12,13]) == "111819202225"

print(solve([11,18,19,20,22,25]))
