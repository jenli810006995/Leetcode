Time: 10/11/2020

According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

```
Example:

Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
```
Follow up:

Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?

Solution:
```
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        if board and board[0]:
            M, N = len(board), len(board[0])
            board_next = copy.deepcopy(board)
            for m in range(M):
                for n in range(N):
                    lod = self.liveOrDead(board, m, n)
                    if lod == 2:
                        board_next[m][n] = 0
                    elif lod == 1:
                        board_next[m][n] = 1
            for m in range(M):
                for n in range(N):
                    board[m][n] = board_next[m][n]

    def liveOrDead(self, board, i, j):
        ds = [(1,1), (1, -1), (1, 0), (-1, 1), (-1, 0), (-1, -1), (0, 1), (0, -1)]
        live_count = 0
        M, N = len(board), len(board[0])
        for d in ds:
            r, c = i + d[0], j + d[1]
            if 0 <= r < M and 0 <= c < N:
                if board[r][c] == 1:
                    live_count += 1
        if live_count < 2 or live_count > 3:
            return 2
        elif board[i][j] == 1 or (live_count == 3 and board[i][j] == 0):
            return 1
        else:
            return 0
           
```

[Link](https://leetcode.com/problems/game-of-life/)

[Reference](https://blog.csdn.net/fuxuemingzhu/article/details/82809923)