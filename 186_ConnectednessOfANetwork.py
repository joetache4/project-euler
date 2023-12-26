'''
Joe Walter

difficulty: 60%
run time:   0:05
answer:     2325629

	***

186 Connectedness of a Network

Here are the records from a busy telephone system with one million users:
RecNr	Caller	Called
1		200007	100053
2		600183	500439
3		600863	701497
...		...		...

The telephone number of the caller and the called number in record n are Caller(n) = S_2n-1 and Called(n) = S_2n where S1,2,3,... come from the "Lagged Fibonacci Generator":

For 1 ≤ k ≤ 55, S_k = [100003 - 200003k + 300007k^3] (modulo 1000000)
For 56 ≤ k, S_k = [S_k-24 + S_k-55] (modulo 1000000)

If Caller(n) = Called(n) then the user is assumed to have misdialled and the call fails; otherwise the call is successful.

From the start of the records, we say that any pair of users X and Y are friends if X calls Y or vice-versa. Similarly, X is a friend of a friend of Z if X is a friend of Y and Y is a friend of Z; and so on for longer chains.

The Prime Minister's phone number is 524287. After how many successful calls, not counting misdials, will 99% of the users (including the PM) be a friend, or a friend of a friend etc., of the Prime Minister?
'''

from itertools import cycle

def LFG():
	S = []
	for k in range(1, 56):
		S.append((100003 - 200003*k + 300007*k*k*k) % 1000000)
		yield S[-1]
	for k in cycle(range(len(S))):
		S[k] = (S[k-24] + S[k-55]) % 1000000
		yield S[k]

def pairs(gen):
	while True:
		yield (next(gen), next(gen))

class Clique:
	cliques = {} # user -> clique
	def get_clique(user):
		try:
			return Clique.cliques[user]
		except KeyError:
			return Clique(user)
	def __init__(self, user):
		self.members = [user]
		self.special = user == 524287
		Clique.cliques[user] = self
	def absorb(self, other):
		for user in other.members:
			Clique.cliques[user] = self
		self.members += other.members
		self.special |= other.special
	def __len__(self):
		return len(self.members)

calls = 0
for x,y in pairs(LFG()):
	if x == y:
		continue
	calls += 1
	x_clique = Clique.get_clique(x)
	y_clique = Clique.get_clique(y)
	if x_clique is y_clique:
		continue
	if len(x_clique) < len(y_clique):
		x_clique, y_clique = y_clique, x_clique
		# x, y = y, x
	x_clique.absorb(y_clique)
	if x_clique.special:
		if 100*len(x_clique) >= 99*1000000:
			print(calls)
			break
