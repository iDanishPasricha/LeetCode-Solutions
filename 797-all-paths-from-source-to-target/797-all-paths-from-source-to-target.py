class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans=[];
        def dfs(curr,temp):
            if curr == len(graph)-1:
                ans.append(temp.copy())
                return
            for neighbor in graph[curr]:
                temp.append(neighbor)
                dfs(neighbor,temp)
                temp.pop()
                

        dfs(0,[0]);
        return ans
    
    
    
    	