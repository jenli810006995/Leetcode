'''
referred to https://blog.csdn.net/coder_orz/article/details/51406015
'''

# Solution 1: sorted(), working for string as well as unicode

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # if the two have different lengths, return False
        
        return sorted(s) == sorted(t)
        
        
# Solution 2: array

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    
         if len(s) != len(t):
             return False
    
         alpha = [0]*26
         beta = [0]*26
     
         for c in s:
             alpha[ord(c) - 97] += 1
         for c in t:
             beta[ord(c) - 97] += 1
         
         return alpha == beta
