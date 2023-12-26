'''
Joe Walter

difficulty: 25%
run time:   0:18
answer:     54.12691621

	***

815 Group By Value

A pack of cards contains 4n cards with four identical cards of each value. The pack is shuffled and cards are dealt one at a time and placed in piles of equal value. If the card has the same value as any pile it is placed in that pile. If there is no pile of that value then it begins a new pile. When a pile has four cards of the same value it is removed.

Throughout the process the maximum number of non empty piles is recorded. Let E(n) be its expected value. You are given E(2) = 1.97142857 rounded to 8 decimal places.

Find E(60). Give your answer rounded to 8 digits after the decimal point. 
'''

from functools import cache

def E(n):
	@cache
	def _E(a=0, b=0, c=0, d=0, score=0, hiscore=0):
		if a+b+c+d == 0:
			return hiscore
		s = a + 2*b + 3*c + 4*d
		val = 0
		if a:
			val += 1*a/s*_E(a-1, b, c, d, score-1, hiscore)
		if b:
			val += 2*b/s*_E(a+1, b-1, c, d, score, hiscore)
		if c:
			val += 3*c/s*_E(a, b+1, c-1, d, score, hiscore)
		if d:
			val += 4*d/s*_E(a, b, c+1, d-1, score+1, max(score+1, hiscore))
		return val
	val = _E(d=n)
	val = f"{val:.8f}"
	return val

assert E(2) == "1.97142857"

print(E(60))
