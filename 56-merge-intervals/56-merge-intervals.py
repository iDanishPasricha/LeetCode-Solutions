class Solution:
    def merge(self, nums: List[List[int]]) -> List[List[int]]:
        if len(nums)==0: return 
        if len(nums)==1: return nums
        nums.sort(key = lambda x:x[0])
        ans = [nums[0]];
        for start,end in nums[1:]:  #LIEV --> Last Input's Ending Value
            LIEV = ans[-1][1];
            if start<=LIEV:
                ans[-1][1] = max(LIEV,end)
            else:
                ans.append([start,end])
        return ans
        
            
       
        
