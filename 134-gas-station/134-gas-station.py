class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start,total = 0,0;
        if sum(cost)>sum(gas): return -1
        for i in range(len(gas)):
            total+=(gas[i]-cost[i]);
            if total<0:
                total = 0;
                start = i+1
        return start