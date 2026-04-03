class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxP = 0
        minB = prices[0]

        for price in prices:
            minB = min(minB, price)
            maxP = max(maxP, price - minB)
        return maxP
        