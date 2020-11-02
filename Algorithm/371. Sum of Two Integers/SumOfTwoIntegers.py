'''
referred to https://darktiantian.github.io/371-Sum-of-Two-Integers-Python/
'''
# Use np.int32

import numpy as np

class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b != 0:
            a, b = np.int32(a ^ b), np.int32((a & b)<< 1)
        return int(a)
        
# Time Complexity: O(n)
# Space Complexity: O(1)

