class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(grid,r,c):
            if r>=m or r<0 or c<0 or c>=n:return 0
            if grid[r][c]==0: return 0
            else:
                self.count+=1;
                grid[r][c]=0;
                dfs(grid,r+1,c);
                dfs(grid,r-1,c);
                dfs(grid,r,c+1);
                dfs(grid,r,c-1);
                
            
        m=len(grid);
        n=len(grid[0]);
        ans=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    self.count=0;
                    dfs(grid,i,j);
                    ans = max(ans,self.count);
        return ans
                