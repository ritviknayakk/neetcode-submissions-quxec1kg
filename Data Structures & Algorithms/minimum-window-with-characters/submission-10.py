class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if t == '':
            return ''
        
        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        have, need = 0, len(countT)
        res, reslen = [-1,-1], float('infinity')
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and countT[c] == window[c]:
                have += 1
            
            while have == need:
                if (r-l+1) < reslen:    # Forgot this 
                    res = [l,r]
                    reslen = r-l+1

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res          # This is necessary
        return s[l:r+1]  

'''
First I would get the count of characters in t
Then prepare the have, need
Prepare pointers and length of window

IN THE FOR LOOP WITH r POINTER:
Add into window
Then check for if have == need
Update pointers and window size
Subtract window and increase l pointer


so basically make use of 2 hasmaps and pointers
'''
