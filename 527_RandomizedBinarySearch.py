'''
Joe Walter

difficulty: 30%
run time:   0:00
answer:     11.92412011

	***

527 Randomized Binary Search

A secret integer t is selected at random within the range 1≤t≤n.

The goal is to guess the value of t by making repeated guesses, via integer g. After a guess is made, there are three possible outcomes, in which it will be revealed that either g<t, g=t, or g>t. Then the process can repeat as necessary.

Normally, the number of guesses required on average can be minimized with a binary search: Given a lower bound L and upper bound H (initialized to L=1 and H=n), let g=floor((L+H)/2). If g=t, the process ends. Otherwise, if g<t, set L=g+1, but if g>t instead, set H=g-1. After setting the new bounds, the search process repeats, and ultimately ends once t is found. Even if t can be deduced without searching, assume that a search will be required anyway to confirm the value.

Your friend Bob believes that the standard binary search is not that much better than his randomized variant: Instead of setting g=floor((L+H)/2), simply let g be a random integer between L and H, inclusive. The rest of the algorithm is the same as the standard binary search. This new search routine will be referred to as a random binary search.

Given that 1≤t≤n for random t, let B(n) be the expected number of guesses needed to find t using the standard binary search, and let R(n) be the expected number of guesses needed to find t using the random binary search. For example, B(6)=2.33333333 and R(n)=2.71666667 when rounded to 8 decimal places.

Find R(10^10)-B(10^10) rounded to 8 decimal places.
'''

from math import floor, ceil, log
from functools import cache

def B(n):
	@cache
	def _B(n):
		if n <= 1:
			return n
		n -= 1
		L = floor(n/2)
		R = ceil(n/2)
		return 1+L+R+_B(L)+_B(R)
	return _B(n)/n

def R(n):
	if n <= 1:
		return n
	else:
		# R(1)=1
		# R(n) = sum of
		# 	[g=1]	1/n + ((n-1)/n)*R(n-1)
		# 	[g=2]	(1/n)*R(1) + 1/n + ((n-2)/n)*R(n-2)
		# 	[g=3]	(2/n)*R(2) + 1/n + ((n-3)/n)*R(n-3)
		# 	...
		# 	[g=n-1]	((n-2)/n)*R(n-2) + 1/n + (1/n)*R(1)
		# 	[g=n]	((n-1)/n)*R(n-1) + 1/n
		# over n (each has 1/n probability)
		'''
		return 1 + 2*sum(R(x)*x for x in range(1,n))/(n*n)
		'''
		# convert to a loop
		'''
		s = 0 # running sum
		for k in range(1,n):
			r  = 1 + s/k/k
			s += 2*k*r
		return 1 + s/k/k
		'''
		# convert to a recurrence relation
		'''
		a = 0
		for k in range(1,n):
			a = ((k+2)/k)*a + 2*k
		return 1 + a/n/n
		'''
		# solve the recurrence relation
		# https://en.wikipedia.org/wiki/Recurrence_relation#Solving
		F  = n*(n+1)//2
		# a1=0 (index starting at 1)
		# S = sum( 4*m/((m+2)*(m+1)) for m in range(1,n) )
		# S = 4*sum( ( 2/(m+2) - 1/(m+1) ) for m in range(1,n) )
		# S = 8*sum(1/m for m in range(3,n+2)) - 4*sum(1/m for m in range(2,n+1))
		# S = 4*sum(1/m for m in range(3,n+1)) + 8/(n+1) - 4/2
		# S = 4*Hn - 4*H2 + 8/(n+1) - 4/2 where Hk is the k-th Harmonic number
		S  = 4*H(n) - 8*n/(n+1)
		An = F*S
		return 1 + An/n/n

def H(n):
	'''n-th Harmonic number.'''
	if n < 1000:
		return sum(1/n for n in range(1,n+1))
	else:
		# https://en.wikipedia.org/wiki/Harmonic_number#Calculation
		return log(n) + 0.5772156649015329 + 1/(2*n) - 1/(12*n**2) + 1/(120*n**4)

def round(n):
	return f"{n:.8f}"

assert round(B(6)) == "2.33333333"
assert round(R(6)) == "2.71666667"

print(round(R(10**10)-B(10**10)))




'''
from random import randint
from statistics import mean
def R0(n):
	def _R0(n):
		t = randint(1, n)
		count = 1
		L, H = 1, n
		while H > L:
			g = randint(L, H)
			if g > t:
				H = g-1
			elif g < t:
				L = g+1
			else:
				break
			count += 1
		return count
	return mean(_R0(n) for _ in range(10000))
print(R0(10**10))
print(R(10**10))
'''
