def lenRecur(aStr):
	if aStr == "":
		return 0 
	# This will always return a string that is one smaller. 
	# It adds 1 each time it recurs and eventually returns
	# the total number of ones
	return 1 + lenRecur(aStr[0:-1])

print lenRecur('food')