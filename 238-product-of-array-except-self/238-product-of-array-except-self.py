class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        L, R, answer = [0]*length, [0]*length, [0]*length
        L[0] = 1
        for i in range(1, length):
            L[i] = nums[i - 1] * L[i - 1]
        R[length - 1] = 1
        for i in reversed(range(length - 1)):
            R[i] = nums[i + 1] * R[i + 1]
        for i in range(length):
            answer[i] = L[i] * R[i]
        return answer
    '''
    Time complexity : O(N) where N represents the number of elements in the input array. We use one iteration to construct the array L, one to construct the array R and one last to construct the answer array using L and R.
Space complexity : O(N) used up by the two intermediate arrays that we constructed to keep track of product of elements to the left and right.
'''
    '''
    another optimised
    
    The only change in this approach is that we don't explicitly build the R array from before. Instead, we simply use a variable to keep track of the running product of elements to the right and we keep updating the answer array by doing answer[i]=answer[i]∗R. For a given index i, answer[i] contains the product of all the elements to the left and R would contain product of all the elements to the right. We then update R as R = R * nums[i]
    
        length = len(nums)

        answer = [0]*length
        answer[0] = 1
        for i in range(1, length):
            answer[i] = nums[i - 1] * answer[i - 1]
        R = 1;
        for i in reversed(range(length)):
            answer[i] = answer[i] * R
            R *= nums[i]

        return answer
        
Time complexity : O(N) where N represents the number of elements in the input array. We use one iteration to construct the array L, one to update the array answer
.
Space complexity :O(1) since don't use any additional array for our computations. The problem statement mentions that using the answer array doesn't add to the space complexity.
'''
    