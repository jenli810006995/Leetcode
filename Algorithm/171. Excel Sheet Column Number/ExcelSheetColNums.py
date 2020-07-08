'''
referred to https://blog.csdn.net/coder_orz/article/details/51406455
'''
# Solution 1:

class Solution:
    def titleToNumber(self, s: str) -> int:
        '''
        :type s: str
        :rtype:int
        '''
        
        sum = 0
        for c in s:
            sum = sum * 26 + ord(c) - 64 # 64 = ord('A') -1
        return sum

# Solution 2: Map and Reduce

class Solution:
    def titleToNumber(self, s: str) -> int:
        '''
        :type s: str
        :rtype:int
        '''
        
        return reduce(lambda x, y: x*26 + y, map(lambda x: ord(x) - 64, s), 0)
        
