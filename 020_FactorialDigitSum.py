'''
Joe Walter

difficulty: 5%
run time:   0:00
answer:     648

	***

020 Factorial Digit Sum

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

from math import perm

def solve(n):
	num = perm(n)
	sum = 0
	for d in str(num):
		sum += int(d)
	return sum

assert solve(10) == 27

print(solve(100))
