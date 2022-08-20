class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1: return True
        jump = nums[0] + 0
        
        for i in range(1,len(nums)):
            if i>jump: return False
            if i>=len(nums)-1: return True
            
            jump = max(jump,i+nums[i])
      
    
    