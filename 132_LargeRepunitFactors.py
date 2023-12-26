'''
Joe Walter

difficulty: 45%
run time:   0:00
answer:     843296

	***

132 Large Repunit Factors

A number consisting entirely of ones is called a repunit. We shall define to be a repunit of length k.

For example, R(10)=1111111111 = 11 x 41 x 271 x 9091, and the sum of these prime factors is 9414.

Find the sum of the first forty prime factors of R(10^9).
'''

from lib.num import factor, get_primes

class I:
	'''A decimal number with 1's at the given indicies and 0s elsewhere.'''
	def __init__(self, ind):
		self.ind = ind
	def mod(self, m):
		return sum(pow(10,i,m) for i in self.ind) % m

class R:
	'''A Repunit of length k.'''
	def __init__(self, k):
		self.k = k
	def div_by_R(self, k2):
		return I(list(range(0,self.k,self.k//k2)))
	def mod(self, m):
		return sum(pow(10,i,m) for i in range(self.k)) % m

# If n|m, then R(n)|R(m)
def semifactor(K):
	f = []
	r = R(K)
	for k in sorted(factor(K))[:-1]:
		f.append(r.div_by_R(k))
		K //= k
		r = R(K)
	f.append(r)
	return f

primes = get_primes(10**6)

def S(k, n):
	P = []
	for p in primes:
		for f in semifactor(k):
			if f.mod(p) == 0:
				P.append(p)
				if len(P) == n:
					return sum(P)

assert S(10, 4) == 9414

print(S(10**9, 40))
