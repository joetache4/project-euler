'''
Joe Walter

difficulty: 30%
run time:   0:00
answer:     18934502

	***

506 Clock Sequence

Consider the infinite counteating sequence of digits : (
1234321234321234321...

Amazingly, you can break this sequence of digits into a sequence of integers such that the sum of the digits in the n'th value is n.

The sequence goes as follows : (
1, 2, 3, 4, 32, 123, 43, 2123, 432, 1234, 32123, ...

Let vn be the n'th value in this sequence. For example, v2 = 2, v5 = 32 and v11 = 32123.

Let S(n) be v1 + v2 + ... + vn. For example, S(11) = 36120, and S(1000) mod 123454321 = 18232686.

Find S(10^14) mod 123454321.

	***

Observations

Notice that:
	Sequence has a period of 6
	Any 6 consecutive terms sum to 15
	For 1<=n<=15, it is seen that n == sum_digits(v_n)
	To get v_(n+15), just append the next 6 terms to v_n

Also note:
	1000001000001...000001 (x 1's) == (10^(6x)-1)/999999
	1000002000003...00000x         == ((10^(6x)-1)/999999 - x)/999999

For each index i,
	Define "strain" to be all v_j s.t. (j-1)%15 == i
	Define n = v_i
	Define k = the next six consecutive digits in the sequence after the last digit of v_i

	If size(strain) == x, then:
	sum(strain) == 1000001000001...000001*n + 1000002000003...00000x*k
'''

from lib.num import mod_inverse

M = 123454321

def sum_strain(index, size):
	n, k = {
		1  : (1     ,234321),
		2  : (2     ,343212),
		3  : (3     ,432123),
		4  : (4     ,321234),
		5  : (32    ,123432),
		6  : (123   ,432123),
		7  : (43    ,212343),
		8  : (2123  ,432123),
		9  : (432   ,123432),
		10 : (1234  ,321234),
		11 : (32123 ,432123),
		12 : (43212 ,343212),
		13 : (34321 ,234321),
		14 : (23432 ,123432),
		15 : (123432,123432)
	}[index]
	inv = mod_inverse(999999, M)
	a  = n*(pow(10,6*size,M)-1)*inv
	a += k*(((pow(10,6*size,M)-1)*inv - size)*inv)
	return a % M

def strain_sizes(n, num_strains=15):
	q, r = n//num_strains, n%num_strains
	for i in range(1, num_strains+1):
		yield (i, q + (1 if i <= r else 0))

def S(n):
	a = 0
	for index, size in strain_sizes(n):
		a += sum_strain(index, size)
	return a % M

assert S(  11) == 36120
assert S(1000) == 18232686

print(S(10**14))


'''
Interesting tidbit:

https : www.reddit.com/r/math/comments/3bjk2a/1234321234321/

This sequence was made by taking traingular numbers modulo M=15. Sequences with similar properties as this can be made by taking triangular number modulo a different M. For example,
1,2,... (M = 3)
1,2,2,... (M = 5)
1,2,3,1,... (M = 7)
'''
