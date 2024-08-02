'''
Joe Walter

difficulty: 10%
run time:   0:40
answer:     827850196

	***

869 Prime Guessing

For a positive integer d, let f(d) be the number created by sorting the digits of d in ascending order, removing any zeros. For example, f(3403) = 334.

Let S(n) be the sum of f(d) for all positive integers d of n digits or less. You are given S(1) = 45 and S(5) = 1543545675.

Find S(18). Give your answer modulo 1123455689.
'''

from lib.num import partitions
from math import prod, factorial as f

# from more_itertools import distinct_permutations
def distinct_permutations(seq):
	'''Given a sequence of n elements, generate all permutations of the sequence in lexicographically correct order.'''
	# Algorithm L for The Art of Computer Programming, Volume 4, Fascicle 2: Generating All Tuples and Permutations.

	def reverse(seq, start, end):
		'''In-place reverse.'''
		# seq = seq[:start] + reversed(seq[start:end]) + seq[end:]

		end -= 1
		while start < end:
			seq[start], seq[end] = seq[end], seq[start]
			start += 1
			end -= 1

	if not seq:
		return

	seq = sorted(seq)
	end = len(seq)

	yield seq

	while True:
		j = end - 1
		while True:
			# Step 1
			j -= 1
			if j == -1:
				return
			if seq[j] < seq[j+1]:
				# Step 2
				l = end - 1
				while not seq[j] < seq[l]:
					l -= 1
				seq[j], seq[l] = seq[l], seq[j]
				# Step 3
				reverse(seq, j+1, end)
				# Change to yield references to get rid of (at worst) |seq|! copy operations.
				#yield seq[:]
				yield seq
				break

def _S(L):
	total = 0
	for unordered_counts in {tuple(p) for p in partitions(L) if len(p) <= 10}:
		unordered_counts = list(unordered_counts)
		while len(unordered_counts) < 10:
			unordered_counts.append(0)
		for digit_counts in distinct_permutations(unordered_counts):
			count = f(L)//prod(f(c) for c in digit_counts)
			if digit_counts[0]:
				# discount numbers starting with 0
				count -= count * f(L-1) * f(digit_counts[0]) // f(L) // f(digit_counts[0]-1)
			value = int("".join(str(d)*c for d,c in enumerate(digit_counts)))
			total += value*count
	return total

def S(L):
	return sum(_S(n) for n in range(1, L+1))

assert(S(1)) == 45
assert(S(5)) == 1543545675

print(S(18) % 1123455689)
