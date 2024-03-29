'''
Joe Walter

difficulty: 5%
run time:   0:00
answer:     997651

	***

050 Consecutive Prime Sum

The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''

from lib.num import get_primes

n = 10**6

# Use a sliding window approach
# Work from a big window down to a small window and stop at the first solution
def solve(max_sum):
	# get primes
	primes = get_primes(max_sum+1)
	# find max window length
	max_window_len = 0
	tmp_sum = 0
	for x in primes:
		tmp_sum += x
		if tmp_sum <= max_sum:
			max_window_len += 1
	# start with the longest window
	for window_len in reversed(range(1, max_window_len+1)):
		# start with the smallest primes
		for start in range(len(primes) - window_len):
			test_sum = sum(primes[start:start + window_len])
			if test_sum > max_sum:
				# sliding the window right will only increase the sum
				break
			elif test_sum in primes:
				# first answer is THE answer
				# return (test_sum, window_len, primes[start])
				return test_sum

assert solve(100)  == 41
assert solve(1000) == 953

print(solve(n))
