'''
referred to https://youtu.be/hSBOIbmbssE
'''
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:     
        ans = []
        N = len(nums)
        
        for index in range(N//2):
            ans.append(nums[index])
            ans.append(nums[index+N//2])
            
        return ans
 
# Time Complexity: O(n)
# Space Complexity: O(n)

