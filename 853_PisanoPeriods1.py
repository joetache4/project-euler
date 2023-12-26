'''
Joe Walter

difficulty: 5%
run time:   0:00
answer:     44511058204

	***

853 Pisano Periods 1

For every positive integer n the Fibonacci sequence modulo n is periodic. The period depends on the value of n. This period is called the Pisano period for n, often shortened to pi(n).

There are three values of n for which pi(n) equals 18: 19, 38 and 76. The sum of those smaller than 50 is 57.

Find the sum of the values of n smaller than 1000000000 for which pi(n) equals 120.
'''

from lib.sequences import fibonacci
from lib.num import divisors
from itertools import islice

def p853(N, M):
	F   = list(islice(fibonacci(), N+2))
	dFN = list(divisors(F[N]))
	dN  = list(divisors(N))
	dN.remove(N)
	ans = 0
	for n in dFN:
		if n >= M:
			continue
		if F[N+1]%n != 1:
			continue
		if any(F[d]%n==0 and F[d+1]%n==1 for d in dN):
			continue
		ans += n
	return ans

assert p853(18, 50) == 57

print(p853(120, 10**9))
