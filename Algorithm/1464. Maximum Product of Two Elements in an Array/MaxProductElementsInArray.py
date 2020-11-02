'''
referred to https://youtu.be/XJ1pYgzimYo
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # greedy
        
        nums.sort()        
        return (nums[-1]-1)*(nums[-2]-1)
        
 
 # Time Complexity: O(n)
 # Space Complexity: O(1)
 
 
