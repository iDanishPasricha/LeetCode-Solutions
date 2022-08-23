class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # basically twosum + twosum II
        
        ans = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i]>0: break
            if (i>0 and nums[i]==nums[i-1]):continue
            
            left = i+1
            right = len(nums)-1
            target = -1*nums[i]
            while(left<right):
                sum = nums[i]+nums[left]+nums[right] 
                if sum>0:
                    right-=1
                elif sum<0:
                    left+=1
                elif sum==0:
                    ans.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while(left<right and nums[left]==nums[left-1]):
                        left+=1
        return ans
    '''
    Time Complexity: O(n2) twoSumII is O(n), and we call it n times.

Sorting the array takes O(nlogn), so overall complexity is O(nlogn+n2). This is asymptotically equivalent to O(n2) 

Space Complexity: from O(logn) to O(n), depending on the implementation of the sorting algorithm. For the purpose of complexity analysis, we ignore the memory required for the output.

Another approach using hashset

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSum(nums, i, res)
        return res

    def twoSum(self, nums: List[int], i: int, res: List[List[int]]):
        seen = set()
        j = i + 1
        while j < len(nums):
            complement = -nums[i] - nums[j]
            if complement in seen:
                res.append([nums[i], nums[j], complement])
                while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                    j += 1
            seen.add(nums[j])
            j += 1
    
Time Complexity: O(n2). twoSum is O(n), and we call it n times.

Sorting the array takes O(nlogn), so overall complexity is O(nlogn+n2) . This is asymptotically equivalent  O(n2).

Space Complexity:O(n) for the hashset.

'''

        
                
        