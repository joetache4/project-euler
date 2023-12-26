'''
Joe Walter

difficulty: 30%
run time:   0:00
answer:     248155780267521

	***

119 Digit Power Sum

The number 512 is interesting because it is equal to the sum of its digits raised to some power: 5 + 1 + 2 = 8, and 83 = 512. Another example of a number with this property is 614656 = 284.

We shall define an to be the nth term of this sequence and insist that a number must contain at least two digits to have a sum.

You are given that a_2 = 512 and a_10 = 614656.

Find a_30.
'''

from itertools import count

def digit_sum(s):
	sum = 0
	while s > 0:
		sum += s%10
		s //= 10
	return sum

nums = []

for s in count(4):
	for p in count(2):
		a = s**p
		if digit_sum(a) == s:
			nums.append(a)
			nums.sort()
			#print(f"{s} ^ {p} == {a}")
		try:
			if a > nums[29]:
				# a will increase with each iteration, already bigger than our smallest 30
				break
		except IndexError:
			pass
		if len(str(a)) > s:
			# break once the average digit value of 'a' would need to be <1
			# TODO not guaranteed -- 'a' could be a number with a bunch of 0 digits, though this would make the number large and unlikely part of the smallest 30
			break
	try:
		if s//9 > len(str(nums[29])):
			# smallest number that could have this sum is bigger than our smallest 30
			break
	except IndexError:
		pass

print(sorted(nums)[29])
