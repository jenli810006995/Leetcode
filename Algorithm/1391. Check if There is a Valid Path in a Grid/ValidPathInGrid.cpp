'''
referred to https://www.acwing.com/file_system/file/content/whole/index/content/406546/
'''
class Solution {
public:
    void add(int x, int y, queue<pair<int, int>>& q, vector<vector<bool>>& vis){
        if (!vis[x][y]){
            vis[x][y] = true;
            q.push(make_pair(x, y));
        }
    }
    
    bool hasValidPath(vector<vector<int>>& grid){
        int m = grid.size(), n = grid[0].size();
        
        vector<vector<bool>> vis(m, vector<bool>(n, false));
        queue<pair<int, int>> q;
        vis[0][0] = true;
        
        q.push(make_pair(0, 0));
        
        while(!q.empty()){
            auto u = q.front();
            q.pop();
            int x = u.first, y = u.second;
            if (x == m-1 && y == n-1)
                return true;
            
            if ((grid[x][y] == 2 || grid[x][y] == 5|| grid[x][y] == 6)
                && x - 1 >= 0 
                &&(grid[x-1][y] == 2 || grid[x-1][y] == 3 || grid[x-1][y]==4))
                add(x - 1, y, q, vis);
            
            if ((grid[x][y] == 1 || grid[x][y] == 3 || grid[x][y] == 5)
               && y - 1 >=0 
               && (grid[x][y - 1] == 1 || grid[x][y - 1] == 4 || grid[x][y - 1] == 6))
                add(x, y - 1, q, vis);
            
            if ((grid[x][y] == 2 || grid[x][y] == 3 || grid[x][y] == 4)
               && x + 1 < m
               && (grid[x + 1][y]==2 || grid[x + 1][y] == 5 || grid[x + 1][y] == 6))
               add(x + 1, y, q, vis);
            
            if ((grid[x][y] == 1 || grid[x][y] == 4 || grid[x][y] == 6)
               && y + 1 < n
               && (grid[x][y + 1]==1 || grid[x][y + 1] == 3 || grid[x][y + 1] == 5))
               add(x, y + 1, q, vis);
        }
        return false;
    }
};

