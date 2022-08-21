class Solution:
    def trap(self, height: List[int]) -> int:
        
        water=0;
        total_water=0;
        right_max=0;
        right_max_index=0;
        
        for i in range(len(height)):
            if height[i]>right_max:
                right_max=height[i];
                right_max_index=i;
                
        left_max=0;
        for i in range(0,right_max_index):
            left_max=max(left_max,height[i]);
            water=left_max-height[i];
            total_water+=water;
            
            
        left_max=0;
        height=height[right_max_index:][::-1];
        for i in range(len(height)):
            left_max=max(left_max,height[i]);
            water=min(left_max,right_max)-height[i];
            total_water+=water;
            
        return total_water
        