def isIn(char, aStr):
	"""Every time you use 'is in', something like this is being called. """
	
	if len(aStr) == 0:
		return False
	elif len(aStr) == 1:
		return char == aStr
	elif char == aStr[len(aStr)/2]:
		return True
	elif char > aStr[len(aStr)/2]:
		return isIn(char, aStr[len(aStr)/2:0])
	elif char < aStr[len(aStr)/2]:
		return isIn(char, aStr[0:len(aStr)/2])
