class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = {i:[] for i in range(numCourses)}
        
        for crs,pre in prerequisites:
            premap[crs].append(pre)
        visited = set()
        def dfs(crs):
            if crs in visited: return False # its a cycle--> [[1,0],[0,1]]
            if premap[crs]==[]: return True  # all prequisites of that course clear
            
            visited.add(crs)
            for prereqs in premap[crs]:
                if not dfs(prereqs): return False  #if we find just 1 course only which can't be completed i.e it has a loop then we will immediately return False

            visited.remove(crs)
            premap[crs] = []
            return True
        
        
        
        for i in range(numCourses):
            if not dfs(i): return False
        return True