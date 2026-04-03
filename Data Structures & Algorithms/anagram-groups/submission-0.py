from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}  # plain dictionary
        for s in strs:
            key = ''.join(sorted(s))  # sorted string as the key
            if key not in res:        # if key not seen before, init empty list
                res[key] = []
            res[key].append(s)        # add the word to the correct group
        return list(res.values())     # return the grouped anagrams
