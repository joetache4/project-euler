'''
Joe Walter

difficulty: 5%
run time:   0:00
answer:     9110846700

	***

048 Self Powers

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
'''

def solve(n, num_digits = 10):
	mod = 10**num_digits
	sum = 0
	for k in range(1, n+1):
		sum += pow(k, k, mod)
	return sum % mod

assert solve(10) == 405071317

print(solve(1000))
