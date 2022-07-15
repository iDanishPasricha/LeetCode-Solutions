# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head:
            return head
        
   
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        head2=None
        curr=slow.next
        slow.next=None
        while curr:
            next=curr.next
            curr.next=head2
            head2,curr=curr,next

        
        first, second = head, head2
        
        while second:
            first.next, first = second, first.next
            second.next, second = first, second.next
        return
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
