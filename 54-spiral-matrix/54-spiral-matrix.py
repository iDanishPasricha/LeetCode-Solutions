class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m=len(matrix)
        n=len(matrix[0])
        left,top=0,0;
        right,bottom=n-1,m-1;
        ans=[];
        while left<=right and top<=bottom:
            for i in range(left,right+1):     #--->
                ans.append(matrix[top][i]);
            top+=1;     #shrink
            for i in range(top,bottom+1):     # bottom ja
                ans.append(matrix[i][right]);
            right-=1;    #shrink
            if left>right or top>bottom: break
            
            for i in range(right,left-1,-1):
                ans.append(matrix[bottom][i]);
            bottom-=1;
            for i in range(bottom,top-1,-1):
                ans.append(matrix[i][left]);
            left+=1;
        return ans
            
                