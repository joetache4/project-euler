'''
Joe Walter

difficulty: 5%
run time:   0:00
answer:     104743

	***

007 10001st Prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
'''

from itertools import count
from lib.num import is_prime

n = 0
for p in count(2):
	if is_prime(p):
		n += 1
		if n == 10001:
			break

print(p)
