'''
Joe Walter

difficulty: 10%
run time:   0:00
answer:     510510

	***

069 Totient Maximum

Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of numbers less than n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.

It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.

	***

Solution

Find the greatest number not exceeding 1000000 that is a product of consecutive primes starting with 2.
'''

from lib.num import get_primes

def solve(max_val):
	primes = get_primes(max_val)
	n = 1
	for p in primes:
		if n*p <= max_val:
			n *= p
		else:
			break
	return n

print(solve(10**6))


'''
def test(max_val):
	print("Testing...")
	ans_n = solve(max_val)
	ans_max = ans_n/totient(ans_n)

	test_max = -1
	test_n = -1
	#for n in range(max_val, ans_n-1, -1):
	for n in range(max_val, 1, -1):
		val = n/totient(n)
		if val > test_max:
			test_n = n
			test_max = val
			print("{}/φ({}) = {}...".format(test_n, test_n, test_n/totient(test_n)))
			assert test_max < ans_max + 0.0000000001
	assert test_n == ans_n
	print("[SUCCESS]")
'''
