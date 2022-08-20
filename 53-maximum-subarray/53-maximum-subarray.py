import math
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp=[-math.inf for _ in range(len(nums))]
        
        dp[0]=nums[0]
        for i in range(1,len(nums)):
            dp[i] = max(nums[i],dp[i-1]+nums[i])
        return max(dp)
    
    
    
    #ya to previous sum + cuurent element badha hai ya khaali current element agar khaali current element choose kiya to yeh indicate hota hai ki us element se sub_array start kro like we choose 4 from -2+4 and  4  so subarray ka index 4 se start [ 4, -1 , 2 ,1]
 #Kadane's algorithm   
