'''
referred to https://youtu.be/k4YsQgeJBt0

'''

class Solution:

    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        
        rows = len(nums)
        
        v = []
        
        for x in range(rows):
            for y in range(len(nums[x])):
                v.append((x + y, y, nums[x][y]))
                
            
        ans = list(x[2] for x in sorted(v))
        
        return ans
        
       
