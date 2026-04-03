class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longest = 0
        seen = set(nums)

        for num in nums:
            length = 0
            while num + length in seen:
                length += 1
            longest = max(longest, length)

        return longest 