class Solution:
    def uniqueLetterString(self, s: str) -> int:
        d={}
        for i in s:
            d[i]=[-1,-1]
        ans = 0
        for i in range(len(s)):
            a,b = d[s[i]]
            
            ans+=(b-a)*(i-b)
            
            d[s[i]] = [b,i]

        for i in d:
            a,b  = d[i]
            ans+=(b-a)*(len(s)-b)
        return ans