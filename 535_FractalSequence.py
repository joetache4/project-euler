'''
Joe Walter

difficulty: 60%
run time:   0:00
answer:     611778217

    ***

535 Fractal Sequence

Consider the infinite integer sequence S starting with:
S = 1,1,2,1,3,2,4,1,5,3,6,2,7,8,4,9,1,10,11,5,...

Circle the first occurrence of each integer.
S = ①,1,②,1,③,2,④,1,⑤,3,⑥,2,⑦,⑧,4,⑨,1,⑩,⑪,5,...

The sequence is characterized by the following properties:

    * The circled numbers are consecutive integers starting with 1.
    * Immediately preceding each non-circled numbers a_i, there are exactly floor(sqrt(a_i)) adjacent circled numbers.
    * If we remove all circled numbers, the remaining numbers form a sequence identical to S, so S is a fractal sequence.

Let T(n) be the sum of the first n elements of the sequence.
You are given T(1)=1, T(20)=86, T(10**3)=364089 and T(10**9)=498676527978348241.

Find T(10**18). Give the last digits of your answer.
'''

from math import isqrt

def S(n):
    '''Returns a list of the first n numbers of S.'''
    s = [1]*n
    N = 2
    i = 0
    j = 1
    while j < n:
        s[j] = s[i]
        i += 1
        j += 1
        for _ in range(min(isqrt(s[i]), n-j)):
            s[j] = N
            j += 1
            N += 1
    return s

def sum_isqrt_1_to_n(n):
    '''Returns sum(isqrt(x) for x in range(1, n+1)).'''
    # 1 + 1 + 1 +
    # 2 + 2 + 2 + 2 + 2 +
    # 3 + 3 + 3 + 3 + 3 + 3 + 3 + ...
    sm = 0
    sr = isqrt(n)
    # sum of previous groups
    # sum i=1 to sr-1 of i*(2*i+1) = 2*i**2 + i
    m = sr-1
    sm += (4*m+5)*(m+1)*m//6
    # partial sum of last group
    sm += (n-(sr**2-1))*sr
    return sm

class Number:
    '''Represents a number at a certain position in the sequence S.'''
    def __init__(self, index, val, lval, sum_reg, sum_isqrt):
        '''
        index     = the position of this Number in the sequence S (0- or 1-indexed both work)
        val       = the actual number value
        lval      = the value of the Number immediately to the left in S
        sum_reg   = the sum of all numbers up to and including this one in S
        sum_isqrt = the sum of the isqrt of all numbers up to and including this one in S
        '''
        self.index     = index
        self.val       = val
        self.lval      = lval
        self.sum_reg   = sum_reg
        self.sum_isqrt = sum_isqrt
    def map(self, it=1):
        '''
        Returns the Number this is mapped to after placing the entire sequence S into its uncircled spots.

        it = how many times to repeat this process
        '''
        A = self
        for _ in range(it):
            i = A.sum_isqrt
            A = Number(
                index     = A.index + i,
                val       = A.val,
                lval      = i,
                sum_reg   = A.sum_reg + i*(i+1)//2,
                sum_isqrt = i + sum_isqrt_1_to_n(i)
            )
        return A
    def left(self):
        '''Returns the Number immediately to the left in the sequence. Only works when going to a 'circled' number in S.'''
        return Number(
            index     = self.index - 1,
            val       = self.lval,
            lval      = self.lval - 1,
            sum_reg   = self.sum_reg - self.val,
            sum_isqrt = self.sum_isqrt - isqrt(self.val)
        )
    def update(self, other):
        '''Copy another Number into this object.'''
        self.index     = other.index
        self.val       = other.val
        self.lval      = other.lval
        self.sum_reg   = other.sum_reg
        self.sum_isqrt = other.sum_isqrt

def update_A_and_B(A, B, n):
    '''
    Being a fractal sequence, all of S can be mapped onto the uncircled spots of S. Consider two numbers A and B that will be mapped into new positions A' and B'. After mapping S, there is a range of values between A' and B', larger than between A and B. The range shifts and grows for each subsequent mapping. For certain initial A and B this (A'-inclusive, A''-inclusive, etc.) range eventually contains the n-th number in S. Call such pairs (A,B) "appropriate".

    Additionally, if A and B are adjacent, then all numbers between A' and B' are circled. Note that A' and B' are no longer adjacent.

    The strategy then is to start with A=S_1 and B=S_2 (which is an appropriate pair in all cases of n), and look at the range between A' and B'. Update A and B to be the adjacent pair of appropriate numbers in this range. Repeat this, and eventually A will be the n-th number.

    Technical Details:

    Accept Numbers A and B such that A.map(k).index <= n and B.map(k).index > n for some integer k.

    Update A and B in place to Numbers A2 and B2 such that
        A.map(1).index <= A2.index = B2.index-1 < B.map(1).index and
        A2.map(k-1).index <= n and B2.map(k-1).index > n.
    '''
    assert B.index <= n

    # find the number of iterations k needed
    # so that A.map(k).index <= n and B.map(k).index > n
    k = 0
    _A, _B = A, B
    while _B.index <= n:
        _A, _B = _A.map(), _B.map()
        k += 1

    assert _A.index <= n and _B.index >  n

    # look at all the Numbers between A.map(1) and B.map(1)
    A.update(A.map())
    B.update(B.map())
    L = B.left()
    while L.index > A.index:
        if L.map(k-1).index > n:
            B.update(L)
        else:
            A.update(L)
            break
        L = L.left()

def T(n):
    '''Update A and B until A is the n-th Number.'''
    A = Number(1,1,-1,1,1) # Numbers are 1-indexed
    B = Number(2,1, 1,2,2)
    while A.index != n:
        update_A_and_B(A, B, n)
    return A.sum_reg

assert T(1)     == 1
assert T(20)    == 86
assert T(10**3) == 364089
assert T(10**9) == 498676527978348241

for i in range(2, 20):
    assert T(i) == sum(S(i))

print(T(10**18) % 10**9) # 611778217





# Generate the sequence
'''
from queue import Queue
from itertools import islice

def S(n):
    def _S():
        yield 1
        yield 1
        q = Queue()
        q.put(1)
        high = 2
        while True:
            n = q.get()
            for _ in range(isqrt(n)):
                yield high
                q.put(high)
                high += 1
            yield n
            q.put(n)
    yield from islice(_S(), n)
'''
