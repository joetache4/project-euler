'''
Joe Walter

difficulty: 40%
run time:   0:00
answer:     44043947822

	***

207 Integer Partition Equations

For some positive integers k, there exists an integer partition of the form 4^t = 2^t + k,
where 4^t, 2^t, and k are all positive integers and t is a real number.

The first two such partitions are 4^1 = 2^1 + 2 and 4^1.5849625... = 2^1.5849625... + 6.

Partitions where t is also an integer are called perfect.
For any m ≥ 1 let P(m) be the proportion of such partitions that are perfect with k ≤ m.
Thus P(6) = 1/2.

In the following table are listed some values of P(m)

   P(5) = 1/1
   P(10) = 1/2
   P(15) = 2/3
   P(20) = 1/2
   P(25) = 1/2
   P(30) = 2/5
   ...
   P(180) = 1/4
   P(185) = 3/13

Find the smallest m for which P(m) < 1/12345
'''

from math import isqrt

def perfect_k(t):
	return 4**t - 2**t

def k(i):
	return i*(i+1)

def k_inv(k):
	return (isqrt(1+4*k)-1)//2

def solve(F):
	# i = number of perfect k's (k's that produce a perfect partition)
	# j = number of all k's
	for i in range(2, 999999):
		j = k_inv(perfect_k(i))
		if (i-1) / (j-1) < F:
			i -= 1
			j -= 1
			while i/j < F:
				j -= 1
			j += 1
			return k(j)

print(solve(1/12345))
