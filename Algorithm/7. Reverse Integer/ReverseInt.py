# Time: 10/30/2020
# Link: https://leetcode.com/problems/reverse-integer/
# Reference: https://blog.csdn.net/coder_orz/article/details/52039990

class Solution:
    def reverse(self, x) -> int:
        '''
        type: int
        rtype: int 
        '''   
        x = int(str(x)[::-1]) if x >= 0 else -int(str(-x)[::-1])
        return x if x < 2147483648 and x >= -2147483648 else 0
    
    
