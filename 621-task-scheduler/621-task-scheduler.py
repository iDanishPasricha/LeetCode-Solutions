import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c=Counter(tasks)
        maxHeap = [-i for i in c.values()]
        heapq.heapify(maxHeap)
        q=deque();
        t = 0;
        while maxHeap or q:
            t+=1;
            if maxHeap:
                MFE = 1+heapq.heappop(maxHeap)#Most Frequent Element right now
                if MFE!=0:
                    q.append([MFE , t+n])
            if q and q[0][1] == t:

                heapq.heappush(maxHeap, q.popleft()[0])
                
        return t
    
            
        