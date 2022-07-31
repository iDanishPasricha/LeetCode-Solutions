class Solution:
    def nextPermutation(self, nums: List[int]) -> None:

        i = len(nums)-1
        while i>0:
            if nums[i-1] < nums[i]:
                break
            i = i-1
        
        stored = i-1
        j = len(nums)-1
        while j>stored:
            if nums[stored] < nums[j]: #jado next bigger element milgya odo chak
                break
            j=j-1
            
        nums[stored],nums[j]=nums[j],nums[stored]  
        nums[stored+1:]=sorted(nums[stored+1:]) 
        
        