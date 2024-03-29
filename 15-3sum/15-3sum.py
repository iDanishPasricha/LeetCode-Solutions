class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # basically twosum + twosum II
        ans = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i]>0: break
            if (i>0 and nums[i] == nums[i-1]): continue
                
            left = i+1
            right = len(nums)-1

            while(left<right):
                sum = nums[i]+nums[left]+nums[right]
                if sum>0:
                    right-=1
                elif sum<0:
                    left+=1
                elif sum==0:
                    ans.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while(left<right and nums[left]==nums[left-1]):
                        left+=1
        return ans
        
        
        