def isPalindrome(s):
	
	def toChars(s):
		s = s.lower()
		ans = ""
		for char in s:
			if char in 'abcdefghijklmnopqrstuvwxyz':
				ans += char

		return ans

	def isPal(s):
		if len(s) <= 1:
			return 1
		else:
			s[0] == s[-1] and isPal(s[1:-1])

	return isPal(toChars(s))