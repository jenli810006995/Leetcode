'''
referred to https://youtu.be/H8_hAPOW5UE
'''

class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        
        q = sorted(s1)
        w = sorted(s2)
        
        def can(a,b):
            for x, y in zip(a,b):
                if x > y:
                    return False
            return True
            
        return can(q,w) or can(w,q)
        
        
