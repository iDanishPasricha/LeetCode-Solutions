class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        counter = collections.Counter(nums)
        end = defaultdict(int)
        print("counter-->",counter)
        print("end-->",end)
                
        for i in nums:
            if counter[i]:
                counter[i]-=1;
                if end[i-1]:
                    end[i]+=1;
                    end[i-1]-=1;
                elif counter[i+1] and counter[i+2]:
                    counter[i+1]-=1;
                    counter[i+2]-=1;
                    end[i+2]+=1;
                else:
                    return False
        return True
        