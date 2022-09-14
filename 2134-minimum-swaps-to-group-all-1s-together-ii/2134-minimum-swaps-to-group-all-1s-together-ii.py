class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        window_width = sum(nums)
        nums = nums + nums
        l = 0
        r = 0
        curr_window = 0
        max_window_length  = 0
        
        while r < len(nums):
            
            curr_window += nums[r]
            r += 1
  
            if r - l > window_width:
                curr_window -= nums[l]
                l += 1
                
                
            max_window_length = max(max_window_length,curr_window)
                
        
        return window_width - max_window_length
    
    
    
    
    