class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans =  0
        d = {}
        
        l = 0
        
        for r in range(len(s)):
            d[s[r]] =  1 + d.get(s[r],0)
            
            while( (r-l+1) - max(d.values()) > k):
                d[s[l]]-=1
                l+=1
            
            ans = max(ans,r-l+1)
        return ans
                
        