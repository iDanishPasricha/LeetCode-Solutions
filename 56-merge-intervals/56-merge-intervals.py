class Solution:
    def merge(self, nums: List[List[int]]) -> List[List[int]]:
        if len(nums)==0: return 
        if len(nums)==1: return nums
        nums.sort(key = lambda x:x[0])
        
        stack =[];
        for i in nums:
            if not stack:
                stack.append(i);
            if stack[-1][1]<i[0]:
                stack.append(i);
            else:
                stack[-1][1] = max(i[1] , stack[-1][1])
        return stack
            
       
        
