import numpy as np
from copy import deepcopy

def mpow(mat, pow, mod=None):
	'''
	Exponentiate a matrix.

	mat = numpy matrix
	pow = positive integer exponent
	mod = optional modulus
	'''
	if pow <= 0 or not isinstance(pow, int):
		raise ValueError("pow must be a positive int.")
	if mod is None:
		mod=float("inf")
	if pow == 1:
		pass
	elif pow%2 == 1:
		mat = (mat*mpow(mat, pow-1, mod)) % mod
	else:
		mat = mpow(mat, pow//2, mod)
		mat = (mat*mat) % mod
	return mat % mod

# for when np.uint64 is too small
class matrix:
	def __init__(self, array):
		self.array = array

	def __getitem__(self, ind):
		return self.array[ind[0]][ind[1]]

	def __setitem__(self, ind, val):
		self.array[ind[0]][ind[1]] = val

	def dim(self):
		return len(self.array), len(self.array[0])

	def __mod__(self, mod):
		val = deepcopy(self)
		h, w = self.dim()
		for i in range(h):
			for j in range(w):
				val[i,j] %= mod
		return val

	def __mul__(self, other):
		# see Strassen algorithm
		val = deepcopy(self)
		h, w = self.dim()
		for i in range(h):
			for j in range(w):
				val[i,j] = sum(self[i,k]*other[k,j] for k in range(w))
		return val

	def exp(self, pow, mod=None):
		return mpow(self, pow, mod)

	def __str__(self):
		return str(self.array)
