'''
Joe Walter

difficulty: 45%
run time:   0:01
answer:     1000023

	***

129 Repunit Divisibility

A number consisting entirely of ones is called a repunit. We shall define R(k) to be a repunit of length k; for example, R(6)=111111.

Given that n is a positive integer and gcd(n,10)=1, it can be shown that there always exists a value, k, for which R(k) is divisible by n, and let A(n) be the least such value of k; for example, A(7)=6 and A(41)=5.

The least value of n for which A(n) first exceeds ten is 17.

Find the least value of n for which A(n) first exceeds one-million.
'''

from itertools import count

# A(n) < n
# So, the first A(n) > 10**6 will be for some n > 10**6

def p129():
	N = []
	for n in count(10**6+3):
		if n%2==0 or n%5==0:
			continue
		m = 0
		for k in count(1):
			m = (m+pow(10,k-1,n))%n
			if m == 0:
				print(f"A({n}) = {k}")
				if k > 10**6:
					return n
				break

print(p129())
