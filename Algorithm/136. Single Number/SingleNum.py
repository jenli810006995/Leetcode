'''
referred to https://medium.com/@angelahiking/136-single-number-python-easy-3066a526d2aa
'''
# Solution 1: create a dict, use python.get()

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # create a dict
        '''
        :type nums: List[int]
        :rtype: int
        '''
        
        dict = {}
        for num in nums:
            dict[num] = dict.get(num, 0) + 1
        for key, value in dict.items():
            if value == 1:
                return key
 
 # Time Complexity: O(n)
 # Space Complexity: O(n)
 
 # Solution 2: Bit manipulation
 
 class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # bit manipulation
        '''
        :type nums: List[int]
        :rtype: int
        '''
        
        return reduce((lambda x,y: x^y), nums)
        
  # Time Complexity: O(n)
  # Space Complexity: O(1)
  
  
