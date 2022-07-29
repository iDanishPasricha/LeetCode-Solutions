import math
class Solution:
    def sumSubarrayMins(self, nums: List[int]) -> int:
        nums.append(0);
        stack = [-1]
        
        modulo = 10**9+7
        print(modulo)
        
        ans = 0;
        for currIndex in range(len(nums)):
            while stack and nums[currIndex]<nums[stack[-1]]:
                indexOfThatnumberJehdaPopKarna = stack.pop()
                
                indexOfThesecondBiggestNumber = stack[-1]
                
                left = indexOfThatnumberJehdaPopKarna - indexOfThesecondBiggestNumber
                
                right = currIndex - indexOfThatnumberJehdaPopKarna
                
                ans+= nums[indexOfThatnumberJehdaPopKarna]*left*right
            stack.append(currIndex)
        return (ans%modulo)
        
        '''
        sums = 0
        arr.append(0) #Sentinel value to pop all elements off the stack
        stack = [-1]
        
        for i2,num in enumerate(arr):
	      #Mantain a monotone increasing stack
            while stack and num < arr[stack[-1]]:
                index = stack.pop()
                i1 = stack[-1]   # First lesser element to the left
                left = index-stack[-1]
                right = i2-index
                sums += right*left*arr[index]
            stack.append(i2)
            
        return sums%M
        '''