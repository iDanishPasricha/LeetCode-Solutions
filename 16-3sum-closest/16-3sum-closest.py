class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = sum(nums[:3])
        for i in range(len(nums)):
            l = i+1
            r = len(nums)-1
            while(l<r):
                curr_sum = nums[i]+nums[l]+nums[r]
                if abs(curr_sum - target) < abs(ans - target):
                    ans = curr_sum
                elif curr_sum > target:
                    r-=1
                elif curr_sum < target:
                    l+=1
                else:
                    return ans
        return ans
                    
                
                
    '''
Time Complexity: O(n2). We have outer and inner loops, each going through n elements.

Sorting the array takes O(nlogn), so overall complexity is O(nlogn+n2). This is asymptotically equivalent to O(n2).

Space Complexity: from O(logn) to O(n), depending on the implementation of the sorting algorithm.
'''

    
    
    
