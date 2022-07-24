class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def helper(idx):
            left, right = 0, len(nums1)-1
            while left <= right:
                mid = (left + right) // 2
                if nums1[mid] > nums2[idx]:
                    right = mid - 1
                else:
                    left = mid + 1
            if left < len(nums1):
                temp = left
            else:
                temp = 0
            ans.append(nums1[temp])
            nums1.pop(temp)
            
        nums1.sort()
        visited = [False] * len(nums1)
        ans = []
        for i in range(len(nums2)):
            helper(i)
        return ans
    
    
    
    