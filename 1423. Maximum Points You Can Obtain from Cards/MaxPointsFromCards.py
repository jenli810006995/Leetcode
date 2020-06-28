'''
referred to https://youtu.be/qwmvDm20F5o
'''

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        best = 0
        current = 0
        
        for x in range(k):
            current += cardPoints[x]
            
        best = max(best, current)
        
        N = len(cardPoints)
     
        for x in range(k):
            current -= cardPoints[k-x-1]
            current += cardPoints[N-x-1]
            best = max(best, current)
            
        return best
    
