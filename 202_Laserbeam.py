r'''
Joe Walter

difficulty: 60%
run time:   0:00
answer:     1209002624

	***

202 Laserbeam

Three mirrors are arranged in the shape of an equilateral triangle, with their reflective surfaces pointing inwards. There is an infinitesimal gap at each vertex of the triangle through which a laser beam may pass.

Label the vertices A, B and C. There are 2 ways in which a laser beam may enter vertex C, bounce off 11 surfaces, then exit through the same vertex: one way is shown below; the other is the reverse of that.

[https://projecteuler.net/resources/images/0202_laserbeam.gif?1678992055]

There are 80840 ways in which a laser beam may enter vertex C, bounce off 1000001 surfaces, then exit through the same vertex.

In how many ways can a laser beam enter at vertex C, bounce off 12017639147 surfaces, then exit through the same vertex?

	***

Solution Method

With the initial triangle at the bottom, partially tile the plane as below ("upwards and to the right"), labelling vertices (A,B,C) so that no two adjacent vertices have the same label.

        ...
       \/\/\/
       /\/\/
       \/\/
       /\/
       \/

Each vertex is given by a coordinate pair (x,y). Vertex C of the initial triangle is the origin (0,0). The basis for this coordinate system is the x-direction being diagonally up and to the right; the y-direction being vertically up.

Every valid laserbeam path then is equivalent to a line segment interecting the origin and one other C-vertex (and no other vertices). The number of bounces is 4(y-1)+2x+1 where (x,y) are the non-origin coordinates. To get N bounces, x is unique for each y: x = (N-1)/2+2 - 2y.

From these facts and the restriction* 0<x<y, one derives: (N-1)/6 + 2/3 < y < (N-1)/4 + 1. (*The inequalities are strict because 0=x corresponds to the edge case where N=1 and is handled separately; x=y corresponds to invalid paths.)

For each valid line segment, it must be that gcd(x,y)=1. Otherwise, the vertex at (x/gcd(x,y),y/gcd(x,y)) is intersected. Using also the formula for x, this means gcd((N-1)/2+2, y)=1.

The problem is then to count the number of y's in the above range that are not divisible by the prime factors of (N-1)/2+2. Finally, double the count, because each path can be reversed.
'''

from math import floor, ceil, prod
from lib.num import factor
from lib.array import subsets

def count_divisible_in_range(lo, hi, p):
	return len(range(0,hi,p)) - len(range(0,lo,p))

def count(N):
	if N == 1:
		return 1
	y_lo, y_hi = floor((N-1)/6 + 2/3 + 1), ceil((N-1)/4 + 1)
	count = 0
	for primes in subsets(set(factor((N-1)//2+2))):
		count += count_divisible_in_range(y_lo, y_hi, prod(primes)) * pow(-1, len(primes))
	return 2*count

assert count(11) == 2
assert count(1000001) == 80840

print(count(12017639147))



'''
N = 12017639147
y_lo, y_hi = floor((N-1)/6 + 2/3 + 1), ceil((N-1)/4 + 1)

def x(y):
	return (N-1)//2-2*(y-1)

def bounces(x,y):
	return 4*(y-1)+2*x+1

assert x(y_lo  ) <  y_lo
assert x(y_lo-1) >= y_lo
assert x(y_hi-1) >  0
assert x(y_hi  ) <= 0

assert bounces(x(y_lo  ),y_lo  ) == N
assert bounces(x(y_lo+1),y_lo+1) == N
#'''
