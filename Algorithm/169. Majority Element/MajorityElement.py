'''
referred to https://blog.csdn.net/coder_orz/article/details/51407713
'''

# Solution 1: Create an empty dict and then iterate the array, if the freq. > len(array)//2 then return the value

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        :type nums: List[int]
        :rtyoe:int
        '''
        
        # solution 1: Hashtable
        
        digits = {}
        
        # iterate
        
        for i in nums:
            digits[i] = digits.get(i, 0) + 1
            if digits[i] > len(nums)//2:
                return i
                
# Solution 2: creating a set

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        :type nums: List[int]
        :rtyoe:int
        '''
        
        # solution 2: Set
        
        nums_set = set(nums)
        
        for i in nums_set:
            if nums.count(i) > len(nums)//2:
                return i
                
# Solution 3: Sort: the majority element would be in the middle after sorting

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        :type nums: List[int]
        :rtyoe:int
        '''
        
        # solution 3: Sort
        
        nums.sort()
        
        return nums[len(nums)//2]
       
# Solution 4:
        
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        :type nums: List[int]
        :rtyoe:int
        '''
        
        # Solution 4: Moore Voting Algorithm
        
        major = count = 0
        
        for i in nums:
            if count == 0:
                major = i
                count = 1
            else:
                count += 1 if major == i else -1
                
        return major
        
        
# Solution 5: Bit manipulation

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        :type nums: List[int]
        :rtyoe:int
        '''
        
        # Solution 5: Bit manipulation
        
        major = 0
        mask = 1
        for i in range(0, 32):
            count = 0
            for j in nums:
                if j & mask:
                    count += 1
                    if count > len(nums)/2:
                        major |= mask
                        break
            mask <<= 1
            
        return major if major >> 31 == 0 else major - (1 << 32) # >> shift to the right by 31 places
        
 
    
                
