'''
Joe Walter

difficulty: 50%
run time:   0:01
answer:     1120149658760

	***

137 Fibonacci Golden Nuggets

<p>Consider the infinite polynomial series $A_F(x) = x F_1 + x^2 F_2 + x^3 F_3 + \dots$, where $F_k$ is the $k$th term in the Fibonacci sequence: $1, 1, 2, 3, 5, 8, \dots$; that is, $F_k = F_{k-1} + F_{k-2}$, $F_1 = 1$ and $F_2 = 1$.</p>
<p>For this problem we shall be interested in values of $x$ for which $A_F(x)$ is a positive integer.</p>

<table class="p236" cellpadding="0" cellspacing="0" border="0"><tr><td valign="top">Surprisingly</td><td>$\begin{align*} 
A_F(\tfrac{1}{2})
 &amp;= (\tfrac{1}{2})\times 1 + (\tfrac{1}{2})^2\times 1 + (\tfrac{1}{2})^3\times 2 + (\tfrac{1}{2})^4\times 3 + (\tfrac{1}{2})^5\times 5 + \cdots \\ 
 &amp;= \tfrac{1}{2} + \tfrac{1}{4} + \tfrac{2}{8} + \tfrac{3}{16} + \tfrac{5}{32} + \cdots \\
 &amp;= 2
\end{align*}$</td>
</tr></table>

<p>The corresponding values of $x$ for the first five natural numbers are shown below.</p>
<div class="center">
<table cellspacing="0" cellpadding="2" border="1" align="center"><tr><th>$x$</th><th width="50">$A_F(x)$</th>
</tr><tr><td>$\sqrt{2}-1$</td><td>$1$</td>
</tr><tr><td>$\tfrac{1}{2}$</td><td>$2$</td>
</tr><tr><td>$\frac{\sqrt{13}-2}{3}$</td><td>$3$</td>
</tr><tr><td>$\frac{\sqrt{89}-5}{8}$</td><td>$4$</td>
</tr><tr><td>$\frac{\sqrt{34}-3}{5}$</td><td>$5$</td>
</tr></table></div>
<p>We shall call $A_F(x)$ a golden nugget if $x$ is rational, because they become increasingly rarer; for example, the $10$th golden nugget is $74049690$.</p>
<p>Find the $15$th golden nugget.</p>
'''

nuggets = []
m = 2
n = 1
while len(nuggets) < 15:
	s = m*m-n*n-1
	t = m*n
	if s > t:
		n += 1
	elif s < t:
		m += 1
	else:
		m += 1
		nuggets.append(t)

assert nuggets[9] == 74049690

print(nuggets[14])
