'''
referred to https://www.bilibili.com/video/av328159525/

'''

class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        
        def gcd(x, y):
            return y if x == 0 else gcd(y % x, x)
        
        # gcd(i, j)==1 means it is simplified fraction
        
        return ["%s/%s" % (i,j) for j in range(2, n+1) for i in range(1, j) if gcd(i, j) == 1]
        
        
'''
time complexity: n^2(logn)

'''
