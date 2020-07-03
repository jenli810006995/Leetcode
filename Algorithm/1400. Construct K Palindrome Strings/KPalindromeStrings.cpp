'''
referred to https://zxi.mytechroad.com/blog/hashtable/leetcode-1400-construct-k-palindrome-strings/
'''
class Solution {
public:
    bool canConstruct(string s, int k) {
        
        // Hashtable
        
        if (k > s.length()) return false;
        
        vector<int> f(26); // 26 lower case English alphabet
        
        for (char c : s) f[c - 'a'] ^=1;
        int odd = accumulate(begin(f), end(f), 0);
        return k >= odd;
    }
};

