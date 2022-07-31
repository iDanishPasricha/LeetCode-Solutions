class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        positive = []
        negative = []
        zeroes = []
        
        for i in nums:
            if i>0:
                positive.append(i)
            elif i<0:
                negative.append(i)
            else:
                zeroes.append(i)
                
        P = set(positive)
        N = set(negative)
        ans = set()
        
        if zeroes:
            for i in P:
                if -1*i in N:
                    ans.add((-1*i,0,i))
        if len(zeroes)>=3:
            ans.add((0,0,0))
            
        for i in range(len(negative)):
            for j in range(i+1,len(negative)):
                target = -1*(negative[i]+negative[j])
                if target in P:
                    ans.add(tuple(sorted([negative[i],negative[j],target])))
                    
        for i in range(len(positive)):
            for j in range(i+1,len(positive)):
                target = -1*(positive[i]+positive[j])
                if target in N:
                    ans.add(tuple(sorted([positive[i],positive[j],target])))
                    
        return ans