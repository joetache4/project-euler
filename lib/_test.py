import math
from random import randint

import pytest

from . import num
from . import gints
from . import sequences
from . import array
from . import string
from . import geom
from . import helpers

class TestLib:

	primes = num.get_primes(10**5)

	def test_get_primes(self):
		assert num.get_primes(1000) == [x for x in range(1001) if num.is_prime(x)]

	def test_is_prime_trial_division(self):
		assert num.is_prime_trial_division(2)
		assert num.is_prime_trial_division(13)
		assert num.is_prime_trial_division(7919)
		assert num.is_prime_trial_division(1046527)
		assert not num.is_prime_trial_division(1)
		assert not num.is_prime_trial_division(63)
		assert not num.is_prime_trial_division(7919*1046527)

	def test_factor(self):
		assert num.factor(2) == [2]
		assert num.factor(16) == [2, 2, 2, 2]
		assert num.factor(7919*1046527) == [7919, 1046527]
		assert num.factor(2*2*7*11, num.get_primes(2*2*7*11)) == [2,2,7,11]

	'''
	def test_factorial(self):
		assert num.factorial(0) == 1
		assert num.factorial(1) == 1
		assert num.factorial(2) == 2
		assert num.factorial(5) == 120

	def test_gcd(self):
		assert num.gcd(4, 8) == 4
		assert num.gcd(12, 8) == 4
		assert num.gcd(4, 9) == 1
		assert num.gcd(1, 8) == 1
		assert num.gcd(0, 8) == 8
		assert num.gcd(0, 0) == 0

	def test_lcm(self):
		assert num.lcm(1, 13) == 13
		assert num.lcm(3, 5) == 15
		assert num.lcm(9, 15) == 45
		assert num.lcm(0, 15) == 0
		assert num.lcm(0, 0) == 0
	'''

	def test_extended_gcd(self):
		assert num.extended_gcd(4, 8) == (4, 1, 0)
		assert num.extended_gcd(12, 8) == (4, 1, -1)
		assert num.extended_gcd(4, 9) == (1, -2, 1)
		assert num.extended_gcd(1, 8) == (1, 1, 0)
		#assert num.extended_gcd(0, 8) == 8
		#assert num.extended_gcd(0, 0) == 0

	def test_totient(self):
		assert num.totient(1) == 1
		assert num.totient(2) == 1
		assert num.totient(31) == 30
		assert num.totient(7*11) == 6 * 10
		assert num.totient(3*5*11) == 2 * 4 * 10
		assert num.totient(3*3*11) == num.totient(3*3) * 10
		assert num.totient(3*3*11, TestLib.primes) == num.totient(3*3) * 10

	def test_divisors(self):
		assert num.divisors(0) == None
		assert num.divisors(1) == set([1])
		assert num.divisors(10) == set([1,2,5,10])
		assert num.divisors(12, TestLib.primes) == set([1,2,3,4,6,12])

	def test_count_divisors(self):
		assert num.count_divisors(0) == 0
		assert num.count_divisors(1) == 1
		assert num.count_divisors(2) == 2
		assert num.count_divisors(12, TestLib.primes) == 6

	def test_miller_rabin(self):
		assert num.miller_rabin(2) == True
		assert num.miller_rabin(3) == True

		primes = num.get_primes235(100)
		for n in range(2,100):
			if n in primes:
				assert num.miller_rabin(n)
			else:
				assert not num.miller_rabin(n)

		# Mersenne primes
		for p in [2,3,5,7,13,17,19,31,61]:
			assert num.miller_rabin(2**p - 1) == True

		for n in range(4, 10**10, 77778):
			assert num.miller_rabin(n) == False

		assert num.miller_rabin(10**10) == False
		assert num.miller_rabin(2**63) == False

	def test_subsets(self):
		a = [1,2,3]
		b = list(array.subsets(a))
		c = [[],[1],[2],[3],[1,2],[2,3],[1,3],[1,2,3]]
		for item in b:
			assert item in c
		assert len(b) == 2**len(a)
		assert a == [1,2,3]
		a = []
		b = list(array.subsets(a))
		assert b == [[]]

	def test_min_superstring(self):
		assert string.min_superstring(["CATGC", "CTAAGT", "GCTA", "TTCA", "ATGCATC"]) == "GCTAAGTTCATGCATC"

	def test_binary_search(self):
		for i in range(1000):
			arr = [randint(-1000,1000) for n in range(100)]
			tar = arr[0]
			arr = sorted(arr)
			assert array.binary_search(arr, tar)
			assert array.binary_search(arr, 1001 + randint(0,1000))

	def test_geom_point(self):
		p1 = geom.Point(0,0)
		p2 = geom.Point(0,1)
		p3 = geom.Point(1,1)
		assert math.isclose(p1.angle(p2, p3), math.pi/4)
