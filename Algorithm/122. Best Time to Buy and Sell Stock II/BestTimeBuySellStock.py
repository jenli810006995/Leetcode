'''
referred to https://www.cnblogs.com/zuoyuan/p/3765980.html
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        :type prices: List[int]
        :rtype int
        '''
        
        maxprofit = 0
        for i in range(1, len(prices)):
            if prices[i] >= prices[i - 1]:
                maxprofit += prices[i] - prices[i - 1]
        return maxprofit
    
