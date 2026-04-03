class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        indices = {}

        for key,value in enumerate(nums):
            indices[value] = key

        for key,value in enumerate(nums):
            diff = target - value

            if diff in indices and indices[diff] != key:
                return[key, indices[diff]]

        return[]