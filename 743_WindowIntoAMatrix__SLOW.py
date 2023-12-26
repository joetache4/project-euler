'''
Joe Walter

difficulty: 10%
run time:   1:30
answer:     259158998

	***

743 Window Into A Matrix

A window into a matrix is a contiguous sub matrix.

Consider a 2xN matrix where every entry is either 0 or 1.
Let A(K,N) be the total number of these matrices such that the sum of the entries in every 2xK window is K.

You are given that A(3,9) = 560 and A(4,20) = 1060870.

Find A(10^8, 10^16). Give your answer modulo 1000000007.

	***

Observations

Every valid matrix will repeat with period K (if you allow for equivalence of 1-0 and 0-1 columns)

Let:
k = window width
L = matrix width
n = number of 'one' columns

Then, the number of valid matrices is

Sum		k!2^(nL/k)/n!/((k-n)/2)!^2		for n from 0 to k, step of 2

(TODO: actually n goes from 1 to k when k is odd)

The terms cans be expressed recursively like so:

a_0 = k!/(k/2)!^2
a_n = a_n-2 • 2^(2L/k-2)(k-n+2)^2/(n-1)/n
'''

from lib.num import mod_inverse_range

def A(k, L, mod = 1000000007):
	r = pow(2, 2*L//k-2, mod)

	# calc (k/2)!
	fact_half_k = 1
	for i in range(1, k//2+1):
		fact_half_k = (fact_half_k * i) % mod
	# calc k!
	fact_k = fact_half_k
	for i in range(k//2+1, k+1):
		fact_k = (fact_k * i) % mod

	inv = mod_inverse_range(k+1, mod)

	a = [(fact_k * pow(fact_half_k**2, -1, mod)) % mod]
	for n in range(2, k+1, 2):
		a.append((a[-1]*r*(k-n+2)**2*inv[n-1]*inv[n]) % mod)

	return sum(a) % mod

#assert A(3, 9) == 560 # currently does not work for odd k
assert A(4, 20) == 1060870

print(A(10**8, 10**16))



# works but slow
'''
fact = [1]
for i in range(1, 10**8+1):
	fact.append(fact[-1]*i % mod)

fact_inv = mod_inverse_arr(fact, mod)

#def choose(a,b):
#	return (fact[a] * fact_inv[a-b] * fact_inv[b]) % mod

def solve(k, L):
	period = L//k # assumes L is a multiple of k
	total = 0
	fact_k = fact[k]
	for ones in range(k, -1, -2):
		twos = (k-ones)//2
		#count = choose(k, ones) * choose(k-ones, twos)
		#count = (fact_k * fact_inv[ones] * fact_inv[twos] * fact_inv[k-ones-twos]) % mod
		count = (fact_k * fact_inv[ones] * fact_inv[twos]**2) % mod
		count *= pow(2, ones*period, mod)
		total += count
	return total % mod

assert solve(3, 9) == 560
assert solve(4, 20) == 1060870

print(solve(10**8, 10**16))
'''
