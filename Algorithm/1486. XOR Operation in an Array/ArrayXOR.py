'''
referred to https://youtu.be/5SC8TvrkD8w
'''
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        
        # Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.
        
        x = 0
        
        for  y in range(n):
            x^= (start + 2*y)
            
        return x
        
        
 # Time Complexity: O(n)
 # Space Complexity: O(1)
