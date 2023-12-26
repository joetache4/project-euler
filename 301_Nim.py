'''
Joe Walter

difficulty: 15%
run time:   0:00
answer:     2178309

	***

301 Nim

Nim is a game played with heaps of stones, where two players take it in turn to remove any number of stones from any heap until no stones remain.

We'll consider the three-heap normal-play version of Nim, which works as follows:

    At the start of the game there are three heaps of stones.
    On each player's turn, the player may remove any positive number of stones from any single heap.
    The first player unable to move (because no stones remain) loses.

If (n1,n2,n3) indicates a Nim position consisting of heaps of size n1, n2, and n3, then there is a simple function, which you may look up or attempt to deduce for yourself, X(n1,n2,n3) that returns:

    * zero if, with perfect strategy, the player about to move will eventually lose; or
    * non-zero if, with perfect strategy, the player about to move will eventually win.

For example X(n1,n2,n3)=0 because, no matter what the current player does, the opponent can respond with a move that leaves two heaps of equal size, at which point every move by the current player can be mirrored by the opponent until no stones remain; so the current player loses. To illustrate:

    * current player moves to (1,2,1)
	* opponent moves to (1,0,1)
	* current player moves to (0,0,1)
	* opponent moves to (0,0,0), and so wins.

For how many positive integers n<=2**30 does X(n,2n,3n)=0?

	***

Solution

X(a,b,c) = 0 iff. (a xor b xor c) = 0
	see https://web.mit.edu/sp.268/www/nim.pdf
X(n,2n,3n) = 0 iff. (n xor 2n) == 3n == (n + 2n) iff. there are no consecutive 1s in the binary representation of n
|{x:x has n digits in binary and no consecutive 1s}| = n-th Fibonacci number (where f(1)=1, f(2)=1)
The sum of the first n Fibonnaci numbers is f(n+2)-1
Add 1 to account for the only 31-digit number (2**30)
'''

from lib.sequences import nth_fibonacci as f

p = 30
print(f(p+2))
