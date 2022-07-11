# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast=slow=head;
        """
        Part 1 --> Do we have a cylce?

        Use Floyd's algo to check if cycle:

        Basic idea:
        Two points both start off at the head node, one pointer moves one step at a time, while the   other pointer moves two steps at a time. If there is a cycle the two pointers will meet at some
        point.           
        """
        while(fast and fast.next):
            fast=fast.next.next
            slow=slow.next
            if fast == slow:
                break
        else:
            return None
        
        """
        Part 2 --> We have a cycle so now find the start of the cycle

        Use the previous fast pointer and a new pointer which starts at head. Move each of the pointers by one step, the point where the two pointers meets will be the start of the cycle.
        """
        pointer = head;
        while(pointer!=fast):
            pointer = pointer.next;
            fast    = fast.next;
        return pointer
            
     
        