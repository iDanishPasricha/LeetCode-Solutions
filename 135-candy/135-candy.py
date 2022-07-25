class Solution:
    def candy(self, ratings: List[int]) -> int:
        n=len(ratings)
        ans = [1 for _ in range(n)]
        left = [1 for _ in range(n)]
        right = [1 for _ in range(n)] 
        
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                left[i] = 1+left[i-1]   #check left side
        
        
        for i in range(n-2,-1,-1):    #check right side
            if ratings[i]>ratings[i+1]:
                right[i] = 1+right[i+1]
        for i in range(n):
            ans[i] = max(left[i],right[i])
        
        return sum(ans)
    