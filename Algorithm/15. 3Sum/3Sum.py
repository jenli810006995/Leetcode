## Time: 9/26/2020

## Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

## Notice that the solution set must not contain duplicate triplets.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        
        for i in range(n - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, n - 1
            while j < k:
                cur = nums[i] + nums[j] + nums[k]    
                if cur < 0:
                    j += 1
                elif cur > 0:
                    k -=1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    while j + 1 < k and nums[j] == nums[j + 1]:
                        j += 1
                    while k - 1 > j and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
        return res
    
    ## Link: https://leetcode.com/problems/3sum/
    ## Reference: https://maxming0.github.io/2020/07/08/3Sum/
    
