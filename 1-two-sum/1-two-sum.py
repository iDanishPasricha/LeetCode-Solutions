class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i
        print(d)
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in d and d[complement]!=i: return [i, d[complement]];
            