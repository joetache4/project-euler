'''
Joe Walter

difficulty: 35%
run time:   0:00
answer:     100808458960497

	***

117 Red Green And Blue Tiles

Using a combination of grey square tiles and oblong tiles chosen from: red tiles (measuring two units), green tiles (measuring three units), and blue tiles (measuring four units), it is possible to tile a row measuring five units in length in exactly fifteen different ways.
png117.png

How many ways can a row measuring fifty units in length be tiled?

NOTE: This is related to Problem 116.
'''

from functools import cache

@cache
def count(grey_len, color_lens = (2,3,4)):
	a = 0
	if grey_len == 0:
		a = 1
	elif grey_len > 0:
		for color_len in color_lens:
			a += count(grey_len - color_len)
		a += count(grey_len - 1)
	return a

assert count(5) == 15

print(count(50))
