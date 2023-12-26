'''
Joe Walter

difficulty: 45%
run time:   0:00
answer:     48861552

	***

183 Maximum Product of Parts

Let N be a positive integer and let N be split into k equal parts, r = N/k, so that N = r + r + ... + r.
Let P be the product of these parts, P = r × r × ... × r = r^k.

For example, if 11 is split into five equal parts, 11 = 2.2 + 2.2 + 2.2 + 2.2 + 2.2, then P = 2.25 = 51.53632.

Let M(N) = Pmax for a given value of N.

It turns out that the maximum for N = 11 is found by splitting eleven into four equal parts which leads to Pmax = (11/4)^4; that is, M(11) = 14641/256 = 57.19140625, which is a terminating decimal.

However, for N = 8 the maximum is achieved by splitting it into three equal parts, so M(8) = 512/27, which is a non-terminating decimal.

Let D(N) = N if M(N) is a non-terminating decimal and D(N) = -N if M(N) is a terminating decimal.

For example, ∑D(N) for 5 ≤ N ≤ 100 is 2438.

Find ∑D(N) for 5 ≤ N ≤ 10000.

	***

Observations

d/dx((N/k)^k)=0 -> ln(N/k)=1 -> k=N/e
(N/k)^k is a terminating decimal iff. N/k is a terminating decimal.
N/k (in lowest terms) is terminating iff. k has no prime factors other than 2 or 5.
'''

from math import e, floor, ceil, log, gcd
from lib.num import factor, get_primes

primes = get_primes(10001)

def D(N):
	k = N/e
	#k = round(k) # works, but the following seems easier to prove correct
	k = max(floor(k), ceil(k), key=lambda x: x*log(N/x))
	d = k//gcd(N,k)
	f = factor(d, primes) # factor(1)=[1]
	if len(set(f)-{1,2,5}) == 0:
		return -N
	else:
		return N

def solve(M):
	return sum(D(N) for N in range(5, M+1))

assert solve(100) == 2438

print(solve(10000))
