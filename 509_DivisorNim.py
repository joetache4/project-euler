'''
Joe Walter

difficulty: 45%
run time:   0:00
answer:     151725678

	***

509 Divisor Nim

Anton and Bertrand love to play three pile Nim.
However, after a lot of games of Nim they got bored and changed the rules somewhat.
They may only take a number of stones from a pile that is a proper divisor of the number of stones present in the pile.
E.g. if a pile at a certain moment contains 24 stones they may take only 1, 2, 3, 4, 6, 8, or 12 stones from that pile.
So if a pile contains one stone they can't take the last stone from it as 1 isn't a proper divisor of 1.
The first player that can't make a valid move loses the game.
Of course both Anton and Bertrand play optimally.

The triple (a,b,c) indicates the number of stones in the three piles.
Let S(n) be the number of winning positions for the next player for 1 <= a,b,c <= n.
S(10)=692 and S(100)=735494.

Find S(123456787654321) modulo 1234567890.
'''

from collections import Counter

def get_count(target_len):
	# calculate cumulative count of Nim values at indices that are powers of 2
	counts = [Counter({0:1})]
	for _ in range(51): # TODO calc upper bound
		count = counts[-1].copy()
		count[len(count)] += 1
		for i in range(0, len(count)-2, 1):
			count[i] *= 2
		counts.append(count)

	count = Counter()
	while target_len > 0:
		for i in range(50, -1, -1):
			if 2**i <= target_len:
				assert i != 50
				count += counts[i]
				target_len -= 2**i
				break
	return count

def S(n):
	ans = 0
	count = get_count(n)
	for a in count.keys():
		for b in count.keys():
			for c in count.keys():
				if a^b^c > 0:
					ans += count[a]*count[b]*count[c]
	return ans

assert S(10) == 692
assert S(100) == 735494

print(S(123456787654321) % 1234567890)

# A pattern in Nim values
'''
All divisors...
1-indexed Nim values			Increment				Cumulative
1								{1:1}					{1:1}
2,								{2:1}					{1:1, 2:1}
1, 3							{1:1, 3:1}				{1:2, 2:1, 3:1}
1, 2, 1, 4						{1:2, 2:1, 4:1}			{1:4, 2:2, 3:1, 4:1}
1, 2, 1, 3, 1, 2, 1, 5			{1:4, 2:2, 3:1, 5:1}	{1:8, 2:4, 3:2, 4:1, 5:1}

Proper divisors...
0								{0:1}					{0:1}
1								{1:1}					{0:1, 1:1}
0, 2							{0:1, 2:1}				{0:2, 1:1, 2:1}
0, 1, 0, 3						{0:2, 1:1, 3:1}			{0:4, 1:2, 2:1, 3:1}
0, 1, 0, 2, 0, 1, 0, 4			{0:4, 1:2, 2:1, 4:1}	{0:8, 1:4, 2:2, 3:1, 4:1}
'''

# Finds the pattern
'''
from lib.num import divisors

def mex(s):
	s = sorted(set(s))
	for i,v in enumerate(s):
		if i != v:
			return i
	return len(s)

def next(i):
	D = divisors(i)
	D.remove(i)
	for d in D:
		yield i-d

n = 10
nim = [0]*(n+1)
for i in range(1, n+1):
	nim[i] = mex(nim[j] for j in next(i))
print(nim[1:])
'''
