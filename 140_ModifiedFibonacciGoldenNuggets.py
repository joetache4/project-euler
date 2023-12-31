'''
Joe Walter

difficulty: 55%
run time:   0:00
answer:     5673835352990

	***

140 Modified Fibonacci Golden Nuggets

Consider the infinite polynomial series A_G(x) = x G_1 + x^2 G_2 + x^3 G_3 + ..., where G_k is the kth term of the second order recurrence relation G_k = G_{k-1} + G_{k-2}, G_1 = 1 and G_2 = 4; that is, 1, 4, 5, 9, 14, 23, ....

For this problem we shall be concerned with values of x for which A_G(x) is a positive integer.

The corresponding values of x for the first five natural numbers are shown below.

x					A_G(x)
(sqrt(5)-1)/4		1
2/5					2
(sqrt(22)-2)/6		3
(sqrt(137)-5)/14	4
1/2					5

We shall call A_G(x) a golden nugget if x is rational, because they become increasingly rarer; for example, the 20th golden nugget is 211345365.

Find the sum of the first thirty golden nuggets.
'''

def is_gn(a):
	k = (a+1)**2+4*a*(a+3)
	return int(k**0.5)**2 == k

# the ratio between consecutive golden nuggets alternates ~2 & ~4, approaches limits from above
'''
prev_a = 1
for a in range(1,100000):
	if is_gn(a):
		print((a, a/prev_a))
		prev_a = a
'''

r, ri = [5, 2], 0
gn    = [2, 5]
a     = 5

while len(gn) < 30:
	a = int(a*r[ri])
	while not is_gn(a):
		a -= 1
	r[ri], ri = a/gn[-1], (ri+1)%2
	gn.append(a)

assert gn[19] == 211345365

print(sum(gn))
