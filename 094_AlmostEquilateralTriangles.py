'''
Joe Walter

difficulty: 35%
run time:   0:00
answer:     518408346

	***

094 Almost Equilateral Triangles

It is easily proved that no equilateral triangle exists with integral length sides and integral area. However, the almost equilateral triangle 5-5-6 has an area of 12 square units.

We shall define an almost equilateral triangle to be a triangle for which two sides are equal and the third differs by no more than one unit.

Find the sum of the perimeters of all almost equilateral triangles with integral side lengths and area and whose perimeters do not exceed one billion (1,000,000,000).

	***

Observations

https://en.wikipedia.org/wiki/Heron%27s_formula

If (k,k,k+1) is an almost equilateral triangle, then (k-1) is a perfect square and the perimeter 3k+1 is a perfect square.
k-1 is the square of a term in OEIS/A052530
a(n) = 4*a(n-1) - a(n-2), with a(0) = 0, a(1) = 2

If (k,k,k-1) is an almost equilateral triangle, then (k-1) is divisible by 16.
k-1 is 16 times a term in the sequence OEIS/A076139 (Triangular numbers that are one-third of another triangular number)
a(n) = 14 * a(n-1) - a(n-2) + 1, with a(0) = 0, a(1) = 1
'''

P = 10**9

ans = 0

#(k,k,k+1)
a = [0,2]
while True:
	k = a[-1]**2 + 1
	p = 3*k + 1
	if p <= P:
		ans += p
	else:
		break
	a.append(4*a[-1] - a[-2])

#(k,k,k-1)
a = [0,1]
while True:
	k = 16*a[-1] + 1
	p = 3*k - 1
	if p <= P:
		ans += p
	else:
		break
	a.append(14*a[-1] - a[-2] + 1)

print(ans)


# 5:00
'''
from math import isqrt

def heronian_perimeter2(a,b,c):
	p = a+b+c
	A2 = p*c*c*(a+b-c)
	A = isqrt(A2)
	if A2 == A*A:# and (A&3) == 0 :
		input((a,b,c))
		return p
	return 0

ans = 0
for x in range(3, (10**9)//3 + 1, 2): # 1,1,2 is not Heronian, so skip it for simplicity's sake
	ans += heronian_perimeter2(x, x, x+1)
	ans += heronian_perimeter2(x, x, x-1)
print(ans)
'''
