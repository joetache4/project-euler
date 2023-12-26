'''
Joe Walter

difficulty: 10%
run time:   1:07
answer:     94586478

	***

745 Sum Of Squares II

For a positive integer, n, define g(n) to be the maximum perfect square that divides n.

For example, g(18) = 9, g(19) = 1.

Also define S(N) = sum(g(n), n = 1 to N)

For example, S(10) = 24 and S(100) = 767.

Find S(10^14). Give your answer modulo 1000000007.
'''

from lib.num import get_primes

def square_free_count(n, primes2):
	'''Counts numbers without any square divisor.'''
	def square_count(n, primes2, sign=1, prod=1, start_ind=0):
		'''Counts numbers that are multiples of squares.'''
		sum = 0
		for i in range(start_ind, len(primes2)):
			new_prod = prod*primes2[i]
			if new_prod <= n:
				# Use the inclusion-exclusion principle to count all multiples of squares
				sum += sign*(n//new_prod)
				sum += square_count(n, primes2, -sign, new_prod, i+1)
			else:
				break
		return sum
	return n - square_count(n, primes2)

def solve(N):
	sqrtN = int(N**0.5)
	primes = get_primes(sqrtN+1)
	primes2 = [p*p for p in primes]
	squares = [a*a for a in range(1, sqrtN+1)]

	ans = 0
	for s in squares:
		# find how many square-free numbers <= N//s
		sf = square_free_count(N//s, primes2)
		ans += sf*s
	return ans % 1000000007

assert solve(10) == 24
assert solve(100) == 767

print(solve(10**14))
