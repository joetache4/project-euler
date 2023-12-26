'''
Joe Walter

difficulty: 75%
run time:   28:00
answer:     994345168

	***

560 Coprime Nim

Coprime Nim is just like ordinary normal play Nim, but the players may only remove a number of stones from a pile that is coprime with the current size of the pile. Two players remove stones in turn. The player who removes the last stone wins.

Let L(n,k) be the number of losing starting positions for the first player, assuming perfect play, when the game is played with k piles, each having between 1 and n-1 stones inclusively.

For example, L(5,2)=6 since the losing initial positions are (1,1), (2,2), (3,3), (4,2), and (4,4).
You are also given L(10,5)=9964, L(10,10)=472400303, L(10**3,10**3) mod 1000000007 = 954021836.

Find L(10**7,10**7) mod 1000000007.

	***

Observations

Nim values for 1..64:
1, 0, 2, 0, 3, 0, 4, 0, 2, 0, 5, 0, 6, 0, 2, 0, 7, 0, 8, 0, 2, 0, 9, 0, 3, 0, 2, 0, 10, 0, 11, 0, 2, 0, 3, 0, 12, 0, 2, 0, 13, 0, 14, 0, 2, 0, 15, 0, 4, 0, 2, 0, 16, 0, 3, 0, 2, 0, 17, 0, 18, 0, 2, 0

1 -> 1
even -> zero
n-th prime -> n, then propagate to all multiples that don't have a value

nim[n] = nim[smallest prime factor of n]
nim[i-th prime] = i+1

By Sprague-Grundy Theorem, two Nim heaps a and b are equaivalent to a Nim heap a xor b
'''

from collections import Counter
from lib.num import get_primes

# get nim vals up to n, inclusive
def get_nim(n):
	primes = get_primes(n)
	val    = [None] * n
	val[1] = 1
	for i in range(len(primes)-1, 0, -1):
		p = primes[i]
		val[p::p] = [i+1] * len(range(p,len(val),p))
	val[0::2] = [0] * len(range(0,len(val),2))
	return val[1:] # throw out 0, there no piles of this size

def pow(a, p, mod):
	if p == 1:
		return a
	elif p%2 == 1:
		return xor(pow(a, p-1, mod), a, mod)
	else:
		x = pow(a, p//2, mod)
		return xor(x, x, mod)

# XOR counts of Nim values
# Returns Nim values of adjoined piles
def xor(a, b, mod):
	c = [0] * len(a)
	# Can be easily sped up when a==b: keep j>=i and add 2xy except when i==j
	#for i,x in enumerate(a):
	#	for j,y in enumerate(b):
	#		c[i^j] = (c[i^j] + x*y) % mod
	L = range(len(a))
	for i in L:
		c[i] = sum(a[j]*b[i^j] for j in L) % mod
	return c

def L(n, k, mod=1000000007):
	nim   = get_nim(n)
	count = Counter(nim)
	# [index = nim value: number of pile sizes with this nim value]
	count = [count[i] for i in range(max(nim)+1)]
	# append zeros until len(count) is a power of 2
	# that way the list is big enough for the XOR of any two nim values
	x     = 1
	while x < len(count): x *= 2
	count += [0] * (x-len(count))
	return pow(count, k, mod)[0]

assert L(5,2)         == 6
assert L(10,5)        == 9964
assert L(10,10)       == 472400303
assert L(10**3,10**3) == 954021836
# print(L(10**7,10**7)) # too slow



# there's a lot of repetition in count[], even when it's been xor()'ed with itself many times
# runs(pow(count, k)) is seemingly constant for k>=3
# so, just need to calculate one value in each run
# for example, the runs for n=10**3 are
# k=1, runs=[1,1,1,1,1,1,1,1,1,1,1,1,157,87]
# k=2, runs=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,16,32,64,32,1,1,1,1,4,1,1,1,1,1,1,1,1,80]
# k>2, runs=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,16,32,64,32,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,16,64]
# as seen above, runs may split, but they do not merge with each other
# they tend to be powers of 2, but this is not always the case
# runs of runs also tend to be powers of 2

from itertools import groupby

def runs(arr):
	return (len(list(g)) for i,g in groupby(arr))

def pow2(a, p, mod):
	if p == 1:
		return a
	elif p%2 == 1:
		return xor2(pow2(a, p-1, mod), a, mod, True if p-1>2 else False, False)
	else:
		x = pow2(a, p//2, mod)
		return xor2(x, x, mod, True if p//2>2 else False, True)

def xor2(a, b, mod, trust_runs=False, ab_equal=False):
	if trust_runs:
		# trust that runs will not change in the xor2()'ed list
		# this is true when a = pow(count, k) for k>2
		L = len(a)
		c = [0]*L
		start = 0
		for r in runs(a):
			#val = sum(a[j]*b[start^j] for j in range(L)) % mod
			val = get_val(a, b, start, L, mod, ab_equal)
			c[start:start+r] = [val]*r
			start += r
		return c
	else:
		L = len(a)
		c = [0]*L
		start = 0
		for r in runs(a):
			if r == 1:
				#c[start] = sum(a[j]*b[start^j] for j in range(L)) % mod
				c[start] = get_val(a, b, start, L, mod, ab_equal)
			else:
				# runs may split in the xor2()'ed list, but this seems to work
				i, j = start, start+r-1
				binary_fill(a,b,c,i,j,L,mod,ab_equal)
			start += r
		return c

def binary_fill(a, b, c, i, j, L, mod, ab_equal):
	#c[i] = sum(a[k]*b[i^k] for k in range(L)) % mod
	c[i] = get_val(a, b, i, L, mod, ab_equal)
	#c[j] = sum(a[k]*b[j^k] for k in range(L)) % mod
	c[j] = get_val(a, b, j, L, mod, ab_equal)
	if j-i > 1:
		m = (i+j)//2
		#c[m] = sum(a[k]*b[m^k] for k in range(L)) % mod
		c[m] = get_val(a, b, m, L, mod, ab_equal)
		if c[i] == c[m]:
			c[i+1:m] = [c[m]] * len(range(i+1,m,1))
		else:
			binary_fill(a, b, c, i+1, m-1, L, mod, ab_equal)
		if c[m] == c[j]:
			c[m+1:j] = [c[m]] * len(range(m+1,j,1))
		else:
			binary_fill(a, b, c, m+1, j-1, L, mod, ab_equal)

def get_val(a, b, start, L, mod, ab_equal=False):
	if ab_equal and start>0:
		# find w = highest power of 2 <= start
		# alternate adding w numbers, then skipping w numbers
		# this adds all pairs a[x]*b[y] while skipping a[y]*b[x]
		# multiply sum by 2
		# TODO there's probably a better way to do this w/o nested loops
		w = 2**(start.bit_length()-1)
		i = 0
		s = 0
		while i < L:
			for j in range(i,i+w):
				s += a[j]*b[start^j]
			i += 2*w
		return (2*s) % mod
	else:
		return sum(a[j]*b[start^j] for j in range(L)) % mod

def L2(n, k, mod=1000000007):
	nim   = get_nim(n)
	count = Counter(nim)
	count = [count[i] for i in range(max(nim)+1)]
	x     = 1
	while x < len(count): x *= 2
	count += [0] * (x-len(count))
	if k%2 == 0:
		return sum(x*x for x in pow2(count, k//2, mod)) % mod
	else:
		return pow2(count, k, mod)[0] # will work for even k too


assert L2(5,2)         == 6
assert L2(10,5)        == 9964
assert L2(10,10)       == 472400303
assert L2(10**3,10**3) == 954021836


#from lib.helpers import timeit
#with timeit():
#	print(L(10**5,10**5))  # 12 minutes
#with timeit():
#	print(L2(10**5,10**5)) # 7 seconds


print(L2(10**7,10**7))  # xor2() will be called 30 times for n=10**7



# runs for n=10**7
'''
k=1
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 664133, 383996]

k=2
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 512, 1024, 6144, 8192, 114688, 131072, 262144, 140288, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 383552]

k>2
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 512, 1024, 6144, 8192, 114688, 131072, 262144, 131072, 8192, 1024, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 512, 6144, 114688, 262144]
'''



# calculates nim values, displays pattern
'''
from math import gcd

def mex(s):
	s = sorted(set(s))
	for i,v in enumerate(s):
		if i != v:
			return i
	return len(s)

def next(i):
	for j in range(1,i+1):
		if gcd(i,j) == 1:
			yield i-j

n = 100
nim = [0]*(n+1)
for i in range(1, n+1):
	nim[i] = mex(nim[j] for j in next(i))

w = 5
for i in range(0,n,w):
	print(nim[i:i+w])
input()
'''



# shows that count[] has many repeated values and the pattern of repeated values--that is, runs(pow(count, k))--is seemingly constant for k>=3
'''
n, mod = 10**3, 1000000007 # 1 <= pile size < n
nim   = get_nim(n)
count = Counter(nim)
count = [count[i] for i in range(0,max(nim)+1)] # [index = nim value: number of pile sizes with this nim value]
x = 1
while x < len(count): x *= 2
count += [0] * (x-len(count))

#print(count)
print(runs(count))

print("**")
p = pow(count, 2, mod) # how many 2-pile games have nim value of [index]
#print(p)
print(runs(p))
print(runs(xor(count, count, mod)))

print("**")
p = pow(count, 3, mod)
#print(p)
print(runs(p))
print(runs(xor(p, count, mod)))

print("**")
p = pow(count, n, mod)
#print(p)
print(runs(p))
print(runs(xor(p, p, mod)))
print("--")
'''



# This is also O(n**2)
'''
def xor(c1, c2, mod):
	#print("+")
	total = (sum(c1) * sum(c2)) % mod
	c3 = [total] * len(c1)
	subtract_partial_sums(c3, TreeSum(c1), TreeSum(c2), 0, len(c3), mod)
	return c3

# see https://en.wikipedia.org/wiki/Exclusive_or#/media/File:Z2^4;_Cayley_table;_binary.svg

# Binary tree holding the partial sums of a bisected list
# len(list) == 2**k for some k
class TreeSum:
	def __init__(self, a):
		if len(a) == 1:
			self.left  = None
			self.right = None
			self.val   = a[0]
		else:
			m = len(a)//2
			self.left  = TreeSum(a[:m])
			self.right = TreeSum(a[m:])
			self.val   = self.left.val + self.right.val

def subtract_partial_sums(arr, sums1, sums2, lo, hi, mod):
	if sums1.left is None:
		return

	m = (lo+hi)>>1
	d = sums1.left.val*sums2.right.val + sums1.right.val*sums2.left.val
	d %= mod
	for i in range(lo, m):
		arr[i] -= d
	d = sums1.left.val*sums2.left.val + sums1.right.val*sums2.right.val
	d %= mod
	for i in range(m, hi):
		arr[i] -= d
	subtract_partial_sums(arr, sums1.left,  sums2.left,  lo, m,  mod)
	subtract_partial_sums(arr, sums1.right, sums2.right, lo, m,  mod)
	subtract_partial_sums(arr, sums1.left,  sums2.right, m,  hi, mod)
	subtract_partial_sums(arr, sums1.right, sums2.left,  m,  hi, mod)
#'''
