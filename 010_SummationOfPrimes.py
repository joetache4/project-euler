'''
Joe Walter

difficulty: 5%
run time:   0:00
answer:     142913828922

	***

010 Summation Of Primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

from lib.num import get_primes

print(sum(get_primes(2*10**6)))
