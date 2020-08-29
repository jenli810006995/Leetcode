/* Logic: The prerequisite for this question is 1 <= a[i] <= n, so we can complete this in O(n) time and O(1) space. */
/* We replace nums[i] and nums[nums[i]-1], and then we compare nums[i] and i + 1. If nums[i] is not equal to i+1,
/* we store i+1 in res

/* Solution */

class Solution{
    public: 
        vector<int> findDisappearedNumbers(vector<int>&nums){
        /* create a res object */    
        vector<int> res;
        
        for (int i = 0; i < nums.size(); ++i){
            if (nums[i] != nums[nums[i] - 1]){
                swap(nums[i], nums[nums[i]-1]);
                --i;
                }
            }
        
        for (int i = 0; i < nums.size(); ++i){
            if (nums[i] != i + 1){
                res.push_back(i + 1);
                }
            }
        return res;
    }
};

/* Link: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/ */

/* Reference: https://www.cnblogs.com/grandyang/p/6222149.html */

