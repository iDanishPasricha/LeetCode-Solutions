class MedianFinder:

    def __init__(self):
        # we will be initializing 2 heaps small --> maxheap and large --> minheap
        
        self.small = []   # self.small[0] = maximum num in small array
        self.large = []   # self.large[0] = minimum num in large array
        
    def addNum(self, num: int) -> None:  # every time we encounter small do it this way
        heapq.heappush(self.small , -1*num)   # as small is maxheap so we have to insert it in this way
        
        # make sure every num in small <= every num in large
        if (self.small and self.large and (-1*self.small[0]) > self.large[0]): # violation
            val = -1 *heapq.heappop(self.small)
            heapq.heappush(self.large,val)
        # if there is uneven size
        
        if len(self.small) > len(self.large)+1:
            val = -1*heapq.heappop(self.small)
            heapq.heappush(self.large,val)
            
        if len(self.large) > len(self.small)+1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small,-1*val)
        
        
        

    def findMedian(self) -> float:
        if len(self.small)>len(self.large):
            return -1*self.small[0]
        if len(self.small)<len(self.large):
            return self.large[0]
        if len(self.small)==len(self.large):
            return (-1*self.small[0]+self.large[0])/2
        
        

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()