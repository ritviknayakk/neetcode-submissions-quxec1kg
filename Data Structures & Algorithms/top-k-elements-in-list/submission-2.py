class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        return sorted(count, key=count.get, reverse=True)[:k] 

        # Same logic but shorter
        '''
        
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        return sorted(count, key=count.get, reverse=True)[:k]
        
        '''
        