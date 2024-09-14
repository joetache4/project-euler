'''
Joe Walter

difficulty: 20%
run time:   0:00
answer:     28684

	***

061 Cyclical Figurative Numbers

Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers are all figurate (polygonal) numbers and are generated by the following formulae:
Triangle       P3,n=n(n+1)/2     1, 3, 6, 10, 15, ...
Square         P4,n=n2           1, 4, 9, 16, 25, ...
Pentagonal     P5,n=n(3n−1)/2    1, 5, 12, 22, 35, ...
Hexagonal      P6,n=n(2n−1)      1, 6, 15, 28, 45, ...
Heptagonal     P7,n=n(5n−3)/2    1, 7, 18, 34, 55, ...
Octagonal      P8,n=n(3n−2)      1, 8, 21, 40, 65, ...

The ordered set of three 4-digit numbers: 8128, 2882, 8281, has three interesting properties.

    The set is cyclic, in that the last two digits of each number is the first two digits of the next number (including the last number with the first).
    Each polygonal type: triangle (P3,127=8128), square (P4,91=8281), and pentagonal (P5,44=2882), is represented by a different number in the set.
    This is the only set of 4-digit numbers with this property.

Find the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal type: triangle, square, pentagonal, hexagonal, heptagonal, and octagonal, is represented by a different number in the set.
'''

from math import sqrt
import lib.sequences as fig

F3 = [f for f in fig.triangular(10**4) if f > 999]
F4 = [f for f in fig.square(10**4) if f > 999]
F5 = [f for f in fig.pentagonal(10**4) if f > 999]
F6 = [f for f in fig.hexagonal(10**4) if f > 999]
F7 = [f for f in fig.heptagonal(10**4) if f > 999]
F8 = [f for f in fig.octagonal(10**4) if f > 999]

inv3 = lambda y: int(-1/2 + sqrt(1/4 + 2*y))
inv4 = lambda y: int(sqrt(y))
inv5 = lambda y: int(1/6 + sqrt(1/4 + 6*y)/3)
inv6 = lambda y: int(1/4 + sqrt(1 + 8*y)/4)
inv7 = lambda y: int(3/10 + sqrt(9/4 + 10*y)/5)
inv8 = lambda y: int(1/3 + sqrt(4 + 12*y)/6)

F = [F3, F4, F5, F6, F7, F8]
inv = [inv3, inv4, inv5, inv6, inv7, inv8]

def search_in_order(i1, i2, i3, i4, i5, i6):
	for n1 in F[i1]:
		end1 = n1 % 100
		for n2 in F[i2]:
			if n2//100 != end1:	continue
			end2 = n2 % 100
			for n3 in F[i3]:
				if n3//100 != end2:	continue
				end3 = n3 % 100
				for n4 in F[i4]:
					if n4//100 != end3:	continue
					end4 = n4 % 100
					for n5 in F[i5]:
						if n5//100 != end4:	continue
						end5 = n5 % 100
						for n6 in F[i6]:
							if n6//100 != end5:	continue
							end6 = n6 % 100
							if end6 == n1//100:
								indices = set()
								indices.add(inv[i1](n1))
								indices.add(inv[i2](n2))
								indices.add(inv[i3](n3))
								indices.add(inv[i4](n4))
								indices.add(inv[i5](n5))
								indices.add(inv[i6](n6))
								if len(indices) == 6:
									ans = [n1,n2,n3,n4,n5,n6]
									# print(ans)
									print(sum(ans))
									return True
	return False

def solve():
	i1 = 5 # smallest first, F8
	for i2 in [0, 1, 2, 3, 4]:
		for i3 in [0, 1, 2, 3, 4]:
			if i3 in [i2]: continue
			for i4 in [0, 1, 2, 3, 4]:
				if i4 in [i2, i3]: continue
				for i5 in [0, 1, 2, 3, 4]:
					if i5 in [i2, i3, i4]: continue
					for i6 in [0, 1, 2, 3, 4]:
						if i6 in [i2, i3, i4, i5]: continue
						if search_in_order(i1, i2, i3, i4, i5, i6):
							return

solve()