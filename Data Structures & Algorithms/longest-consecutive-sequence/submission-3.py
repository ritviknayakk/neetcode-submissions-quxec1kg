class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        longest = 0

        for num in nums:
            length = 0
            while num + length in nums:
                length+=1
            longest = max(length,longest)

        return longest