'''
Joe Walter

difficulty: 45%
run time:   15:00
answer:     4037526

	***

291 Panaitopol Primes

A prime number p is called a Panaitopol prime if p = (x^4 - y^4)/(x^3 + y^3) for some positive integers x and y.

Find how many Panaitopol primes are less than 5×10^15.
'''

from lib.num import get_primes, is_prime

'''
for p in get_primes(10**3):
	for x in range(2, 10**3):
		for y in range(x-1, 0, -1):
			q = (x**4-y**4)/(x**3+y**3)
			if q == p:
				print((p,x,y))
			elif q > p:
				break
'''
'''
for p in get_primes(10**5)[1:]:
	d = (p+1)//2
	for y in range(d, 10**7, d):
		x = y+d
		q = (x**4-y**4)/(x**3+y**3)
		if q > p:
			break
		elif q == p:
			k = y//d
			print((p, x, y, k, 2*k*k+2*k+1))
			break
'''

count = 0
M = 5*10**15
for k in range(10**8):
	p = 2*k*k+2*k+1
	if p > M:
		break
	elif is_prime(p):
		count += 1
print(count)
