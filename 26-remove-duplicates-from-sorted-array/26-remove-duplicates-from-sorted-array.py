class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start = 1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[start]=nums[i]
                start+=1
        return start
        