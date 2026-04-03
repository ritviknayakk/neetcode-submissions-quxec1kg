class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS = {}
        countT = {}

        for index in range(len(s)):
            countS[s[index]] = 1 + countS.get(s[index],0)  # gets key based on index and then adds 1 to the value 
            countT[t[index]] = 1 + countT.get(t[index],0)
        
        return countS == countT
        
        # Could do it without using range like this. Need 2 for loops as there are 2 different strings
        # But not ideal because if they ask many different strings, then you would need
        #many loops.
        # Although the complexity will remain same
        
        '''if len(s) != len(t):
            return False

        countS = {}
        countT = {}

        for char in s:
            countS[char] = 1 + countS.get(char,0)
        for char in t:
            countT[char] = 1 + countT.get(char,0)
        
        return countS == countT'''

        