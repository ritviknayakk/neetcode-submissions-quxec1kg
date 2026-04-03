class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        suffix = [1]*n
        prefix = [1]*n

        for i in range(1,n):
            prefix[i] = prefix[i-1] * nums[i-1]

        for i in range(n-2,-1,-1):
            suffix[i] = suffix[i+1] * nums[i+1]
        
        for i in range(n):
            res[i] = suffix[i] * prefix[i]

        return res

'''for i in range(len(nums) - 1, -1, -1)

example: [4,7,6]
in python it is start stop step. Here for loop goes from end of the list 
i.e 3, with a decrement of -1 till it reaches 0 value and stops right before it becomes -1 that is our stop value.

remember that stop of -1 is the number itself, it is not an index -1
index - 1 is last element on the list
'''