'''
w: BFS
h:  1) find the position of the person
    2) start from the position of the person, search all the possible positions
        then go the next 
    3) we only increase the count after 2)
'''


import collections
class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(0, -1), (0, 1), (1, 0), (-1,0)]
        seen = set()
        
        #1 .find the person
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '*':
                    start = (r,c)
                    break
        
        q = collections.deque([start])
        res = 0

        
        while q:
            # we only need finish the search at current level 
            # then go to next level
            for _ in range(len(q)):
                currR, currC = q.popleft()
                seen.add((currR, currC))
                # 2. reach the pizza
                if grid[currR][currC] == '#':
                    return res

                for dx, dy in directions:
                    x = currR + dx
                    y = currC + dy

                    if 0 <= x < rows and 0 <= y < cols and grid[x][y] != 'X' and (x,y) not in seen:
                        q.append((x,y))
                        seen.add((x,y))
            
            res += 1
        
        return -1