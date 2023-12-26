'''
Joe Walter

difficulty: 40%
run time:
answer:     1677366278943

	***

214 Totient Chains

Let φ be Euler's totient function, i.e. for a natural number n, φ(n) is the number of k, 1 ≤ k ≤ n, for which gcd(k,n) = 1.

By iterating φ, each positive integer generates a decreasing chain of numbers ending in 1.
E.g. if we start with 5 the sequence 5,4,2,1 is generated.
Here is a listing of all chains with length 4:
5,4,2,1
7,6,2,1
8,4,2,1
9,6,2,1
10,4,2,1
12,4,2,1
14,6,2,1
18,6,2,1

Only two of these chains start with a prime, their sum is 12.

What is the sum of all primes less than 40000000 which generate a chain of length 25?
'''

from lib.num import get_primes

def totient_range(n):
	t = [1]*(n+1)
	t[0] = 0
	for i in range(2, n+1):
		if t[i] > 1:
			continue
		pk = 1
		while True:
			pk *= i
			if pk > n:
				break
			m = i-1 if pk == i else i
			for j in range(pk, n+1, pk):
				t[j] *= m
	return t

# slower, need to cast float->int too
'''
def totient_range2(n):
	t = list(range(n+1))
	for i in range(2, n+1):
		if t[i] == i:
			v = 1-1/i
			for j in range(i, n+1, i):
				t[j] *= v
	return t
'''

def solve(n, L):
	t = totient_range(n)
	for i in range(2, len(t)):
		t[i] = t[t[i]]+1
	return sum(p for p in get_primes(n) if t[p] == L)

assert solve(18, 4) == 12

print(solve(40*10**6, 25))
