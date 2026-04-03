class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        res = 0
        l, r = 0, len(heights) - 1

        while l < r:
            area = min(heights[l], heights[r]) * (r-l)
            res = max(res,area)

            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return res

# First step is assigning l, r
# Second step is calculate area
# Decide which pointer to move ---> l or r based on the height value