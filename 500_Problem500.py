'''
Joe Walter

difficulty: 15%
run time:   0:01
answer:     35407281

	***

500 Problem 500!!!

The number of divisors of 120 is 16.
In fact 120 is the smallest number having 16 divisors.

Find the smallest number with 2^500500 divisors.
Give your answer modulo 500500507.

	***

Observations

Let n = prod(p[i] ^ a[i])
In order to have 2^500500 divisors, prod(1 + a[i]) = 2^500500
This means every 1 + a[i] is a power of 2.  (a[i] = 2^k[i] - 1)

Meaning, n = prod( p[i] ^ (2^k[i] - 1) )

Note that each increment of k[i] produces exactly 2x more divisors:
ratio = prod(1 + a[i]_final) / prod(1 + a[i]_init)
      = (1 + 2^k[i]_final - 1) / (1 + 2^k[i]_init - 1)
      = 2^(k[i]+1) / 2^k[i]
	  = 2

So, going from n = 2^0 to 2^1 to 2^3 to 2^7 to 2^15 etc. doubles the number of divisors each time.

Note that the ratio between these doublngs is p^(2^x).

The solution, then is to make 500500 doublings, choosing the smallest p^(2^x). This is achieved using a min-heap initialized with the first 500500 primes. After popping the head, p^(2^x), push the value p^(2*2^x).

Basically, this method doubles the number of divisors each iteration, because it keeps the powers of primes in the prime factorization as one less than a power of two. After adding one and multiplying per the divisor count function, we're left with 2^500500 divisors.

Solution Method (Old)

Let n = prod(p[i] ^ a[i])
In order to have 2^500500 divisors, prod(1 + a[i]) = 2^500500
This means every 1 + a[i] is a power of 2.  (a[i] = 2^k[i] - 1)

Each increment of k[i] produces exactly 2x more divisors:
ratio = prod(1 + a[i]_final) / prod(1 + a[i]_init)
      = (1 + 2^k[i]_final - 1) / (1 + 2^k[i]_init - 1)
      = 2^(k[i]+1) / 2^k[i]
	  = 2

So, sum(k[i]) = 500500  ->  2^500500 divisors.

Solution is to greedily increment k[i] that has the smallest increase to n

The change in n after incrementing k[i]:
ratio = p[i]^( 2^(k[i]+1)) / p[i]^(2^k[i] )
      = p[i]^( log(p[i]^(2^(k[i]+1))) - log(p[i]^(2^k[i])) )
      = p[i]^( 2^(k[i]+1) - 2^k[i] )
      = p[i]^( 2^k[i] )

In order to choose the correct k[i], I quickly compare my options:
    a^(2^b) > c^(2^d)
 2^b*log(a) > 2^d*log(c)
(2^b)/(2^d) > log(c)/log(a)
    2^(b-d) > log_a(c)
'''

from heapq import heappush, heappop
from primesieve import n_primes

def solve(D, M = 500500507):
	h = list(n_primes(D))
	n = 1
	for _ in range(D):
		p = heappop(h)
		heappush(h, p**2)
		n = n*p % M
	return n

assert solve(4) == 120

print(solve(500500))



# Old method
'''
from math import log
from primesieve import n_primes

p = list(n_primes(500500))
k = [0] * len(p)
k[0] = 1
klen = 1

for i in range(500500-1): # one increment has already been done above
	min_index = 0
	exp = k[0]

	for j in range(1, klen):
		d = k[j]
		if d != exp:
			exp = d
			a = p[min_index]
			b = k[min_index]
			c = p[j]
			if 2**(b-d) > log(c, a):
				min_index = j
			if exp == 1:
				break

	# compare to first prime with k[i] = 0
	a = p[min_index]
	b = k[min_index]
	c = p[klen]
	d = k[klen]
	if 2**(b-d) > log(c, a):
		min_index = klen
		klen += 1
	k[min_index] += 1

m = 500500507
ans = 1
for i in range(klen):
	ans = (ans * pow(p[i], 2**k[i]-1, m)) % m
print(ans)
'''
