class Solution:
    def minMoves(self, nums: List[int]) -> int:
        sums = 0
        min_number = min(nums)
        nums = sorted(nums)

        for i in nums[1:]:
            diff = i - min_number
            sums+=diff
        return sums
        