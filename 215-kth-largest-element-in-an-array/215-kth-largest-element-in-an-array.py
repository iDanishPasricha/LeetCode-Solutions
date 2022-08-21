import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxheap =[]
        #We use heapq class to implement Heaps in Python. By default Min Heap is implemented by this class. But we multiply each value by -1 so that we can use it as MaxHeap.
        for x in nums:
            maxheap.append(-1*x);
            
        heapq.heapify(maxheap) #convert it to heap
        print(maxheap)
        ans=[];
        while k>0:
            a = heapq.heappop(maxheap)
            k-=1;
        return -a