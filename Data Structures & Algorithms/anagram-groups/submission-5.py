from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
         res = defaultdict(list)   # we use this instead of a normal empty dict
                                   # Because now if there are any new key values
         for s in strs:            # then they get added automatically
            count = [0] * 26       #otherwise (read bottom of page)

            for c in s:
                count[ord(c) - ord('a')] += 1 # Here the position gets specified(ord(a) - ord(a) = 97 - 97 = 0th position) and at that position we put a 1
            #IMPORTANT TO USE TUPLE HERE BECAUSE THEY ARE IMMPUTABLE AND CAN BE USED AS KEYS
            res[tuple(count)].append(s)  # VERY IMPORTANT THAT YOU USE APPEND AND NOT = s. We need to group the strings together one after the other. if you use =, then it rewrites the string
         return list(res.values())  # Imporitant to say list here
'''You would have to  do 
if tuple(count) not in res:
    res[tuple(count)] = []      which will come after the ord line of code'''

