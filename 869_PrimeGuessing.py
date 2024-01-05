'''
Joe Walter

difficulty: TBD
run time:   0:14
answer:     14.97696693

	***

869 Prime Guessing

A prime is drawn uniformly from all primes not exceeding N. The prime is written in binary notation, and a player tries to guess it bit-by-bit starting at the least significant bit. The player scores one point for each bit they guess correctly. Immediately after each guess, the player is informed whether their guess was correct, and also whether it was the last bit in the number - in which case the game is over.

Let E(N) be the expected number of points assuming that the player always guesses to maximize their score. For example, E(10)=2, achievable by always guessing "1". You are also given E(30)=2.9.

Find E(10^8). Give your answer rounded to eight digits after the decimal point.
'''

from lib.num import get_primes

def binary_search(primes, depth, lo, hi):
	while lo <= hi:
		m = (lo+hi)//2
		if primes[m][depth] == '1':
			return binary_search(primes, depth, lo, m-1)
		elif primes[m+1][depth] == '0':
			return binary_search(primes, depth, m+1, hi)
		else:
			return m
	raise ValueError()

def E(N):
	primes = sorted(f"{p:b}"[::-1] for p in get_primes(N))
	def _E(depth, lo, hi):
		try:
			_ = primes[lo][depth]
		except IndexError:
			lo += 1
		if lo > hi:
			return 0
		elif primes[lo][depth]=='1' or primes[hi][depth]=='0':
			return (hi-lo+1) + _E(depth+1, lo, hi)
		else:
			#m = next(i for i in range(lo, hi+1) if primes[i+1][depth]=='1')
			m = binary_search(primes, depth, lo, hi)
			return max(m-lo+1, hi-m) + _E(depth+1, lo, m) + _E(depth+1, m+1, hi)
	val = _E(0, 0, len(primes)-1) / len(primes)
	return f"{val:.8f}"

assert E(10) == '2.00000000'
assert E(30) == '2.90000000'

print(E(10**8))
