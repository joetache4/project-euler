'''
Joe Walter

difficulty: 5%
run time:   0:00
answer:     7273

	***

067 Max Path Sum 2

Harder version of problem 18.
'''

from data.p067 import get_data

def max_pathsum(tri):
	depth = len(tri)
	for level in range(depth - 2, -1, -1):
		for index in range(len(tri[level])):
			tri[level][index] += max(tri[level+1][index], tri[level+1][index+1])
	return tri[0][0]

print(max_pathsum(get_data()))
