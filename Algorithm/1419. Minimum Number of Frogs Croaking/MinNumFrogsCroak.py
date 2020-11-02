'''
referred to https://blog.csdn.net/fuxuemingzhu/article/details/105613506
'''
class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
    
        count = collections.Counter()
    
        prev = {'k':'a','a': 'o', 'o': 'r', 'r': 'c'}
    
        res = 0
    
        for c in croakOfFrogs:
    
            if c =='c':
                count[c] +=1
            else:
                if count[prev[c]] >0:
                    if c != 'k':
                        count[c] += 1
                    count[prev[c]] -=1
                else:
                    return -1
            
            res = max(res, sum(count.values()))
    
        
        return res if sum(count.values())== 0 else -1
    
    
   
