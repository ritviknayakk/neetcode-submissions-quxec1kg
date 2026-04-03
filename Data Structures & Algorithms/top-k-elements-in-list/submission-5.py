class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        res = {}
        for num in nums:
            res[num] = 1 + res.get(num, 0)
        
        arr = []
        for key, val in res.items():
            arr.append([val,key])
        arr.sort(reverse = True)

        result = []
        for i in range(k):
            result.append(arr[i][1])
        return result