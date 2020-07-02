'''
referred to https://zxi.mytechroad.com/blog/greedy/leetcode-1414-find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/

'''
class Solution {
public:
    int findMinFibonacciNumbers(int k) {
        
        int f1 = 1;
        int f2 = 1;
        int ans = 1;
        
        while (f2 <= k){
            swap(f1, f2);
            f2 += f1;
        }
        k -= f1;
        while (k){
            if (k >= f1){
                k -= f1;
                ans +=1;
            }
            f2 -= f1;
            swap( f1, f2);
        }
        return ans;
    }
};




