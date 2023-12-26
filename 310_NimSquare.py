'''
Joe Walter

difficulty: 40%
run time:   0:04
answer:     2586528661783

	***

310 Nim Square

Alice and Bob play the game Nim Square.
Nim Square is just like ordinary three-heap normal play Nim, but the players may only remove a square number of stones from a heap.
The number of stones in the three heaps is represented by the ordered triple (a,b,c).
If 0 <= a <= b <= c <= 29 then the number of losing positions for the next player is 1160.

Find the number of losing positions for the next player if 0 <= a <= b <= c <= 100000.
'''

# Sprague-Grundy Theorem: Every impartial game (each player has the same moves) is equivalent to a game of Nim, and
# The Nim value is found as the minimum excluded value (mex) of nim values of positions reached in a single move
# Faster way to calculate Nim values: https://drops.dagstuhl.de/opus/volltexte/2018/8811/pdf/LIPIcs-FUN-2018-20.pdf

from itertools import count

def mex(s):
	s = sorted(set(s))
	for i,v in enumerate(s):
		if i != v:
			return i
	return len(s)

def next(i):
	for m in count(1):
		m = m*m
		if m > i:
			break
		yield i-m

# The mex of two (or more) separate Nim games turns out to be XOR of the nim values
# Losing positions for the starting player are those games that have value 0

from collections import Counter
from math import comb

def L(n):
	nim = [0]*(n+1)
	for i in range(1, n+1):
		nim[i] = mex(nim[j] for j in next(i))

	ans = 0
	C   = Counter(nim)
	N   = sorted(C.keys())

	# (x1,x2,x3)
	# there are no repeated nim values if they're all >0
	for n1 in N:
		for n2 in N:
			for n3 in N:
				if n1>0 and n2>0 and n3>0:
					if n1^n2^n3 == 0:
						ans += C[n1]*C[n2]*C[n3]
	ans //= 6 # exactly 1/6 of permutations are 'correct' (i<j<k)

	front = C
	back  = Counter()
	for n in nim:
		front[n] -= 1
		if n == 0:
			# (0,n1,n2)
			ans += sum(comb(y,2) for x,y in front.items() if x>0)
			# (n1,0,n2)
			ans += sum(back[x]*front[x] for x in back.keys() if x>0)
			# (n1,n2,0)
			ans += sum(comb(y,2) for x,y in back.items() if x>0)

			# (0,0,0)
			# TODO check this
			ans += comb(front[0]+2,2) # without +2, this adds to front[0] choose 3, which is wrong. With +2 it accounts for repeated selections (combinations with repetition)

			# (0,n1,n1)
			ans += sum(y for x,y in front.items() if x>0)
			# (n1,n1,0)
			ans += sum(y for x,y in back.items() if x>0)
		back[n] += 1

	return ans

assert L(29) == 1160

print(L(100000))

'''
# (0,0,0)
ans += C[0]*(C[0]-1)*(C[0]-2)//6
ans += C[0]*(C[0]-1) # div by 2 b/c of double-counting, mult by 2 to choose which one is doubled up
ans += C[0]

# (0,x1,x1) (x1,x1,0)
ans += C[0]*(n+1-C[0])
'''
