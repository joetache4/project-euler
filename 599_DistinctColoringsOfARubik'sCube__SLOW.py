'''
Joe Walter

difficulty: 60%
run time:   8:00
answer:     12395526079546335

	***

599 Distinct Colorings of a Rubik's Cube

The well-known Rubik's Cube puzzle has many fascinating mathematical properties. The 2×2×2 variant has 8 cubelets with a total of 24 visible faces, each with a coloured sticker. Successively turning faces will rearrange the cubelets, although not all arrangements of cubelets are reachable without dismantling the puzzle.

Suppose that we wish to apply new stickers to a 2×2×2 Rubik's cube in a non-standard colouring. Specifically, we have n different colours available (with an unlimited supply of stickers of each colour), and we place one sticker on each of the 24 faces in any arrangement that we please. We are not required to use all the colours, and if desired the same colour may appear in more than one face of a single cubelet.

We say that two such colourings c1,c2 are essentially distinct if a cube coloured according to c1 cannot be made to match a cube coloured according to c2 by performing mechanically possible Rubik's Cube moves.

For example, with two colours available, there are 183 essentially distinct colourings.

How many essentially distinct colourings are there with 10 different colours available?
'''

FACES = 24

def Permutation(cycles):
	''' Create permutation array from cycles '''
	x = list(range(FACES))
	for cycle in cycles:
		for i in range(len(cycle)):
			j = (i+1) % len(cycle)
			x[cycle[i]] = cycle[j]
	return tuple(x)

I = tuple(range(FACES))

# group operation
def f(a,b):
	''' Composition of permutations (group operation) '''
	return tuple(b[a] for a in a)

def generate_permutation_group(I, generators):
	G     = set([I])
	G_new = [I]
	while len(G_new):
		tmp = []
		for a in G_new:
			for b in generators:
				c = f(a,b)
				size = len(G)
				G.add(c)
				if size < len(G):
					tmp.append(c)
		G_new = tmp
	return G

def count_cycles(p):
	count = 0
	for i in range(FACES):
		j = i
		while True:
			j = p[j]
			if j == i:
				count += 1
				break
			elif j < i:
				break
	return count

print("Generating 2x2x2 Rubik's Cube group")

# twist each face counterclockwise
U = Permutation([[ 0, 1, 2, 3], [ 6,11,12,17], [ 7, 8,13,18]])
R = Permutation([[16,17,18,19], [ 0,12,22, 4], [ 3,15,21, 7]])
F = Permutation([[12,13,14,15], [ 2,10,22,18], [ 3,11,23,19]])

# rubik's cube twists
# |G| = 3674160 (*6*4 = 88179840 if ignoring rotational symmetry)
G1 = generate_permutation_group(I, [U,F,R])
print(f"|G1| = {len(G1)}")
# 976 MB

D = Permutation([[20,21,22,23], [ 4,19,14, 9], [ 5,16,15,10]])
L = Permutation([[ 8, 9,10,11], [ 1, 5,23,13], [ 2, 6,20,14]])
B = Permutation([[ 4, 5, 6, 7], [ 0,16,20, 8], [ 1,17,21, 9]])

X = f(f(f(U,D),D),D)
Y = f(f(f(L,R),R),R)
Z = f(f(f(F,B),B),B)

# cube rotations
G2 = generate_permutation_group(I, [X,Y,Z])
print(f"|G2| = {len(G2)}")

print("Counting fixed points")

def count_distinct(n):
	# Burnside's Lemma
	count = 0
	for g1 in G1:
		for g2 in G2:
			count += n**count_cycles(f(g1,g2))
	count //= (len(G1)*len(G2))
	return count

#print(count_distinct(2)) # =183 (correct)
print(count_distinct(10))
