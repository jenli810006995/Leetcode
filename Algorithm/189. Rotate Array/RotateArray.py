'''
referred to https://blog.csdn.net/coder_orz/article/details/52052767
'''

# Solution 1:

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        k = k % len(nums)
        nums[:k], nums[k:] = nums[len(nums)-k:], nums[:len(nums) - k]
        
# Solution 2:

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        old_nums = nums[:]
        for i in range(len(nums)):
            nums[(i + k) % len(nums)] = old_nums[i]
            
# Solution 3:

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        :type nums: List[int]
        :type k: int
        :rtype: void
        '''
        
        k = k % len(nums)
        self.reversePart(nums, 0, len(nums) -k- 1)
        self.reversePart(nums, len(nums) - k, len(nums) - 1)
        self.reversePart(nums, 0 , len(nums)-1)
        
    def reversePart(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1
            
            
## Time: 10/28/2020

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %=n
        
        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)
        
        
    def reverse(self, arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -=1
            
 ## Reference: https://youtu.be/8kyZPizZzWc


