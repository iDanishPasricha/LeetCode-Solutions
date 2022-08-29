import heapq
class Solution:
    def isNStraightHand(self, nums: List[int], k: int) -> bool:
        if len(nums)%k!=0: return False
        d={};
        
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]]=1
            else:
                d[nums[i]]+=1;
        
        minHeap=[i for i in d.keys()]
        heapq.heapify(minHeap)
        while minHeap:
            first = minHeap[0]
            for i in range(first,first+k):
                if i not in d: return False
                d[i]-=1;
                if d[i]==0:
                    if i!=minHeap[0]: return False  #EX"- [1,2,3,6,2,3,4,7,3,8,8,5] AND groupSize = 3
                    heapq.heappop(minHeap)
        return True
        