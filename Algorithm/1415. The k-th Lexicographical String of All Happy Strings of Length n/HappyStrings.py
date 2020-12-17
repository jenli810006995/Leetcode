'''
referred to https://www.cnblogs.com/seyjs/p/12985249.html

'''
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        queue = ['a', 'b', 'c']
        
        l = []
        
        while len(queue) > 0:
            item = queue.pop(0)
            if len(item) == n:
                l.append(item)
                continue
            if item[-1] == 'a':
                queue.append(item + 'b')
                queue.append(item + 'c')
            elif item[-1] == 'b':
                queue.append(item + 'a')
                queue.append(item + 'c')
                
            elif item[-1] == 'c':
                queue.append(item + 'a')
                queue.append(item + 'b')
                
        l.sort()
        if len(l) < k:
            return ''
        return l[k-1]
    
    # O(n)
