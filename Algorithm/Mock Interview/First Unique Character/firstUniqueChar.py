import collections
class Solution:
    def firstUniqueChar(self, s:str) -> int:
        c= collections.Counter(s)
        for index, x in enumerate(s):
            if c[x] == 1:
                return index
        return -1
        
