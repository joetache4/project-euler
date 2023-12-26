'''
Joe Walter

difficulty: 25%
run time:   0:15
answer:     1004195061

	***

348 Sum of a Square and a Cube

Many numbers can be expressed as the sum of a square and a cube. Some of them in more than one way.

Consider the palindromic numbers that can be expressed as the sum of a square and a cube, both greater than 1, in exactly 4 different ways.
For example, 5229225 is a palindromic number and it can be expressed in exactly 4 different ways:

2285**2 + 20**3
2223**2 + 66**3
1810**2 + 125**3
1197**2 + 156**3

Find the sum of the five smallest such palindromic numbers.
'''

from itertools import count

def palindromes():
	for L in count(2):
		L2 = (L+1)>>1		
		if L%2:
			for n in range(10**(L2-1), 10**L2):
				n = str(n)
				yield int(n + n[L2-2::-1])
		else:
			for n in range(10**(L2-1), 10**L2):
				n = str(n)
				yield int(n + n[::-1])

cubes   = [n**3 for n in range(2,1000)]
count_p = 0
ans     = 0

for p in palindromes():
	# p must be odd
	if not p%2:
		continue
	count_s = 0
	for c in cubes:
		s = p-c
		if s < 2:
			break
		elif s == int(s**0.5)**2:
			count_s += 1
			if count_s > 4:
				break
	if count_s == 4:
		print(p)
		count_p += 1
		ans += p
		if count_p == 5:
			break

print(ans)
