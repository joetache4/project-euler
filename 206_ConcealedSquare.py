'''
Joe Walter

difficulty: 5%
run time:   0:03
answer:     1389019170

	***

206 Concealed Square

Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0, where each “_” is a single digit.
'''

def check(n):
	return str(n*n)[0::2] == "1234567890"

def solve():
	n = 1000000030
	while True:
		if check(n):
			return n
		n += 40
		if check(n):
			return n
		n += 60

print(solve())
