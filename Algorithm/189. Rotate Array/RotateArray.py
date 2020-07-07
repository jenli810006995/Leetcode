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


