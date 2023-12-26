'''
Joe Walter

difficulty: 20%
run time:   0:01
answer:     0.3916721504

	***

613 Pythagorean Ant

Dave is doing his homework on the balcony and, preparing a presentation about Pythagorean triangles, has just cut out a triangle with side lengths 30cm, 40cm and 50cm from some cardboard, when a gust of wind blows the triangle down into the garden.
Another gust blows a small ant straight onto this triangle. The poor ant is completely disoriented and starts to crawl straight ahead in random direction in order to get back into the grass.

Assuming that all possible positions of the ant within the triangle and all possible directions of moving on are equiprobable, what is the probability that the ant leaves the triangle along its longest side?

Give your answer rounded to 10 digits after the decimal point.
'''

from math import acos, sqrt, pi
from scipy.integrate import dblquad

'''
P = dblquad(lambda x,y: acos(
((40-x)*(-x)+(30-y)*(-y)) /
sqrt(((40-x)**2+(30-y)**2)*(x**2+y**2))
), 0, 30, lambda y: 40*y/30, lambda y: 40)[0]
P = P / (2*pi) / (0.5*30*40)
'''

p = lambda x,y: acos(
((40-x)*(-x)+(30-y)*(-y)) /
sqrt(((40-x)**2+(30-y)**2)*(x**2+y**2))
) / (2*pi)
P = dblquad(p, 0, 30, lambda y: 40*y/30, lambda y: 40)[0] / (0.5*30*40)

print(f"{P:.10f}")

'''
import random
from datetime import datetime

random.seed(datetime.now().timestamp())

dot = lambda a,b: a[0]*b[0] + a[1]*b[1]

P = 0
for i in range(1, 100000):
	x = random.uniform(0, 40)
	y = random.uniform(0, 30*x/40)

	a = (40-x, 30-y)
	b = ( 0-x,  0-y)

	p = acos(dot(a,b)/sqrt(dot(a,a)*dot(b,b))) / (2*3.1415926535)
	P += p
	if i % 100 == 0:
		print(f"{P/i:.10f}")
'''
