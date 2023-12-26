'''
Joe Walter

difficulty: 35%
run time:   0:00
answer:     95962097

	***

188 The Hyperexponentiation of a Number

The hyperexponentiation or tetration of a number a by a positive integer b, denoted by a↑↑b or ba, is recursively defined by:

a↑↑1 = a,
a↑↑(k+1) = a(a↑↑k).

Thus we have e.g. 3↑↑2 = 3^3 = 27, hence 3↑↑3 = 3^27 = 7625597484987 and 3↑↑4 is roughly 103.6383346400240996*10^12.

Find the last 8 digits of 1777↑↑1855.
'''

from lib.num import totient

# only guaranteed to work if a and m are coprime
def tet(a, b, m):
	if m == 1 or b == 0:
		return 1
	else:
		return pow(a, tet(a, b-1, totient(m)), m) # Euler's Theorem

assert tet(3, 3, 10**8) == 97484987

print(tet(1777, 1855, 10**8))
