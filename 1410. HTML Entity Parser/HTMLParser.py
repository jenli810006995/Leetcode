'''
referred to https://medium.com/algorithm-solving/leetcode-1410-html-entity-parse-c81865719408
'''
class Solution:
    def entityParser(self, text: str) -> str:
        
        mapping = {'&quot;': '"',
                  '&apos;': "'",
                  '&amp;':'&',
                  '&gt;':'>',
                  '&lt;':'<',
                  '&frasl;':'/'}
        
        res = ''
        i = 0
        n = len(text)
        
        while i < n:
            x = text[i]
            pattern_len = 1 # the jump interval for index
            
            if x =='&':
                y = ''
                for j in range(i + 1, min(i + 7, n)): # 7 is the max of the length of an entity
                    if text[j] == ';':
                        sub = text[i: j+1]
                        y = mapping.get(sub, '')
                        break
                            
                # if found symbol, refresh x and update pattern_len
                if y != '':
                    x = y
                    pattern_len = len(sub)
                        
            i += pattern_len
            res += x
        return res
        
        
        
        
