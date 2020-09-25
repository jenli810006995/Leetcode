## Time: 9/24/2020

## Given an unsorted array of integers, find the length of longest increasing subsequence.

## Example:

## Input: [10,9,2,5,3,7,101,18]
## Output: 4 
## Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
## Note:
## There may be more than one LIS combination, it is only necessary for you to return the length.
## Your algorithm should run in O(n2) complexity.
## Follow up: Could you improve it to O(n log n) time complexity?

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        :type nums: List[int]
        :rtype: int
        '''
        if not nums: return 0
        dp = [0]* len(nums)
        dp[0] = 1
        for i in range(1, len(nums)):
            tmax = 1
            for j in range(0, i):
                if nums[i] > nums[j]:
                    tmax = max(tmax, dp[j] + 1)
            dp[i] = tmax
        return max(dp)
        
## Link: https://leetcode.com/problems/longest-increasing-subsequence/
## Reference: https://blog.csdn.net/fuxuemingzhu/article/details/79820919
    
    
