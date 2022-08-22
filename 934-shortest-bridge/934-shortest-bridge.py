class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        # DFS + BFS 
        n=len(grid);
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        visited=set()
        q=deque();
        def dfs(i,j):
            if i<0 or j<0 or i>=n or j>=n or (i,j) in visited or grid[i][j]==0: return
            q.append([i,j])
            visited.add((i,j))
            dfs(i+1,j);
            dfs(i-1,j);
            dfs(i,j+1);
            dfs(i,j-1);
            
            
        def bfs():
            levels = 0;
            while q:
                for i in range(len(q)):
                    x,y=q.popleft()
                    for direction in directions:
                        new_x=x+direction[0];
                        new_y=y+direction[1];
                        if new_x<0 or new_y<0 or new_x>=n or new_y>=n or (new_x,new_y) in visited :continue
                        if grid[new_x][new_y]==1: return levels # we have reached the second island
                        q.append([new_x,new_y])
                        visited.add((new_x,new_y))
                levels+=1;
            
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    dfs(i,j)
                    return bfs()