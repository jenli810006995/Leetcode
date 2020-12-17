/* 315. Count of Smaller Numbers After Self */

/* Time: 09/24/2020 */

class Solution {
    public:
        vector<int> countSmaller(vector<int> & nums){
        vector<int> t, res(nums.size());
        for (int i = nums.size() - 1; i >=0 ; i--){
            int left = 0, right = t.size();
            while (left < right){
                int mid = left + (right - left)/2;
                if (t[mid] >= nums[i])
                    right = mid;
                else
                    left = mid + 1;
            }
            res[i] = right;
            t.insert(t.begin() + right, nums[i]);
        }
     return res;
    };
};

/* Link: https://leetcode.com/problems/count-of-smaller-numbers-after-self/ */

/* Reference: https://www.cnblogs.com/grandyang/p/5078490.html  */

