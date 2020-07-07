'''
referred to https://blog.csdn.net/coder_orz/article/details/51705094
'''

# Solution 1

class Solution:
    def reverseBits(self, n: int) -> int:
        
        '''
        :type n :int
        :rtype: int
        '''
        
        # use bin()
        
        b = bin(n)[:1:-1]
        return int(b + '0'*(32- len(b)), 2)

# Solution 2

class Solution:
    def reverseBits(self, n: int) -> int:
        
        '''
        :type n :int
        :rtype: int
        '''
        res = 0
        for i in range(32):
            res <<= 1
            res |= ((n >> i)&1)
        return res


