'''
referred to https://youtu.be/hTEVGYRGLsQ
'''
class Solution:
    def average(self, salary: List[int]) -> float:       
        # first sort 
        salary.sort()
        return (sum(salary) - salary[0] - salary[-1])/(len(salary)-2)
        
 
# Time Complexity: O(n)
# Space Complexity: O(1)

