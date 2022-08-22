import math
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        for row in range(1, len(matrix)):
            for col in range(len(matrix)):
                matrix[row][col]+= min(matrix[row-1][col], matrix[row-1][col-1] if col - 1 >= 0 else math.inf, matrix[row-1][col+1] if col + 1 < len(matrix) else math.inf)
	
        return min(matrix[-1])