class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        ans= 0
        low = -math.inf
        for i in nums:
            low = max(low+1, i)
            ans += low - i
        return ans