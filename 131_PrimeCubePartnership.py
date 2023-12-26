'''
Joe Walter

difficulty: 50%
run time:   0:01
answer:     173

	***

131 Prime Cube Partnership

There are some prime values, p, for which there exists a positive integer, n, such that the expression n^3 + n^2p is a perfect cube.

For example, when p = 19, 8^3 + 8^2×19 = 12^3.

What is perhaps most surprising is that for each prime with this property the value of n is unique, and there are only four such primes below one-hundred.

How many primes below one million have this remarkable property?

'''

from bisect import bisect
from lib.num import get_primes

primes = get_primes(10**6)
cubes  = [n*n*n for n in range(10**3)]

def contains(arr, x):
	return arr[bisect(arr, x)-1] == x

count = 0
c_start, c_stop = 0, len(cubes)
for p in primes:
	for i in range(c_start, c_stop):
		c = cubes[i]
		if cubes[i+1]-c > p:
			break
		if contains(cubes, c+p):
			count += 1
			c_start = i+1
			break

print(count)
