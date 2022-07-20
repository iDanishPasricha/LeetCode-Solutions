import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        c=Counter(s)
        maxHeap = [[-count,char] for char,count in c.items()]
        heapq.heapify(maxHeap)
        prev = None
        ans=""
        while maxHeap or prev:
            if prev and not maxHeap: return ""
            count,char = heapq.heappop(maxHeap)
            ans+=char
            count+=1;
            
            if prev:  #je prev pehla to hi kuch hai ta add kr maxheap ch te pdate kr none
                heapq.heappush(maxHeap,prev)
                prev=None
            if count!=0:  #yaani halle count bache aa char ch aa sakda halle maxheap ch
                prev=[count,char]
        return ans
                
                