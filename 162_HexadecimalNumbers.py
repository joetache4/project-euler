'''
Joe Walter

difficulty: 45%
run time:   0:00
answer:     3D58725572C62302

	***

162 Hexadecimal Numbers

In the hexadecimal number system numbers are represented using 16 different digits:
0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F

The hexadecimal number AF when written in the decimal number system equals 10x16+15=175.

In the 3-digit hexadecimal numbers 10A, 1A0, A10, and A01 the digits 0,1 and A are all present.
Like numbers written in base ten we write hexadecimal numbers without leading zeroes.

How many hexadecimal numbers containing at most sixteen hexadecimal digits exist with all of the digits 0,1, and A present at least once?
Give your answer as a hexadecimal number.

(A,B,C,D,E and F in upper case, without any leading or trailing code that marks the number as hexadecimal and without leading zeroes , e.g. 1A3F and not: 1a3f and not 0x1a3f and not $1A3F and not #1A3F and not 0000001A3F)
'''

from lib.array import subsets

base    = 16
length  = 16
include = '01A'

def count(base, length):
	'''Count the integers up to the given length, in the given base.'''
	return base**length

def count_without(base, length, exclude):
	'''Count the integers up to the given length, in the given base, with the given digits simulataneously not present.'''
	num_excluded = len(exclude)
	# If each excluded digit is non-zero, then it's no different than if the base were shrunk by that amount
	c = count(base - num_excluded, length)
	if '0' in exclude:
		# If zero is excluded, then we need to "add back" integers with only leading zeros
		# e.g., for length 4 the following integers were not counted in the previous step, but need to included:
		#    2
		#   35
		#  666
		# (if padded to length 4, any number with leading zeros and no zeros elsewhere)
		for sub_length in range(1, length):
			c += count(base - num_excluded, sub_length)
	return c

def count_with(base, length, include):
	'''Count the integers up to the given length, in the given base, with the given digits each present at least once.'''
	ans = 0
	# repeated use of the identity count(X+Y) = count(X) + count(Y) - count(X*Y)
	for s in subsets(include, 0):
		ans += ((-1)**len(s)) * count_without(base, length, s)
	return f"{ans:x}".upper()

print(count_with(base, length, include))

'''
ans = count(base, length) - (
	count_without(base, length, '0') + count_without(base, length, '1') + count_without(base, length, 'A') - (
		count_without(base, length, '01') + count_without(base, length, '0A') + count_without(base, length, '1A') - (
			count_without(base, length, '01A')
		)
	)
)
'''
