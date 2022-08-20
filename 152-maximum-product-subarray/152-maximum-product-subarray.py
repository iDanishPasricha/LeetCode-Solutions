class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = max(nums)
        curr_max = 1
        curr_min = 1
        
        for i in nums:
            temp1 = i* curr_max;
            temp2 = i* curr_min;
        
            curr_max = max(temp1,temp2,i)
            curr_min = min(temp1,temp2,i)
            
            ans = max(ans,curr_max)
        return ans