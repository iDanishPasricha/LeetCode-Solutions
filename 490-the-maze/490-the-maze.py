from collections import deque

class Solution:
       def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        if not maze or not start or not destination:
            return False
        if start == destination:
            return True

        q = deque([(start[0], start[1])])

        visited = set()
        # a set will provide constant time access, we will never have duplicates
        directions_to_go = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while q:
            current = q.popleft()
            if current[0] == destination[0] and current[1] == destination[1]:
                return True
            for direction in directions_to_go: #The ball can go through the empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.
                # move in a direction
                x = current[0] + direction[0]
                y = current[1] + direction[1]
                while 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0:
                    # keep moving until ONE PAST where you can't move (roll) anymore
                    x += direction[0]
                    y += direction[1]
                # roll back one so that you're actually where you should be
                rolled_to_x = x - direction[0]
                rolled_to_y = y - direction[1]
                if (rolled_to_x, rolled_to_y) not in visited:
                    visited.add((rolled_to_x, rolled_to_y))
                    # add this position to be searched from as well
                    q.append((rolled_to_x, rolled_to_y))
        # if you're here no solution was found and everything has been visited
        return False

