'''
Joe Walter

difficulty: 55%
run time:   0:00
answer:     227485267000992000

	***

172 Investigating Numbers With Few Repeated Digits

How many 18-digit numbers n (without leading zeros) are there such that no digit occurs more than three times in n?
'''

from math import prod, comb, factorial as f
from lib.num import partitions

# returns all partitions of int n with the following restrictions:
# 1. no part is greater than 3
# 2. there are 9 or fewer parts
def P(n):
	yield from (p for p in partitions(n, range(1,4)) if len(p) <= 9)

total = 0

# 0 zeros
for partition in P(18):
	# each part refers to the multiplicity of some digit
	# a = count ways to assign positive digits to each part
	# b = count permutations of these digits
	# c = count ways to insert the digit 0 into the number: choose(length + #0s - 1, #0s)
	a = f(9)//f(9-len(partition))//f(partition.count(1))//f(partition.count(2))//f(partition.count(3))
	b = f(18)//prod(f(part) for part in partition)
	c = comb(17, 0)
	total += a*b*c

# 1 zero
for partition in P(17):
	a = f(9)//f(9-len(partition))//f(partition.count(1))//f(partition.count(2))//f(partition.count(3))
	b = f(17)//prod(f(part) for part in partition)
	c = comb(17, 1)
	total += a*b*c

# 2 zeros
for partition in P(16):
	a = f(9)//f(9-len(partition))//f(partition.count(1))//f(partition.count(2))//f(partition.count(3))
	b = f(16)//prod(f(part) for part in partition)
	c = comb(17, 2)
	total += a*b*c

# 3 zeros
for partition in P(15):
	a = f(9)//f(9-len(partition))//f(partition.count(1))//f(partition.count(2))//f(partition.count(3))
	b = f(15)//prod(f(part) for part in partition)
	c = comb(17, 3)
	total += a*b*c

print(total)


# too slow
'''
from math import comb, factorial

def count(L, d_start=0):
	if L == 0:
		return 1
	elif L < 0:
		return 0
	total = 0
	for d in range(d_start, 10):
		Ld = L-1 if d == 0 else L
		for d_count in range(4):
			total += comb(Ld, d_count)*count(L-d_count, d_start+1)
	return total

print(count(18))
'''
