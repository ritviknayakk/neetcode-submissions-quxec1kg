class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()

        for i,a in enumerate(nums):
            if a>0:                 # If first number > 0 then remaining will also be > 0 
                break               # so sum of those cant be = 0
            if i > 0 and nums[i] == nums[i-1]:  # This prevents duplicate triplets. If the number we are 
                continue      # are currently on is equal to previous then skip current number "continue"
            
            l,r = i+1, len(nums) -1  # l = i + 1 is used because i is already the first element of the triplet (a = nums[i]).
            while l<r:
                threesum = a + nums[l] + nums[r]

                if threesum > 0:
                    r-=1
                elif threesum<0:
                    l+=1
                else:
                    res.append([a,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l-1]:   #At this point we found a valid triplet, so we increase l+ and r-
                        l+=1                    #We prevent the second number from being a duplicate.
        return res





