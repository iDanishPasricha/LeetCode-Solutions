class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row_highest=[];
        column_highest=[];
        m=len(grid);
        n=len(grid[0])
        for i in grid:
            row_highest.append(max(i));
        transposed_matrix = [[grid[j][i] for j in range(m)] for i in range(n)]
        for i in transposed_matrix:
            column_highest.append(max(i));
        new_matrix = [[0 for j in range(n)] for i in range(m)]
        
        for i in range(len(row_highest)):
            for j in range(len(column_highest)):
                new_matrix[i][j] = min(row_highest[i],column_highest[j])
        sum1=0;
        for i in range(len(new_matrix)):
            for j in range(len(new_matrix[0])):
                sum1+=abs(new_matrix[i][j]-grid[i][j])
        return sum1
            
        