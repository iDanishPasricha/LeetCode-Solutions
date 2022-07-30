class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums = sorted(nums)
        l = 0
        r = len(nums)-1
        mid = (l+r)//2
        sums = 0
        for i in nums:
            diff = abs(i - nums[mid])
            sums+=diff
        return sums