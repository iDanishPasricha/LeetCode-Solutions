import math
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp=[-math.inf for _ in range(len(nums))]
        
        dp[0]=nums[0]
        for i in range(1,len(nums)):
            dp[i] = max(nums[i],dp[i-1]+nums[i])
        return max(dp)
    
    
    
    #either previous sum + current element is bigger or just current element if we choose current element then it indicates that we should start out subarray from that index like we choose 4 from -2+4 and  4  so subarray starting number 4 se start [ 4, -1 , 2 ,1]
 #Kadane's algorithm   
