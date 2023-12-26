'''
Joe Walter

difficulty: 95%
run time:   0:01
answer:     14655308696436060

	***

768 Chandelier

A certain type of chandelier contains a circular ring of evenly spaced candleholders.
If only one candle is fitted, then the chandelier will be imbalanced. However, if a second identical candle is placed in the opposite candleholder (assuming n is even) then perfect balance will be achieved and the chandelier will hang level.

Let f(n,m) be the number of ways of arranging m identical candles in distinct sockets of a chandelier with n candleholders such that the chandelier is perfectly balanced.

For example, f(4,2)=2: assuming the chandelier's four candleholders are aligned with the compass points, the two valid arrangements are "North & South" and "East & West". Note that these are considered to be different arrangements even though they are related by rotation.

You are given that f(12,4)=15 and f(36,6)=876.

Find f(360,20).
'''

# AKA Certrifuge Problem

# Step 1: Count the ways to balance up to 20 candles in a 30-cup chandelier

from collections import Counter

# bitwise rotate, assumes 30-bit length
def rot(n):
	return (n>>1) + ((n&1)<<29)

# regular 2, 3, and 5-sided polygon vertex indices
a = (1<<15) + 1
b = (1<<20) + (1<<10) + 1
c = (1<<24) + (1<<18) + (1<<12) + (1<<6) + 1

# find all ways to rotate regular polygons
base_configs = set()
for poly,size in [(a,2),(b,3),(c,5)]:
	x = poly
	while (x,size) not in base_configs:
		base_configs.add((x,size))
		x = rot(x)

# find balanced configurations in "waves" by adding or removing base polygons
# each wave is generated solely from the previous wave
all_configs = set([(0,0)]) # (config,size)
new_configs = set([(0,0)])
while new_configs:
	new_add = set()
	new_sub = set()
	for a_config, a_size in new_configs:
		for b_config, b_size in base_configs:
			if a_config&b_config == 0: # no conflict
				c = (a_config+b_config, a_size+b_size)
				if c[1] <= 20 and c not in all_configs:
					new_add.add(c)
	for a_config, a_size in new_add:
		for b_config, b_size in base_configs:
			if a_config&b_config == b_config: # all present
				c = (a_config-b_config, a_size-b_size)
				if c not in all_configs:
					new_sub.add(c)
	new_configs  = new_add | new_sub
	all_configs |= new_configs

# tabulate result
count30 = Counter(size for _,size in all_configs)

# Brute force - SLOW (~20mins) but confirms count30 is correct
'''
print("beginning brute force confirmation...")

from math import cos, sin, pi, isclose
from itertools import combinations

i = list(range(30))
z = complex(cos(2*pi/30), sin(2*pi/30))
Z = [z**_i for _i in i]

def is_balanced(data, selectors, _tol=1.0e-8):
	center = sum(data[s] for s in selectors)
	return isclose(center.real, 0.0, abs_tol=_tol) and isclose(center.imag, 0.0, abs_tol=_tol)

for size in range(2, 16):
	count = sum(1 for select in combinations(i, size) if is_balanced(Z, select))
	print(f"{size}: {count}")
#'''

# Step 2: Count the ways to balance exactly 20 candles in a 360-cup chandelier (which is essentially 12 independent subsets of 30)

# if all balanced configurations stem from adding (or removing) candles based on regular polygons,
# then "balanced" and "constructed from regular polygons" are logically equivalent

# with 360 candleholders, each regular 2,3,5-gon (the only regular polygons that will fit)
# 	will have its vertices on indices with equal residue mod 12
# so, subsets of candles with equal residue mod 12 are themselves balanced
# therefore, a config. that isn't balanced in any modular subset isn't balanced overall

from math import prod, factorial
from lib.num import partitions

count360 = 0
for partition in partitions(20):
	if len(partition) > 12 or 1 in partition:
		continue
	count = prod(count30[p] for p in partition)
	# multiply by ways to permute the parts (distribute across the 12 subsets)
	while len(partition) < 12:
		partition.append(0)
	C = Counter(partition)
	count *= factorial(12)//prod(factorial(n) for n in C.values())
	count360 += count

print(count360)
