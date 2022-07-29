class Solution:
    def uniqueLetterString(self, S: str) -> int:
        d = {i: [-1, -1] for i in ascii_uppercase}
        print(d)
        ans = 0
        for i, c in enumerate(S):
            k, j = d[c]
            ans += (i - j) * (j - k)
            d[c] = [j, i]
            
            
            
        for i in d:
            k, j = d[i]
            ans += (len(S) - j) * (j - k)
            
            
            
        return ans % (10**9 + 7)
        
        