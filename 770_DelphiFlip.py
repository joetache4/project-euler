'''
Joe Walter

difficulty: 30%
run time:   0:19
answer:     127311223

	***

770 Delphi Flip

A and B play a game. A has originally 1 gram of gold and B has an unlimited amount. Each round goes as follows:

    A chooses and displays, x, a nonnegative real number no larger than the amount of gold that A has.
	Either B chooses to TAKE. Then A gives B x grams of gold.
	Or B chooses to GIVE. Then B gives A x grams of gold.

B TAKEs n times and GIVEs n times after which the game finishes.

Define g(X) to be the smallest value of so that A can guarantee to have at least X grams of gold at the end of the game. You are given
g(1.7) = 10.

Find g(1.9999).

	***

Observations

Let mult(t,g) be the min guaranteed multiple of principal, p, after t Takes and g Gives. mult shouldn't vary according to p, so assume p = 1.

A plays optimally when selecting an amount x, s.t.
p - x + (mult(t-1, g)-1)*(p-x) = p + x + (mult(t, g-1)-1)*(p+x)

(If Taking or Giving did not give the same result, then one would be worse than the other for A, and B would make that choice.)

So, x = (a-b)/(a+b) where a,b = mult(t-1,g), mult(t,g-1);
and mult(t,g) = (p - x + (mult(t-1, g)-1)*(p-x))/p = (a*(p-x))/p = a*(1-x) = a*(1-(a-b)/(a+b)) = 2ab/(a+b)

These mult values can be placed on a grid like so:


# of Takes remaining
|

1		2		4		8		16		...		<- # of Gives remaining
1	2*1*2/(1+2)
1			2ab/(a+b)
1
1
...


The values on the diagonal, where # of Takes = # of Gives, are of interest. Using a symbolic expression simplifier and the OEIS, a non-recursive formula for the diagonals is found:

mult(n,n) = 2^(2n+1) / ( 2^(2n) + T(n,1) )

where T(n,k) are the terms in OEIS A164705.

Notes:
* T(n+1,1) equals the sum of the n-th row in T.
* n is 1-indexed, k is 0-indexed

Dividing through by 2^(2n), this simplifies to:

mult(n,n) = 2 / ( 1 + prod(odds <= 2n)/prod(evens <= 2n) )

The answer then is to find n s.t. mult(n,n) >= 1.9999.

'''

def g(X):
	X = 2/X-1
	a = 1
	b = 1
	while b > X:
		b *= a
		a += 1
		b /= a
		a += 1
	return a//2

assert g(1.7) == 10

print(g(1.9999)) #127311223



'''


# Recursive (error: stack overflow)

def mult(t, g = None, mem = {}):
	if g is None:
		g = t

	try:
		return mem[t,g]
	except:
		pass

	if t == 0:
		m = 2**g
	elif g == 0:
		m = 1
	else:
		a, b = mult(t-1,g), mult(t,g-1)
		#x = (a - b) / (a + b)
		#m = (1 - x) * a
		m = 2*a*b/(a+b)

	mem[t,g] = m
	return m

print(mult(5))

from itertools import count


# Iterative (error: numerical overflow)


# mult[# of takes, # of gives] -> min guaranteed multiple of principal
mult = {}
def g(X):
	try:
		for n in count(1):
			mult[0,n] = 2**n
			mult[n,0] = 1

			for t in range(1, n):
				a, b = mult[t-1,n], mult[t,n-1]
				mult[t,n] = 2*a*b/(a+b)

			for g in range(1, n):
				a, b = mult[n-1,g], mult[n,g-1]
				mult[n,g] = 2*a*b/(a+b)

			a, b = mult[n-1,n], mult[n,n-1]
			mult[n,n] = 2*a*b/(a+b)

			print(f"mult[{n},{n}] = {mult[n,n]}")

			if mult[n,n] > X:
				return n
	except OverflowError:
		print((n,a,b))
		input()

print(g(1.9))
input()




# temp code

# Observation: the coefficients in the denominator sum to the numerator coefficient

# see https://oeis.org/A164705

a = 2
b = 4
c = 8
d,f,g = 1,1,1

print(16*a*b*c*d*f*g/(2*a*b*c*d*f + 3*a*b*c*d*g + 3*a*b*c*f*g + 2*a*b*d*f*g + 3*a*c*d*f*g + 3*b*c*d*f*g))
print(32/21)

a = 2
b = 4
c = 8
d = 16
f,g,h,k = 1,1,1,1

print(32*a*b*c*d*f*g*h*k/(2*a*b*c*d*f*g*h + 4*a*b*c*d*f*g*k + 5*a*b*c*d*f*h*k + 5*a*b*c*d*g*h*k + 2*a*b*c*f*g*h*k + 4*a*b*d*f*g*h*k + 5*a*c*d*f*g*h*k + 5*b*c*d*f*g*h*k))
print(256/163)

input('**')


import sympy as sym

F = lambda a,b: f"(2*{a}*{b}/({a}+{b}))"





coord = lambda i,j: 3*i+j

blocks = [None]*9

blocks[coord(0,1)] = sym.Symbol('a')
blocks[coord(0,2)] = sym.Symbol('b')
blocks[coord(1,0)] = sym.Symbol('c')
blocks[coord(2,0)] = sym.Symbol('d')

for i in range(1,3):
	for j in range(1,3):
		blocks[coord(i,j)] = F(blocks[coord(i,j-1)], blocks[coord(i-1,j)])

print(sym.simplify(blocks[coord(2,2)]))





coord = lambda i,j: 4*i+j

blocks = [None]*16

blocks[coord(0,1)] = sym.Symbol('a')
blocks[coord(0,2)] = sym.Symbol('b')
blocks[coord(0,3)] = sym.Symbol('c')
blocks[coord(1,0)] = sym.Symbol('d')
blocks[coord(2,0)] = sym.Symbol('f')
blocks[coord(3,0)] = sym.Symbol('g')

for i in range(1,4):
	for j in range(1,4):
		blocks[coord(i,j)] = F(blocks[coord(i,j-1)], blocks[coord(i-1,j)])

print(sym.simplify(blocks[coord(3,3)]))







coord = lambda i,j: 5*i+j

blocks = [None]*25

blocks[coord(0,1)] = sym.Symbol('a')
blocks[coord(0,2)] = sym.Symbol('b')
blocks[coord(0,3)] = sym.Symbol('c')
blocks[coord(0,4)] = sym.Symbol('d')
blocks[coord(1,0)] = sym.Symbol('f')
blocks[coord(2,0)] = sym.Symbol('g')
blocks[coord(3,0)] = sym.Symbol('h')
blocks[coord(4,0)] = sym.Symbol('k')

for i in range(1,5):
	for j in range(1,5):
		blocks[coord(i,j)] = F(blocks[coord(i,j-1)], blocks[coord(i-1,j)])

print(sym.simplify(blocks[coord(4,4)]))






coord = lambda i,j: 6*i+j

blocks = [None]*36

blocks[coord(0,1)] = sym.Symbol('a')
blocks[coord(0,2)] = sym.Symbol('b')
blocks[coord(0,3)] = sym.Symbol('c')
blocks[coord(0,4)] = sym.Symbol('d')
blocks[coord(0,5)] = sym.Symbol('f')
blocks[coord(1,0)] = sym.Symbol('g')
blocks[coord(2,0)] = sym.Symbol('h')
blocks[coord(3,0)] = sym.Symbol('k')
blocks[coord(4,0)] = sym.Symbol('m')
blocks[coord(5,0)] = sym.Symbol('n')

for i in range(1,6):
	for j in range(1,6):
		blocks[coord(i,j)] = F(blocks[coord(i,j-1)], blocks[coord(i-1,j)])

print(sym.simplify(blocks[coord(5,5)]))

input()

'''
