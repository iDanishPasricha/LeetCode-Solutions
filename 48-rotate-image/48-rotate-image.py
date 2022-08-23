class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix) 
        
        # Transpose and reflect
        
        # Transpose
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
                
        #Reflect
        for i in range(n):
            matrix[i]=matrix[i][::-1]
            
            
'''
Let M be the number of cells in the grid.

Time complexity : O(M) We perform two steps; transposing the matrix, and then reversing each row. Transposing the matrix has a cost of O(M) because we're moving the value of each cell once. Reversing each row also has a cost of O(M), because again we're moving the value of each cell once.

Space complexity : O(1) because we do not use any other additional data structures.

'''
    