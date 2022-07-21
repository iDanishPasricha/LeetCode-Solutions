class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        laddersused=[];
        for i in range(len(heights)-1):
            diff  = heights[i+1]-heights[i];
            if diff<=0:continue
            else:
                heapq.heappush(laddersused,diff)
                if ladders:   #agar ladders bachi hao to
                    ladders-=1
                    continue
                else:  #je nhi bachi ta sabto choti height wali ladder naal bricks replace kro
                    
                    lowest= heapq.heappop(laddersused)
                    bricks-=lowest
                    if bricks<0: return i  #je bricks v mukk gyi fer ehto gaah nhi jaa sakde
        return len(heights)-1
                    
                    