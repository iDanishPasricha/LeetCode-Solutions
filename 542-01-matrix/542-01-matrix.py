from collections import deque
class Solution:
    def updateMatrix(self, grid: List[List[int]]) -> int:
        m=len(grid);
        n=len(grid[0]);
        #BFS approach
        visited=set();
        q=deque();
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    q.append((i,j));
                    grid[i][j]=0
        visited.update(q)
        directions=[(-1,0),(0,1),(1,0),(0,-1)]
        level=0;
        while q:
            for i in range(len(q)):
                (x,y)=q.popleft();
                for direction in directions: 
                    new_x = x + direction[0];
                    new_y = y + direction[1];
                    
                    if new_x>=0 and new_x<=m-1 and new_y>=0 and new_y<=n-1 and (new_x,new_y) not in visited:
                        q.append((new_x,new_y))
                        visited.add((new_x,new_y)); 
                        
                
                grid[x][y] = level
            level+=1;
        return grid

                    
                
        
        