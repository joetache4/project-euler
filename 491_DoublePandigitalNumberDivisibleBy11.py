'''
Joe Walter

difficulty: 20%
run time:   0:00
answer:     194505988824000

	***

491 Double Pandigital Number Divisible by 11

We call a positive integer double pandigital if it uses all the digits 0 to 9 exactly twice (with no leading zero). For example, 40561817703823564929 is one such number.

How many double pandigital numbers are divisible by 11?

	***

Consider n = 40561817703823564929
             abababababababababab

abs(a-sum - b-sum) % 11 == 0 <-> n % 11 == 0	(divisibility rule for 11)
a-sum + b-sum = 90								(double pandigital)
abs(2*a-sum - 90) % 11 == 0 <-> n % 11 == 0
'''

from itertools import combinations
from collections import Counter
from math import prod, factorial

def visited(x, _mem=set()):
	x = tuple(sorted(x))
	if x in _mem:
		return True
	_mem.add(x)
	return False

def subtract(x, y):
	x2 = list(x)
	for y2 in y:
		x2.remove(y2)
	return x2

def count_orderings(x):
	return factorial(len(x))//prod(factorial(v) for v in Counter(x).values())

D   = list(range(10))*2
ans = 0
for a in combinations(D, 10):
	if abs(2*sum(a)-90) % 11 == 0 and not visited(a):
		b = subtract(D, a)
		count_a = count_orderings(a)
		if 0 in a:
			# discount numbers with leading zeros
			count_a -= count_orderings(subtract(a, [0]))
		count_b = count_orderings(b)
		ans += count_a*count_b

print(ans)
