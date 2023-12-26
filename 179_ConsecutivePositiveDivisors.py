'''
Joe Walter

difficulty: 25%
run time:   0:16
answer:     986262

	***

179 Consecutive Positive Divisors

Find the number of integers 1 < n < 10^7, for which n and n + 1 have the same number of positive divisors. For example, 14 has the positive divisors 1, 2, 7, 14 while 15 has 1, 3, 5, 15.
'''

n = 10**7

def count_divisors(n):
	div = [1 for x in range(n+1)]
	div[0] = 0
	for d in range(2, n+1):
		for q in range(d, n+1, d):
			div[q] += 1
	return div

div = count_divisors(n)
ans = sum(1 for i in range(n) if div[i] == div[i+1])
print(ans)
