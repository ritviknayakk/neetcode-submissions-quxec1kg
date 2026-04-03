class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num,0)

        arr = []
        for key,val in count.items():
            arr.append([val,key])

        arr.sort(reverse=True)

        result = []
        for i in range(k):
            result.append(arr[i][1])

        return result


        



