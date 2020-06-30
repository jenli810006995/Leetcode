'''
referred to https://youtu.be/sOnpt2zHWfQ
'''
# brute-force way

class Solution:
    def maxDiff(self, num: int) -> int:
        
        # there is only 100 possibilities for x and y's permutations
        
        small = 1 << 60
        big = 0
        
        # x and y are both 0 - 9
        
        for x in range(10):
            for y in range(10):
                k = str(num).replace(str(x), str(y))
                
        # check if there are leading zeros or if the new integer is 0
        
                if k[0] == '0':
                    continue
                if int(k) == 0:
                    continue
                    
                k = int(k)

                small = min(k, small)
                big = max(k, big)
                
        return big - small
    
        
        
    
