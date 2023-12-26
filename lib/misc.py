# methods that aren't really useful right now
# may be more helpful for brainstorming ideas

def isnumeric(n):
	return type(n) is int or type(n) is float

# convert to reverse Polish notation
# https://en.wikipedia.org/wiki/Shunting_yard_algorithm

import re

def precedence(f, g):
	if f == g:
		return 0
	if f == "^":
		return -1
	if f in ["*", "/"] and g in ["+", "-"]:
		return -1
	return 1

# TODO accept negation (-) by converting it to neg()
def lexer(s):
	s = s.replace(" ", "")
	s = s.replace(",", " ")
	s = s.replace("**", "^")
	s = s.replace("^", " ^ ")
	s = s.replace("*", " * ")
	s = s.replace("/", " / ")
	s = s.replace("+", " + ")
	s = s.replace("-", " - ")
	s = s.replace("(", " ( ")
	s = s.replace(")", " ) ")
	s = s.replace("  ", " ")
	return s.split(" ")

# Does not implement composite functions, functions with a variable number of arguments, or unary operators
# Assumes variables are 1 character long and function names are more than 1 character long
def reverse_polish_notation(s):
	out = []
	op  = []
	for tok in lexer(s):
		if re.fullmatch("\d+\.?\d*", tok):
			# number
			out.append(tok)
		elif len(tok) > 1:
			# function
			op.append(tok)
		elif tok == "(":
			op.append(tok)
		elif tok == ")":
			assert len(op) > 0
			while op[-1] != "(":
				out.append(op.pop())
			op.pop()
			if len(op[-1]) > 1:
				out.append(op.pop())
		elif tok in "^*/+-":
			# operator
			while len(op) > 0 and op[-1] != "(" and (precedence(tok, op[-1]) == 1 or (precedence(tok, op[-1]) == 0 and tok != "^")):
				out.append(op.pop())
			op.append(tok)
		else:
			# variable or constant
			out.append(tok)
	while len(op) > 0:
		assert op[-1] != "("
		out.append(op.pop())
	return " ".join(str(a) for a in out)

f = "3 + 4 * 2 / ( x - 5 ) ^ 2 ^ 3" # expected: 3 4 2 * x 5 - 2 3 ^ ^ / +
#f = "sin ( max ( 2, 3 ) / 3 * π )" # expected: 2 3 max 3 / π * sin
print(reverse_polish_notation(f))



# find a root of an expression

from math import sqrt

def sign(n):
	if n < 0:
		return -1
	elif n == 0:
		return 0
	else:
		return 1

# This could fail for a variety of reasons, such as no roots, muliple roots, complex values, and division by zero
# TODO handle ZeroDivisionError
def root(f, a=0, b=1, precision=0.0000001):
	# find bounds which have opposite signs
	while sign(f(a))*sign(f(b)) == 1:
		b *= -1.1
	# repeatedly replace one bound with midpoint
	while abs(a-b) > precision:
		c = (a+b)/2
		if sign(f(b))*sign(f(c)) == 1:
			b = c
		else:
			a = c
	return a

f = lambda x: x**3 - 3**x
x = root(f, 0, -2)
print(x)
print(f(x))



# calculate derivative for any arithmetic expression

import math

# TODO reduce number of printed parentheses
# TODO further simplify expressions by combining like terms. see http://www.semdesigns.com/Products/DMS/SimpleDMSDomainExample.html
class term:
	def __init__(self, *inputs):
		self.inputs = []
		for i in inputs:
			if isnumeric(i):
				i = const(i)
			self.inputs.append(i)
	def __getitem__(self, i):
		return self.inputs[i]
	def __setitem__(self, i, v):
		self.inputs[i] = v
	def __eq__(self, other):
		return type(self) is type(other) and self.inputs == other.inputs
	def __call__(self, x=None, **vars):
		if x is not None:
			assert "x" not in vars
			vars["x"] = x
		return self._value(vars)
	def __add__(self, other):
		return add(self, other)
	def __radd__(self, other):
		return self.__add__(other)
	def __sub__(self, other):
		return sub(self, other)
	def __rsub__(self, other):
		return self.__sub__(other)
	def __mul__(self, other):
		return mul(self, other)
	def __rmul__(self, other):
		return self.__mul__(other)
	def __truediv__(self, other):
		return div(self, other)
	def __rtruediv__(self, other):
		return self.__div__(other)
	def __pow__(self, other):
		return exp(self, other)
	def __rpow__(self, other):
		return self.__pow__(other)
	def __neg__(self):
		return neg(self)
	def __pos__(self):
		return self
	def _simplify(self):
		return self
	def d(self, x):
		return self._d(x)._simplify()

class const (term):
	def __init__(self, a):
		self.inputs = [a]
	def _d(self, x):
		return const(0)
	def _value(self, vars):
		return self[0]
	def __str__(self):
		return str(self[0])
		
class var (term):
	def _d(self, x):
		if self[0] == x:
			return const(1)
		else:
			return const(0)
	def _value(self, vars):
		try:
			return vars[self[0]]
		except KeyError:
			return self
	def __str__(self):
		return str(self[0])

class add (term):
	def _d(self, x):
		return self[0]._d(x) + self[1]._d(x)
	def _value(self, vars):
		return self[0]._value(vars) + self[1]._value(vars)
	def __str__(self):
		return f"({self[0]}+{self[1]})"
	def _simplify(self):
		self[0] = self[0]._simplify()
		self[1] = self[1]._simplify()
		if self[0] == const(0):
			return self[1]
		if self[1] == const(0):
			return self[0]
		if type(self[0]) is const and type(self[1]) is const:
			return const(self[0].f + self[1].f)
		return self

class sub (term):
	def _d(self, x):
		return self[0]._d(x) - self[1]._d(x)
	def _value(self, vars):
		return self[0]._value(vars) - self[1]._value(vars)
	def __str__(self):
		return f"({self[0]}-{self[1]})"
	def _simplify(self):
		self[0] = self[0]._simplify()
		self[1] = self[1]._simplify()
		if self[0] == self[1]:
			return const(0)
		if self[1] == const(0):
			return self[0]
		if type(self[0]) is const and type(self[1]) is const:
			return const(self[0].f - self[1].f)
		return self

class neg (term):
	def _d(self, x):
		return -self[0]._d(x)
	def _value(self, vars):
		return -self[0]._value(vars)
	def __str__(self):
		return f"(-{self[0]})"
	def _simplify(self):
		self[0] = self[0]._simplify()
		if self[0] == const(0):
			return const(0)
		return self

class mul (term):
	def _d(self, x):
		return self[0] * self[1]._d(x) + self[0]._d(x) * self[1]
	def _value(self, vars):
		return self[0]._value(vars) * self[1]._value(vars)
	def __str__(self):
		return f"({self[0]}*{self[1]})"
	def _simplify(self):
		self[0] = self[0]._simplify()
		self[1] = self[1]._simplify()
		if self[0] == const(0) or self[1] == const(0):
			return const(0)
		if self[0] == const(1):
			return self[1]
		if self[1] == const(1):
			return self[0]
		if type(self[0]) is const and type(self[1]) is const:
			return const(self[0].f * self[1].f)
		return self

class div (term):
	def _d(self, x):
		return (self[1] * self[0]._d(x) - self[1]._d(x) * self[0]) / (self[1] * self[1])
	def _value(self, vars):
		return self[0]._value(vars) / self[1]._value(vars)
	def __str__(self):
		return f"({self[0]}/{self[1]})"
	def _simplify(self):
		self[0] = self[0]._simplify()
		self[1] = self[1]._simplify()
		if self[0] == self[1]:
			return const(1)
		if self[0] == const(0):
			return const(0)
		if self[1] == const(1):
			return self[0]
		if type(self[0]) is const and type(self[1]) is const:
			return const(self[0].f / self[1].f)
		return self

class log (term):
	def _d(self, x):
		return (
			(log(self[1], math.e) * self[0]._d(x) / self[0]) -
			(log(self[0], math.e) * self[1]._d(x) / self[1])
			) / (log(self[1], math.e) ** 2)
	def _value(self, vars):
		return math.log(self[0]._value(vars)) / math.log(self[1]._value(vars))
	def __str__(self):
		return f"log({self[0]}, {self[1]})"
	def _simplify(self):
		self[0] = self[0]._simplify()
		self[1] = self[1]._simplify()
		if self[0] == const(1):
			return const(0)
		if self[0] == self[1]:
			return const(1)
		return self
	
class exp (term):
	def _d(self, x):
		return self * (div(self[1], self[0]) * self[0]._d(x) + self[1]._d(x) * log(f, math.e))
	def _value(self, vars):
		return self[0]._value(vars) ** self[1]._value(vars)
	def __str__(self):
		return f"({self[0]}**{self[1]})"
	def _simplify(self):
		self[0] = self[0]._simplify()
		self[1] = self[1]._simplify()
		if self[1] == const(0):
			return const(1)
		if self[0] == const(1):
			return const(1)
		if self[0] == const(0):
			return const(0)
		return self

class sin (term):
	def _d(self, x):
		return cos(self[0]) * self[0]._d(x)
	def _value(self, vars):
		v = self[0]._value(vars)
		if isnumeric(v):
			return math.sin(v)
		elif type(v) is const:
			return math.sin(v[0])
		else:
			return sin(v)
	def __str__(self):
		return f"sin({self[0]})"

class cos (term):
	def _d(self, x):
		return -sin(self[0]) * self[0]._d(x)
	def _value(self, vars):
		v = self[0]._value(vars)
		if isnumeric(v):
			return math.cos(v)
		elif type(v) is const:
			return math.cos(v[0])
		else:
			return cos(v)
	def __str__(self):
		return f"cos({self[0]})"

'''
a = const(1)
b = const(2)
c = const(0)
d = const(3)
print(a+b==c+d)

x = var('x')
y = var('y')
#f = (x**3)/(x**log(x, 3))
f = cos(x**2)
print(f)
print(f(2))
print(f(x=2))
print(f(y=2))
print(f.d('x'))
print(f.d('y'))
print()

f = cos(4)
print(f)
f = cos(const(4))
print(f)
print(f.d('x'))
print()

g = x*y + x**2
print(g)
print(g.d('x'))
'''
