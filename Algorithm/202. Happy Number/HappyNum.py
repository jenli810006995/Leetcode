'''
referred to https://www.polarxiong.com/archives/LeetCode-202-happy-number.html
'''
class Solution:
    def isHappy(self, n: int) -> bool:
        '''
        :type n: int
        :rtype: bool
        '''
        got = set()
        
        while n != 1 and n not in got:
            got.add(n)
            sum = 0
            while n:
                sum += (n % 10)**2
                n //= 10
            n = sum
            
        return n == 1
        
        # check if n = 1 or if the sum of squared has seen before. If not, store in the set
        
        
