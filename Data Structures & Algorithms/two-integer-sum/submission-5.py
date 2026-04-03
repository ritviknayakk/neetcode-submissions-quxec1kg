class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        indices = {}
        for key,val in enumerate(nums):
            indices[val] = key


        for key,val in enumerate(nums):
            diff = target - val
            if diff in indices and indices[diff] != key:
                return [key, indices[diff]]
