'''
Joe Walter

difficulty: 20%
run time:   0:53
answer:     475808650131120

	***

793 Median Of Products

Let S_i be an integer sequence produced with the following pseudo-random number generator:

	* S_0 = 290797
	* S_i+1 = (S_i)^2 mod 50515093

Let M(n) be the median of the pairwise products S_iS_j for 0 <= i < j < n.

You are given M(3)=3878983057768 and M(103)=492700616748525.

Find M(1000003).
'''

from math import ceil, log2
from bisect import bisect

def S(n, start = 290797, mod = 50515093):
	def _S():
		a = start
		for _ in range(n):
			yield a
			a = (a*a) % mod
	return sorted(_S())

# count the product pairs on either side of m
def split_count(s, s_inv, m):
	lte = 0
	for i in range(len(s)):
		a = s_inv[i]
		b = m*a
		lte += bisect(s, b, lo=0, hi=i)
	gt = len(s)*(len(s)-1)//2-lte
	return (lte, gt)

# find the largest number that has more product pairs higher than lower
# this number is one less than the lowest the median could be
# TODO add 1 so it's actually the lower bound
def find_pp_lower_bound(s, s_inv):
	lower_bound = 0
	mask = 1 << ceil(log2(s[-1]*s[-2]))
	while mask > 0:
		#print(len(f'{mask:b}'))
		lower_bound ^= mask
		lte, gt = split_count(s, s_inv, lower_bound)
		if lte < gt:
			pass
		else:
			lower_bound ^= mask
		mask >>= 1
	return lower_bound

# find the smallest product pair that is >= lower_bound -- this is the answer
def find_pp_median(s):
	s_inv = [1/t for t in s]
	lower_bound = find_pp_lower_bound(s, s_inv)
	med = float('inf')
	for i in range(len(s)):
		try:
			#j = min(len(s)-1, bisect(s, lower_bound * s_inv[i]))
			j = bisect(s, lower_bound*s_inv[i])
			m = s[i] * s[j]
			#if m >= lower_bound:
			med = min(med, m)
		except IndexError:
			# happens when s[i] is so small that all its pp's are less than lower_bound and so j is set to len(s)
			pass
	return med

def solve(n):
	s = S(n)
	return find_pp_median(s)

assert solve(3)   == 3878983057768
assert solve(103) == 492700616748525

print(solve(1000003)) # 475808650131120









'''
# use bins to find general location of median

ans = 492700616748525

def bin(s):
	return int(log(s,2)*1000)

S_bins = {}
for s in S:
	b = bin(s)
	try:
		sb = S_bins[b]
		sb[0] += 1
		sb[1].append(s)
	except KeyError:
		S_bins[b] = [1, [s]]
S_bins = [(k,v[0],v[1]) for k,v in S_bins.items()]


#tmp
assert sum(v for k,v,l in S_bins) == N
print(f'{len(S)=}')
print(f'{len(S_bins)=}')

S2_bins = {}
for i in range(len(S_bins)):
	for j in range(i+1):
		a = S_bins[i]
		b = S_bins[j]
		k = a[0]+b[0]
		if i == j:
			v = a[1]*(a[1]-1)//2
		else:
			v = a[1]*b[1]
		try:
			S2_bins[k] += v
		except KeyError:
			S2_bins[k] = v

#tmp
for s in S:
	s2 = ans // s
	if s < s2 and s*s2 == ans:
		x = s
		y = s2
		break
b = bin(x)+bin(y)
assert b in S2_bins
assert sum(v for k,v in S2_bins.items()) == N*(N-1)//2

S2_bins = sorted((k,v) for k,v in S2_bins.items())

#tmp
i = sum(v for k,v in S2_bins if k < b)
j = sum(v for k,v in S2_bins if k == b)
k = sum(v for k,v in S2_bins if k > b)
print(f'{bin(ans)=}')
print((i, j, k))

index = (N*(N-1)//2)//2 # index of median, also the number of terms before the median
for k,v in S2_bins:
	m_bin = k
	index -= v
	if index < 0:
		index += v
		break

#tmp
i = sum(v for k,v in S2_bins if k < m_bin)
j = sum(v for k,v in S2_bins if k == m_bin)
k = sum(v for k,v in S2_bins if k > m_bin)
print(f'{m_bin=}')
print((i, j, k))

#tmp
count = 0

candidates = []
for i in range(1, len(S_bins)):
	for j in range(i):
		a = S_bins[i][0]
		b = S_bins[j][0]
		if a+b == m_bin or a+b == m_bin+1:
			count += S_bins[i][1]*S_bins[j][1]
			for x in S_bins[i][2]:
				for y in S_bins[j][2]:
					candidates.append(x*y)
candidates = sorted(candidates)

print(count)
#print(f'{len(candidates)=}')
print(candidates[index])
#475808689511340
#475808771991540
print(ans in candidates)






# todo: use bisect
def count_lte(arr, m, lo = 0, hi = None):
	#input((lo,hi))
	if hi is None:
		hi = len(arr) - 1

	if lo >= hi:
		if arr[lo] <= m:
			return lo + 1
		else:
			return lo

	i = (lo + hi)//2
	if arr[i] <= m:
		return count_lte(arr, m, i+1, hi)
	else:
		return count_lte(arr, m, lo, i-1)

assert count_lte([1,2,4,7,8,9,10,12], 0) == 0
assert count_lte([1,2,4,7,8,9,10,12], 1) == 1
assert count_lte([1,2,4,7,8,9,10,12], 2) == 2
assert count_lte([1,2,4,7,8,9,10,12], 3) == 2
assert count_lte([1,2,4,7,8,9,10,12], 4) == 3
assert count_lte([1,2,4,7,8,9,10,12], 5) == 3
assert count_lte([1,2,4,7,8,9,10,12], 6) == 3
assert count_lte([1,2,4,7,8,9,10,12], 7) == 4
assert count_lte([1,2,4,7,8,9,10,12], 11) == 7
assert count_lte([1,2,4,7,8,9,10,12], 12) == 8
assert count_lte([1,2,4,7,8,9,10,12], 13) == 8
assert count_lte([1,2,4,7,8,9,10,12,13], 0) == 0
assert count_lte([1,2,4,7,8,9,10,12,13], 1) == 1
assert count_lte([1,2,4,7,8,9,10,12,13], 2) == 2
assert count_lte([1,2,4,7,8,9,10,12,13], 3) == 2
assert count_lte([1,2,4,7,8,9,10,12,13], 4) == 3
assert count_lte([1,2,4,7,8,9,10,12,13], 5) == 3
assert count_lte([1,2,4,7,8,9,10,12,13], 6) == 3
assert count_lte([1,2,4,7,8,9,10,12,13], 7) == 4
assert count_lte([1,2,4,7,8,9,10,12,13], 12) == 8
assert count_lte([1,2,4,7,8,9,10,12,13], 13) == 9
assert count_lte([1,2,4,7,8,9,10,12,13], 14) == 9

assert count_lte([1,2,4,7,8,9,10,12], 0, 0, 0) == 0
assert count_lte([1,2,4,7,8,9,10,12], 1, 0, 0) == 1
assert count_lte([1,2,4,7,8,9,10,12], 2, 0, 1) == 2
assert count_lte([1,2,4,7,8,9,10,12], 2, 0, 0) == 1
assert count_lte([1,2,4,7,8,9,10,12], 3, 0, 1) == 2
assert count_lte([1,2,4,7,8,9,10,12], 4, 0, 2) == 3
assert count_lte([1,2,4,7,8,9,10,12], 4, 0, 1) == 2
assert count_lte([1,2,4,7,8,9,10,12], 4, 0, 0) == 1
assert count_lte([1,2,4,7,8,9,10,12], 5, 0, 3) == 3
assert count_lte([1,2,4,7,8,9,10,12], 5, 0, 2) == 3
assert count_lte([1,2,4,7,8,9,10,12], 5, 0, 1) == 2
assert count_lte([1,2,4,7,8,9,10,12], 5, 0, 0) == 1
assert count_lte([1,2,4,7,8,9,10,12], 6, 0, 3) == 3
assert count_lte([1,2,4,7,8,9,10,12], 6, 0, 2) == 3
assert count_lte([1,2,4,7,8,9,10,12], 6, 0, 1) == 2
assert count_lte([1,2,4,7,8,9,10,12], 6, 0, 0) == 1
assert count_lte([1,2,4,7,8,9,10,12], 7, 0, 4) == 4
assert count_lte([1,2,4,7,8,9,10,12], 7, 0, 3) == 4
assert count_lte([1,2,4,7,8,9,10,12], 7, 0, 2) == 3
assert count_lte([1,2,4,7,8,9,10,12], 7, 0, 1) == 2
assert count_lte([1,2,4,7,8,9,10,12], 7, 0, 0) == 1

assert count_lte([1,2,4,7,8,9,10,12], 11) == 7
assert count_lte([1,2,4,7,8,9,10,12], 12) == 8
assert count_lte([1,2,4,7,8,9,10,12], 13) == 8
assert count_lte([1,2,4,7,8,9,10,12,13], 0) == 0
assert count_lte([1,2,4,7,8,9,10,12,13], 1) == 1
assert count_lte([1,2,4,7,8,9,10,12,13], 2) == 2
assert count_lte([1,2,4,7,8,9,10,12,13], 3) == 2
assert count_lte([1,2,4,7,8,9,10,12,13], 4) == 3
assert count_lte([1,2,4,7,8,9,10,12,13], 5) == 3
assert count_lte([1,2,4,7,8,9,10,12,13], 6) == 3
assert count_lte([1,2,4,7,8,9,10,12,13], 7) == 4
assert count_lte([1,2,4,7,8,9,10,12,13], 12) == 8
assert count_lte([1,2,4,7,8,9,10,12,13], 13) == 9
assert count_lte([1,2,4,7,8,9,10,12,13], 14) == 9
input('tests succeeded')
'''
