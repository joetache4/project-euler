'''
Joe Walter

difficulty: 45%
run time:   0:00
answer:     1.710637717

	***

197 Investigating The Behaviour Of A Recursively Defined Sequence

Given is the function f(x) = floor(230.403243784-x^2) × 10^-9,
the sequence un is defined by u_0 = -1 and u_n+1 = f(u_n).

Find un + u_n+1 for n = 10^12.

Give your answer with 9 digits after the decimal point.
'''

u, v = -1, None

# the sequence appears to repeat after fewer than 1000 iterations
for _ in range(1000):
	v, u = u, int(2**(30.403243784-u*u))*10**(-9)

print(f"{u+v:0.9f}")
