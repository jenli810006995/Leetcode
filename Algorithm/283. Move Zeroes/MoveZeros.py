'''
referred to https://blog.csdn.net/coder_orz/article/details/51384498
'''
# Solution 1

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = fast = 0
        while fast < len(nums):
            if nums[fast] != 0 :
                if slow != fast:
                    nums[slow] = nums[fast]
                    nums[fast] = 0
                slow += 1
            fast += 1
            
         
# Solution 2 : Use two loops, put all non 0's to the front, and remove all values at the end to 0's

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # use two loops
        
        i = 0
        for num in nums:
            if num != 0:
                nums[i] = num
                i += 1
        for j in range(i, len(nums)):
            nums[j] = 0
            
            
 # Time: 11/5/2020

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        n = len(nums)
        count = 0
        
        for i in range(n):
            if nums[i] != 0:
                nums[count] = nums[i] # move all the non-zero elements to the front
                count += 1
                
        while count < n:
            nums[count] = 0
            count += 1
        return nums
    
# Reference: https://www.geeksforgeeks.org/move-zeroes-end-array/
    
