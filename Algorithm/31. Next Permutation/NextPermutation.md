Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

```
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
```

Solution:
```
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
    '''
    do not return anything, modify in-place instead
    '''
    n = len(nums)
    i = n -1
    while i > 0 and nums[i] <= nums[i - 1]:
        i -= 1
    self.reverse(nums, i, n - 1)
    if i > 0:
        for j in range(i, n):
            if nums[j] > nums[i - 1]:
                self.swap(nums, i - 1, j)
                break
                
   def reverse(self, nums, i, j):
       for k in range(i, (i + j)//2 + 1):
           self.swap(nums, k, i + j - k)
           
  def swap(self, nums, i, j):
      nums[i], nums[j] = nums[j], nums[i]     
        
```

[Link](https://leetcode.com/problems/next-permutation/)

[Reference](https://blog.csdn.net/fuxuemingzhu/article/details/82113409)
