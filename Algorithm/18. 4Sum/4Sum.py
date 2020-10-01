## Time: 10/1/2020

## Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? 
## Find all unique quadruplets in the array which gives the sum of target.

## Note: The solution set must not contain duplicate quadruplets.

Class solution:
    def fourSum(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        N = len(nums)
        res = []
        i = 0
        
        while i < N - 3:
            j = i + 1
            while j < N - 2:
                k = j + 1
                l = N - 1
                remain = target - nums[i] - nums[j]
                
                while k < l:
                    if nums[k] + nums[l] > remain:
                        l -= 1
                    elif nums[k] + nums[l] < remain:
                        k += 1
                    else:
                        res.append([nums[i], nums[j], nums[k], nums[l]])
                        
                        while k < l and nums[k] == nums[k + 1]:
                            k += 1
                        while k < l and nums[l] == nums[l - 1]:
                            l -= 1
                        k += 1
                        l -= 1
                while j < N - 2 and nums[j] == nums[j + 1]:
                    j += 1
                j += 1
            while i < N - 3 and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        return res
                   
## Link: https://leetcode.com/problems/4sum/
## Reference: https://blog.csdn.net/fuxuemingzhu/article/details/83543296
