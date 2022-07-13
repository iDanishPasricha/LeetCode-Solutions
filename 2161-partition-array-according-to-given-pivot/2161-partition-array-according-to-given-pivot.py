class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l1=[];
        middle = [];
        l2=[];
        
        for i in nums:
            if i<pivot:
                l1.append(i);
            if i==pivot:
                middle.append(i)
            if i>=pivot and i not in middle:
                l2.append(i);
        print(l1);
        print(middle)
        print(l2)
        
        ans  = l1+middle+l2
        return ans
        