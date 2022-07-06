import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums #creating member variables
        self.k = k   #creating member variables
        
        #minheap with k largest elements
        heapq.heapify(self.heap)
      
        while len(self.heap) > k:
            heapq.heappop(self.heap);
       

        
    def add(self, val: int) -> int:
        heapq.heappush(self.heap,val)          #yeh apne app  top 3 (k=3) largest banadega je 
        if len(self.heap)>self.k:  #je number end te judd rea means heap hoke this means starting position bakwaas hai hataao top k largest to last k honge starting no need
            heapq.heappop(self.heap)
        return self.heap[0]
       
        

    
