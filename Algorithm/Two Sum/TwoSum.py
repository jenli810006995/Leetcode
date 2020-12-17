class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        
        for idx, num in enumerate(nums):
            d[num] = idx
            
        for idx, num in enumerate(nums):
            if (target - num) in d and d[target - num] != idx:
                return [idx, d[target - num]]
                
 # Link: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/546/
 # Reference: https://youtu.be/B0ja2efUAEI
