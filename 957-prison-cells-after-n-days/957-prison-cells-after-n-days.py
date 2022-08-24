class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        
        
        def nextDay(cells):
            temp_array = [0]*len(cells)
            for i in range(1,len(cells)-1):
                if cells[i-1]==cells[i+1]:
                    temp_array[i]=1
            return temp_array
        
        
        
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
            
            
        
        