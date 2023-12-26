'''
Joe Walter

difficulty: 15%
run time:   0:14
answer:     11109800204052

	***

347 Largest Integer Divisible By Two Primes

The largest integer ≤ 100 that is only divisible by both the primes 2 and 3 is 96, as 96=32*3=2^5*3. For two distinct primes p and q let M(p,q,N) be the largest positive integer ≤N only divisible by both p and q and M(p,q,N)=0 if such a positive integer does not exist.

E.g. M(2,3,100)=96.
M(3,5,100)=75 and not 90 because 90 is divisible by 2 ,3 and 5.
Also M(2,73,100)=0 because there does not exist a positive integer ≤ 100 that is divisible by both 2 and 73.

Let S(N) be the sum of all distinct M(p,q,N). S(100)=2262.

Find S(10 000 000).
'''

from lib.num import FactorRange

def solve(N):
	F = FactorRange(N+1)
	M = {} #(p,q) -> M(p,q,N)
	for n, f in F.factors():
		f = set(f)
		if len(f) == 2:
			M[tuple(f)] = n
	return sum(M.values())

assert solve(100) == 2262

print(solve(10**7))
