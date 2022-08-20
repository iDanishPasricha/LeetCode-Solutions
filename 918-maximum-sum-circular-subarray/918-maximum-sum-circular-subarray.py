class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def kadane(nums):
            
            dp=[-math.inf for _ in range(len(nums))]

            dp[0]=nums[0]
            for i in range(1,len(nums)):
                dp[i] = max(nums[i],dp[i-1]+nums[i])
            return max(dp)
        
        
        n1=nums;
        n2=nums;
        ans1 = kadane(n1);
        inverted_nums = [-i for i in nums];
        n = kadane(inverted_nums)
        ans2= -(sum(inverted_nums)-n)
        ans=max(ans1,ans2)
        if ans!=0:
            return ans
        else:
            return ans1
        