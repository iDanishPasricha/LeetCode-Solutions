class Solution:
    def uniqueLetterString(self, S: str) -> int:
        d = {i: [-1, -1] for i in ascii_uppercase}

        ans = 0
        for i in range(len(S)):
            
            k, j = d[S[i]]
            ans += (i - j) * (j - k)
            d[S[i]] = [j, i]
            
            
            
        for i in d:
            k, j = d[i]
            ans += (len(S) - j) * (j - k)
            
            
            
        return ans % (10**9 + 7)
        
        