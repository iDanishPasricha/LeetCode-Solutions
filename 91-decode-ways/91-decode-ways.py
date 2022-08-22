class Solution:
    def numDecodings(self, s: str) -> int:
        
        
        def helper(s,index,dp):
            if index == len(s): return 1
            if s[index] == "0": return 0
            if index == len(s)-1: return 1
            
            if dp[index]: return dp[index]
            
        
            path1 = helper(s,index+1,dp);
            if int(s[index:index+2])<=26: path2= helper(s,index+2,dp);
            else: path2=0;
            dp[index]=path1+path2
            return dp[index]
        
        dp=[0]*(len(s)+1);
        ans=helper(s,0,dp);
        return ans
        