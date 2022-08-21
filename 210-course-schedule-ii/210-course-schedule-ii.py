class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap = {i:[] for i in range(numCourses)}
        
        for crs,pre in prerequisites:
            premap[crs].append(pre)
        
        visited = set()
        cycle = set()
        ans = []
        def dfs(crs):
            if crs in cycle : return False
            if crs in visited : return True
            
            cycle.add(crs)
            for pre in premap[crs]:
                if not dfs(pre): return False
            cycle.remove(crs)
            visited.add(crs)
            ans.append(crs)
            
            return True
            
        
        
        for i in range(numCourses):
            if not dfs(i): return []
        return ans
            
        