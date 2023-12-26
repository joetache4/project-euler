'''
Joe Walter

difficulty: 20%
run time:   0:00
answer:     250591.442792

	***

838 Not Coprime

Let f(N) be the smallest positive integer that is not coprime to any positive integer n<=N whose least significant digit is 3.

For example f(40) equals to 897 = 3*13*23 since it is not coprime to any of 3,13,23,33. By taking the natural logarithm (log to base e) we obtain ln f(40) = ln897 ~ 6.799056 when rounded to six digits after the decimal point.

You are also given ln f(2800) ~ 715.019337.

Find f(10^6). Enter its natural logarithm rounded to six digits after the decimal point.

	***

Observations

"Not Coprime" means the m=f(N) shares at least one prime factor with each positive integer n<=N whose ones significant digit is 3

"d-prime" = prime ending in digit d
"m covers n" = m shares a prime factor with n

Can disregard n with prime factors ending in 1. Dropping the 1-prime will still yield a product ending in 3. Covering these smaller numbers will cover the larger ones.

Fully covering n requires m being the product of the following.
1. 3-primes <= N
2. 7-primes such that cubes are <= N
3. minimum-product subset of 7-primes and a 9-primes that cover remaining n

All numbers ending in 3 must be covered by at least one of the above.
'''


from math import prod, log
from lib.num import get_primes

def logsum(arr):
	return sum(log(n) for n in arr)

def f(N):
	nums = [n for n in [7, 17, 37, 47, 67, 97, 107] if n*n*n <= N] # these to the third power end in 3
	p7   = [] # primes ending in 7 that can multiply with a p9 to an n<N
	p9   = []
	for p in get_primes(N+1):
		d = p%10
		if d == 3:
			nums.append(p)
		elif d == 7 and p*19 <= N and p not in nums:
			p7.append(p)
		elif d == 9 and p*7 <= N:
			p9.append(p)

	num2 = p7+p9
	if len(p7) >= 2 and len(p9) >= 2:
		i, j = 1, len(p7)-1
		while j > 0 and i < len(p9):
			while j > 0 and p7[j-1]*p9[i] > N:
				j -= 1
			if p7[j]*p9[i-1] <= N:
				num2 = min(num2, p7[:j]+p9[:i], key=logsum)
			i += 1

	return f"{logsum(nums+num2):.6f}"


assert f(40)   == "6.799056"
assert f(2800) == "715.019337"

print(f(10**6))
