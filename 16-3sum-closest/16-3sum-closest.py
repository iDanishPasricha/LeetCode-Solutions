class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = sum(nums[:3])
        for i in range(len(nums)):
            l = i+1
            r = len(nums)-1
            
            while(l < r):
                curr_triplet_sum = sum((nums[i],nums[l],nums[r]))
                if abs(curr_triplet_sum - target) < abs(ans - target):
                    ans = curr_triplet_sum
                if curr_triplet_sum > target:
                    r-=1;
                elif curr_triplet_sum < target:
                    l+=1;
                else:
                    return ans
        return ans
