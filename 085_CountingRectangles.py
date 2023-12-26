'''
Joe Walter

difficulty: 15%
run time:   0:00
answer:     2772

	***

085 Counting Rectangles

By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles:

Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with the nearest solution.
'''

from math import isqrt

def count_rect(h, w):
	'''Counts the total number of rectangles in a grid.'''
	sum = 0
	sum += h*w						# 1 x 1
	sum += h*w*(w-1)//2				# 1 x n
	sum += w*h*(h-1)//2				# n x 1
	sum += h*(h-1)//2*w*(w-1)//2	# m x n
	return sum

def solve(target):
	h   = 1
	w   = isqrt(target)
	ans = (float("inf"), None)
	while w >= h:
		count = count_rect(h, w)
		pair  = (abs(count-target), h*w)
		ans   = min(pair, ans)
		if count > target:
			w -= 1
		else:
			h += 1	
	return ans[1]

print(solve(2*10**6))
