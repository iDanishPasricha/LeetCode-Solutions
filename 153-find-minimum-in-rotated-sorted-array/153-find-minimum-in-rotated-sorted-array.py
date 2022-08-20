class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[-1]>nums[0] or len(nums)==1: return nums[0]
    
        start=0;
        end=len(nums)-1;
        while start<=end:
            mid=(start+end)//2;
            if nums[mid]<nums[mid-1]: return nums[mid]
            if nums[mid+1]<nums[mid]: return nums[mid+1]
            if nums[mid]>nums[0]: start = mid+1
            if nums[mid]<nums[0]: end = mid-1
                
      
    
    
'''
Time Complexity : O(log N)    Same as Binary Search
Space Complexity : O(1)

'''

