class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        h = {}
        for i in arr:
            h[i] = 1 + h.get(i, 0)
        
        k_smallest = list(h.values())
        heapq.heapify(k_smallest)
        
        removal_count =0
        while (removal_count<k):
            removal_count+= heapq.heappop(k_smallest)
        
        if removal_count == k:
            return len(k_smallest)
        return len(k_smallest)+1