'''
referred to http://bookshadow.com/weblog/2016/08/01/leetcode-kth-smallest-element-in-a-sorted-matrix/
'''
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        '''
        :type matrix: List[List[int]]
        :type k: int
        rtype: int
        '''
        
        m, n = len(matrix), len(matrix[0])
        
        visited = [[False]*n for _ in range(m) ]
        q = [(matrix[0][0], 0 , 0)]
        ans = None
        visited[0][0] = True
        for _ in range(k):
            ans, i, j = heapq.heappop(q)
            if i + 1 < m and not visited[i + 1][j]:
                visited[i + 1][j] = True
                heapq.heappush(q, (matrix[i + 1][j], i + 1, j))
            if j + 1 < n and not visited[i][j + 1]:
                visited[i][j + 1] = True
                heapq.heappush(q, (matrix[i][j + 1], i, j + 1))
        return ans
        
       
