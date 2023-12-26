'''
Joe Walter

difficulty: 35%
run time:   0:00
answer:     1918080160

	***

191 Prize Strings

A particular school offers cash rewards to children with good attendance and punctuality. If they are absent for three consecutive days or late on more than one occasion then they forfeit their prize.

During an n-day period a trinary string is formed for each child consisting of L's (late), O's (on time), and A's (absent).

Although there are eighty-one trinary strings for a 4-day period that can be formed, exactly forty-three strings would lead to a prize:

OOOO OOOA OOOL OOAO OOAA OOAL OOLO OOLA OAOO OAOA
OAOL OAAO OAAL OALO OALA OLOO OLOA OLAO OLAA AOOO
AOOA AOOL AOAO AOAA AOAL AOLO AOLA AAOO AAOA AAOL
AALO AALA ALOO ALOA ALAO ALAA LOOO LOOA LOAO LOAA
LAOO LAOA LAAO

How many "prize" strings exist over a 30-day period?
'''

def count(length, num_leading_a = 0, num_L = 0, mem = {}):
	if num_L >= 2 or num_leading_a >= 3:
		return 0
	if length <= 0:
		return 1
	try:
		return mem[(length, num_leading_a, num_L)]
	except KeyError:
		num = 0
		num += count(length-1, 0, num_L)
		num += count(length-1, num_leading_a+1, num_L)
		num += count(length-1, 0, num_L+1)
		mem[(length, num_leading_a, num_L)] = num
		return num

print(count(30))
