'''
Joe Walter

difficulty: 30%
run time:   0:01
answer:     2944730

	***

204 Generalized Hamming Numbers

A Hamming number is a positive number which has no prime factor larger than 5.
So the first few Hamming numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15.
There are 1105 Hamming numbers not exceeding 10^8.

We will call a positive number a generalised Hamming number of type n, if it has no prime factor larger than n.
Hence the Hamming numbers are the generalised Hamming numbers of type 5.

How many generalised Hamming numbers of type 100 are there which don't exceed 10^9?
'''

from lib.num import get_primes

def count(max, type, _num = 1, _index = 0, _primes = None):
	if _primes is None:
		_primes  = get_primes(type)
	_count = 1
	for i in range(_index, len(_primes)):
		n = _num * _primes[i]
		if n > max:
			break
		_count += count(max, type, n, i, _primes)
	return _count

assert count(10**8, 6) == 1105

print(count(10**9, 100))
