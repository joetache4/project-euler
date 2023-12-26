'''
Joe Walter

difficulty: 60%
run time:   2:20
answer:     3857447

	***

155 Counting Capacitor Circuits

An electric circuit uses exclusively identical capacitors of the same value C.

The capacitors can be connected in series or in parallel to form sub-units, which can then be connected in series or in parallel with other capacitors or other sub-units to form larger sub-units, and so on up to a final circuit.

Using this simple procedure and up to n identical capacitors, we can make circuits having a range of different total capacitances. For example, using up to n=3 capacitors of 60 mF each, we can obtain the following 7 distinct total capacitance values:

https://projecteuler.net/project/images/p155_capacitors1.gif

If we denote by D(n) the number of distinct total capacitance values we can obtain when using up to n equal-valued capacitors and the simple procedure described above, we have: D(1)=1, D(2)=3, D(3)=7 ...

Find D(18).

Reminder : When connecting capacitors C1, C2 etc in parallel, the total capacitance is CT = C1 + C2 +..., whereas when connecting them in series, the overall capacitance is given by: 1/CT=1/C1+1/C2+...
'''

from fractions import Fraction as F

def D(N):
	caps = [set() for _ in range(N+1)]
	caps[1].add(F(1,1))
	for n in range(2, N+1):
		for i in range(1, n+1):
			j = n - i
			if j < i:
				break
			c = caps[n]
			for a in caps[i]:
				for b in caps[j]:
					s = a + b
					c.add(s)
					c.add(a*b/s)
	for n in range(2, N+1):
		caps[n].update(caps[n-1])
	return len(caps[N])

assert D(1) == 1
assert D(2) == 3
assert D(3) == 7

print(D(18))
