class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums)-1
        
        while(l < r):
            if nums[l]+nums[r]>target:
                r-=1
            if nums[l]+nums[r]<target:
                l+=1
            if nums[l]+nums[r]==target:
                return [l+1,r+1]
            
                
            
        
        
        
        
        
        
        
        
'''
        answer=[];
        l=0;
        r=len(numbers)-1;
        while(l<r):
            if (numbers[l]+numbers[r]==target):
                return [l+1,r+1];
            if (numbers[l]+numbers[r]<target):
                     l+=1;
            else:
                     r-=1;
'''