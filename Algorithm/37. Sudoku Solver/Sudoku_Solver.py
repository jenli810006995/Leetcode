class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or len(board) == 0: return 
        self.solve(board)
        
    def solve(self, board):
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == '.':
                    for c in '123456789':
                        if self.is_valid(board, i, j, c):
                            board[i][j] = c
                            if self.solve(board):
                                return True
                            else:
                                board[i][j] = '.'
                    return False
        return True
        
    def is_valid(self, board, row, col, c):
        for num in range(0,9): # row and col would be between 0 and 8, while c would be in 1 and 9
            if board[row][num] == c: return False 
            if board[num][col] == c: return False
            if board[3 * int(row/3) + int(num/3)][3 * int(col/3) + num%3] == c: return False
        return True
        
        
# Link: https://leetcode.com/problems/sudoku-solver/

# Reference: https://youtu.be/cgXgwzurhrs
