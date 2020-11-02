Time: 10/8/2020

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

``` 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
Example 4:

Input: nums = [1,3,5,6], target = 0
Output: 0
Example 5:

Input: nums = [1], target = 0
Output: 0

```

Hint: Use Binary Tree

Solution:

```
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
    
        if target > nums[len(nums) - 1]: # target > the last element in the list
            return len(nums)
            
        if target <= nums[0]:
            return 0
           
        return self.bsearch(0, len(nums) - 1, target, nums)
        
    def bsearch(self, left, right, target, nums):
        p = (left + right) // 2 # identify the middle point
        if target == nums[p]:
            return p
        if target < nums[p] and target > nums[p - 1]: # on the left side of p
            return p
        if target > nums[p] and target <= nums[p + 1]: # on the right side of p
            return p + 1
        if target > nums[p]:
            return self.bsearch(p, right, target, nums)
        if target < nums[p]:
            return self.bsearch(left, p , target, nums)

```

[Link](https://leetcode.com/problems/search-insert-position/)

[Reference](https://statyang.wordpress.com/python-practice-25-search-insert-position/)
