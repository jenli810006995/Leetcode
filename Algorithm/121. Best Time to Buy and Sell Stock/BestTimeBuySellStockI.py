'''
referred to https://www.cnblogs.com/zuoyuan/p/3765934.html
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # idea: loop through the whole list, marking the min price 
        # if encountering the lower price, then replace the min price with that
        
        if len(prices) <= 1: return 0
        
        low = prices[0]
        
        maxprofit = 0
        
        for i in range(len(prices)): # loop through the whole list
            if prices[i] < low:
                low = prices[i] # replace low if the ith price is lower
            maxprofit = max(maxprofit, prices[i] - low)       
        return maxprofit
        
        
 # Time: O(n)
 # Space: O(1)
 
 
