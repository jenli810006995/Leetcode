## Time: 10/3/2020

## Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

## Integers in each row are sorted in ascending from left to right.
## Integers in each column are sorted in ascending from top to bottom.

Class solution:
    def searchMatrix(self, target, matrix)-> int:
    '''
    :type target: int
    :type matrix: List[List[int]]
    :rtype: bool
    '''
    if not matrix or not matrix[0]:
        return False
    rows = len(matrix)
    cols = len(matrix[0])
    row, col = 0, cols - 1
    while True:
        if row < rows and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row += 1
            else:
                col -= 1
       else:
           return False
           
           
## Link: https://leetcode.com/problems/search-a-2d-matrix-ii/
## Reference: https://blog.csdn.net/fuxuemingzhu/article/details/79459314
           
           
                
