class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def kadane(a):
            
            max_so_far =a[0]
            curr_max = a[0]

            for i in range(1,len(a)):
                curr_max = max(a[i], curr_max + a[i])
                max_so_far = max(max_so_far,curr_max)

            return max_so_far
        
        
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
        