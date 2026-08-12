class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

        '''
        nums = [100, 4, 200, 1, 3, 2]
        So you're effectively doing:
        1 → 2 → 3 → 4  ✓ count
        2                ✗ skip  since 2-1 = 1 and we already counted for that
        3                ✗ skip
        4                ✗ skip
        100              ✓ count
        200              ✓ count
        '''