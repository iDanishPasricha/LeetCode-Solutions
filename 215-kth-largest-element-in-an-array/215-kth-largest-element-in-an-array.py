import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxheap =[]
        
        for x in nums:
            maxheap.append(-1*x);
            
        heapq.heapify(maxheap) #convert it to heap
        print(maxheap)
        ans=[];
        temp = 0;
        while temp!=k:
            a = heapq.heappop(maxheap)
            ans.append(a)
            temp+=1;
        return -ans[-1]