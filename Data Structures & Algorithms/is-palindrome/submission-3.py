class Solution:
    def isPalindrome(self, s: str) -> bool:
        

        newstr = ''
        for c in s:
            if c.isalnum():
                newstr += c.lower()
        return newstr == newstr[::-1]

# Basically this whole thing is to get rid of whitespaces using isalnum() and make everyhting lower case