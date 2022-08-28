# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        count = 0;
        temp=head;
        # step1:- count the length
        while temp:
            count+=1;
            temp = temp.next;
        
        #step2:- count how many equal and extra parts we can make
        #ex:- [1,2,3,4,5,6,7,8,9,10] equal parts = 3, extra = 1
        equals = count//k 
        extras = count%k;
        
        ans =  [[] for _ in range(k)]
        prev,curr = None,head
        for i in range(k):
            ans[i] = curr
            for j in range(equals + (1 if extras>0 else 0)):
                prev,curr = curr,curr.next;
            if prev:prev.next=None
            extras-=1;
        return ans
            
        
        
        