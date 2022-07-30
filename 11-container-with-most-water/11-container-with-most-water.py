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

        