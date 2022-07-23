class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min1 = min2 = float("inf")
        for n in nums:
            if n < min1: 
                min1 = n
            elif min1 < n < min2:
                min2 = n
            elif min1 < min2 < n:
                print(min1,min2,n)
                return True
        return False
    
    '''
    Intuitively, we'd like the ending number of our current subsequence to be small. This way there's a higher chance to encounter a greater value in the future as we scan through the numbers. We keep track of two numbers, min1 and min2 which are the smallest and second smallest numbers we've encountered so far. There can be three cases:

If we have min1 <min2 < n, we've found the triplet subsequence
If n < min1, we replace min1 with n greedily therefore we're more likely to encounter a greater value in the future
If min1 <n < min2, we replace min2 with n greedily for the same reason as case 2.
'''