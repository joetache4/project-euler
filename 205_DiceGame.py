'''
Joe Walter

difficulty: 15%
run time:   0:00
answer:     0.5731441

	***

205 Dice Game

Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.
Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.

Peter and Colin roll their dice and compare totals: the highest total wins. The result is a draw if the totals are equal.

What is the probability that Pyramidal Pete beats Cubic Colin? Give your answer rounded to seven decimal places in the form 0.abcdefg
'''

from collections import Counter
from itertools import product

D4 = list(range(1,5))
D6 = list(range(1,7))

P4 = Counter()
P6 = Counter()

for roll4 in product(D4,D4,D4,D4,D4,D4,D4,D4,D4):
	P4[sum(roll4)] += 1

for roll6 in product(D6,D6,D6,D6,D6,D6):
	P6[sum(roll6)] += 1

n,d = 0,0
for roll4, count4 in P4.items():
	for roll6, count6 in P6.items():
		if roll4 > roll6:
			n += count4*count6
		d += count4*count6

print(f"{n/d:0.7f}")
