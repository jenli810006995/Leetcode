class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = 0
        n = len(matrix)
        
        while m <= n/2:
            k = m
            while k < n-1-m:
                matrix[m][k], matrix[k][n-1-m], matrix[n-1-m][n-1-k], matrix[n-1-k][m] = \
                matrix[n-1-k][m], matrix[m][k], matrix[k][n-1-m], matrix[n-1-m][n-1-k]
                k += 1
            m += 1
            
            
## Link: https://leetcode.com/problems/rotate-image/
## Reference: https://www.programmersought.com/article/16062119088/
            
