class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m=len(grid);
        n=len(grid[0])
        
        def dfs(grid,r,c):
            
            if (r<0 or r>=m) or (c<0 or c>=n) or grid[r][c]!=1: return
         
            grid[r][c]=3
            self.count+=1;
            dfs(grid,r+1,c);
            dfs(grid,r-1,c);
            dfs(grid,r,c+1);
            dfs(grid,r,c-1);
        def dfs2(grid,r,c):
            
            if (r<0 or r>=m) or (c<0 or c>=n) or grid[r][c]!=1: return
         
            grid[r][c]=2
            dfs2(grid,r+1,c);
            dfs2(grid,r-1,c);
            dfs2(grid,r,c+1);
            dfs2(grid,r,c-1);
            
        for i in range(m):
            dfs2(grid,i,0);                
            dfs2(grid,i,n-1)
            
        for j in range(n):
            dfs2(grid,0,j)
            dfs2(grid,m-1,j)
        
        ans= 0;
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    self.count=0;
                    dfs(grid,i,j)
                    ans+=self.count
        return ans
        