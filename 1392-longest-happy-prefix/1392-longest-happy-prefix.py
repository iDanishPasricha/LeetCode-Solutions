class Solution:
    def longestPrefix(self, s: str) -> str:
        ans =  ''
        for i in range(len(s)):
            if s[:i]==s[-i:]:
                ans = s[:i]
        return ans
        