'''
referred to https://youtu.be/qNbwIHhMOr8
'''
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        ans = []
        
        c = 0
        
        for x in nums:
            c += x
            ans.append(c)
            
        return ans
        
        

