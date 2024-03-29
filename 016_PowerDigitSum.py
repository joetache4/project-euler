'''
Joe Walter

difficulty: 5%
run time:   0:00
answer:     1366

	***

016 Power Digit Sum

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''

print(sum(int(d) for d in str(2**1000)))
