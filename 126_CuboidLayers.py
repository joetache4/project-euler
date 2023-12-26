'''
Joe Walter

difficulty: 55%
run time:   0:17
answer:     18522

	***

126 Cuboid Layers

The minimum number of cubes to cover every visible face on a cuboid measuring 3 x 2 x 1 is twenty-two.

If we then add a second layer to this solid it would require forty-six cubes to cover every visible face, the third layer would require seventy-eight cubes, and the fourth layer would require one-hundred and eighteen cubes to cover every visible face.

However, the first layer on a cuboid measuring 5 x 1 x 1 also requires twenty-two cubes; similarly the first layer on cuboids measuring 5 x 3 x 1, 7 x 2 x 1, and 11 x 1 x 1 all contain forty-six cubes.

We shall define C(n) to represent the number of cuboids that contain n cubes in one of its layers. So C(22) = 2, C(46) = 4, C(78) = 5, and C(118) = 8.

It turns out that 154 is the least value of n for which C(n) = 10.

Find the least value of n for which C(n) = 1000.
'''

from heapq import heappush, heappop

def layer(l,w,h,d):
	size = 2*l*w + 2*l*h + 2*w*h  + \
	(d-1) * (4*l + 4*w + 4*h) + \
	4 * (d-2) * (d-1)
	return (size,l,w,h,d)

N = 1000

q = []
visited = set()

heappush(q, layer(1,1,1,1))
visited.add((1,1,1,1))

old_size = -1
count = 0

while True:
	size,l,w,h,d = heappop(q)

	if old_size != size:
		if count == N:
			break
		count = 0

	count += 1

	if (l+1,w,h,d) not in visited:
		heappush(q, layer(l+1,w,h,d))
		visited.add((l+1,w,h,d))
	if l >= w+1 >= h and (l,w+1,h,d) not in visited:
		heappush(q, layer(l,w+1,h,d))
		visited.add((l,w+1,h,d))
	if l >= w >= h+1 and (l,w,h+1,d) not in visited:
		heappush(q, layer(l,w,h+1,d))
		visited.add((l,w,h+1,d))
	if (l,w,h,d+1) not in visited:
		heappush(q, layer(l,w,h,d+1))
		visited.add((l,w,h,d+1))

	old_size = size

print(old_size)
