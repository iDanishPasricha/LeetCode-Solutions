class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        
        
        def nextDay(cells):
            temp_array = [0]*len(cells)
            for i in range(1,len(cells)-1):
                if cells[i-1]==cells[i+1]:
                    temp_array[i]=1
            return temp_array
        
        
        # cycle detection
        if len(cells)==0 or n<=0: return cells
        visited = set()
        hasCycle = False
        cycle = 0
        for i in range(n):
            next_day = nextDay(cells)
            next_day_string = ''.join(''.join([str(x) for x in next_day]))
            if next_day_string not in visited:
                visited.add(next_day_string)
                cycle+=1
            else:
                hasCycle=  True
                break
            cells = next_day_string  # now your current cells day is this
        if hasCycle:
            n = n%cycle   #ex:- n = 100 cycle len = 24  now n = 4
            for i in range(n):
                cells = nextDay(cells)
        return cells
    
    
'''
Let K be the number of cells, and N be the number of steps.

Time Complexity: O(K.min(N,2^K))

As we discussed before, at most we could have 2^K possible states. While we run the simulation with N steps, we might need to run min(N, 2^K) steps without fast-forwarding in the worst case.

For each simulation step, it takes O(K) time to process and evolve the state of cells.

Hence, the overall time complexity of the algorithm is O(K.min(N,2^K))


Space Complexity:

The main memory consumption of the algorithm is the hashmap that we used to keep track of the states of the cells. The maximal number of entries in the hashmap would be 2^K as we discussed before.

In the Python implementation, we keep the states of cells as they are in the hashmap. As a result, for each entry, it takes O(K) space. In total, its space complexity becomes O(K⋅2^K)

 '''
            
            
        
        