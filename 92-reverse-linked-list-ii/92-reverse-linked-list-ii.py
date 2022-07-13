# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy =ListNode(0,head);
        lp = dummy
        curr = head;
        #phase 1 (pehla curr nu te lp nu left takk leke jaa)
        for _ in range(left-1):
            lp,curr = curr,curr.next;
            
        #phase 2 (reverse)
        prev = None
        for _ in range(right-left+1):
            saved = curr.next;
            curr.next = prev
            prev,curr = curr, saved
        #phase 3 (update pointers)
        lp.next.next = curr
        lp.next = prev
        
        return dummy.next
            