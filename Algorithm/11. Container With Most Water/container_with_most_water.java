// Brute Force

class Solution{
    public int maxArea(int[] height){
        int maxarea = 0;
        for (int i = 0; i < height.length; i ++)
            for (int j = 0; j < height.length; j ++)
                maxarea = Math.max(maxarea, Math.min(height[i] , height[j])* (j - i));
        return maxarea;
    }
}


// Two-pointer solution

class Solution{
    public int maxArea(int[] height){
        int maxarea = 0; // initialize to 0
        int left = 0;
        int right = height.length - 1;
        
        while (left < right){ // compare b/w left and right pointers
            maxarea = Math.max(maxarea, Math.min(height[right], height[left])*(right - left));
            if (height[left] < height[right])
                left ++;
            else
                right --;
        }
        return maxarea;
    }
}


// Link: https://leetcode.com/problems/container-with-most-water/
// Reference: https://youtu.be/TI3e-17YAlc
