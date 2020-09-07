class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        start = 0
        end = len(height) - 1 # height is a list
        
        while start < end:
            area = (end - start)*min(height[end], height[start])
            if area > max_area:
                max_area = area
            if height[end] < height[start]: # height is a list, and here is to compare the values
                end -=1
            else:
                start += 1
        return max_area
        
        
## Link: https://leetcode.com/problems/container-with-most-water/
## Reference: http://jelices.blogspot.com/2014/05/leetcode-python-container-with-most.html
        
