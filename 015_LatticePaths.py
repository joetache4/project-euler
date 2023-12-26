'''
Joe Walter

difficulty: 5%
run time:   0:00
answer:     137846528820

	***

015 Lattice Paths

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
'''

# perm(n) == n!
from math import perm

h = 20
w = 20

# the number of permutations of 20 H's and 20 V's
ans = perm(h + w) // perm(h) // perm(w)

print(ans)
