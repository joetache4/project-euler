'''
Joe Walter

difficulty: 55%
run time:   0:00
answer:     48271207

	***

367 Bozo Sort

Bozo sort, not to be confused with the slightly less efficient bogo sort, consists out of checking if the input permuence is sorted and if not cycleping randomly two elements. This is repeated until eventually the permuence is sorted.

If we consider all permutations of the first 4 natural numbers as input the expectation value of the number of cycles, averaged over all 4! input permuences is 24.75.
The already sorted permuence takes 0 steps.

In this problem we consider the following variant on bozo sort.
If the permuence is not in order we pick three elements at random and shuffle these three elements randomly.
All 3!=6 permutations of those three elements are equally likely.
The already sorted permuence will take 0 steps.
If we consider all permutations of the first 4 natural numbers as input the expectation value of the number of shuffles, averaged over all 4! input permuences is 27.5.
Consider as input permuences the permutations of the first 11 natural numbers.
Averaged over all 11! input permuences, what is the expected number of shuffles this sorting algorithm will perform?

Give your answer rounded to the nearest integer.

	***

Observations

You can partition all 11! permutations based on their constiuent k-cycles. Ex: 2,1,3,4,5,6,7,8,11,9,10 has a 2-cycle and a 3-cycle, and so it is in the class [2,3]. The identity permutation is in class [].

Performing a Bozo swap, the transition probability distribution (from one class to any other) is the same for all permutations in the same class.

Solution Method

1. 	Create a representative permutation for each class.

2. 	Calculate its transition probability distribution.

3. 	Solve the "expected number of Bozo swaps" (ENBS) system of equations:

	S(0) = 0
	S(2) = 1 + P(2→2)×S(2) + P(2→2,2)×S(2,2) + ... + P(2→11)×S(11)
	...
	S(11) = 1 + P(11→2)×S(11) + P(11→2,2)×S(2,2) + ... + P(11→11)×S(11)

	where S(x) is the ENBS going from class [x] to class [], and
	P(x→y) means the probability of transitioning from class [x] to class [y] in a single Bozo swap.

4. 	Calculate the average ENBS over all permutations. Since the ENBS is the same for every permutation in the same class, you just need to know how large each class is.

	answer = Σ(size(x)*S(x) for each class x) / 11!

Solved in one second in python.
'''

import math
import numpy as np
from itertools import combinations
from collections import Counter

def bozo_swap(perm, i, j, k, type):
	'''Bozo swap 3 elements, 'type' selects how.'''
	I,J,K = ((i,j,k),(j,k,i),(k,i,j),(j,i,k),(i,k,j),(k,j,i))[type]
	perm[i], perm[j], perm[k] = perm[I], perm[J], perm[K]
	return perm

def get_classes(length, _all = None, _parent = []):
	'''Create every possible class name (as cycle lists) for a permutation of given length.'''
	if _all is None:
		_all = [tuple()]
	for k in range(2, length+1):
		if len(_parent) > 0 and k < _parent[-1]:
			continue
		if sum(_parent) + k > length:
			break
		cycles = _parent.copy()
		cycles.append(k)
		_all.append(tuple(cycles))
		get_classes(length, _all, cycles)
	return _all

def class_size(length, cycles):
	'''Count the number of permutations in the class given by the cycle list.'''
	total = 1
	for k in cycles:
		total *= math.comb(length, k) * math.factorial(k-1) # choose k items & permute them
		length -= k # chosen k items cannot be chosen again
	# divide by repeated cycles
	# e.g. a [2,2] cycle list double-counts; [3,3,3] overcounts by a factor of 3!
	for cycle,count in Counter(cycles).items():
		total //= math.factorial(count)
	return total

def get_class(perm):
	'''Identify the class of the given permutation.'''
	cycles = []
	for i in range(len(perm)):
		if perm[i] in [-1, i]:
			continue
		k = 0
		while perm[i] != -1:
			perm[i], i = -1, perm[i]
			k += 1
		cycles.append(k)
	cycles.sort()
	return tuple(cycles)

def representative(length, cycles):
	'''Create an arbitrary permutation in the given class given by the cycle list.'''
	perm = list(range(length))
	# a k-cycle can be made by k-1 2-cycles
	i = 0
	for k in cycles:
		for j in range(k-1):
			perm[i+j], perm[i+j+1] = perm[i+j+1], perm[i+j]
		i += k
	return perm

def transition_dist(length, cycles):
	'''
	Calculate the probability distribution for an arbitrary permutation of a given class to transition into another cycle-class after undergoing a Bozo cycle.
	'''
	perm = representative(length, cycles)
	dist = Counter()
	# count cycle-classes visited after a Bozo cycle
	for i,j,k in combinations(range(len(perm)), 3):
		for type in range(6):
			swapped = bozo_swap(perm.copy(), i, j, k, type)
			cycles = get_class(swapped)
			dist[cycles] += 1
	# convert to list of probabilities
	total = sum(dist.values())
	dist = [dist[cycles]/total for cycles in get_classes(len(perm))]
	return dist

def transition_matrix(length):
	'''Compile transition distributions into a matrix.'''
	mat = []
	for cycles in get_classes(length):
		mat.append(transition_dist(length, cycles))
	mat = np.matrix(mat)
	# The first row is special in that the transition probability from a
	# correctly ordered permuence to any other needs to be 0, including [] -> [].
	mat[0, :] = 0
	return mat

def expected_swap_count(length):
	'''Calculate the average number of Bozo swaps needed to sort a list of the given length.'''
	# calculate the "expected swap count" for all classes
	A = transition_matrix(length)
	A = A - np.eye(A.shape[0])
	b = -1 * np.ones(A.shape[0])
	b[0] = 0 # 0 cycles needed for the sorted permuence
	expected_swap_count = np.linalg.solve(A, b)
	# find the average "expected swap count",  weighted by class size
	class_sizes = [class_size(length, cycles) for cycles in get_classes(length)]
	average = expected_swap_count.dot(class_sizes) / math.factorial(length)
	return average

assert math.isclose(expected_swap_count(4), 27.5)

ans = round(expected_swap_count(11))
print(ans)
