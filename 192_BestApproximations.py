'''
Joe Walter

difficulty: 75%
run time:   0:48
answer:     57060635927998347

	***

192 Best Approximations

Let x be a real number.
A best approximation to x for the denominator bound d is a rational number r/s
in reduced form, with s<=d, such that any rational number which is closer to x than r/s has a denominator larger than d.

For example, the best approximation to sqrt(13) for the denominator bound 20 is
18/5 and the best approximation to sqrt(13) for the denominator bound 30 is 101/28.

Find the sum of all denominators of the best approximations to sqrt(n) for the denominator bound 10^12, where n is not a perfect square and 1<n<=100000.

	***

Solution Method

1. Generate continued fraction for sqrt(n) to an arbitrary length.
   https://stackoverflow.com/questions/12182701/generating-continued-fractions-for-square-roots
2. Use continued fraction to generate best rational approximations (convergents & semiconvergents).
   https://en.wikipedia.org/wiki/Continued_fraction#Best_rational_approximations
'''

from math import sqrt, isqrt, floor, pi, gcd, ceil

def sqrt_cf_generator(n):
	'''
	Generates continued fraction terms for sqrt of non-square n.

	See https://stackoverflow.com/questions/12182701/generating-continued-fractions-for-square-roots
	'''
	r = isqrt(n)
	#if r*r == n:
	#	raise Exception(f"perfect square: {n}")
	yield r
	a, p, q = r, 0, 1
	while True:
		p = a*q - p
		q = (n - p*p)//q
		a = (r + p)//q
		yield a
		# begins to repeat when q == 1

def convergent(f, _i = 0):
	'''Generate a (semi)convergent from the truncated continued fraction.'''
	if _i == len(f)-1:
		n, d = f[_i], 1
	else:
		n, d = convergent(f, _i+1)
		n, d = n*f[_i]+d, n
	return (n, d)

def best_sqrt_approx(n, denom_bound):
	r        = sqrt(n)
	cf       = sqrt_cf_generator(n)
	a        = next(cf)
	cf_trunc = [a]
	best     = (a, 1)
	while True:
		a = next(cf)
		cf_trunc.append(None)
		for i in range(ceil(a/2), a+1):
			cf_trunc[-1] = i
			conv = convergent(cf_trunc)
			if conv[1] > denom_bound:
				return best
			if 2*i == a:
				w = conv[0]**2
				x = conv[1]**2
				y = best[0]**2
				z = best[1]**2
				#if abs(conv[0] / conv[1] - r) < abs(best[0] / best[1] - r):
				if abs(z*w-z*n*x) >= abs(x*y-z*x*n):
					continue
			best = conv
	raise Exception("Loop Error")

assert best_sqrt_approx(13, 20) == (18, 5)
assert best_sqrt_approx(13, 30) == (101, 28)

ans = 0
for n in range(2, 100001):
	if isqrt(n)**2 != n:
		ans += best_sqrt_approx(n, 10**12)[1]
print(ans)
