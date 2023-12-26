'''
Joe Walter

difficulty: 5%
run time:   0:00
answer:     233168

	***

001 Multiples Of 3 And 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

# one-liner but slow for large upper bounds
# print(sum(x for x in range(1000) if x%3 == 0 or x%5 == 0))

def sum_multiples(m, N = 1000):
	count = (N-1)//m
	return m*count*(count+1)//2

print(sum_multiples(3) + sum_multiples(5) - sum_multiples(15))
