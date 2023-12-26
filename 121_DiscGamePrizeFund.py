'''
Joe Walter

difficulty: 35%
run time:   0:00
answer:     2269

	***

121 Disc Game Prize Fund

A bag contains one red disc and one blue disc. In a game of chance a player takes a disc at random and its colour is noted. After each turn the disc is returned to the bag, an extra red disc is added, and another disc is taken at random.

The player pays £1 to play and wins if they have taken more blue discs than red discs at the end of the game.

If the game is played for four turns, the probability of a player winning is exactly 11/120, and so the maximum prize fund the banker should allocate for winning in this game would be £10 before they would expect to incur a loss. Note that any payout will be a whole number of pounds and also includes the original £1 paid to play the game, so in the example given the player actually wins £9.

Find the maximum prize fund that should be allocated to a single game in which fifteen turns are played.
'''

from math import floor

def perms(numT, numF, start = None):
	if start is None:
		start = []
	if numT == 0 and numF == 0:
		yield start.copy()
	if numT > 0:
		start.append(True)
		yield from perms(numT - 1, numF, start)
		start.pop()
	if numF > 0:
		start.append(False)
		yield from perms(numT, numF - 1, start)
		start.pop()

def solve(turns):
	prob_win = 0
	for b in range(turns//2+1, turns+1):
		for perm in perms(b, turns-b):
			prob_perm = 1
			for i, draw in enumerate(perm):
				if draw:
					prob_perm *= 1/(i+2)
				else:
					prob_perm *= (i+1)/(i+2)
			prob_win += prob_perm

	return floor(1/prob_win)

assert solve(4) == 10

print(solve(15))
