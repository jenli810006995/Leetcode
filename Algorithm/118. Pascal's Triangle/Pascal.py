# Time: July 18 2020

# Solution 1:

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        # Solution 1
        
        '''
        :type numRows: int
        :rtype: List[List[int]]
        '''
        
        if numRows == 0:
            return []
        res = [[1]]
        for i in range(1, numRows):
            res.append([])
            for j in range(i+1):
                res[i].append((res[i-1][j-1] if j > 0 else 0) + (res[i-1][j] if j < i else 0))
        return res
    
 # Solution 2: Consider the first and the last number of each row are all 1
 
 class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        # Solution 2
        # the first and the last number in each row are all 1
        
        '''
        :type numRows: int
        :rtype: List[List[int]]
        '''
        
        res = []
        
        for i in range(0, numRows):
            res.append([1] * ( i + 1))
            for j in range(1, i):
                res[i][j] = res[i-1][j-1] + res[i-1][j] 
        return res
        
 # Credit: http://blog.csdn.net/coder_orz/article/details/51589254
        
