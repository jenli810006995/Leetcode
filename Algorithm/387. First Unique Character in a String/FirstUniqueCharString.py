'''
referred to https://blog.csdn.net/coder_orz/article/details/52387946
'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        letters = {}
        
        for c in s:
            letters[c] = letters[c] + 1 if c in letters else 1
        
        for i in range(len(s)):
            if letters[s[i]] == 1:
                return i
            
        return -1
        
        
 # Time Complexity: O(n)
 # Space Complexity: O(1)
 
 
