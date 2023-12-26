'''
Joe Walter

difficulty: 50%
run time:   0:00
answer:     178653872807

	***

169 Sums of Powers of Two

Define f(0)=1 and f(n) to be the number of different ways can be expressed as a sum of integer powers of 2 using each power no more than twice.

For example, f(10)=5 since there are five different ways to express 10:

	1+1+8
	1+1+4+4
	1+1+2+2+4
	2+4+4
	2+8

What is f(10**25)?
'''

from functools import cache
from itertools import groupby

# count runs of 0s in binary representation of n
# take care to count zero 0s between adjacent 1s
def zero_runs(n):
	b = f"{n:b}".replace("1","10")
	r = [len(list(g))-1 for _,g in groupby(b)][1::2]
	return r

# consider binary(n) as a list of integers
# count the ways you can subtract 1 from an entry
# and add 2 immediately to the right
# with the restriction that entries must be <= 2
def f(n):
	runs = zero_runs(n)
	@cache # not necessary
	def _f(i, extra):
		if i == 0:
			return 1 + runs[0]+extra
		return _f(i-1,0) + (runs[i]+extra)*_f(i-1,1)
	return _f(len(runs)-1,0)

assert f(10) == 5

print(f(10**25))
