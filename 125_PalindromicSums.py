'''
Joe Walter

difficulty: 25%
run time:   0:00
answer:     2906969179

	***

125 Palindromic Sums

The palindromic number 595 is interesting because it can be written as the sum of consecutive squares: 6^2 + 7^2 + 8^2 + 9^2 + 10^2 + 11^2 + 12^2.

There are exactly eleven palindromes below one-thousand that can be written as consecutive square sums, and the sum of these palindromes is 4164. Note that 1 = 0^2 + 1^2 has not been included as this problem is concerned with the squares of positive integers.

Find the sum of all the numbers less than 10^8 that are both palindromic and can be written as the sum of consecutive squares.
'''

from math import ceil, sqrt

def is_pal(n):
	s = str(n)
	return s == s[::-1]

def solve(M):
	squares = [n*n for n in range(1, ceil(sqrt(M)))]
	ps      = set()

	for i in range(len(squares)-1):
		partial = squares[i]
		for j in range(i+1, len(squares)):
			partial += squares[j]
			if partial >= M:
				break
			if is_pal(partial):
				ps.add(partial)

	return sum(ps)

assert solve(10**3) == 4164

print(solve(10**8))
