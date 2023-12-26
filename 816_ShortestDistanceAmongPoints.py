#816

# https://en.wikipedia.org/wiki/Closest_pair_of_points_problem

# 5%
# 0:20
# 20.880613018

# TODO need to compute number of buckets (1000^2) using an algorithm
# TODO hash table might be better than array if the bucketed grid is sparse

from math import sqrt, floor

k = 2000000

L = 1000 # controls how many buckets to use; too small => few buckets => lots of comparisons => very slow, too big => possibly no comparisons => inf as answer 

def get_points(n):
	def _get_points(n):
		s = 290797
		m = 50515093
		for _ in range(n):
			s2 = s*s % m
			yield (s, s2)
			s = s2*s2 % m
	return list(_get_points(n))

def dist2(p, q):
	return (p[0]-q[0])**2 + (p[1]-q[1])**2

def index(x):
	return floor(x/50515093*L)

points = get_points(k)
buckets = [[[] for _ in range(L)] for _ in range(L)]

for p in points:
	buckets[index(p[0])][index(p[1])].append(p)

min_dist = float('inf')
for x in range(len(buckets)-1):
	for y in range(len(buckets[x])-1):
		for p1 in buckets[x][y]:
			for p2 in buckets[x][y]:
				if p1 == p2:
					continue
				d2 = dist2(p1, p2)
				if d2 < min_dist:
					min_dist = d2
			for p2 in buckets[x+1][y]:
				d2 = dist2(p1, p2)
				if d2 < min_dist:
					min_dist = d2
			for p2 in buckets[x][y+1]:
				d2 = dist2(p1, p2)
				if d2 < min_dist:
					min_dist = d2
			for p2 in buckets[x+1][y+1]:
				d2 = dist2(p1, p2)
				if d2 < min_dist:
					min_dist = d2
min_dist = sqrt(min_dist)
print(f"{min_dist:.9f}")