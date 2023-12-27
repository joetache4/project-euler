'''
Joe Walter

difficulty: 45%
run time:   0:01
answer:     149253

	***

130 Composites with Prime Repunit Property

A number consisting entirely of ones is called a repunit. We shall define R(k) to be a repunit of length k; for example, R(6)=111111.

Given that n is a positive integer and gcd(n,10)=1, it can be shown that there always exists a value, k, for which R(k) is divisible by n, and let A(n) be the least such value of k; for example, A(7)=6 and A(41)=5.

You are given that for all primes, p>5, that p-1 is divisible by A(p). For example, when p=41, A(41)=5, and 40 is divisible by 5.

However, there are rare composite values for which this is also true; the first five examples being 91, 259, 451, 481, and 703.

Find the sum of the first twenty-five composite values of n for which gcd(n,10)=1 and n-1 is divisible by A(n).
'''

from lib.num import get_primes

primes = get_primes(10**6)

def A(n):
	m = k = 1
	while True:
		m = (10*m+1)%n
		k += 1
		if m == 0:
			return k

# TODO: for composite n, A(n)=lcm(A(p) for p in factor(n))

def p130():
	N = []
	for n in range(4,10**6):
		if n%2==0 or n%5==0 or n in primes:
			continue
		k = A(n)
		if (n-1)%k == 0:
			print(n)
			N.append(n)
			if len(N) == 25:
				return sum(N)

print(p130())
