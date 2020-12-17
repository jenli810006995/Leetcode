## Time: 10/1/2020

## Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.
## Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

## two pointers
class Solution:
    def removeDuplicates(self, nums:List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
            
       j = 1 # slow pointer
       
       for i in range(1, len(nums)): # fast pointer
           if nums[i] != nums[i - 1]: # this means, nums[i] is unique, assign nums[i] to nums[j]
               nums[j] = nums[i]
               j += 1
      # delete duplicates backwards
      
      for delete_index in range(i - 1, j, -1):
          del nums[delete_index]
          
      return j
      
## Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
## Reference: https://medium.com/leetcode-cracker/26-remove-duplicates-from-sorted-array-19e2de4ca555


# Time: 11/1/2020
# JS

var removeDuplicates = function(nums){
    
    var head = 0;
    
    for (let i = 1; i < nums.length; i ++){
    
        if (nums[i] !== nums[head]){
            head ++;
            nums[head] = nums[i];
            }
    }
    
    return head + 1;
}

# Python

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0
        
        head = 0
        
        for i in range(1, len(nums)):
            if nums[i] != nums[head]:
                head +=1
                nums[head] = nums[i]
        
        return head + 1

# Reference: https://youtu.be/xwZ8TFMLy8I
