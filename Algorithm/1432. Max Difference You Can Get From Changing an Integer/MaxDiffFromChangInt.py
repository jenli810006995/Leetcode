'''
referred to https://youtu.be/sOnpt2zHWfQ
'''
# brute-force way

class Solution:
    def maxDiff(self, num: int) -> int:
        
        small = 1<< 60
        big = 0
        
        for x in range(10):
            for y in range(10):
                k = str(num).replace(str(x), str(y))
                
                # test if the new integer is 0 or have leading 0's
                
                if k[0] == '0':
                    continue
                if int(k) == 0:
                    continue
                k = int(k)
                
                small = min(k, small)
                big = max(k, big)
                
        return big - small
        
        
    
