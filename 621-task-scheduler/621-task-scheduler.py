import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c=Counter(tasks)
        maxHeap = [-i for i in c.values()]
        heapq.heapify(maxHeap)
        print(maxHeap)
        q=deque();
        curr_time = 0;
        while maxHeap or q:
            curr_time+=1;
            if maxHeap:
                count = 1+heapq.heappop(maxHeap)
                if count:
                    q.append([count,curr_time+n])
            if q and q[0][1]==curr_time:
                heapq.heappush(maxHeap,q.popleft()[0])
        return curr_time
        
        