'''
Joe Walter

difficulty: 5%
run time:   0:00
answer:     73162890

	***

079 Passcode Derivation

A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.

	***

Any solution without repeated digits will be shorter than any solution with repeated digitis. So look without repetitions first.
'''

from itertools import permutations
from data.p079 import get_data

def contains(p, code):
	L = len(code)
	match = 0
	for d in p:
		if d == code[match]:
			match += 1
			if match == len(code):
				return True
	return False

codes = set(get_data())
digits = set()
for code in codes:
	digits |= {d for d in code}

for p in permutations(digits):
	if all(contains(p,code) for code in codes):
		print("".join(p))
		break
