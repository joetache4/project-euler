'''
Joe Walter

difficulty: 30%
run time:   0:00
answer:     1572729

	***

173 Using Up To One Million Tiles How Many Different "Hollow" Square Laminae Can Be Formed?

We shall define a square lamina to be a square outline with a square "hole" so that the shape possesses vertical and horizontal symmetry. For example, using exactly thirty-two square tiles we can form two different square laminae:

With one-hundred tiles, and not necessarily using all of the tiles at one time, it is possible to form forty-one different square laminae.

Using up to one million tiles how many different square laminae can be formed?
'''

def solve(M):
	ans = 0
	D = 3
	while True:
		if 4*D - 4 > M:
			break
		for d in range(D-2, 0, -2):
			size = D*D - d*d
			if size <= M:
				ans += 1
			else:
				break
		D += 1
	return ans

assert solve(100) == 41

print(solve(10**6))
