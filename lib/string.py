# This can be sped up greatly by sliding a or b based on number of (non-)matching characters
def overlap(a, b):
	max_overlap = (0, a + b)
	for i in range(1, min(len(a), len(b))):
		a_test = a[-i:]
		b_test = b[0:i]
		if a_test == b_test:
			max_overlap = max(max_overlap, (i, a + b[i:]))
			continue
		a_test = a[0:i]
		b_test = b[-i:]
		if a_test == b_test:
			max_overlap = max(max_overlap, (i, b + a[i:]))
	return max_overlap

# Create minimum-length superstring with all given strings as substrings
# Repeatedly replace the most-overlapping pairs of strings with their combination
# No string can be a substring of another
def min_superstring(subs):
	while len(subs) > 1:
		max_overlap = (0, "", 0, 1) # overlap amount, concat, index 1, index 2
		for i in range(len(subs)-1):
			for j in range(i+1, len(subs)):
				amount, combined = overlap(subs[i], subs[j])
				max_overlap = max(max_overlap, (amount, combined, i, j))

		#print(max_overlap)
		_, combined, i, j = max_overlap
		if i < j:
			subs.pop(j)
			subs.pop(i)
		else:
			subs.pop(i)
			subs.pop(j)
		subs.append(combined)
		#print(subs)

	return subs[0]
