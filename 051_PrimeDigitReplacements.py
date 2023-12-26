'''
Joe Walter

difficulty: 15%
run time:   0:00
answer:     121313

	***

051 Prime Digit Replacements

By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.

	***

Observations

The answer is a prime constructed from a template T (e.g. *2*2*3 -> 121213, 222223, 323233, etc.)

Assuming the answer is short enough, the template T can be made from some prime number by replacing *all* of a particular digit. (e.g. 525253, replace all 5s -> *2*2*3).

To find out how many primes belong to this template, add the following.
1. the number of primes that produce this this template when *all* of a particular digit is replaced
2. the number of primes that are produced when all * are replaced with each of the non-* in the template
(1. and 2. are disjoint sets of primes and together comprise all primes represented by this template.)

T must have a number of * equal to a multiple of 3, and the non-* must not sum to a multiple of 3. Otherwise, there would be 3 replacement digits that would produce composite numbers (sum of digits = 3 -> number is divisible by 3), and so a maximum of 7 numbers would be prime.
'''

from collections import Counter
from itertools import count
from primesieve import primes as get_primes
from lib.array import binary_search

for length in count(5):
	# Look at primes in batches of equal length.
	primes = sorted(get_primes(10**(length-1), 10**length))
	primes = [str(p) for p in primes]

	# 1. Replace digits 0-9 with * and count occurrences.
	template_count = Counter()
	for d in "0123456789":
		replaced = Counter(p.replace(d, "*") for p in primes)
		for t in replaced:
			count = t.count("*")
			if count > 0 and count%3 == 0:
				template_count[t] += replaced[t]

	# 2. Replace * with digits already in the template and see if the result is prime.
	for t, count in template_count.items():
		not_replaced = {d for d in t}
		not_replaced.remove("*")
		if len(not_replaced) + count < 8:
			continue # not possible so don't try
		for d in not_replaced:
			if binary_search(primes, t.replace("*", d)):
				template_count[t] += 1

	# Get templates for 8-family primes.
	templates = set()
	for t in template_count:
		if template_count[t] == 8:
			templates.add(t)

	# Find smallest prime that's part of one of these tempaltes.
	if len(templates) > 0:
		candidates = set()
		for t in templates:
			# For an 8-family, there must be a prime after replacing with 0, 1, or 2.
			a = t.replace("*", "0")
			if binary_search(primes, a) and t[0] != "*":
				candidates.add(a)
			a = t.replace("*", "1")
			if binary_search(primes, a):
				candidates.add(a)
			a = t.replace("*", "2")
			if binary_search(primes, a):
				candidates.add(a)
		print(min(candidates))
		break
