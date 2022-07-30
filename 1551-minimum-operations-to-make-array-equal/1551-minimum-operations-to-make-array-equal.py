class Solution:
    def minOperations(self, n: int) -> int:
        ans = 0;
        while(n>0):
            ans+=(n-1)
            n-=2
        return ans
        