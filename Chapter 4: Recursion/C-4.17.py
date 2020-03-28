""" 
Write a short recursive Python function that determines if a string s is a
palindrome, that is, it is equal to its reverse. For example, "racecar" and
"gohangasalamiimalasagnahog" are palindromes.
"""

def isPalindrome(s):
    if len(s)==0:
        return "Palindrome"
    elif len(s)==1:
        return "Palindrome"
    elif s[0]!=s[len(s)-1]:
        return "Not Palindrome"
    else: return isPalindrome(s[1:len(s)-1])

if __name__ == '__main__':
    print(isPalindrome("gohangasalamiimalasagnahog"))
    print(isPalindrome("racecar"))
