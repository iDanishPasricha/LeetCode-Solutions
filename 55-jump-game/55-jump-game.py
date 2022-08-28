class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1: return True
        jump = nums[0] + 0
        
        for i in range(1,len(nums)):
            if i>jump: return False
            if i>=len(nums)-1: return True
            
            jump = max(jump,i+nums[i])
      
    
    '''
    another approach greedy
    Case 1:- [2,3,1,1,4] --> True
    Case 2:- [3,2,1,0,4] --> False
    Try with both cases
    last = n-1
    for ( i= n-2,i>=0;i--)
    {
        if (nums[i]+i) >= last
        {
            last = i
        }
    }
    return last<=0
    
    '''
    
    
    