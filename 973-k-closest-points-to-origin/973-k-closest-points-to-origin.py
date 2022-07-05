import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap =[]
        
        for x,y in points:
            dist = (x**2)+(y**2)
            minheap.append([dist,x,y])
            
        heapq.heapify(minheap) #convert it to heap
        ans=[];
        while k>0:
            dist,x,y = heapq.heappop(minheap)
            ans.append([x,y])
            k-=1;
        return ans
        
        
        