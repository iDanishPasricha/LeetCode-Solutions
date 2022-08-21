class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = {i:[] for i in range(numCourses)}
        
        for crs,pre in prerequisites:
            premap[crs].append(pre)
        visited = set()
        def dfs(crs):
            if crs in visited: return False
            if premap[crs]==[]: return True
            
            visited.add(crs)
            for neighbour in premap[crs]:
                if not dfs(neighbour): return False

            visited.remove(crs)
            premap[crs] = []
            return True
        
        
        
        for i in range(numCourses):
            if not dfs(i): return False
        return True