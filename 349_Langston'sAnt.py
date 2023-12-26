'''
Joe Walter

difficulty: 35%
run time:   0:00
answer:     115384615384614952

	***

349 Langston's Ant

An ant moves on a regular grid of squares that are coloured either black or white.
The ant is always oriented in one of the cardinal directions (left, right, up or down) and moves from square to adjacent square according to the following rules:
- if it is on a black square, it flips the colour of the square to white, rotates 90 degrees counterclockwise and moves forward one square.
- if it is on a white square, it flips the colour of the square to black, rotates 90 degrees clockwise and moves forward one square.

Starting with a grid that is entirely white, how many squares are black after 10^18 moves of the ant?
'''

n = 10**18

class Ant():
	D = [(-1,0), (0,1), (1,0), (0,-1)]
	def __init__(self):
		self.black_squares = {}
		self.x, self.y = 0, 0
		self.dir = 0
		self.iterations = 0
	def tick(self):
		try:
			square = self.black_squares[(self.x, self.y)]
			# black
			self.dir = (self.dir - 1) % 4
			del self.black_squares[(self.x, self.y)]
		except KeyError:
			# white
			self.dir = (self.dir + 1) % 4
			self.black_squares[(self.x, self.y)] = True
		self.x += Ant.D[self.dir][0]
		self.y += Ant.D[self.dir][1]
		self.iterations += 1
	def local_state(self):
		state = [self.dir]
		radius = 5
		for dx in range(-radius, radius+1, 1):
			for dy in range(-radius, radius+1, 1):
				coord = (self.x+dx, self.y+dy)
				if coord in self.black_squares:
					state.append((dx, dy))
		return state
	def count(self):
		return len(self.black_squares)

# the ant shifts into an orderly mode after about 10000 iterations
ant = Ant()
for _ in range(11000):
	ant.tick()

A = (ant.iterations, ant.count())

state = ant.local_state()
while True:
	ant.tick()
	if ant.local_state() == state:
		break

# addition of 12 black squares after 104 iterations
B = (ant.iterations, ant.count())
di = B[0] - A[0]
db = B[1] - A[1]

while (n - ant.iterations) % di != 0:
	ant.tick()

print(ant.count() + (n - ant.iterations)//di*db)
