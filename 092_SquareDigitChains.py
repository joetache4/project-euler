'''
Joe Walter

difficulty: 5%
run time:   0:12
answer:     8581146

	***

092 Square Digit Chains

A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
'''

s = {'0':0, '1':1, '2':4, '3':9, '4':16, '5':25, '6':36, '7':49, '8':64, '9':81} # faster than casting to int and squaring

v = [None] * (10**7)
v[0]  = False
v[1]  = False
v[89] = True

def find_val(n):
	vn = v[n]
	if vn is None:
		n2 = sum(s[d] for d in str(n))
		vn = find_val(n2)
		v[n] = vn
	return vn

for n in range(len(v)):
	find_val(n)

print(sum(1 for n in v if n))
