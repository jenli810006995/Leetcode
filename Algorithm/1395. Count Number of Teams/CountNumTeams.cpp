'''
referred to https://zxi.mytechroad.com/blog/algorithms/array/leetcode-1395-count-number-of-teams/
'''
class Solution {
public:
    int numTeams(vector<int>& rating) {
        // Brute Force
        int n = rating.size();
        int ans = 0;
        for (int i = 0; i < n; i++)
            for (int j = i+1 ; j< n; j++)
                for (int k = j+1; k < n; k++){
                    if (rating[i] < rating[j] && rating[j] < rating[k]
                        || rating[i] > rating[j] && rating[j] > rating[k])
                        ans++;
                }
        return ans;
    }
};

# Time Complexity: O(n^3)
# Space Complexity: O(1)

