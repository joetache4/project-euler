'''
Joe Walter

difficulty: 5%
run time:   0:20
answer:     40730

	***

034 Digit Factorials

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

	***

Observations

After 1999999, numbers n are too large to be expressed as sum_fact_digits(n)
'''

max = 19_999_999

f = {'0':1, '1':1, '2':2, '3':6, '4':24, '5':120, '6':720, '7':5040, '8':40320, '9':362880} # faster than a list

def sum_fact_digits(n):
	return sum(f[d] for d in str(n))

def solve():
	ans = 0
	for n in range(10, max):
		if n == sum_fact_digits(n):
			ans += n
	return ans

print(solve())
