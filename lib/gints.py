from random import randint

#########################################################################################
# Gaussian integers
# https://stackoverflow.com/questions/2269810/whats-a-nice-method-to-factor-gaussian-integers
# https://math.stackexchange.com/questions/1562858/gaussian-prime-factorization

def gaussian_remainder(a, b):
	r = a / b
	r = complex(round(r.real), round(r.imag))
	return a - r * b

def gaussian_gcd(a, b):
	r = gaussian_remainder(a, b)
	if r == complex(0,0):
		return b
	else:
		return gaussian_gcd(b, r)

def gaussian_factor_prime(p):
	if p == 2:
		return [complex(1,1), complex(1,-1)]
	elif p % 4 == 3:
		return [complex(p,0)] # irreducible
	else:
		k = None
		while True:
			k = randint(2, p-1)
			if (k**((p-1)//2)) % p == p - 1:
				k = k**((p-1)//4) % p
				break
		f = gaussian_gcd(complex(p,0), complex(k,1))
		return [f, f.conjugate()]

# TODO test this
def gaussian_factor(n, primes = None):
	if n.imag == 0:
		fac = []
		for p in factor(n, primes):
			for g in gaussian_factor_prime(p):
				fac.append(g)
		return fac

	else:
		n = n*n.conjugate()
		gfac = []
		skip = False
		for p in sorted(factor(n, primes)):
			if p == 2:
				q = complex(1,1)
			elif p % 4 == 3:
				if skip:
					skip = False
				else:
					q = complex(p,0) # irreducible and a factor of n
					skip = True	  # skip duplicate made by squaring
			else:
				k = None
				while True:
					a = randint(2, p-1)
					if (a**((p-1)//2)) % p == p - 1:
						k = a**((p-1)//4)
						break
				q = gaussian_gcd(complex(p,0), complex(k,1))
				if gaussian_remainder(n, q) != 0:
					q = q.conjugate()

			gfac.append(q)
			n /= q

		gfac[-1] = gfac[-1] * n # fix signs
		return gfac
