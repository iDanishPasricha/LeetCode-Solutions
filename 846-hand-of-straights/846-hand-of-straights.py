class Solution:
    def isNStraightHand(self, nums: List[int], k: int) -> bool:
        def func(nums):
            start = min(nums)
            l=[start];
            nums.remove(start)
            i=1
            while(i<k):
                if (start+i) in nums:
                    l.append(start+i)
                    nums.remove(start+i)
                else: return [78]
                i+=1;
            print(l)

            return nums
        if len(nums)%k!=0: return False
        else:
            
            while(len(nums)):
                new_nums = func(nums)
                if new_nums==[78]:return False
                if len(new_nums)==0:break
                else:
                    nums=new_nums
            return True
        