'''
Joe Walter

difficulty: 5%
run time:   0:00
answer:     5777

	***

046 Goldbachs Other Conjecture

Find the smallest odd composite number that cannot be written as the sum of a prime and twice a square.
'''

from itertools import count
from lib.num import is_prime

def representable(n):
	for s in count(1):
		s2 = 2*s*s
		if s2 >= n:
			return False
		if is_prime(n-s2):
			return True

for n in count(9, 2):
	if is_prime(n):
		continue
	if not representable(n):
		print(n)
		break
