class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}

        for num in nums:
            count[num] = 1 + count.get(num,0)

        arr = []
        for key, val in count.items():
            arr.append([val,key])       # arranged as frequency, which number
        
        arr.sort(reverse=True)

        result = []
        for i in range(k):
            result.append(arr[i][1])        # So basically arr is an array and has 2 elements. So when we do for i in range(k): we have to specify again index 1 as that is the number
        return result 

        # Same logic but shorter
        '''
        
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        return sorted(count, key=count.get, reverse=True)[:k]
        
        '''
        