class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        ans = []
        for i, j in adjacentPairs:
            graph[i].append(j)
            graph[j].append(i)
            
        visited =set();
        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in visited:
                    ans.append(neighbor)
                    visited.add(neighbor);
                    dfs(neighbor);
                 
            
        for i in graph:
            if len(graph[i])==1:
                start = i;
                break;
                
        visited.add(start);
        ans.append(start)
        dfs(start);
        return ans