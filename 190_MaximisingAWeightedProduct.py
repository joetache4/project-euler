'''
Joe Walter

difficulty: 50%
run time:   0:00
answer:     371048281

	***

190 Maximising a Weighted Product

<p>Let $S_m = (x_1, x_2, \dots , x_m)$ be the $m$-tuple of positive real numbers with $x_1 + x_2 + \cdots + x_m = m$ for which $P_m = x_1 \cdot x_2^2 \cdot \cdots \cdot x_m^m$ is maximised.</p>

<p>For example, it can be verified that $\lfloor P_{10}\rfloor = 4112$ ($\lfloor \, \rfloor$ is the integer part function).</p>

<p>Find $\sum \lfloor P_m \rfloor$ for $2 \le m \le 15$.</p>
'''

from math import prod, floor

def P(x):
	return prod(_x**(i+1) for i,_x in enumerate(x))

def p190():
	ans = 0
	for m in range(2, 16):
		x = list(range(1, m+1)) # equal to the gradient at S=(1,1,...,1)
		s = sum(x)
		x = [_x*m/s for _x in x]
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
