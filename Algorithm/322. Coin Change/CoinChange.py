## Time: Sep. 22 2020

## You are given coins of different denominations and a total amount of money amount. 
## Write a function to compute the fewest number of coins that you need to make up that amount. 
## If that amount of money cannot be made up by any combination of the coins, return -1.

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        :type: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                if dp[i - coin] != float('inf'):
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return -1 if dp[amount] == float('inf') else dp[amount]
        
## Link: https://leetcode.com/problems/coin-change/
## Reference: https://blog.csdn.net/fuxuemingzhu/article/details/83592442
        
        
                    
            
