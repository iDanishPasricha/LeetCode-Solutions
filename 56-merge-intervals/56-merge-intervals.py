class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)==0: return
        if len(intervals)==1: return intervals
        
        intervals.sort(key = lambda x:x[0])
        
        ans = [intervals[0]]
        
        for start,end in intervals[1:]:
            prevEnd = ans[-1][1]
            if start<=prevEnd:
                ans[-1][1] = max(prevEnd,end)
            else:
                ans.append([start,end])
        return ans
        
            
       
        
