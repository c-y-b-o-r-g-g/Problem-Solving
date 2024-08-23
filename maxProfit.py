class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        lowest = min(prices)
        index = lowest.__index__()
        highest = max(prices[index:len(prices)])
        if highest.index() > lowest.__index__():
            return 0
        else:
            return highest - lowest        
        
    maxProfit(0,[7,6,4,3,1])