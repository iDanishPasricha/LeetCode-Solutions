# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        count = 0;
        temp=head;
        while temp:
            count+=1;
            temp = temp.next;
        
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
            
        
        
        