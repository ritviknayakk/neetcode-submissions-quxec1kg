class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        longest = 0

        for num in nums:
            length = 0                          #It is important that we use a for and while loop
            while num + length in nums:         # Because length value = 0 with each iteration
                length+=1
            longest = max(length,longest)

        return longest