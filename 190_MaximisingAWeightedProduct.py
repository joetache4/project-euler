'''
Joe Walter

difficulty: 50%
run time:   0:00
answer:     371048281

	***

190 Maximising a Weighted Product

Let S_m = (x_1, x_2, ... , x_m) be the m-tuple of positive real numbers with x_1 + x_2 + ... + x_m = m for which P_m = x_1 * x_2^2 * ... * x_m^m is maximised.

For example, it can be verified that floor(P_10) = 4112 (floor is the integer part function).

Find sum floor(P_m) for 2 <= m <= 15.
'''

from math import prod, floor

def P(x):
	return prod(y**(i+1) for i,y in enumerate(x))

def p190():
	ans = 0
	for m in range(2, 16):
		x = list(range(1, m+1)) # equal to the gradient of P at (1,1,...,1)
		s = sum(x)
		x = map(lambda y: m*y/s, x)
		ans += floor(P(x))
	print(ans)

p190()

'''
from math import prod, floor

def partial(wrt):
	return lambda x: prod( ((i+1)*_x**i if i == wrt else (_x**(i+1)) for i,_x in enumerate(x)) )

def nabla(n):
	return [partial(i) for i in range(n)]

def update(nab, x):
	m    = len(x)
	grad = [p(x) for p in nab]
	for i in range(len(x)):
		x[i] += grad[i]
	s = sum(x)
	for i in range(len(x)):
		x[i] = x[i]*m/s

def P(x):
	return prod(_x**(i+1) for i,_x in enumerate(x))

def p190():
	ans = 0
	for m in range(2, 16):
		x = [1]*m
		nab = nabla(m)
		for _ in range(10):
			update(nab, x)		
		ans += floor(P(x))
	print(ans)

p190()

'''
