'''
Joe Walter

difficulty: 45%
run time:   0:12
answer:     378158756814587

	***

164 Numbers for which no three consecutive digits have a sum greater than a given value

How many 20 digit numbers n (without any leading zero) exist such that no three consecutive digits of n have a sum greater than 9?
'''

import numpy as np

def digit_sum(n):
	return sum(int(d) for d in n)

B = np.zeros((1000,1000), dtype=np.int64)
for a in range(1000):
	for b in range(1000):
		c = str(a).zfill(3) + str(b).zfill(3)
		if all(digit_sum(c[i:i+3]) <= 9 for i in range(4)):
			B[a][b] = 1

A = B.copy()
A[0:10,] = 0
A[100:1000,] = 0

ans = A.dot(np.linalg.matrix_power(B,5)).sum()
print(ans)
