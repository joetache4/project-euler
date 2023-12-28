'''
Joe Walter

difficulty: 50%
run time:   0:20
answer:     453647705

	***

133 Repunit Nonfactors

A number consisting entirely of ones is called a repunit. We shall define R(k) to be a repunit of length k; for example, R(6) = 111111.

Let us consider repunits of the form R(10^n).

Although R(10), R(100), or R(1000) are not divisible by 17, R(10000) is divisible by 17. Yet there is no value of n for which R(10^n) will divide by 19. In fact, it is remarkable that 11, 17, 41, and 73 are the only four primes below one-hundred that can be a factor of R(10^n).

Find the sum of all the primes below one-hundred thousand that will never be a factor of R(10^n).

	***

p|A(p)=R(k) where A(p) is the smallest repunit that is divisible by p and has length k
k|10^n  -->  A(p)|R(10^n)  -->  p|R(10^n)

not k|10^n
  suppose A(p)|R(10^n)
    --> 10^n = ak+b where 0<b<k
    --> A(p)|A(b)
    --> contradiction, as A(p)>A(b)
  therefore, not A(p)|R(10^n)
  R(1)%p, R(2)%p, ... is cyclical
    --> the only R(n) divisible by p are those where k|n (where A(p)=R(k))
  therefore, not p|R(10^n)
'''

from lib.num import get_primes

def A(n):
	m = k = 1
	while True:
		m = (10*m+1)%n
		k += 1
		if m == 0:
			return k

primes = get_primes(100000)
ans    = sum(primes)

primes.remove(2)
primes.remove(5)

for p in primes:
	k = A(p)
	# check if k is a product of powers of 2 and 5
	# i.e., k|10^n for some n
	while not k&1:
		k >>= 1
	# don't use math.log !!
	t = 1
	while t < k:
		t *= 5
	if t == k:
		print(p)
		ans -= p

print(ans)
