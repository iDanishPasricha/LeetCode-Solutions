class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0;
        d={0:-1}
        max_length = 0;
        
        for i in range(len(nums)):
            curr = nums[i]
            if curr == 0:
                count-=1;
            if curr == 1:
                count+=1;
            if count not in d:
                d[count] = i
            if count in d:
                max_length = max(max_length , i-d[count])
        return max_length
        