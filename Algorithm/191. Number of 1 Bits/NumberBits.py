'''
referred to https://blog.csdn.net/coder_orz/article/details/51323188
'''
# Solution

class Solution:
    def hammingWeight(self, n: int) -> int:
        
        '''
        :type n: int
        :rtype: int
        
        '''
        
        return bin(n).count('1')
        
# Solution

class Solution:
    def hammingWeight(self, n: int) -> int:
        
        '''
        :type n: int
        :rtype: int
        
        '''
        
        count = 0
        while n:
            count += n & 1
            n >>=1
        return count
        
# Solution

class Solution:
    def hammingWeight(self, n: int) -> int:
        
        '''
        :type n: int
        :rtype: int
        
        '''
        
        count = 0
        while n:
            count += 1
            n &= n - 1
        return count
    
    
    


