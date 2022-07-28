class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        original_pattern = grid[0];
        inverted_pattern = [1-i for i in grid[0]]
        
        for i in range(1,len(grid)):
            if grid[i]!=original_pattern and grid[i]!=inverted_pattern:
                return False
        return True
        
        