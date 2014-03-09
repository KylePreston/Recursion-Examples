def gcdIter(a, b):
	"""Return the greatest common denominator """

	a, b = abs(a), abs(b)
	if a == b:
		return a

	small = min(a, b)
	big = max(a, b)
	cd = small

	for i in range(small):
		if small == 1:
			return 1
		elif big%small == 0:
			if cd%small == 0:
				return small
			else:
				small -= 1
		else:
			small -= 1
