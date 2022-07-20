class Solution:
    def findLongestChain(self, nums: List[List[int]]) -> int:
        if len(nums)==1: return len(nums)
        nums.sort(key=lambda x:x[0])
        ans = [nums[0]]
        for start,end in nums[1:]:
            LIEV = ans[-1][1];
            if start<=LIEV:
                ans[-1][1] = min(LIEV,end)
            else:
                ans.append([start,end])
        return len(ans)
        