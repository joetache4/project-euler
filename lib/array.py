from itertools import combinations
from bisect import bisect

def binary_search(arr, target):
	'''Return index of target if contained within arr, else None.'''
	i = bisect(arr, target)
	return i-1 if arr[i-1] == target else None

def subsets(collection, min_size=0, max_size=None):
	'''
	Return subsets of collection, between the given sizes (inclusive). The empty set is returned when min_size is 0.

	Requirements:
	  collection must be convertable to a list.
	'''
	if max_size is None:
		max_size = len(collection)
	def _subsets(arr):
		for s in range(min_size, max_size+1):
			yield from combinations(collection, s)
	if isinstance(collection, list):
		yield from _subsets(collection)
	elif isinstance(collection, str):
		for x in _subsets(list(collection)):
			yield ''.join(x)
	elif isinstance(collection, set):
		for x in _subsets(list(collection)):
			yield set(x)
	else:
		raise ValueError("Collection must be a list, set, or string.")

def perm(n, arr):
	'''
	Returns the n-th permutation of arr.

	Requirements:
	  len(arr) > 1
	  n needs to between 0 and len(arr)! - 1
	'''
	# create list of factorials
	factorials = [0, 1]
	while len(arr) != len(factorials):
		factorials.append(factorials[-1] * len(factorials))
	factorials.reverse()
	# convert n to its representation in the factorial numbering system
	fact_index = 0
	m = 10 # 10 is used instead of 0 so m can be a a bunch of 0's if needed
	while n > 0:
		if n >= factorials[fact_index]:
			m += 1
			n -= factorials[fact_index]
		else:
			fact_index += 1
			m = 10 * m
	while fact_index < len(factorials)-1:
		m = 10 * m
		fact_index += 1
	m = [int(x) for x in str(m)]
	m.pop(0)
	# create permuted list
	new_arr = []
	for x in m:
		new_arr.append(arr.pop(int(x)))
	return new_arr

def cmp_to_key(mycmp):
    '''Convert a cmp= function into a key= function'''
    class K(object):
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K

# Old and slow
'''
def subsets(collection, min_size = 0, max_size = -1):
	def _subsets(arr, min_size, max_size, _subarr = None, _index = 0):
		# TODO this will cause a RecursionError if len(arr) >= 1000
		if _subarr is None:
			_subarr = []
		if max_size == -1:
			max_size = len(arr)
		if len(_subarr) > max_size or len(_subarr) + len(arr) - _index < min_size:
			return
		if _index == len(arr):
			yield _subarr.copy()
		else:
			yield from _subsets(arr, min_size, max_size, _subarr, _index + 1)
			_subarr.append(arr[_index])
			yield from _subsets(arr, min_size, max_size, _subarr, _index + 1)
			_subarr.pop()

	if isinstance(collection, list):
		yield from _subsets(collection, min_size, max_size)
	elif isinstance(collection, str):
		for x in _subsets(list(collection), min_size, max_size):
			yield ''.join(x)
	else:
		for x in _subsets(list(collection), min_size, max_size):
			yield set(x)

def binary_search(arr, target):
	L = 0
	R = len(arr) - 1
	while L <= R:
		mid = (L+R) // 2
		if accessor(arr[mid]) < target:
			L = mid + 1
		elif accessor(arr[mid]) > target:
			R = mid - 1
		else:
			return (mid, arr[mid])
	return (-1, None)

def permutations(arr, _ind = None):
	if _ind is None:
		_ind = []
	if len(_ind) == len(arr):
		yield [arr[i] for i in _ind]
	else:
		for i in range(len(arr)):
			if i not in _ind:
				_ind.append(i)
				yield from permutations(arr, _ind)
				_ind.pop()

'''
