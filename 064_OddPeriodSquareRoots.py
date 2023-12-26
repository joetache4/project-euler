'''
Joe Walter

difficulty: 20%
run time:   0:00
answer:     1322

	***

064 Odd Period Square Roots

How many continued fractions of sqrt(n) for n≤10000 have an odd period?
'''

# https://en.wikipedia.org/wiki/Periodic_continued_fraction#Canonical_form_and_repetend

from math import isqrt

def nonsquare(m):
	n = 2
	while n < m:
		if isqrt(n)**2 != n:
			yield n
		n += 1

def frac_len(n):
	m = [0]
	d = [1]
	a = [isqrt(n)]
	while True:
		m_new = d[-1]*a[-1] - m[-1]
		d_new = (n - m_new**2)//d[-1]
		a_new = (a[0] + m_new)//d_new
		m.append(m_new)
		d.append(d_new)
		a.append(a_new)
		if a_new == 2*a[0]:
			break
	return len(a) - 1

ans = sum( 1 for n in nonsquare(10001) if frac_len(n) % 2 == 1 )
print(ans)
