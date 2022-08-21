class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        visited = set()
        def dfs(r,c,idx):
            if idx==len(word):return True
            if r<0 or r>=m or c<0 or c>=n or board[r][c]!=word[idx] or (r,c) in visited: return False
            visited.add((r,c))
            ans = (dfs(r+1,c,idx+1) or dfs(r-1,c,idx+1) or dfs(r,c+1,idx+1) or dfs(r,c-1,idx+1))
            visited.remove((r,c))
            
            return ans
            

            
        for i in range(m):
            for j in range(n):
                if dfs(i,j,0): return True
        return False
    #O(N*M*4^N)  DFS-->4^N
        