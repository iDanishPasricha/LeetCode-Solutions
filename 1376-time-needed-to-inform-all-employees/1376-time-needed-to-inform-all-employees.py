class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        self.Tree = [[] for _ in range(n)]
        
        
        for i in range(len(manager)):
            if manager[i]==-1:
                starting_row = i;
                continue;
            self.Tree[manager[i]].append(i);
        print(self.Tree)
            
            
        def dfs(i):
            if len(self.Tree[i])==0: return 0
            ans2=0;
            for j in self.Tree[i]:
                ans2=max(ans2,dfs(j)+informTime[i])
            return ans2
            
            
        ans=0;
        for i in self.Tree[starting_row]:
            ans=max(ans, dfs(i)+informTime[starting_row]);
        return ans
            