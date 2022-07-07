import heapq
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap=[]
        ans = []
        for row in range(len(mat)):
            heap.append((sum(mat[row]), row))
        print(heap)
        heapq.heapify(heap)
        print(heap)
        while k > 0:
            ans.append(heapq.heappop(heap)[1])
            
            k -= 1
        return ans
