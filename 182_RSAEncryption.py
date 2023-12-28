'''
Joe Walter

difficulty: 60%
run time:   1:30
answer:     399788195976

	***

182 RSA Encryption

The RSA encryption is based on the following procedure:

Generate two distinct primes p and q.
Compute n = pq and phi = (p-1)(q-1).
Find an integer e, 1 < e < phi, such that gcd(e, phi) = 1.

A message in this system is a number in the interval [0, n-1].
A text to be encrypted is then somehow converted to messages (numbers in the interval [0, n-1]).
To encrypt the text, for each message, m, c = m^e mod n is calculated.

To decrypt the text, the following procedure is needed: calculate d such that ed = 1 mod phi, then for each encrypted message, c, calculate m = c^d mod n.

There exist values of e and m such that m^e mod n = m.
We call messages m for which m^e mod n = m unconcealed messages.

An issue when choosing e is that there should not be too many unconcealed messages.For instance, let p = 19 and q = 37.
Then n = 19 x 37 = 703 and phi = 18 x 36 = 648.
If we choose e = 181, then, although gcd(181, 648) = 1 it turns out that all possible messages m (0 <= m <= n-1) are unconcealed when calculating m^e mod n.
For any valid choice of e there exist some unconcealed messages.
It's important that the number of unconcealed messages is at a minimum.

Choose p = 1009 and q = 3643.
Find the sum of all values of e, 1 < e < phi(1009, 3643) and gcd(e, phi) = 1, so that the number of unconcealed messages for this value of e is at a minimum.
'''

from math import gcd, lcm
from collections import Counter

p, q = 1009, 3643
n, phi = p*q, (p-1)*(q-1)

a = lcm(p-1, q-1)+1
f = lambda n: (a+n)/(n+1)
E = sorted(int(f(n)) for n in range(a) if int(f(n))==f(n))

E_range = range(len(E))
count_minimal = [0]*len(E)

for m in range(n):
	for i in E_range:
		if pow(m,E[i],n) == m:
			count_minimal[i] += 1
			break

count = Counter()

for e,c in zip(E,count_minimal):
	d = e-1
	_e = e
	while _e < phi:
		if gcd(_e, phi) == 1:
			count[_e] += c
		_e += d

min_count = min(count.values())
ans = sum(e for e,c in count.items() if c==min_count)
print(ans)


# all equal
# print(pow(9,50989+50988*0,n))
# print(pow(9,50989+50988*1,n))
# print(pow(9,50989+50988*2,n))
# print(pow(9,50989+50988*3,n))
# print(pow(9,(50989+1)/2,n))
# print(pow(9,(50989+2)/3,n))
# print(pow(9,(50989+3)/4,n))
# print(pow(9,50989*50989,n))

# brute search, minimal e seen in the first 5000 m
# [2, 15, 113, 337, 505, 608, 1009, 1215, 1822, 2429, 3643, 4250, 4857, 5464, 7285, 8499, 9713, 10927, 12748, 14569, 16997, 21853, 25495, 29137, 33993, 38242, 43705, 50989, 67985, 76483, 87409, 101977, 152965, 203953, 305929, 611857]

# if pow(m,e,n) == m, this might not be the minimal e for m
# it could be (e+1)/2, (e+2)/3, (e+3)/4, etc. if these are integers

# above pattern with e starting as 611857, 3643, and 1009
# (notice 3643 and 1009 show up in the 611857 pattern)
# (also notice 611857=lcm(1009-1,3643-1)+1)
# [611857, 305929, 203953, 152965, 101977, 87409, 76483, 67985, 50989, 43705, 38242, 33993, 29137, 25495, 21853, 16997, 14569, 12748, 10927, 9713, 8499, 7285, 5464, 4857, 4250, 3643, 2429, 1822, 1215, 1009, 608, 505, 337, 253, 169, 145, 127, 113, 85, 73, 64, 57, 49, 43, 37, 29, 25, 22, 19, 17, 15, 13, 10, 9, 8, 7, 5, 4, 3, 2]
# [3643, 1822, 1215, 608, 7, 4, 3, 2]
# [1009, 505, 337, 253, 169, 145, 127, 113, 85, 73, 64, 57, 49, 43, 37, 29, 25, 22, 19, 17, 15, 13, 10, 9, 8, 7, 5, 4, 3, 2]

# combined and sorted
# E = [2, 3, 4, 5, 7, 8, 9, 10, 13, 15, 17, 19, 22, 25, 29, 37, 43, 49, 57, 64, 73, 85, 113, 127, 145, 169, 253, 337, 505, 608, 1009, 1215, 1822, 2429, 3643, 4250, 4857, 5464, 7285, 8499, 9713, 10927, 12748, 14569, 16997, 21853, 25495, 29137, 33993, 38242, 43705, 50989, 67985, 76483, 87409, 101977, 152965, 203953, 305929, 611857]

# Confirmed that all m are unconcealed by at least one of these e listed

# counts of m with the corresponding minimal e
# (keep in mind if e leaves m unconcealed, then so does 2*e-1, 3*e-2, etc.)
# count = [4, 5, 12, 6, 28, 12, 12, 24, 36, 24, 24, 60, 60, 72, 36, 84, 156, 144, 72, 144, 168, 216, 144, 360, 336, 432, 504, 864, 1008, 1212, 2016, 2424, 6060, 2424, 15756, 3636, 4848, 10908, 19392, 10908, 9696, 32724, 29088, 38784, 14544, 43632, 87264, 77568, 29088, 65448, 87264, 116352, 58176, 196344, 174528, 232704, 261792, 465408, 523584, 1047168]
