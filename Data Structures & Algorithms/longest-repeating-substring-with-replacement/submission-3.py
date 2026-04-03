class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = {}
        l = 0
        res = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)

            while (r - l + 1) - max(count.values()) >k:
                count[s[l]] -=1
                l+=1
            res = max(res,r-l+1)
        return res


'''
Imaging a string AAABB and k = 1
Keeps going till we have read AAAB
while loop false
res gets updated to window size 4
then we read AAABB
while loop true
we remove count of left most at l = 0 so A:2, B:2
while loop true
again remove at l = 1 sp A:1, B:2
while loop false
res remains at 4, does not get updated
so now we get max at res = 4 which is final value

'''      