'''
Joe Walter

difficulty: 55%
run time:   0:11
answer:     -271248680

	***

150 Searching A Triangular Array For A Sub-Triangle Having Minimum-Sum

In a triangular array of positive and negative integers, we wish to find a sub-triangle such that the sum of the numbers it contains is the smallest possible.

(https://projecteuler.net/project/images/p150.gif)

In the example below, it can be easily verified that the marked triangle satisfies this condition having a sum of −42.

We wish to make such a triangular array with one thousand rows, so we generate 500500 pseudo-random numbers s[k] in the range ±2e19, using a type of random number generator (known as a Linear Congruential Generator) as follows:

t := 0
for k = 1 up to k = 500500:
    t := (615949*t + 797807) modulo 2e20
    s[k] := t−2e19

Thus: s[1] = 273519, s[2] = −153582, s[3] = 450905 etc

Our triangular array is then formed using the pseudo-random numbers thus:
s1
s2  s3
s4  s5  s6
s7  s8  s9  s10
...

Sub-triangles can start at any element of the array and extend down as far as we like (taking-in the two elements directly below it from the next row, the three elements directly below from the row after that, and so on).

The "sum of a sub-triangle" is defined as the sum of all the elements it contains.
Find the smallest possible sub-triangle sum.

	***

Observations

The sums for larger sub-triangles can be easily calculated from the sums of smaller sub-triangles.

This algorithm is O(n^(3/2)). Naively computing the sum of sub-triangles is O(n^(5/2)).
'''

import numpy as np

def rng(depth):
	N = depth*(depth+1)//2
	a = [None]*N
	t = 0
	for i in range(N):
		t = (615949*t+797807)%(2**20)
		a[i] = t-(2**19)
	return a

def triangle(vals):
	L     = len(vals)
	depth = int(-1+(1+8*L)**0.5)//2
	mat   = np.zeros((depth, depth), dtype=np.int32)
	row, col = 0, 0
	for v in vals:
		mat[(row, col)] = v
		if col == 0:
			row, col = 0, row+1
		else:
			row, col = row+1, col-1
	return mat

def shift_left(tri):
	n = tri.shape[0]
	b = np.roll(tri, n-1, 0)
	b[n-1,:] = 0
	return b

def shift_right(tri):
	n = tri.shape[0]
	b = np.roll(tri, n-1, 1)
	b[:,n-1] = 0
	return b

def min_sub_triangle(tri):
	ans   = float('inf')
	depth = tri.shape[0]
	tri0  = np.zeros_like(tri)
	tri1  = np.zeros_like(tri)
	tri2  = np.zeros_like(tri)
	for h in range(depth):
		tri0 = tri + shift_left(tri1) + shift_right(tri1) - shift_left(shift_right(tri2))
		ans = min(ans, tri0.min())
		tri2, tri1, tri0 = tri1, tri0, tri2
	return ans

tri = triangle([15,-14,-7,20,-13,-5,-3,8,23,-26,1,-4,-5,-18,5,-16,31,2,9,28,3])
assert min_sub_triangle(tri) == -42

tri = triangle(rng(1000))
print(min_sub_triangle(tri))


# Original Solution, 0:50
'''
# Return the triangle to the given depth as a list with RNG numbers as elements
def triangle(depth):
	def _rng(N):
		t = 0
		for _ in range(N):
			t = (615949*t+797807)%(2**20)
			yield t-(2**19)
	size = depth*(depth+1)//2
	return depth, list(_rng(size))

# Finds the minimum-sum sub-triangle
def min_sub_triangle(x):
	depth, tri = x
	# current, full-height sums of sub-triangles
	sum0 = [0] * len(tri)
	# previous sums, h-1 and h-2
	sum1 = [0] * len(tri)
	sum2 = [0] * len(tri)
	# best solution so far
	min_sum = tri[0]
	# loop for each triangle height
	for h in range(1, depth+1):
		# indexes to various parts of interest in the triangle
		self_index = 0
		child_index_1 = 1    # the first of two elements directly underneath
		child_index_2 = 2
		grandchild_index = 4 # the single element two rows below
		# loop for each triangle row
		for row in range(0, depth-h+1):
			# loop for each triangle col
			for col in range(0, row+1):
				# add parts together
				try:
					val = tri[self_index]
					val += sum1[child_index_1] + sum1[child_index_2]
					val -= sum2[grandchild_index]
				except IndexError:
					# ignore col out of bounds
					# happens at the bottom of the triangle
					pass
				sum0[self_index] = val
				# update minimum
				if val < min_sum:
					min_sum = val
				# going to next element in row, slide indices
				self_index += 1
				child_index_1 += 1
				child_index_2 += 1
				grandchild_index += 1
			# going to next row, indices go to next row
			child_index_1 += 1
			child_index_2 += 1
			grandchild_index += 2
		# going to next higher height, shift sums
		# sum0 will be overwritten next iteration, so set it to the now useless list
		sum2, sum1, sum0 = sum1, sum0, sum2
	return min_sum

# test
t = triangle(1000)[1]
assert t[0] == 273519
assert t[1] == -153582
assert t[2] == 450905
tri = [15,-14,-7,20,-13,-5,-3,8,23,-26,1,-4,-5,-18,5,-16,31,2,9,28,3]
assert min_sub_triangle((6, tri)) == -42

print(min_sub_triangle(triangle(1000)))
'''
