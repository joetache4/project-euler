'''
Joe Walter

difficulty: 5%
run time:   1:32
answer:     128088830547982

	***

719 Number Splitting

We define an S-number to be a natural number, n, that is a perfect square and its square root can be obtained by splitting the decimal representation of n into 2 or more numbers then adding the numbers.

For example, 81 is an S-number because sqrt(81) = 8 + 1.
6724 is an S-number: sqrt(6724) = 6 + 72 + 4.

Further we define T(N) to be the sum of all S numbers n<=N. You are given T(10^4)=41333.

Find T(10^12).
'''

def digits_sum_to(n, sum_to, _mod=10):
	if n == sum_to:
		return True
	elif n < sum_to or n < _mod:
		return False
	return digits_sum_to(n//_mod, sum_to-(n%_mod), 10) or digits_sum_to(n, sum_to, _mod*10)

def T(N):
	return sum(x*x for x in range(2, int(N**0.5)+1) if digits_sum_to(x*x, x))

assert T(10**4) == 41333

print(T(10**12))



# run time: 8:15
'''
def split_sums(n, mem={}):
	if n < 10**6:
		try:
			return mem[n]
		except KeyError:
			pass

	ss = [n]
	if n >= 10:
		m = 10
		while m < n and m <= 10**6: # any higher and the square would be > n
			r = n % m
			l = split_sums(n // m)
			for s in l:
				ss.append(r + s)
			m *= 10

	if n < 10**6:
		mem[n] = ss

	return ss

def solve(N):
	ans = 0
	for x in range(2, int(N**0.5)+1):
		if any(s==x for s in split_sums(x*x)):
			ans += x*x
	return ans

assert solve(10**4) == 41333

print(solve(10**12))
'''
