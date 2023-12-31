'''
Joe Walter

difficulty: 55%
run time:   0:00
answer:     14516824220

	***

128 Hexagonal Tile Differences

A hexagonal tile with number 1 is surrounded by a ring of six hexagonal tiles, starting at "12 o'clock" and numbering the tiles 2 to 7 in an anti-clockwise direction.

New rings are added in the same fashion, with the next rings being numbered 8 to 19, 20 to 37, 38 to 61, and so on. The diagram below shows the first three rings.

https://projecteuler.net/resources/images/0128.png?1678992052

By finding the difference between tile n and each of its six neighbours we shall define PD(n) to be the number of those differences which are prime.

For example, working clockwise around tile 8 the differences are 12, 29, 11, 6, 1, and 13. So PD(8) = 3.

In the same way, the differences around tile 17 are 1, 17, 16, 1, 11, and 10, hence PD(17) = 2.

It can be shown that the maximum value of PD(n) is 3.

If all of the tiles for which PD(n) = 3 are listed in ascending order to form a sequence, the 10th tile would be 271.

Find the 2000th tile in this sequence.
'''

# the only valid cells will be at or above '1' or '7'
# all other cells have two diffs =1 and two more diffs that are even

from itertools import count
from lib.num import is_prime

def layer_start(k):
	if k == 0:
		return 1
	elif k == 1:
		return 2
	return 2 + k*(k-1)*3

def p128(N):
	if N in [1,2]:
		return N
	a = 2              # '1', '2' are valid cells, counted separately
	for k in count(2): # starting in third layer
		# '1' column check
		n = layer_start(k)
		diffs = [
			1,                      # lower left
			n-layer_start(k-1),     # bottom
			layer_start(k+1)-n,     # top
			(layer_start(k+1)+1)-n, # upper left
			(layer_start(k+1)-1)-n, # lower right
			(layer_start(k+2)-1)-n  # upper right
		]
		if sum(1 for d in diffs if is_prime(d)) == 3:
			a += 1
			if a == N:
				return n
		# '7' column check
		n = layer_start(k+1)-1
		diffs = [
			n-layer_start(k),       # upper left
			n-layer_start(k-1),     # lower left
			n-layer_start(k)-1,     # bottom
			1,                      # lower right
			(layer_start(k+2)-2)-n, # upper right
			(layer_start(k+2)-1)-n  # top
		]
		if sum(1 for d in diffs if is_prime(d)) == 3:
			a += 1
			if a == N:
				return n

assert p128(10) == 271

print(p128(2000))
