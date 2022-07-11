# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast=slow=head;
        while(fast and fast.next):
            fast=fast.next.next
            slow=slow.next
            if fast == slow:
                break
        else:
            return None
        
            
        pointer = head;
        while(pointer!=fast):
            pointer = pointer.next;
            fast    = fast.next;
        return pointer
            
     
        