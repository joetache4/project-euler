'''
Joe Walter

difficulty: 10%
run time:   0:00
answer:     842043391019219959

	***

692 Siegbert and Jo

Siegbert and Jo take turns playing a game with a heap of N pebbles:
1. Siegbert is the first to take some pebbles. He can take as many pebbles as he wants. (Between 1 and N inclusive.)
2. In each of the following turns the current player must take at least one pebble and at most twice the amount of pebbles taken by the previous player.
3. The player who takes the last pebble wins.

Although Siegbert can always win by taking all the pebbles on his first turn, to make the game more interesting he chooses to take the smallest number of pebbles that guarantees he will still win (assuming both Siegbert and Jo play optimally for the rest of the game).

Let H(N) be that minimal amount for a heap of N pebbles.
H(1)=1, H(4)=1, H(17)=1, H(8)=8 and H(18)=5.

Let G(n) be sum(H(k) for k in 1...n).

G(13)=43.

Find G(23416728348467685).

	***

Solution Method

This is a game of Fibonacci Nim https://en.wikipedia.org/wiki/Fibonacci_nim
The winning strategy is to select the smallest Fibonacci number in the Zeckendorf Representation of N
'''

# n must be a Fibonacci number
def G(n):
	f = [1,2]
	while f[-1] != n:
		f.append(f[-2]+f[-1])
	for i in range(2, len(f)-1, 1):
		for j in range(i-1):
			f[i] += f[j]
	return sum(f)

assert G(13) == 43

print(G(23416728348467685))
