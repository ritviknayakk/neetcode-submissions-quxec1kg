from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
         res = defaultdict(list)   # we use this instead of a normal empty dict
                                   # Because now if there are any new key values
         for s in strs:            # then they get added automatically
            count = [0] * 26       #otherwise (read bottom of page)

            for c in s:
                count[ord(c) - ord('a')] += 1
            
            res[tuple(count)].append(s)
         return list(res.values())
'''You would have to  do 
if tuple(count) not in res:
    res[tuple(count)] = []      which will come after the ord line of code'''

