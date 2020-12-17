'''
referred to https://blog.csdn.net/fuxuemingzhu/article/details/79473739
'''
class Solution {
public:
    int fourSumCount(vector<int>& A, vector<int>& B, vector<int>& C, vector<int>& D) {
        
        const int N = A.size();
        unordered_map<int, int>AB;
        unordered_map<int, int>CD;
        
        for (int i = 0; i < N; i++){
            for (int j = 0; j < N; j++){
                ++AB[A[i] + B[j]];
                ++CD[C[i] + D[j]];
            }
        }
            
        int res = 0;
        for (auto ab : AB){
            res += ab.second*CD[-ab.first];
        }
        return res;
    }
};
