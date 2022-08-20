class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        d = defaultdict(int)
        max_num = 0
        for i in nums:
            d[i]+=i
            max_num = max(max_num,i)
        dp = [0]*(max_num+1)
        dp[0] = 0
        dp[1] = d[1]
        for i in range(2,len(dp)):
            dp[i] = max(dp[i-1],d[i]+dp[i-2])
        return dp[max_num]
    
        

        
        