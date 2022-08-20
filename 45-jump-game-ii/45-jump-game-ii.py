class Solution:
    def jump(self, nums: List[int]) -> int:
        no_of_levels = 0
        lb = rb = 0;
        while(rb<len(nums)-1):
            jump = 0
            for i in range(lb,rb+1):
                jump = max(jump,nums[i]+i)
            lb = rb+1;
            rb = jump;
            no_of_levels+=1
        return no_of_levels
            
            
    
                
            
                


        
        