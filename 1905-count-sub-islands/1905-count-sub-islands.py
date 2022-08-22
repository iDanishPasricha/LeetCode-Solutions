class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m=len(grid2);
        n=len(grid2[0]);
        
        def dfs(grid,i,j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]!=1:return
            
            grid[i][j]=0;
            dfs(grid,i+1,j);
            dfs(grid,i,j+1);
            dfs(grid,i-1,j);
            dfs(grid,i,j-1);
            

        
        #First check which islands are not there on grid 1 but there on grid 2 
        ans=[];
        for i in range(m):
            for j in range(n):
                if grid1[i][j]==0 and grid2[i][j]==1:
                    dfs(grid2,i,j);
        # mask them and then just count the total islands on grid 2                

        number_of_islands=0;
        for i in range(m):
            for j in range(n):
                if grid2[i][j]==1:
                    dfs(grid2,i,j);
                    number_of_islands+=1;
        return number_of_islands

                

        