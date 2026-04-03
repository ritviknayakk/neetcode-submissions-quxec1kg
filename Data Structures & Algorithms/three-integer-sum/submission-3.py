class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()

        for i,a in enumerate(nums):
            if a>0:     #We break here because we have sorted the array and if  the
                break   #first element is greater than 0, then total sum can't add up to 0 
            if i > 0 and nums[i] == nums[i-1]:
                continue    #We avoid calculating for the same value again this way
            
            l,r = i + 1, len(nums)-1
            while l<r:
                threesum = a + nums[l] + nums[r]
                
                if threesum > 0:
                    r-=1
                elif threesum < 0:
                    l+=1
                else:
                    res.append([a,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
        return res
        