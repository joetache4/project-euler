'''
Joe Walter

difficulty: 20%
run time:   0:00
answer:     501985601490518144

	***

704 Factors Of Two In Binomial Coefficients

Define g(n,m) to be the largest integer k such that 2^k divides (n m). For example (12 5) = 792 = 2^3*3^2*11, hence g(12, 5) = 3. Then define F(n) = max{g(n,m): 0 <= m <= n}. F(10) = 3 and F(100) = 6.

Let S(N) = sum(F(n), n=1 to N). You are given that S(100) = 389 and S(10^7) = 203222840.

Find S(10^16).
'''

from math import comb

# Shows a pattern in F
'''
def g(n, m):
	n = comb(n, m)
	a = 0
	while n & 1 == 0:
		a += 1
		n >>= 1
	return a

for n in range(100+1):
	f = 0
	for m in range(n):
		f = max(c, g(n,m))
	print(f"{n}: {'    ' if n%2==1 else ''} {f}")

input()
'''

def partial(pow, pct = 1.0):
	'''
	Find the partial sum of F(n) where n is between [2**pow, 2**(pow+1)-1]. If pct is supplied, this function will look at just the first pct x 100% terms in the range.
	'''
	if pow == 0:
		return 0
	mult = 2**(pow-1) * (pct + 1/(2**pow))
	return int(mult) * pow + partial(pow-1, pct)

def S(n):
	ans = 0
	for pow in range(1,999):
		lo = 2**pow
		hi = 2*lo-1
		if n < lo:
			break
		pct = (n-lo+1)/(hi-lo+1)
		pct = min(pct, 1.0)
		ans += partial(pow, pct)
	return ans

assert S(100) == 389
assert S(10**7) == 203222840

print(S(10**16))
