class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0;
        r = len(height)-1
        ans = 0
        while(l<r):
            shorter_height = min(height[l],height[r])
            curr_area = shorter_height*(r-l)
            ans = max(ans,curr_area)
            
            if shorter_height == height[l]:
                l+=1;
            if shorter_height == height[r]:
                r-=1;
        
        return ans
#Time complexity: O(n). Single pass.

#Space complexity: O(1). Constant space is used.
'''
Brute force:-
we will simply consider the area for every possible pair of the lines and find out the maximum area out of those.

T->O(n2) Calculating area for n(n-1)/2 height pairs
S->O(1)  Constant extra space is used


maxarea = 0
for left in range(len(height)):
    for right in range(left + 1, len(height)):
        width = right - left
        maxarea = max(maxarea, min(height[left], height[right]) * width)

return maxarea

'''
        
        