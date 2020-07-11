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
 
 # Solution 2: Dynamic Programming
    
 class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # DP
        
        '''
        :type prices: List[int]
        :rtype: int
        '''
        
        if not prices:
            return 0
        
        N = len(prices)
        
        mins = [0] * N
        maxs = [0] * N
        
        mins[0] = prices[0]
        
        for i in range(1, N):
            mins[i] = min(mins[i-1], prices[i])
        maxs[N - 1] = prices[N - 1]
        for j in range(N - 2, -1, -1):
            maxs[j] = max(maxs[j + 1], prices[j])
        return max(maxs[i] - mins[i] for i in range(N))
    
    