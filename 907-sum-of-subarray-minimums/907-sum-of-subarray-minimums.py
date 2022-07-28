class Solution:
    def sumSubarrayMins(self, nums: List[int]) -> int:
        
        M = 10**9+7
        sums = 0
        nums.append(0) 
        stack = [-1]
        
        for i in range(len(nums)):
           
            while stack and nums[i] < nums[stack[-1]]:
                index = stack.pop()
            
                left = index-stack[-1]
                right = i-index
                
                sums += right*left*nums[index]
            stack.append(i)
            
        return sums%M
            
        
        