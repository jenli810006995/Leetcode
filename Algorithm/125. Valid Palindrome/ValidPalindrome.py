'''
referred to https://blog.csdn.net/coder_orz/article/details/51304295
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        :type s: str
        :rtype: bool
        '''
        new_s = [] 
        for c in s:
            if c.isalnum(): # if c is alpha-numeric
                new_s.append(c.lower())

        length = len(new_s)
        for i in range(0, length//2):
            if new_s[i] != new_s[length - i - 1]:
                return False
        return True
    
  # Solution 2: Double pointers
  
  class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        :type s: str
        :rtype: bool
        '''
        # Two pointers 
        
        i = -1
        j = len(s)
        while True:
            i += 1
            j -= 1
            if i > j:
                return True
            while i < j:
                if not s[i].isalnum():
                    i += 1
                else:
                    break
                    
            while i < j:
                if not s[j].isalnum():
                    j -=1
                else:
                    break
            if s[i].lower() != s[j].lower():
                return False
                
  # Solution 3: List
  
  class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        :type s: str
        :rtype: bool
        '''
        # List
        
        cleanlist = [c for c in s.lower() if c.isalnum()]
        return cleanlist == cleanlist[::-1]
        
       
  
