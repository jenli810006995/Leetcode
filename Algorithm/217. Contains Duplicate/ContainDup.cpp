'''
referred to https://zxi.mytechroad.com/blog/hashtable/leetcode-217-contains-duplicate/
'''
# Solution 1: HashTable

class Solution {
    public:
        bool containsDuplicate(vector<int>& nums) {    
            unordered_set<int> s;
            for (int num: nums)
                if (!s.insert(num).second) return true;
            return false;
    }
};

# Time Complexity: O(n)
# Space Complexity: O(n)

# Solution 2: Sorting

class Solution {
    public:
        bool containsDuplicate(vector<int>& nums) {    
           sort(begin(nums), end(nums));
            for (int i = 1; i < nums.size(); i++){
                if (nums[i] == nums[i - 1]) return true;
            }
            return false;
    }
};

# Time Complexity: O(nlongn)
# Space Complexity: O(1)

