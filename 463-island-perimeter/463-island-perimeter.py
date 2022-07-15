class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def dfs(grid,r,c):
            if r>=m or r<0 or c<0 or c>=n or grid[r][c]==0:return 1 #je boundary te pahunch gya ya water cell te ta matlabh permiter ch add ho sakda
            
            if (r,c) in visited: return 0
            
            else:
                visited.add((r,c))
                
                return dfs(grid,r+1,c)+dfs(grid,r-1,c)+dfs(grid,r,c+1)+dfs(grid,r,c-1);
                
                
                
                
        m=len(grid);
        n=len(grid[0]);
        visited=set()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    return dfs(grid,i,j);
                  
        