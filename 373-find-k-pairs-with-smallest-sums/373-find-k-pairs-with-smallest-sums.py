import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ans=[];
        m=len(nums1)
        n=len(nums2);
        visited = set();
        
        heap  = [(nums1[0]+nums2[0],(0,0))]
        for _ in range(min(k,m*n)):
            value,(i,j) = heapq.heappop(heap)
            ans.append([nums1[i],nums2[j]])
            
            #BFS checking neighbours:
            #first checking neighbours of nums1 keeping nums2 j constant
            if i+1<m and (i+1,j) not in visited:
                heapq.heappush(heap,(nums1[i+1]+nums2[j],(i+1,j)))
                visited.add((i+1,j));
            if j+1<n and (i,j+1) not in visited:
                heapq.heappush(heap,(nums1[i]+nums2[j+1],(i,j+1)))
                visited.add((i,j+1));
        return ans
    
    #  Use BFS with heap. In each iteration, we get the pair with minimal sum and then push its neighboring right and bottom (if exists) into the heap. Repeat k or at most m*n times of such iterations. Time complexity O(k lg k). Space complexity O(k) for the heap.