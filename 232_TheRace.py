'''
Joe Walter

difficulty: 65%
run time:   0:02
answer:     0.83648556

	***

232 The Race

Two players share an unbiased coin and take it in turns to play The Race.

On Player 1's turn, the coin is tossed once. If it comes up Heads, then Player 1 scores one point; if it comes up Tails, then no points are scored.

On Player 2's turn, a positive integer, T, is chosen by Player 2 and the coin is tossed T times. If it comes up all Heads, then Player 2 scores 2^(T-1) points; otherwise, no points are scored.

Player 1 goes first and the winner is the first to 100 or more points.

Player 2 will always selects the number, T, of coin tosses that maximises the probability of winning.

What is the probability that Player 2 wins?

Give your answer rounded to eight decimal places in the form 0.abcdefgh.
'''

from itertools import count

# Given b remaining points, get all Player 2's choices as a list of pairs: (#points, probability of getting #points)
def get_choices(b):
	c = []
	for h in count(1):
		c.append((2**(h-1), 0.5**h))
		if c[-1][0] >= b:
			break
	return c

# probability Player 1 loses (Player 2 wins)
# state = (Player 1 remaining, Player 2 remaining)
class P():
	def __init__(self):
		self.p = {}
	def __getitem__(self, state):
		if state[1] <= 0:
			return 1
		return self.p[state]
	def __setitem__(self, state, val):
		self.p[state] = val

def solve(A, B, iterations=30): # 30 is close to the minimum, any more does not change the answer for A,B <= 100
	converged = P()
	for a in range(1, A+1):
		for b in range(1, B+1):
			choices = get_choices(b)
			# The decision tree has loops, so it's easiest to iterate and converge to a value for P(a,b)
			p = 0.5
			for _ in range(iterations):
				if a == 1:
					p1 = 0
				else:
					p1 = max(converged[a-1,b-points]*chance + converged[a-1,b]*(1-chance) for points, chance in choices)
				p0 = max(converged[a,b-points]*chance + p*(1-chance) for points, chance in choices)
				p = (p1+p0)/2
			converged[a,b] = p
	return f"{converged[(A,B)]:.8f}"

print(solve(100,100))

'''
from functools import cache

@cache
def prob(state):
	P1r, P2r, turn, forced = state
	# assume it's P1 to move
	# 3 possibilities where progress is made:
	#	P1 gets a Head, P2 gets a Head
	#	P1 does not get a Head, P2 gets a Head
	#	P1 gets a Head, P2 does not get a Head
	if P1r <= 0:
		return 0
	if P2r <= 0:
		return 1
	if turn == "1":
		if forced:
			return prob((P1r-1, P2r, "2", False))
		else:
			return prob((P1r-1, P2r, "2", False))/2 + prob((P1r, P2r, "2", True))/2
	else:
		h = 1
		choices = []
		while True:
			p = 2**(h-1)
			choices.append((h, p, 0.5**h)) # choice, points, chance of getting 'choice' heads
			h += 1
			if p >= P2r:
				break

		best_choice = (0, 0, 0) # prob of winning, points, chance
		for choice, points, chance in choices:
			p = prob((P1r, P2r-points, "1", False))*chance + prob((P1r, P2r, "1", False))*(1-chance) # recursion error
			best_choice = max(best_choice, (p, points, chance))

		_, points, chance = best_choice
		if forced:
			return prob((P1r, P2r-points, "1", False))
		else:
			return prob((P1r, P2r-points, "1", False))*chance + prob((P1r, P2r, "1", True))*(1-chance)

def solve(P1r, P2r):
	return f"{prob((P1r, P2r, '1', False)):.8f}"

print(solve(100, 100))
'''
