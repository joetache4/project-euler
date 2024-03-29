'''
Joe Walter

difficulty: 5%
run time:   0:00
answer:     8739992577

	***

097 Large Non-Mersenne Prime

The first known prime found to exceed one million digits was discovered in 1999, and is a Mersenne prime of the form 26972593−1; it contains exactly 2,098,960 digits. Subsequently other Mersenne primes, of the form 2p−1, have been found which contain more digits.

However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits: 28433×2^7830457+1.

Find the last ten digits of this prime number.
'''

m = 10**10

n = pow(2, 7830457, m)
n = (28433*n + 1) % m

print(n)
