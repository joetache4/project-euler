'''
Joe Walter

difficulty: 55%
run time:   0:00
answer:     139776,963904

	***

220 Heighway Dragon

Let D0 be the two-letter string "Fa". For n≥1, derive Dn from Dn-1 by the string-rewriting rules:

"a" → "aRbFR"
"b" → "LFaLb"

Thus, D0 = "Fa", D1 = "FaRbFR", D2 = "FaRbFRRLFaLbFR", and so on.

These strings can be interpreted as instructions to a computer graphics program, with "F" meaning "draw forward one unit", "L" meaning "turn left 90 degrees", "R" meaning "turn right 90 degrees", and "a" and "b" being ignored. The initial position of the computer cursor is (0,0), pointing up towards (0,1).

Then Dn is an exotic drawing known as the Heighway Dragon of order n. For example, D10 is shown below; counting each "F" as one step, the highlighted spot at (18,16) is the position reached after 500 steps.

What is the position of the cursor after 10^12 steps in D50?
Give your answer in the form x,y with no spaces.
'''

D = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
R = {"a":"aRbFR", "b":"LFaLb"}

# returns the position after making all moves stemming from an "a" or "b"
# follows the pattern in the commented code below
def skip(pos, dir, action, depth):
	pos = list(pos)
	if action == "a":
		i = D.index(dir)+2
	elif action == "b":
		i = D.index(dir)-2
	for j in range(depth):
		d = D[(i+j)%8]
		m = 2**(j//2)
		for k in range(len(pos)):
			pos[k] += m*d[k]
	pos = tuple(pos)
	dir = tuple(-d for d in dir)
	return pos, dir

def step(pos, dir, q, depth, F):
	action = q.pop(0)
	if action == "F":
		pos = tuple(sum(x) for x in zip(pos, dir))
		F -= 1
	elif action == "L":
		i = (D.index(dir)-2)%8
		dir = D[i]
	elif action == "R":
		i = (D.index(dir)+2)%8
		dir = D[i]
	elif depth > 0: # a or b
		f = 2**depth-1 # number of F's stemming from this a or b
		if f <= F:
			pos, dir = skip(pos, dir, action, depth)
			F -= f
		else:
			q = list(R[action])
			depth -= 1
	return pos, dir, q, depth, F

def solve(depth, F):
	pos = (0, 0)
	dir = (0, 1)
	q   = list("Fa")
	while F > 0:
		pos, dir, q, depth, F = step(pos, dir, q, depth, F)
	return f"{pos[0]},{pos[1]}"

assert solve(10, 500) == "18,16"

print(solve(50, 10**12))


# Shows pattern
'''
def step(s="a", k=1):
	for _ in range(k):
		s = s.replace("a", "aR_FR").replace("b", "LFaLb").replace("_", "b")
	return s

def pos(s):
	pos = [0,0]
	dir = [0,1]
	for c in s:
		if c == "F":
			pos[0] += dir[0]
			pos[1] += dir[1]
		elif c == "L":
			dir = [-dir[1], dir[0]]
		elif c == "R":
			dir = [dir[1], -dir[0]]
	return f"{s.count('F')=} {pos=} {dir=}"

print("a")
print(pos(step(s="a", k=1)))
print(pos(step(s="a", k=2)))
print(pos(step(s="a", k=3)))
print(pos(step(s="a", k=4)))
print(pos(step(s="a", k=5)))
print(pos(step(s="a", k=6)))
print(pos(step(s="a", k=7)))
print(pos(step(s="a", k=8)))
print()

print("b")
print(pos(step(s="b", k=1)))
print(pos(step(s="b", k=2)))
print(pos(step(s="b", k=3)))
print(pos(step(s="b", k=4)))
print(pos(step(s="b", k=5)))
print(pos(step(s="b", k=6)))
print(pos(step(s="b", k=7)))
print(pos(step(s="b", k=8)))
print()
'''
