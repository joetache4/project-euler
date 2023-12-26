'''
Joe Walter

difficulty: 5%
run time:   0:00
answer:     7652413

	***

041 Pandigital Prime

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''

from bisect import bisect
from lib.num import get_primes

# No 8- or 9-digit pandigital primes exist -- they fail divisibility-by-3 rule
max_val = 7654321

primes = get_primes(max_val+1)

def pandigital(num):
	arr = [int(x) for x in str(num)]
	for k in range(1, len(arr)+1):
		if k not in arr:
			return False
	return True

def prime(n):
	i = bisect(primes, n)
	return primes[i-1] == n

for i in range(max_val, 1, -1):
	if prime(i) and pandigital(i):
		print(i)
		break
