class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        window_width = sum(nums)
        nums = nums + nums
        l = 0
        r = 0
        curr_window_length = 0
        max_window_length = 0
        
        while r < len(nums):
            
            if r-l < window_width:
                curr_window_length += nums[r]
                
                r += 1
            else:
                curr_window_length -= nums[l]
                curr_window_length += nums[r]
                
                l += 1
                r += 1
            max_window_length = max(max_window_length,curr_window_length)
                
        
        return window_width - max_window_length