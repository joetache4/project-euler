'''
Joe Walter

difficulty: 35%
run time:   0:00
answer:     18769

	***

098 Anagramic Squares

By replacing each of the letters in the word CARE with 1, 2, 9, and 6 respectively, we form a square number: 1296 = 36^2. What is remarkable is that, by using the same digital substitutions, the anagram, RACE, also forms a square number: 9216 = 96^2. We shall call CARE (and RACE) a square anagram word pair and specify further that leading zeroes are not permitted, neither may a different letter have the same digital value as another letter.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, find all the square anagram word pairs (a palindromic word is NOT considered to be an anagram of itself).

What is the largest square number formed by any member of such a pair?

NOTE: All anagrams formed must be contained in the given text file.
'''

from math import isqrt
from data.p098 import get_data

# can tell if two words are substitutions of each other
def signature(s, alphabet="abcdefghijklmnopqrstuvwxyz"):
	s = str(s)
	sig = []
	map = {}
	j = 0
	for i in range(len(s)):
		c = s[i]
		try:
			sig.append(map[c])
		except:
			map[c] = alphabet[j]
			sig.append(alphabet[j])
			j += 1
	sig = "".join(sig)
	return sig

# returns the permutation that takes a to b
def permutation(a, b):
	if len(a) != len(b) or sorted(a) != sorted(b):
		return None
	perm = []
	for ac in a:
		for i, bc in enumerate(b):
			if ac == bc and i not in perm:
				perm.append(i)
				break
	return perm

# permutes s according to perm
def permute(s, perm):
	s = str(s)
	t = [None]*len(s)
	for i, c in zip(perm, s):
		t[i] = c
	return "".join(t)

def solve():
	# get all permutations that take one word to another
	words = get_data()
	perms = {}
	for i, a in enumerate(words):
		sig_a = signature(a)
		for j, b in enumerate(words):
			if i == j:
				break
			if p := permutation(a,b):
				try:
					perms[sig_a].append(p)
				except:
					perms[sig_a] = []
					perms[sig_a].append(p)
	# find largest square that can be permuted to another square
	L       = max(len(k) for k in perms)
	squares = [m*m for m in range(isqrt(10**L)+1)]
	for s in squares[-1::-1]:
		sig = signature(s)
		try:
			for p in perms[sig]:
				t = permute(s, p)
				if t[0] == "0":
					continue
				t = int(t)
				if isqrt(t)**2 == t:
					return s
		except KeyError:
			pass

print(solve())
