'''
Joe Walter

difficulty: 5%
run time:   0:00
answer:     25164150

	***

006 Sum Square Difference

The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

def solve(n):
	square_of_sum  = (n*(n+1)//2)**2
	sum_of_squares = sum(n*n for n in range(1, n+1))
	return square_of_sum - sum_of_squares

assert solve(10) == 2640

print(solve(100))
