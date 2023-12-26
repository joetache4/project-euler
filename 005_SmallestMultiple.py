'''
Joe Walter

difficulty: 5%
run time:   0:00
answer:     232792560

	***

005 Smallest Multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

from functools import reduce
from lib.num import lcm

print(reduce(lcm, range(2, 20)))
