'''
Joe Walter

difficulty: 20%
run time:   2:35
answer:     4921370551019052

	***

804 Counting Binary Quadratic Representations

Let g(n) denote the number of ways a positive integer n can be represented in the form: x^2 + xy + 41y^2 where x and y are integers. For example, g(53) = 4 due to (x,y) in {(-4,1),(-3,-1),(3,1),(4,-1)}.

Define T(N) = sum(g(n) for n in 1 to N). You are given T(10^3) = 474 and T(10^6) = 492128.

Find T(10^16).
'''

def f(x, y):
	return x*x + x*y + 41*y*y

def T(N):
	ans = 0

	x = 1
	y_hi = 0
	y_lo = 0

	while f(x, y_hi+1) <= N:
		y_hi += 1
	while f(x, y_lo-1) <= N:
		y_lo -= 1

	while y_hi >= y_lo:
		ans += y_hi - y_lo + 1
		x += 1
		while f(x, y_hi+1) <= N:
			y_hi += 1
		while f(x, y_hi) > N:
			y_hi -= 1
			if y_hi < y_lo:
				break
		while f(x, y_lo-1) <= N:
			y_lo -= 1
		while f(x, y_lo) > N:
			y_lo += 1
			if y_hi < y_lo:
				break
	
	ans *= 2

	x = 0
	y_hi = 1
	y_lo = -1

	while f(x, y_hi+1) <= N:
		y_hi += 1
	while f(x, y_lo-1) <= N:
		y_lo -= 1

	ans += y_hi - y_lo # (0,0) should not be included

	return ans

assert T(10**3) == 474
assert T(10**6) == 492128

print(T(10**16))
