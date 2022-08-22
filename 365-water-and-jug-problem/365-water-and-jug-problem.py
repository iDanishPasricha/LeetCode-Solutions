class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        queue = collections.deque()
        queue.append((0,0))
        visited = set()
        visited.add((0,0))

        while queue:
            jug1,jug2 = queue.popleft()
            if jug1 + jug2 == targetCapacity:
                return True

            fill1 = (jug1Capacity, jug2)
            fill2 = (jug1, jug2Capacity)
            empty1 = (0, jug2)
            empty2 = (jug1, 0)
            pour1 = (min(jug1+jug2, jug1Capacity), max(jug2-(jug1Capacity-jug1), 0))
            pour2 = (max(jug1-(jug2Capacity-jug2), 0), min(jug1+jug2, jug2Capacity))

            for option in [fill1, fill2, empty1, empty2, pour1, pour2]:
                if option not in visited:
                    visited.add(option)
                    queue.append(option)

        return False
    
'''
The idea is to traverse over the possible capacity states of the two jugs (Jug1,Jug2).
Any jug can be full, semi-full or empty (in any state)
At any state (a,b) of the jugs we can do 6 things.
Pour contents of jug1 to jug2. (note that jug1 may still have some water left after pouring water to jug2)
Pour contents of jug2 to jug1. (note that jug2 may still have some water left after pouring water to jug1)
Empty jug1 completely.
Empty jug2 completely.
Fill jug1 completely (to its maximum limit)
Fill jug2 completely (to its maximum limit)
We are going to keep a note of the already visited states (a,b) of the jugs in a HashSet of string with key being: "a,b" (the capacities of the jugs separated by a comma. This helps us to avoid redundant calculations).

We are going to start with a queue containing only the state (0,0) (both jugs empty) initially. Apply the above 6 operations on that and add those states to the queue if they weren't already visited. Then simply keep checking whether in any of the states we get the summation of the capacities == z.

If we don't find any such state. return false.

Also, don't skip questions just because they have a low like to dislike ratio (unless the question or the testcases are wrong) because I've observed that interviewers like asking questions which have a lot of loose ends. So try clearing those doubts from the discussion section of leetcode and then try attempting those questions.
'''