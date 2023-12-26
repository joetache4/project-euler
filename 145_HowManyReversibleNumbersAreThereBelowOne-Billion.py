'''
Joe Walter

difficulty: 20%
run time:   0:00
answer:     608720

	***

145 How Many Reversible Numbers Are There Below One-Billion?

Some positive integers n have the property that the sum [ n + reverse(n) ] consists entirely of odd (decimal) digits. For instance, 36 + 63 = 99 and 409 + 904 = 1313. We will call such numbers reversible; so 36, 63, 409, and 904 are reversible. Leading zeroes are not allowed in either n or reverse(n).

There are 120 reversible numbers below one-thousand.

How many reversible numbers are there below one-billion (10^9)?

	***

Observations

All reversible numbers fall into one of two groups:

1.
	Even length
	All digits sum to odd
	No carries in n + reverse(n)
2.
	Odd length
	Digits alternate odd-with-carry and even-with-no-carry
	Since middle digit is added to itself, the sum is even, and so the whole number has 4k-1 digits for some int k>0
'''

from itertools import count

# count digit pairings

odd_no_carry           = 0
even_no_carry          = 0
odd_with_carry         = 0
odd_no_carry_no_zero   = 0
odd_with_carry_no_zero = 0
same_digit_no_carry    = 5

for a in range(10):
	for b in range(10):
		if (a+b)%2 == 1 and a+b < 10:
			odd_no_carry += 1
		elif (a+b)%2 == 0 and a+b < 10:
			even_no_carry += 1
		elif (a+b)%2 == 1 and a+b >= 10:
			odd_with_carry += 1
		if a*b == 0:
			continue
		if (a+b)%2 == 1 and a+b < 10:
			odd_no_carry_no_zero += 1
		elif (a+b)%2 == 1 and a+b >= 10:
			odd_with_carry_no_zero += 1

def solve(D):
	ans = 0
	for d in count(1):
		if 2*d > D:
			break
		ans += 	odd_no_carry_no_zero    * \
				odd_no_carry ** (d-1)
	for d in count(1):
		if 4*d - 1 > D:
			break
		ans += 	odd_with_carry_no_zero  * \
				odd_with_carry ** (d-1) * \
				even_no_carry ** (d-1)  * \
				same_digit_no_carry
	return ans

assert solve(3) == 120

print(solve(9))



# brute force (23m)
'''
total = 0
for a in range(1, 10**9):

	if a%10 == 0: continue

	astr = str(a)
	rstr = astr[::-1]
	r = int(rstr)

	s = str(a+r)
	if all(int(x)%2==1 for x in s):
		total += 1

		#print(astr)
		#print(rstr)
		#print()

		if any((int(astr[i])+int(rstr[i]))%2==0 and (int(astr[i])+int(rstr[i]))>=10 for i in range(len(astr))):
			input("***")

print(total)
input()
'''
