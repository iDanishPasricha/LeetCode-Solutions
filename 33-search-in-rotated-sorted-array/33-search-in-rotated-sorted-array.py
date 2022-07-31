class Solution:
    def search(self, nums, target):
        if not nums: return -1
        
        start = 0
        end = len(nums)-1
        
        while(start<=end):
            mid = (start + end)//2
            
            if target == nums[mid]:
                return mid
            if nums[start]<=nums[mid]: #G1
                if nums[start]<=target<=nums[mid]:
                    end = mid-1
                else:
                    start = mid+1
            if nums[mid]<=nums[end]:   #G2
                if nums[mid]<=target<=nums[end]:
                    start = mid+1
                else:
                    end = mid-1
        return -1
        
            