'''
Joe Walter

difficulty: 10%
run time:   0:01
answer:     471745499

	***

788 Dominating Numbers

A dominating number is a positive integer that has more than half of its digits equal.

For example, 2022 is a dominating number because three of its four digits are equal to 2. But 2022 is not a dominating number.

Let D(N) be how many dominating numbers are less than 10^N. For example, D(4)=603 and D(10)=21893256.

Find D(2022). Give your answer modulo 1000000007.

	***

Observations

The number of numbers of length n where at least one digit d is repeated m>n/2 times is 9*choose(n,m)*9^(n-m).

Proof:

For an n-digit number, there are choose(n,m) ways to "place" m repetitions of d.

Case 1. The number starts with d (e.g., ddXdXXddd). Then there are 9 choices for d (1-9) and 9^(n-m) choices for all X's (because each X != d).

Case 2. The number does not start with d (e.g., XXdddddX). Then there are 10 choices for d (0-9). If d is positive, then there are 8 choices the frst X and 9 for the others (because the first X cannot be 0 or d, the others can't be d). If d is 0, then there are 9 choices for each X. 9*8*9^(n-m-1) + 1*9^(n-m) = 9*9^(n-m)

When m > n/2, all digits other than d must have repetitions less than m. This means that no numbers are double-counted. ☐

This is the basis for the main loop:

choose(n+1,m)*9^(n+1-m) = 9*choose(n,m)*9^(n-m) + choose(n,m-1)*9^(n-(m-1))

(This is essentially saying that tacking on an X increases the amount by 9x (9 choices for X), while tacking on a d increases the amount by 1x)

Proof:

choose(n+1,m) = choose(n,m) + choose(n,m-1)		(a common identity, and since m>n/2>0)
'''

import numpy as np

def D(N, M = 1000000007):
	# row = total number of digits
	# col = number of digits that are equal
	a = np.zeros((N,N+1), dtype=np.uint64)
	a[0][:2] = [9,1]
	for i in range(1,N):
		a[i] = 	np.mod(
					9*a[i-1] + np.roll(a[i-1],1), # np.roll used to shift right
				M)
	for i in range(N):
		a[i][:(i+1)//2+1] = 0
	return 9*int(a.sum()) % M

assert D(4) == 603
assert D(10) == 21893256

print(D(2022))
