class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        ans= 0
        low = -math.inf
        for i in nums:
            low = max(low+1, i)
            ans += low - i
        return ans
    
    
    #compared with the previous number , our current number should be atleast prev+1 but if the current number is already bigger than the prev+1, then no need