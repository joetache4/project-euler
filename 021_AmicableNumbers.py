'''
Joe Walter

difficulty: 5%
run time:   0:00
answer:     31626

	***

021 Amicable Numbers

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

from lib.num import divisors

N = 10000
D = [0]*N

def d(n):
	return sum(divisors(n))-n

for n in range(1,N):
	D[n] = d(n)

ans = 0
for n,m in enumerate(D):
	# assert m == D[n]
	try:
		if n != m and n == D[m]:
			ans += n
	except IndexError:
		pass

print(ans)
