class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #Just remember that when we need to appened strings, use append and for that we need defaultdict

        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1

            res[tuple(count)].append(s)
        
        return list(res.values()) 	        # Important to use res.values as the key is the tuple and the values are the strins that we need

        # The hashmap gets generated for each character
        # Then that hashmap is addded to res. 
        # Similar strings(s) get grouped together as we are indexing based on the tuple value
        

        # ALSO WE MAKEE IT A TUPLE AS LISTS ARE NOT ACCEPTED BY DICTIONARY

        # ALSO we use defaultdict as it is a dictionary that assigns a default value for 
        #the dictionary if key is not present, can also append

        '''if we used normal dictionary we would do
        
        res = {}

        if key not in res:
            res[key] = []

        res[key].append(s)

'''