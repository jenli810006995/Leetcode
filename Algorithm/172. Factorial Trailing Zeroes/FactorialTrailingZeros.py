'''
referred to https://blog.csdn.net/coder_orz/article/details/51590478
'''
# Solution 1: Iterate

class Solution:
    def trailingZeroes(self, n: int) -> int:
        '''
        :type n : int
        :rtype: int
        '''
        
        res = 0
        while n > 0:
            n =n//5
            res += n
        return res
        
 # Solution 2: Recursive
 
 class Solution:
    def trailingZeroes(self, n: int) -> int:
        '''
        :type n : int
        :rtype: int
        '''
        
        return 0 if n == 0 else n//5 + self.trailingZeroes(n//5)
