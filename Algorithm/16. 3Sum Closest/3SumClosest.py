## Time: 9/30/2020

## Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. 
## Return the sum of the three integers. You may assume that each input would have exactly one solution.

Class solution:
    def(self, nums: List[int], target:int) -> int:
        N = len(nums)
        nums = sorted(nums)
        
        if N < 3:
            return []
            
        res = sum(nums[:3])
        
        for t in range(N - 2):
            j = t + 1
            m = N - 1
            
            while (j < m):
                tem = nums[t] + nums[j] + nums[m]
                v = tem - target
                
                if (abs(v) < abs(res - target)):
                    res = tem
                    
                if (v == 0):
                    return target
                elif (v > 0):
                    m -=1
                else:
                    j += 1
         return res
     
 ## Link: https://leetcode.com/problems/3sum-closest/
 ## Reference: https://github.com/sunjunee/LeetCode-Python/blob/master/016.%203Sum%20Closest.md
 
 
         
