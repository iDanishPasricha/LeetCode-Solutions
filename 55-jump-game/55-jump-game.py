class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1: return True
        chalaang= 0+nums[0];
        
        for i in range(len(nums)):
            
            if i > chalaang: return False
            if i >= len(nums)-1: return True
            
            chalaang = max ( chalaang , i + nums[i]);
      
    
    