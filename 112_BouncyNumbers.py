'''
Joe Walter

difficulty: 15%
run time:   0:04
answer:     1587000

	***

112 Bouncy Numbers

Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%.
'''

def bouncy(n):
	if n < 100:
		return 0
	n = str(n)
	diff = [int(n[i]) - int(n[i+1]) for i in range(len(n)-1)]
	if min(diff) * max(diff) < 0:
		return 1
	else:
		return 0

def solve(p):
	n = 1
	b = 0
	while b != n*p:
		n += 1
		b += bouncy(n)
	return n

assert solve(0.5) == 538
assert solve(0.9) == 21780

print(solve(0.99))
