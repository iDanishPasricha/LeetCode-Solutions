import math
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf]*(amount+1)
        print(dp)
        dp[0] = 0
        for curr_amount in range(1,amount+1):
            for c in coins:
                if curr_amount>=c:
                    dp[curr_amount] =  min(dp[curr_amount],1+dp[curr_amount-c])
        if dp[amount] == math.inf: return -1
        else: return dp[-1]

        
        
            
 