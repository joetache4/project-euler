'''
Joe Walter

difficulty: 45%
run time:   0:45
answer:     44680

	***

118 Pandigital Prime Sets

Using all of the digits 1 through 9 and concatenating them freely to form decimal integers, different sets can be formed. Interestingly with the set {2,5,47,89,631}, all of the elements belonging to it are prime.

How many distinct sets containing each of the digits one through nine exactly once contain only prime elements?

	***

Solution Method


After each iteration, "count" contains the number of sets (of successively higher sizes) whose digits produce the given index.
So after the first interation, it's values indicate the number of size-2 sets that have index(set)=i at each array index i. After the second iteration, it's values indicate the number of size-3 sets, and so on.
At the end of each iteration, count_new[2**9-1] counted all pandigital sets.
'''

import primesieve as ps

def index(p):
	v = 0
	while p > 0:
		d = p%10
		if d == 0:
			return 0
		d = 1<<(d-1)
		if d&v:
			return 0
		v += d
		p //= 10
	return v

# get primes & their indices -- this takes the most time by far
count_orig = [0]*(2**9)
it = ps.Iterator()
p = it.next_prime()
#while p <= 987654321: # there are no 9-digit pandigital primes, so this could be 98765432 instead
while p <= 98765432:
	if (i := index(p)) > 0:
		count_orig[i] += 1
	p = it.next_prime()

# main loop
count_prev = count_orig
ans = 0
while True:
	count_new = [0]*len(count_orig)
	for i in range(len(count_orig)):
		for j in range(i):
			if i&j == 0: # no shared digits allowed
				count_new[i+j] += count_orig[i]*count_prev[j]
	if sum(count_new) == 0:
		# no new sets have been made, quit
		break
	else:
		ans += count_new[-1]
		count_prev = count_new

print(ans)

# Old. This overcounts, acting as if {a,b}+{c,d} is different from {a,c}+{b,d}.
'''
for i in range(1, len(count)):
	for j in range(i):
		if i & j == 0:
			# no shared digits
			count[i + j] += count[i] * count[j]

print(count[-1])
'''
