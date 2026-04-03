class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxP = 0
        minB = prices[0]

        for price in prices:
            minB = min(minB, price)         #Important to do like this because this ensures that we take the minimum price upto that day. Do not do minB = min(prices) because that allows buying stock after selling
            maxP = max(maxP, price - minB)
        return maxP
        
'''
Note that minB is the least price of the stock in the array.
So we do price - minB, since that would result in a positive value

ALSO IT DOES'NT MATTER IF YOU CALCULATE THE minB or the maxP first in the for loop
any order is fine
'''