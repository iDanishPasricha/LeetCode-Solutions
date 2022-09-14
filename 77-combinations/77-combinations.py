class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def generate_subsets(nums,temp):
            if len(temp)==k:
                ans.append(temp.copy());
                return
            
            for i in range(len(nums)):
                temp.append(nums[i]);
                generate_subsets(nums[i+1:],temp);
                temp.pop();
                
                
        ans=[];
        nums = []
        for i in range(1,n+1):
            nums.append(i)
        generate_subsets(nums,[]);
        return ans;