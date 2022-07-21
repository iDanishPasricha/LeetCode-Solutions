class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        d={}
        end = defaultdict(int)
        
        for i in nums:
            if i not in d:
                d[i]=1;
            else:
                d[i]+=1;
        print(d)
        for i in nums:
            if d[i]==0:
                continue;
            else:
                if end[i-1]:
                    end[i-1]-=1;
                    end[i]+=1;
                    d[i]-=1;
                elif ((i+1) in d and d[i+1]) and ((i+2) in d and d[i+2]):
                    end[i+2]+=1;
                    d[i]-=1;
                    d[i+1]-=1;
                    d[i+2]-=1;
                else:
                    return False
        return True
                

        