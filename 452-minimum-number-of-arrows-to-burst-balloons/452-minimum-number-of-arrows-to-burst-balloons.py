class Solution:
    def findMinArrowShots(self, nums: List[List[int]]) -> int:
        nums.sort(key = lambda x:x[1])
        if len(nums)==0: return 0
        print(nums)
        end_point = nums[0][1]
        arrows=1
        for start,end in nums[1:]:
            if start<=end_point:
                continue
            else:
                arrows+=1;
                end_point = end
        return arrows

        