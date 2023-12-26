'''
Joe Walter

difficulty: 55%
run time:   0:00
answer:     126461847755

	***

178 Step Numbers

Consider the number 45656.
It can be seen that each pair of consecutive digits of 45656 has a difference of one.
A number for which every pair of consecutive digits has a difference of one is called a step number.
A pandigital number contains every decimal digit from 0 to 9 at least once.
How many pandigital step numbers less than 10^40 are there?
'''

from math import floor, ceil
from functools import cache

@cache
def count_paths(ay, by, dx, miny, maxy):
	if ay > maxy or by > maxy:
		return 0
	if ay < miny or by < miny:
		return 0
	if abs(by - ay) > dx:
		return 0
	if dx == 1:
		if abs(by - ay) == 1:
			return 1
		else:
			return 0
	else:
		return sum(
			count_paths(ay, i, floor(dx/2), miny, maxy) * count_paths(i, by, ceil(dx/2), miny, maxy)
			for i in range(miny, maxy+1)
		)

ans = 0
for dx in range(9, 40):
	for ay in range(1, 10):
		for by in range(10):
			ans += count_paths(ay, by, dx, 0, 9)
			ans -= count_paths(ay, by, dx, 0, 8)
			ans -= count_paths(ay, by, dx, 1, 9)
			ans += count_paths(ay, by, dx, 1, 8)
print(ans)
