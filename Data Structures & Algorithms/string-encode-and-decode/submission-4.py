class Solution:

    def encode(self, strs: List[str]) -> str:
        newstr = ""
        for s in strs:
            newstr += str(len(s)) + "#" + s        
        return newstr

    def decode(self, s: str) -> List[str]:

        i = 0
        res = []

        while i < len(s):
            j = i
            while s[j] != "#": 
                j +=1
            length = int(s[i:j])    
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res

    # ex: 3#Lol  so j increases till it reaches #. So j = 1. Length is whatever there 
    # starting from i position to before j and we make it int.
    # So we get length = 3
    # Then i = j + 1 so i is at L. j then covers i + length
    # Whatever is there that starts from i till before j is read 

'''"3abc"

Here the 3 tells us the length of the next substring.

So the program needs to read the number 3, not the number of characters in "3".

Using int() (correct)
s = "3abc"

length = int(s[0:1])   # "3" → 3
print(length)'''
