import heapq
class Solution:
    def lastStoneWeight(self, nums: List[int]) -> int:
        maxheap=[];
        for i in nums:
            maxheap.append(-i);
  
        heapq.heapify(maxheap);
        print(maxheap)
        
        while(len(maxheap)>1):
            y=-heapq.heappop(maxheap);
            x=-heapq.heappop(maxheap);
            print(y,x)
            print(maxheap)
            if y==x: continue; #kuch na kr jive da bangya nums pop hon to baad ove e rehnde
            if y>x:
                maxheap.append(-(y-x))
                heapq.heapify(maxheap);
        if len(maxheap)==0:return 0
        else:return -maxheap[0]
        
            
        