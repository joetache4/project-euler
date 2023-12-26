'''
Joe Walter

difficulty: 5%
run time:   0:00
answer:     906609

	***

004 Largest Palindrome Product

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def palindrome(n):
	n = str(n)
	r = n[::-1]
	return n == r

print(max(a*b for a in range(100,1000) for b in range(100,1000) if palindrome(a*b)))
