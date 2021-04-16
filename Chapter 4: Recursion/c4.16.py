"""
Write a short recursive Python function that takes a character string s and
outputs its reverse. For example, the reverse of pots&pans would be
snap&stop
"""


def reverseString(s):
	if len(s) == 0:
		return s
	else:
		return s[len(s)-1] + reverseString(s[:len(s)-1])

if __name__=='__main__':
	print(reverseString("abcdefgh"))
	print(reverseString("pots&pans"))