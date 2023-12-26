'''
Joe Walter

difficulty: 50%
run time:   0:00
answer:     0.464399

	***

151 Paper Sheets Of Standard Sizes: An Expected-Value Problem

A printing shop runs 16 batches (jobs) every week and each batch requires a sheet of special colour-proofing paper of size A5.

Every Monday morning, the supervisor opens a new envelope, containing a large sheet of the special paper with size A1.

The supervisor proceeds to cut it in half, thus getting two sheets of size A2. Then one of the sheets is cut in half to get two sheets of size A3 and so on until an A5-size sheet is obtained, which is needed for the first batch of the week.

All the unused sheets are placed back in the envelope.

At the beginning of each subsequent batch, the supervisor takes from the envelope one sheet of paper at random. If it is of size A5, then it is used. If it is larger, then the 'cut-in-half' procedure is repeated until an A5-size sheet is obtained, and any remaining sheets are always placed back in the envelope.

Excluding the first and last batch of the week, find the expected number of times (during each week) that the supervisor finds a single sheet of paper in the envelope.

Give your answer rounded to six decimal places using the format x.xxxxxx .
'''

from functools import cache

def divide(n):
	d = []
	while n := n >> 1:
		d.append(n)
	return d

@cache
def exp(x):
	if len(x) == 0:
		return 0
	hit = 1 if len(x) == 1 else 0
	for i in range(len(x)):
		x2   = list(x)
		x2  += divide(x2.pop(i))
		x2   = tuple(sorted(x2))
		hit += exp(x2)/len(x)
	return hit

def solve(n):
	return f"{exp((n,))-2:.6f}"

print(solve(16))


# Monte Carlo, only good for about 3 decimal places
'''
import random
import math
import statistics

count1_all = []
for _ in range(10**4):
	sheets = [16]
	count1 = 0
	for _ in range(16):
		if len(sheets) == 1:
			count1 += 1
		random.shuffle(sheets)
		s = sheets.pop() // 2
		while s > 0:
			sheets.append(s)
			s //= 2
	count1_all.append(count1)


print(statistics.mean(count1_all)-2)
print(statistics.stdev(count1_all)/math.sqrt(len(count1_all))) # standard error of mean
'''
