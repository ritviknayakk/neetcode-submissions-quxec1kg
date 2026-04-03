class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num,0)
        
        # The key is numbers is the list, value is no. of times they appear

        arr = []
        for key,value in count.items():
            arr.append([value, key])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])  #[1] to get the actual number, not the frequency
        return res

        

        