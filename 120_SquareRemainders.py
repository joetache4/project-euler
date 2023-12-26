'''
Joe Walter

difficulty: 25%
run time:   0:00
answer:     333082500

	***

120 Square Remainders

Let r be the remainder when (a−1)^n + (a+1)^n is divided by a^2.

For example, if a = 7 and n = 3, then r = 42: 6^3 + 8^3 = 728 ≡ 42 mod 49. And as n varies, so too will r, but for a = 7 it turns out that r_max = 42.

For 3 ≤ a ≤ 1000, find ∑ r_max.
'''
def r_max(a):
	n = 1
	m = -1
	while True:
		r = (2*a*n) % (a*a)
		m = max(m, r)
		n += 1
		if r == 0:
			break
	return m

print(sum(r_max(a) for a in range(3, 1001)))
