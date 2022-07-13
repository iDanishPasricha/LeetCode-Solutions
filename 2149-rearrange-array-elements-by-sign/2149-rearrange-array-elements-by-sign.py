class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        l1=[];
        middle = [];
        l2=[];
        
        for i in nums:
            if i>0:
                l1.append(i);
            else:
                l2.append(i)
        print(l1);

        print(l2)
        ans=[]
        for i in range(len(l1)):
            ans.append(l1[i])
            ans.append(l2[i])
        return ans
            
        
   