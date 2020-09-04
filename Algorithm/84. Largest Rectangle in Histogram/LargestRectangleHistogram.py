```
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

Example:

Input: [2,1,5,6,2,3]
Output: 10

```
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        i = 0
        area = 0
        
        while i < len(heights):
            if stack == [] or heights[i] > heights[stack[len(stack)-1]]:
                stack.append(i)
            else:
                curr = stack.pop()
                width = i if stack == [] else i - stack[len(stack) - 1] - 1
                area = max(area, width*heights[curr])
                i -=1
            i += 1
            
        while stack != []:
            curr = stack.pop()
            width = i if stack ==[] else len(heights) - stack[len(stack)-1] - 1
            area = max(area, width*heights[curr])
        return area
                
        # Link: https://leetcode.com/problems/largest-rectangle-in-histogram/
        # Reference: https://www.cnblogs.com/zuoyuan/p/3783993.html
