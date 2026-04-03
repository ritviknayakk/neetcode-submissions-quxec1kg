class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)
        longest = 0

        for num in nums:
            length = 0
            while num+length in numSet:
                length += 1
            longest = max(length, longest)

        return longest

'''1. make a set of the array
   2. Check if there is a number 1 less than the current number, meaning 
      that would already consist of a sequence

      if we were at number 2, and we checked if number 1 existed in the set
      nd if it did, means it has already formed a sequence

      if it does not exist means a new sequence starts from 2

    so we keep increasing the length till num + length does not exist in set'''
            