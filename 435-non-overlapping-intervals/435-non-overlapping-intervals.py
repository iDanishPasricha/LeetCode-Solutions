class Solution:
    def eraseOverlapIntervals(self, nums: List[List[int]]) -> int:
        
        nums.sort();
        ans = 0;        
        prevEnd = nums[0][1]
        for start,end in nums[1:]:
            if start>=prevEnd:
                prevEnd = end
            else:
                ans+=1;
                prevEnd  = min(end,prevEnd)
        return ans