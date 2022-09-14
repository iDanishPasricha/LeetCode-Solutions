class Solution:
    def minSwaps(self, data: List[int]) -> int:
        window_width = sum(data)
        curr_window = max_window = 0
        left = right = 0
        
        #required_window_length = total number of one's in out initial nums
        
        
        while right < len(data):
            curr_window += data[right]
            right += 1
            #maintain the window width
            if right - left > window_width:
                curr_window -= data[left]
                left += 1
            # record the maximum number of 1's in the window
            max_window = max(max_window, curr_window)
            
            
            
        return window_width - max_window
    
    
    
    