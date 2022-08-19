class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if not n: return []
        ans=[[0 for i in range(n)] for i in range(n)];
        left,top = 0,0;
        right,bottom = n-1,n-1;
        num = 1
        
        while left<=right and top<=bottom:
            
            for i in range(left,right+1):  
                ans[top][i] = num;
                num+=1
            top+=1;     
            for i in range(top,bottom+1):     
                ans[i][right]=num;
                num+=1
            right-=1;    
            
            

            
            for i in range(right,left-1,-1):
                ans[bottom][i]=num;
                num+=1
            bottom-=1;
            for i in range(bottom,top-1,-1):
                ans[i][left]=num;
                num+=1;
            left+=1;
            
            
        return ans
        
            