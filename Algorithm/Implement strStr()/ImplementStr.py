class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        j = 0
        m = len(needle)
        n = len(haystack)
        
        if m == 0:
            return 0
        while i < n and n - i + 1 >= m:
            if haystack[i] == needle[j]:
                temp = i
                while j < m and i < n and needle[j] == haystack[i]:
                    i += 1
                    j += 1
                if j == m:
                    return temp
                i = temp + 1
                j = 0
            else:
                i += 1
       return -1
       
## ------------------------------------------------------------------------------------------
## Link: https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/885/
## Reference: https://www.tutorialspoint.com/implement-strstr-in-python#:~:text=%20Implement%20strStr%20%28%29%20in%20Python%20%201,i%20by%201%209%20return%20-1%20More%20
                
                    
