import math

#########################################################################################
# prime numbers

'''
def get_primes(n):
	# Sieve of Eratosthenes. Returns primes below n as a list.
	is_prime = [True] * (n+1)
	is_prime[0] = False
	is_prime[1] = False
	for k in range(2, math.isqrt(n) + 1):
		if not is_prime[k]:
			continue
		not_prime = k * k
		while not_prime <= n:
			is_prime[not_prime] = False
			not_prime += k
	# convert buffer to list of ints
	primes = [i for i,p in enumerate(is_prime) if p]
	return primes
'''

def get_primes(n):
	'''
	Sieve of Eratosthenes with 2,3 wheel factorization.
	Returns primes less than n.
	About 3x faster than without wheel factorization.
	'''
	is_prime = [False, True, False, False, False, True] * ((n+5)//6) # faster than math.ceil(n/6)
	#is_prime = [False, False] + ([False, False, False, True, False, True] * ((n+5)//6))
	is_prime[1] = False
	is_prime[2] = True
	is_prime[3] = True
	while len(is_prime) > n: is_prime.pop()	# faster than slicing
	max_prime = int(n**0.5) # faster than math.isqrt
	gap = 2
	k = 5
	while k <= max_prime:
		if is_prime[k]:
			start, step = k*k, 2*k
			is_prime[start::step] = [False] * len(range(start, n, step)) # faster than assignment inside a while-loop
		k += gap
		gap = 6 - gap
	return [i for i,p in enumerate(is_prime) if p] # return a list since there's no memory savings from being a generator

def get_primes235(n):
	'''
	About twice as fast as 2,3 wheel factorized SoE.
	https://programmingpraxis.com/2012/01/06/pritchards-wheel-sieve/
	'''
	def primes(limit):
		'''Generator for primes at or below limit. Uses 2,3,5 wheel factorization.'''
		yield from (x for x in [2,3,5] if x <= limit)
		if limit < 7: return
		modPrms = [7,11,13,17,19,23,29,31]
		gaps = [4,2,4,2,4,6,2,6,4,2,4,2,4,6,2,6] # 2 loops for overflow
		ndxs = [0,0,0,0,1,1,2,2,2,2,3,3,4,4,4,4,5,5,5,5,5,5,6,6,7,7,7,7,7,7]
		lmtbf = (limit + 23) // 30 * 8 - 1 # integral number of wheels rounded up
		lmtsqrt = (int(limit ** 0.5) - 7)
		lmtsqrt = lmtsqrt // 30 * 8 + ndxs[lmtsqrt % 30] # round down on the wheel
		buf = [True] * (lmtbf + 1)
		for i in range(lmtsqrt + 1):
			if buf[i]:
				ci = i & 7; p = 30 * (i >> 3) + modPrms[ci]
				s, p8 = p * p - 7, p << 3
				for _ in range(8):
					c = s // 30 * 8 + ndxs[s % 30]
					buf[c::p8] = [False] * ((lmtbf - c) // p8 + 1)
					s += p * gaps[ci]; ci += 1
		for i in range(lmtbf - 6 + (ndxs[(limit - 7) % 30])): # adjust for extras
			if buf[i]: yield (30 * (i >> 3) + modPrms[i & 7])
	return list(primes(n-1))

def is_prime(n, primes = None):
	'''
	Primality test.

	primes must be sorted if supplied.
	'''
	if primes is None:
		return miller_rabin(n)
	else:
		for p in primes:
			if p*p > n:
				return True
			elif n%p == 0:
				return False
		raise ValueError

def miller_rabin(n):
	'''Miller-Rabin test for primality. Returns True if n is prime, else False.'''
	if n <= 1:
		return False
	if n == 2:
		return True
	# use minimum number of witnesses needed
	if n < 2047:
		witnesses = [2]
	elif n < 1373653:
		witnesses = [2, 3]
	elif n < 9080191:
		witnesses = [31, 73]
	elif n < 25326001:
		witnesses = [2, 3, 5]
	elif n < 3215031751:
		witnesses = [2, 3, 5, 7]
	elif n < 4759123141:
		witnesses = [2, 7, 61]
	elif n < 1122004669633:
		witnesses = [2, 13, 23, 1662803]
	elif n < 2152302898747:
		witnesses = [2, 3, 5, 7, 11]
	elif n < 3474749660383:
		witnesses = [2, 3, 5, 7, 11, 13]
	elif n < 341550071728321:
		witnesses = [2, 3, 5, 7, 11, 13, 17]
	elif n < 3825123056546413051:
		witnesses = [2, 3, 5, 7, 11, 13, 17, 19, 23]
	elif n < 18446744073709551616: # 2^64
		witnesses = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
	else:
		witnesses = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
	# write n as 2^r·d + 1 with d odd (by factoring out powers of 2 from n−1)
	r = 0
	d = n-1
	while not 1&d:
		r += 1
		d >>= 1
	# test for primality
	for a in witnesses:
		x = pow(a, d, n)
		if x == 1 or x == n-1:
			continue
		comp = True
		for _ in range(r-1):
			x = pow(x, 2, n)
			if x == n-1:
				# continue outer loop
				comp = False
				break
		if comp:
			return False # composite
	return True # prime

def is_prime_trial_division(n):
	if n < 3:
		if n == 2:
			return True
		if n == 1 or n == 0:
			return False
		return is_prime(-n)
	elif n%2 == 0:
		return False
	else:
		k = 3
		while k*k <= n:
			if n%k == 0:
				return False
			else:
				k += 2
		return True

# does not include 1, or n unless n is prime or 1
# factor(0) = [0]
# factor(1) = [1]
# factor(5) = [5]
# factor(8) = [2,2,2]
def factor(n, primes = None):
	if n == 0 or n == 1:
		return [n]
	# trial division
	if primes == None:
		factors = []
		while not n&1:
			factors.append(2)
			n >>= 1
		f = 3
		while f*f <= n:
			if n % f == 0:
				factors.append(f)
				n //= f
			else:
				f += 2
		if n != 1:
			factors.append(n)
		return factors
	# test each prime
	else:
		factors = []
		for p in primes:
			if p*p > n:
				break
			while n%p == 0:
				factors.append(p)
				n //= p
			if n == 1:
				return factors
		factors.append(n)
		return factors

def rho(n, c=1):
	'''
	Pollard's Rho algorithm for integer factorization. Returns a factor >1 of n (possibly n itself, even if n is composite).
	Expected running time is proportional to the square root of the size of the smallest prime factor of n.
	This is a quick, but probabilistic, algorithm that often fails on even numbers and numbers with square factors. On failure, it's best to retry after incrementing the constant in the g function.
	See https://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm for more details.
	'''
	if n < 2:
		raise ValueError(f"must be greater than 1: {n=}")
	x = 2
	y = 2
	d = 1
	g = lambda x: (x*x + c) % n
	while d == 1:
		x = g(x)
		y = g(g(y))
		d, _, _ = math.gcd(abs(x-y), n)
	return d # d is a factor

def divisors_from_factors(fac):
	d = {1}
	for f in fac:
		d |= {f*f2 for f2 in d}
	return d

# a number 'a' is a divisor of n if there exists a nonzero number 'b' such that a*b = n
# includes all divisors, including 1 and n
def divisors(n, primes = None):
	#if n == 0:
	#	return None
	if n <= 0:
		raise ValueError(f"must be positive: {n=}")
	return divisors_from_factors(factor(n, primes))

def count_divisors_from_factors(fac):
	count = {}
	for f in fac:
		try:
			count[f] += 1
		except KeyError:
			count[f] = 1
	return math.prod(v+1 for v in count.values())

def count_divisors(n, primes = None):
	if n <= 0:
		raise ValueError(f"must be positive: {n=}")
	if n in [0,1]:
		return n
	return count_divisors_from_factors(factor(n, primes))

def totient(n, primes = None):
	'''Calculate the Euler totient -- how many numbers < n are coprime with n.'''
	if n in [0,1]:
		return n
	f = set(factor(n, primes))
	for p in f:
		n *= (1 - 1/p)
	return int(n)

class FactorRange:
	'''Finds primes and prime factorizations for all numbers less than N.'''
	def __init__(self, N):
		lp = [0]*N # lowest prime that divides each index
		pr = [] # primes
		for i in range(2, N):
			if lp[i] == 0:
				# lp[i] = 0 means that no number before i is a divisor of i, so i is a prime number
				lp[i] = i
				pr.append(i)
			# consider all the numbers x = i*pr[j]. If  pr[j] <= lp[i], then the least divisor of x is pr[j]
			j = 0
			while j < len(pr) and i*pr[j] < N and pr[j] <= lp[i]:
				lp[i*pr[j]] = pr[j]
				j += 1
		self.lp = lp
		self.primes = pr
	def factor(self, n):
		'''
		Returns the factors of a number in ascending order.
		Does not include 1. Includes n only if n is prime.
		'''
		f = []
		while n > 1:
			p = self.lp[n]
			f.append(p)
			n //= p
		return f
	def factor_all(self):
		return list(self.factors())
	def factors(self):
		for n in range(len(self)):
			yield (n, self.factor(n))
	def __len__(self):
		return len(self.lp)
	def __getitem__(self, n):
		return self.factor(n)


#########################################################################################
# simple math

# https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Pseudocode
def extended_gcd(a, b):
	s, old_s = 0, 1
	t, old_t = 1, 0
	r, old_r = b, a
	while r != 0:
		quotient = old_r // r
		old_r, r = r, (old_r - quotient * r)
		old_s, s = s, (old_s - quotient * s)
		old_t, t = t, (old_t - quotient * t)
	return old_r, old_s, old_t # gcd, Bezout coefficients

def mod_inverse(n, mod):
	'''Calculate the modular inverse for a number.'''
	_, inv, _ = extended_gcd(n, mod)
	return inv % mod

# see https://cp-algorithms.com/algebra/module-inverse.html for derivation
# start with m%i = m - floor(m/i)*i
def mod_inverse_range(n, mod):
	'''Calculate the modular inverse for a range of numbers 0 to n-1.'''
	if n >= mod:
		raise ValueError(f"Modulus must be greater than range: {n=}, {mod=}")
	inv = [0] * n
	inv[0] = None
	inv[1] = 1
	for i in range(2, n):
		q, r = divmod(mod, i)
		inv[i] = -q*inv[r] % mod
	return inv

# see https://cp-algorithms.com/algebra/module-inverse.html for derivation
def mod_inverse_arr(arr, mod):
	'''Calculate the modular inverse for a list of numbers.'''
	# calc prefix products
	inv = [0] * len(arr)
	c = 1
	for i in range(len(arr)):
		inv[i] = c
		c = c * arr[i] % mod
	# inverse of the product of all nums
	c = pow(inv[-1]*arr[-1], -1, mod)
	# calc suffix products
	for i in range(len(arr)-1, -1, -1):
		inv[i] = c * inv[i] % mod
		c = c * arr[i] % mod
	return inv

def partitions(n, sample=None, _i=0, _parts=None):
	'''
	Generate partitions of integer n. WARNING: do not edit yielded lists.
	
	n 		= int to partition
	sample	= values that the parts can take
	'''
	if sample is None:
		sample = list(range(1, n+1))
	if _parts is None:
		_parts = []
	if n == 0:
		yield _parts.copy()
	for i in range(_i, len(sample)):
		p = sample[i]
		if p > n:
			break
		_parts.append(p)
		yield from partitions(n-p, sample, i, _parts)
		del _parts[-1]

def base(n, b):
	'''Convert from base 10 to base b.'''
	if n == 0:
		return [0]
	digits = []
	while n:
		digits.append(n % b)
		n //= b
	return digits[::-1]

def range_length(start, end, step):
	'''Calculate the length of a range.'''
	return (end - start - 1) // step + 1

def pandigital_09(num):
	return len(set(str(num))) == 10

def pandigital_19(num):
	num = set(str(num))
	return "0" not in num and len(num) == 9

def concat(x, y):
	#return int(str(x)+str(y))
	c = 10
	while c <= y:
		c *= 10
	return c*x + y

# use math module equivalents (or the builtin pow())
'''
def factorial(n):
	return math.prod(k for k in range(2, n+1))

def choose(a, b):
	if b > (a-b):
		b = a-b
	prod = 1
	for x in range(a, a-b, -1):
		prod *= x
	for x in range(b, 1, -1):
		prod //= x
	return prod

def mod_pow(base, exp, mod):
	if exp == 0:
		if base == 0:
			raise ValueError("0^0")
		return 1
	elif exp == 1:
		return base
	elif exp % 2 == 0:
		tmp = mod_pow(base, exp//2, mod)
		return (tmp * tmp) % mod
	else:
		tmp = mod_pow(base, exp - 1, mod)
		return (base * tmp) % mod

# see https://math.stackexchange.com/questions/495119/what-is-gcd0-0
def gcd(a, b):
	while a != 0 and b != 0:
		if a > b:
			a %= b
		else:
			b %= a
	if a == 0:
		return b
	else:
		return a

def lcm(a, b):
	if a == 0 or b == 0:
		return 0
	return a * b // gcd(a, b)
'''


# not as fast as I expected
'''
def is_square(n):
	# Trivial checks
	if not isinstance(n, int):
		if n % 1 != 0:
			return False
		else:
			n = int(n)
	if n < 0:
		return False
	if n == 0:
		return True

	# Reduction by powers of 4 with bit-logic
	while n & 3 == 0:
		n >>= 2
	# All perfect squares, in binary, end in 001, when powers of 4 are factored out.
	if n & 7 != 1:
		return False
	if n == 1:
		return True  # is power of 4, or even power of 2

	# Simple modulo equivalency test
	c = n % 10
	if c in {3, 7}:
		return False  # Not 1,4,5,6,9 in mod 10
	if n % 7 in {3, 5, 6}:
		return False  # Not 1,2,4 mod 7
	if n % 9 in {2,3,5,6,8}:
		return False
	if n % 13 in {2,5,6,7,8,11}:
		return False

	# Other patterns
	if c == 5:  # if it ends in a 5
		if (n//10)%10 != 2:
			return False	# then it must end in 25
		if (n//100)%10 not in {0,2,6}:
			return False	# and in 025, 225, or 625
		if (n//100)%10 == 6:
			if (n//1000)%10 not in {0,5}:
				return False	# 0625 or 5625
	else:
		if (n//10)%4 != 0:
			return False	## (4k)*10 + (1,9)

	# Babylonian Algorithm. Find the integer square root.
	s = (len(str(n))-1) // 2
	x = (10**s) * 4
	A = {x, n}
	while x * x != n:
		x = (x + (n // x)) >> 1
		if x in A:
			return False
		A.add(x)
	return True
'''
