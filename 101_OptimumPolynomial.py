'''
Joe Walter

difficulty: 35%
run time:   0:00
answer:     37076114526

	***

101 Optimum Polynomial

If we are presented with the first k terms of a sequence it is impossible to say with certainty the value of the next term, as there are infinitely many polynomial functions that can model the sequence.

As an example, let us consider the sequence of cube numbers. This is defined by the generating function,
un = n^3: 1, 8, 27, 64, 125, 216, ...

Suppose we were only given the first two terms of this sequence. Working on the principle that "simple is best" we should assume a linear relationship and predict the next term to be 15 (common difference 7). Even if we were presented with the first three terms, by the same principle of simplicity, a quadratic relationship should be assumed.

We shall define OP(k, n) to be the nth term of the optimum polynomial generating function for the first k terms of a sequence. It should be clear that OP(k, n) will accurately generate the terms of the sequence for n ≤ k, and potentially the first incorrect term (FIT) will be OP(k, k+1); in which case we shall call it a bad OP (BOP).

As a basis, if we were only given the first term of sequence, it would be most sensible to assume constancy; that is, for n ≥ 2, OP(1, n) = u1.

Hence we obtain the following OPs for the cubic sequence:
OP(1, n) = 1 	1, 1, 1, 1, ...
OP(2, n) = 7n−6 	1, 8, 15, ...
OP(3, n) = 6n^2−11n+6      	1, 8, 27, 58, ...
OP(4, n) = n^3 	1, 8, 27, 64, 125, ...

Clearly no BOPs exist for k ≥ 4.

By considering the sum of FITs generated by the BOPs (indicated in red above), we obtain 1 + 15 + 58 = 74.

Consider the following tenth degree polynomial generating function:

un = 1 − n + n^2 − n^3 + n^4 − n^5 + n^6 − n^7 + n^8 − n^9 + n^10

Find the sum of FITs for the BOPs.

	***

Solution Method

(Assumption) the (k+1)-st prediction from the first k terms is always a FIT

Predictions are made based on the difference between terms ("1st order differences"), the difference between those differences ("2nd order"), and so on.

Ex. : Predict the 2nd term in the sequence {1}
1		(answer)

Ex. : Predict the 3rd term in the sequence {1, 8}
1	8
7			(1st order diff)
8 + 7 = 15	(answer)

Ex. : Predict the 4th term in the sequence {1, 8, 27}
1	8	27
7	19		(1st order diff, what is the "velocity" of terms)
12			(2nd order diff, how much are terms "accelerating")
27 + (19 + 12) = 58	(answer)

Note that the prediction is just the sum of the large-diagonal items.

TODO: I could just sum this entire trianle to get the sum of all FITs.
'''

def generate(coeff):
	n = 1
	while True:
		yield sum(coeff[m]*(n**m) for m in range(len(coeff)))
		n += 1

def sequence(coeff):
	seq = generate(coeff)
	seq = [next(seq) for _ in range(len(coeff))]
	return seq

def predict(seq):
	if len(seq) == 1:
		return seq[0]
	else:
		diff = [seq[i+1] - seq[i] for i in range(len(seq)-1)]
		return seq[-1] + predict(diff)

def solve(coeff):
	seq = sequence(coeff)
	return sum(predict(seq[:k]) for k in range(1, len(seq)))

assert solve([0,0,0,1]) == 74

print(solve([1,-1,1,-1,1,-1,1,-1,1,-1,1]))

# first attempt
'''
import numpy as np

def seq(coeff):
	n = 1
	while True:
		yield sum(coeff[m]*(n**m) for m in range(len(coeff)))
		n += 1

def OP(k, coeff):
	a = []
	for i in range(k):
		a.append([])
		for j in range(k):
			a[-1].append((i+1)**j)

	s = seq(coeff)
	b = [next(s) for _ in range(k)]

	a = np.array(a, dtype = np.int64)
	b = np.array(b, dtype = np.int64)
	x = np.linalg.solve(a,b)
	print(x)
	x = [int(z) for z in x]

	print((k, np.linalg.cond(a)))
	assert np.allclose(a.dot(x), b) # fails -- ill-conditioned matrix

	return x

def FIT(k, coeff):
	#if k >= len(coeff):
	#	return 0
	op = OP(k, coeff)
	for i, (guess, actual) in enumerate(zip(seq(op), seq(coeff))):
		if i > len(coeff):
			break
		if guess != actual:
			print((k, i, guess, actual))
			assert k == i
			return guess
	return 0

def ans(coeff):
	return sum(FIT(k, coeff) for k in range(1, len(coeff)))

print(ans([1,-1,1,-1,1,-1,1,-1,1,-1,1]))
'''