class Solution:
    def uniqueLetterString(self, S: str) -> int:
        d = {S[i]: [-1, -1] for i in range(len(S))}

        ans = 0
        
        
        for i in range(len(S)):
            
            a, b = d[S[i]]
            
    
            ans += (b - a) * (i - b) 
            
        
            
            d[S[i]] = [b, i]
            
            
            

            
        for i in d:
            a, b = d[i]

            ans += (b - a) * (len(S) - b)  
            
            
            
        return ans % (10**9 + 7)
        
        