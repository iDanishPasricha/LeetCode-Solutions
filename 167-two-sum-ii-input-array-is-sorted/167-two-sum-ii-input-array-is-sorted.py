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
    O(n)  --> the input array is traversed at most once
    O(1)
    
    
  What if the problem constraints were different and we needed to consider integer overflow when adding numbers[low]numbers[low] and numbers[high]numbers[high]? In that case, to prevent an overflow error, we could cast our numbers from int data type to long data type before adding them togethe
    '''
                  