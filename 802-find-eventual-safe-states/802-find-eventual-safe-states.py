class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        n=len(graph);
        safe={};
        
        
        def dfs(curr_node):
            if curr_node in safe: return safe[curr_node];
            safe[curr_node]=False #First lets assume this node is not safe
            for neighbours in graph[curr_node]:
                if dfs(neighbours)==False: return False 
                #if any of the neighbors is unsafe then this node is unsafe
            safe[curr_node]=True
            #else safe
            return True
            
            
            
        
        
        ans=[];
        for i in range(n):
            if dfs(i): ans.append(i);
        return ans
            