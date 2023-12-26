'''
Joe Walter

difficulty: 10%
run time:   0:00
answer:     696067597313468

	***

387 Harshad Numbers

A Harshad or Niven number is a number that is divisible by the sum of its digits.
201 is a Harshad number because it is divisible by 3 (the sum of its digits.)
When we truncate the last digit from 201, we get 20, which is a Harshad number.
When we truncate the last digit from 20, we get 2, which is also a Harshad number.
Let's call a Harshad number that, while recursively truncating the last digit, always results in a Harshad number a right truncatable Harshad number.

Also:
201/3=67 which is prime.
Let's call a Harshad number that, when divided by the sum of its digits, results in a prime a strong Harshad number.

Now take the number 2011 which is prime.
When we truncate the last digit from it we get 201, a strong Harshad number that is also right truncatable.
Let's call such primes strong, right truncatable Harshad primes.

You are given that the sum of the strong, right truncatable Harshad primes less than 10000 is 90619.

Find the sum of the strong, right truncatable Harshad primes less than 10^14.
'''

from lib.num import is_prime

def append(a, b):
	return int(str(a)+str(b))

def digit_sum(a):
	return sum(int(d) for d in str(a))

def right_truncatable_harshad_nums(P, _base=""):
	if len(str(_base))+1 > P-1:
		return
	for i in range(10):
		try:
			base = append(_base, i)
			r = base % digit_sum(base)
			if r == 0:
				yield base
				yield from right_truncatable_harshad_nums(P, base)
		except ZeroDivisionError:
			pass

def solve(P):
	ans = 0
	for n in right_truncatable_harshad_nums(P):
		q = n // digit_sum(n)
		if is_prime(q):
			for d in [1,3,7,9]:
				p = append(n, d)
				if is_prime(p):
					ans += p
	return ans

assert solve(4) == 90619

print(solve(14))