class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:

        def printSubsequence(nums, temp):

            if len(nums) == 0:
                if len(temp)>=2 and list(sorted(temp))==temp: final_ans.append(temp)
                return 
            printSubsequence(nums[1:], temp+[nums[0]])

            printSubsequence(nums[1:], temp)
        final_ans=[];
        printSubsequence(nums, [])
        final_ans = [list(item) for item in set(tuple(row) for row in final_ans)]
        return final_ans