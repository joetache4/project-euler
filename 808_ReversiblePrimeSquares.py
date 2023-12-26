'''

Joe Walter

difficulty: 5%
run time:   0:00
answer:     3807504276997394

	***

808 Reversible Prime Squares

Both 169 and 961 are the square of a prime. 169 is the reverse of 961.

We call a number a reversible prime square if:

    1. It is not a palindrome, and
    2. It is the square of a prime, and
    3. Its reverse is also the square of a prime.

169 and 961 are not palindromes, so both are reversible prime squares.

Find the sum of the first 50 reversible prime squares.
'''

import heapq
from lib.num import is_prime, base

def push(heap, item, maxsize = 50):
	if len(heap) == maxsize:
		return heapq.heappushpop(heap, item) != item
	else:
		heapq.heappush(heap, item)
		return True

def base_4_odds():
	i = 1
	while True:
		yield int("".join(str(j) for j in base(i, 4)))
		i += 2

heap = []

for a in base_4_odds():
	b = int(str(a)[::-1])
	if a < b and str(a**2) == str(b**2)[::-1] and is_prime(a) and is_prime(b):
		x = push(heap, -a**2)
		y = push(heap, -b**2)
		if not x and not y:
			break

print(-sum(heap))
