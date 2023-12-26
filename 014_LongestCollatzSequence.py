'''
Joe Walter

difficulty: 5%
run time:   0:01
answer:     837799

	***

014 Longest Collatz Sequence

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

M = 1000000

def collatz_length(n, memmory = dict()):
	if n == 1:
		return 1
	if n in memmory:
		return memmory[n]

	length = 1
	if n%2 == 0:
		length += collatz_length(n/2)
	else:
		length += collatz_length(3*n + 1)

	memmory[n] = length
	return length

ans = max(collatz_length(n) for n in range(1, M))
print(ans)
