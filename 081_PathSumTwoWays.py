'''
Joe Walter

difficulty: 10%
run time:   0:00
answer:     427337

	***

081 Path Sum: Two Ways

In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and down, is indicated in bold red and is equal to 2427.

[grid]

Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by only moving right and down.
'''

from data.p081 import get_data

node = get_data()
N    = len(node)
path = [[None]*N for _ in range(N)]

path[-1][-1] = node[-1][-1]

def get_path(y, x):
	if path[y][x] is None:
		if y == N-1: # at bottom
			path[y][x] = node[y][x] + get_path(y, x+1)
		elif x == N-1: # at right side
			path[y][x] = node[y][x] + get_path(y+1, x)
		else:
			path[y][x] = node[y][x] + min(get_path(y+1, x), get_path(y, x+1))
	return path[y][x]

print(get_path(0, 0))
