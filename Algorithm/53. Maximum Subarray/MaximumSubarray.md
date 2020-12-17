Time: 10/10/2020

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

```
Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [0]
Output: 0
Example 4:

Input: nums = [-1]
Output: -1
Example 5:

Input: nums = [-2147483647]
Output: -2147483647
 

Constraints:

1 <= nums.length <= 2 * 104
-231 <= nums[i] <= 231 - 1
```

Solution:
1. DP
2. Greedy

```
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        df = [0] * len(nums)
        df[0] = nums[0]
        max_num = nums[0]
        for i in range(1, len(nums)):
            df[i] = max(dp[i - 1] + nums[i] , nums[i])
            if dp[i] > max_num: max_num = dp[i]
        return max_num
```

```
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if max(nums) < 0:
            return max(nums)
        curr_sum, max_sum = 0, 0
        for num in nums:
            curr_sum = max(0, curr_sum + num)
            max_sum = max(curr_sum, max_sum)
        return max_sum
        

```

Runtime: 80ms, 68ms
Memory: 14.7 MB, 14.9 MB

[Link](https://leetcode.com/problems/maximum-subarray/)

[Reference](https://zhenyu0519.github.io/2020/02/18/lc53/)

