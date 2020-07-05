'''
referred to https://blog.csdn.net/fuxuemingzhu/article/details/79826703
'''
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        # loop and save the smallest and the second smallest
        # and if we see the value less than the second smallest
        # then we have the list with length = 3
        
        first, second = float('inf'), float('inf')
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False
    
    
