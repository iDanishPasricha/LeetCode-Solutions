class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        ans= 0 
        for i in range(len(nums)):
            left = nums[i]
            right = nums[i]
            for j in range(i,len(nums)):
                left = min(left,nums[j])
                right = max(right,nums[j])
                ans+=(right-left)
        return ans
                
        