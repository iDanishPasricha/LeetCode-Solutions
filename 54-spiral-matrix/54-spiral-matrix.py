class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m=len(matrix)
        n=len(matrix[0])
        
        top_row = 0
        bottom_row = m-1
        
        left_column = 0
        right_column = n-1
        
        
        ans=[];
        
        while left_column<=right_column and top_row<=bottom_row:
            for i in range(left_column,right_column+1):
                ans.append(matrix[top_row][i]);
            top_row+=1;
            for i in range(top_row,bottom_row+1):
                ans.append(matrix[i][right_column]);
            right_column-=1;
            
            if left_column>right_column or top_row>bottom_row: break;
                
            for i in range(right_column,left_column-1,-1):
                ans.append(matrix[bottom_row][i]);
            bottom_row-=1;
            for i in range(bottom_row,top_row-1,-1):
                ans.append(matrix[i][left_column]);
            left_column+=1;
        return ans
                
            
        
                