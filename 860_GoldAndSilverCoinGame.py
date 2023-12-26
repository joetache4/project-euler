'''
Joe Walter

difficulty:
run time:   0:12
answer:     958666903

	***

860 Gold and Silver Coin Game

Gary and Sally play a game using gold and silver coins arranged into a number of vertical stacks, alternating turns. On Gary's turn he chooses a gold coin and removes it from the game along with any other coins sitting on top. Sally does the same on her turn by removing a silver coin. The first player unable to make a move loses.

An arrangement is called fair if the person moving first, whether it be Gary or Sally, will lose the game if both play optimally.

Define F(n) to be the number of fair arrangements of n stacks, all of size 2. Different orderings of the stacks are to be counted separately, so F(2)=4 due to the following four arrangements:

0860_diag3.jpg

You are also given F(10)=63594.

Find F(9898). Give your answer modulo 989898989.

	***

This game is Red-Blue Hackenbush.

a ~  2
b ~  0.5
c ~ -2
d ~ -0.5

2a + b/2 = 2c + d/2
a + b + c + d = 9898

4c + d =         4a +  b
 c + d =  9898 -  a -  b
3c     = -9898 + 5a + 2b
'''

def F(n):
	M = 989898989

	P = 1
	for p in range(1,n+1):
		P = (P*p)%M
	I = [1]*(n+1)
	for i in range(2,n+1):
		I[i] = (I[i-1]*pow(i,-1,M))%M

	ans = 0
	for a in range(0,n+1):
		for b in range(0,n+1-a):
			c = (5*a + 2*b - n)/3
			d = n - a - b - c
			if int(c) != c or c<0 or c>n or d<0 or d>n:
				continue
			c = int(c)
			d = int(d)
			assert 2*a + b/2 - 2*c - d/2 == 0
			assert a + b + c + d == n
			ans += P*I[a]*I[b]*I[c]*I[d]
	return ans % M

assert F(2) == 4
assert F(10) == 63594

print(F(9898))
