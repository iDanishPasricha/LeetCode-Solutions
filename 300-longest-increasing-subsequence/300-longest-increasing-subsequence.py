import math
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        curr_array=[];
        curr_array.append(nums[0]);
        
        def binarysearch(nums,target):
            start=0;
            end=len(nums)-1;
            ans=float(inf)
            while(start<=end):
                mid=(start+end)//2;
                if target<=nums[mid]:
                    ans=min(ans,mid)
                    end=mid-1
                else:
                    start=mid+1;
            if ans!=float(inf):return ans
            else:return -1
            
            
            
            
        for i in range(len(nums)):
            
            nearest_element = binarysearch(curr_array,nums[i]);
            if nearest_element==-1:
                curr_array.append(nums[i])
            else:
                curr_array[nearest_element]=nums[i]
        return len(curr_array)