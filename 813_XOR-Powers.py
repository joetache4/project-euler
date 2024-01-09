r'''
Joe Walter

difficulty: 20%
run time:   0:00
answer:     14063639

	***

813 XOR-Powers

<p>We use $x\oplus y$ to be the bitwise XOR of $x$ and $y$.</p>

<p>Define the <dfn>XOR-product</dfn> of $x$ and $y$, denoted by $x \otimes y$, similar to a long multiplication in base $2$, except that the intermediate results are XORed instead of the usual integer addition.</p>

<p>For example, $11 \otimes 11 = 69$, or in base $2$, $1011_2 \otimes 1011_2 = 1000101_2$:</p>
$$
\begin{align*}
\phantom{\otimes 1111} 1011_2 \\
\otimes \phantom{1111} 1011_2 \\
\hline
\phantom{\otimes 1111} 1011_2 \\
\phantom{\otimes 111} 1011_2 \phantom{9} \\
\oplus \phantom{1} 1011_2  \phantom{999} \\
\hline
\phantom{\otimes 11} 1000101_2 \\
\end{align*}
$$
Further we define $P(n) = 11^{\otimes n} = \overbrace{11\otimes 11\otimes \ldots \otimes 11}^n$. For example $P(2)=69$.

<p>Find $P(8^{12}\cdot 12^8)$. Give your answer modulo $10^9+7$.</p>
'''

class SparseNum:
	'''A number with few ones in its binary representation.'''
	def __init__(self, num):
		self.ones = set()
		for i in range(num.bit_length()):
			if num&(1<<i):
				self.ones.add(i)
	def __mul__(self, other):
		a = SparseNum(0)
		for i in other.ones:
			for j in self.ones:
				try:
					a.ones.remove(i+j)
				except KeyError:
					a.ones.add(i+j)
		return a
	def pow(self, k):
		if k == 1:
			return self
		elif k%2 == 1:
			return self*self.pow(k-1)
		else:
			return self.pow(k//2).square()
	def square(self):
		a = SparseNum(0)
		for i in self.ones:
			a.ones.add(2*i)
		return a
	def __mod__(self, mod):
		return sum(pow(2,i,mod) for i in self.ones)%mod
	def __eq__(self, other):
		if type(other) is SparseNum:
			return self.ones == other.ones
		elif type(other) is int:
			return self % (2**63-1) == other

for i in range(100):
	n = SparseNum(i)
	assert n.square() == n*n

assert SparseNum(11).square() == 69

n = SparseNum(11).pow(8**12*12**8) % (10**9+7)
print(n)


# Trivia
# coefficients to each x^n of (x^3+x+1)^(8^12*12^8) tells how many times to xor-add 2^n
