Time: 10/10/2020

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:
```
Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
```


Solution

```
class Solution:
    def numSquares(self, n: int) ->int:
        squares = [i**2 for i in range(1, int(n**0.5)+1)]
        dp = [1]*(n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            if i in squares:
                continue
            dp[i] = dp[i - 1] + 1
            for square in squares:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)
       return dp[-1]
```

[Link](https://leetcode.com/problems/perfect-squares/)

[Reference](https://zhenyu0519.github.io/2020/02/26/lc279/)
